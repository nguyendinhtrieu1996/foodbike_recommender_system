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

    def __init__(self, neighborhood_size=15, min_sim=0.0):
        self.neighborhood_size = neighborhood_size
        self.min_sim = min_sim
        self.max_candidates = 100

    def recommend_items(self, user_id, num=6):
        active_user_items = Rating.objects.filter(user_id=user_id).order_by('-rating')[:100]
        return self.recommend_items_by_ratings(user_id, active_user_items.values(), num)

    def recommend_items_by_ratings(self, user_id, active_user_items, num=6):
        if len(active_user_items) == 0:
            return {}

        start = time.time()
        food_ids = {food['food_id']: food['rating'] for food in active_user_items}

        print('DEBUG food_ids {}'.format(food_ids))

        user_mean = sum(food_ids.values()) / len(food_ids)

        candidate_items = Similarity.objects.filter(Q(source__in=food_ids.keys())
                                                    & ~Q(target__in=food_ids.keys())
                                                    & Q(similarity__gt=self.min_sim)
                                                    )

        print('DEBUG candidate items {}'.format(candidate_items))

        candidate_items = candidate_items.order_by('-similarity')[:self.max_candidates]

        print('DEBUG candidate len {}')

        recs = dict()
        for candidate in candidate_items:
            target = candidate.target
            pre = 0
            sim_sum = 0

            rated_items = [i for i in candidate_items if i.target == target][:self.neighborhood_size]

            if len(rated_items) > 1:
                for sim_item in rated_items:
                    r = Decimal(food_ids[sim_item.source] - user_mean)
                    pre += sim_item.similarity * r
                    sim_sum += sim_item.similarity
                if sim_sum > 0:
                    recs[target] = {'prediction': Decimal(user_mean) + pre / sim_sum,
                                    'sim_items': [r.source for r in rated_items]}

        sorted_items = sorted(recs.items(), key=lambda item: -float(item[1]['prediction']))[:num]
        return sorted_items

    def predict_score(self, user_id, item_id):
        print('predict score')

    def predict_score_by_ratings(self, item_id, movie_ids):
        print('predict score by ratings')

def main():
    rec = NeighborhoodBasedRecs().recommend_items('dinhtrieu1251996', 30)
    print(len(rec))

if __name__ == '__main__':
    main()