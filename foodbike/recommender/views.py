from django.shortcuts import render
from django.http import JsonResponse
from recs.neighborhood_based_recommender import NeighborhoodBasedRecs

def recs_cf(request, user_id, num=100):
    min_sim = request.GET.get('min_sim', 0.1)
    sorted_items = NeighborhoodBasedRecs(min_sim=min_sim).recommend_items(user_id, num)

    # print(f"cf sorted_items is: {sorted_items}")
    data = {
        'user_id': user_id,
        'data': sorted_items
    }

    return JsonResponse(data, safe=False)