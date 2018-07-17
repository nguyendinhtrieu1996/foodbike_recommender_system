import os
import time
from django.db.models import Q
from decimal import Decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prs_project.settings")

import django

django.setup()

from recs.base_recommender import base_recommender
from analytics.models import Rating
from recommender.models import Similarity

class NeighborhoodBasedRecs(base_recommender):

    def __init__(self, neighborhood_size=100, min_sim=0.0):
        self.neighborhood_size = neighborhood_size
        self.min_sim = min_sim
        self.max_candidates = 100

    def recommend_items(self, user_id):
        active_user_items = Rating.objects.filter(user_id=user_id).order_by('-rating')
        return self.recommend_items_by_ratings(user_id, active_user_items.values())

    def recommend_items_by_ratings(self, user_id, active_user_items):
        if len(active_user_items) == 0:
            return {}

        start = time.time()
        food_ids = {food['food_id']: food['rating'] for food in active_user_items}

        print('DEBUG len food_ids {}'.format(len(food_ids)))

        user_mean = sum(food_ids.values()) / len(food_ids)

        candidate_items = Similarity.objects.filter(Q(source__in=food_ids.keys())
                                                    & ~Q(target__in=food_ids.keys())
                                                    & Q(similarity__gt=self.min_sim)
                                                    )

        candidate_items = candidate_items.order_by('-similarity')

        print('DEBUG candidate len {}'.format(len(candidate_items)))

        recs = dict()
        for candidate in candidate_items:
            target = candidate.target
            pre = 0
            sim_sum = 0

            rated_items = [i for i in candidate_items if i.target == target]

            if len(rated_items) > 1:
                for sim_item in rated_items:
                    r = Decimal(food_ids[sim_item.source] - user_mean)
                    pre += sim_item.similarity * r
                    sim_sum += sim_item.similarity
                if sim_sum > 0:
                    recs[target] = {'prediction': Decimal(user_mean) + pre / sim_sum,
                                    'sim_items': [r.source for r in rated_items]}

        sorted_items = sorted(recs.items(), key=lambda item: -float(item[1]['prediction']))

        return sorted_items

    def predict_score(self, user_id, item_id):
        print('predict score')

    def predict_score_by_ratings(self, item_id, movie_ids):
        print('predict score by ratings')

def main():
    rec = NeighborhoodBasedRecs().recommend_items('dinhtrieu1251996')
    print(len(rec))

if __name__ == '__main__':
    main()