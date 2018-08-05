from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import  Sum
import math
import datetime
import os
import django
import pytz

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prs_project.settings')
django.setup()

from recs.neighborhood_based_recommender import NeighborhoodBasedRecs
from foodbike.models import Food
from foodbike.models import Userdetail
from analytics.models import Rating

def recs_cf(request, user_id):
    min_sim = request.GET.get('min_sim', 0.1)
    sorted_items = NeighborhoodBasedRecs(min_sim=min_sim).recommend_items(user_id)

    data = {
        'user_id': user_id,
        'data': sorted_items
    }

    return JsonResponse(data, safe=False)

def get_all_foods(request):
    foods = Food.objects.using('sql_db').all()
    data = []
    for food in foods:
        value = {
            'Id': food.id,
            'Name': food.name,
        }
        data.append(value)

    response = {
        'Data': data
    }
    return JsonResponse(response, safe=False)

def item_news_feed(request, user_id, page_number):
    min_sim = request.GET.get('min_sim', 0.1)
    sorted_items = NeighborhoodBasedRecs(min_sim=min_sim).recommend_items(user_id)
    if sorted_items.count() < 10:
        response = {
            'NumberPages': 0,
            'Data': None
        }
        return JsonResponse(response, safe=False)
    number_item_per_page = 5
    paginator = Paginator(sorted_items, number_item_per_page)
    number_pages = paginator.num_pages

    page_items = paginator.page(page_number)
    page_items = page_items.object_list
    data = []

    for item in page_items:
        id = item[0]
        rating = calculate_rating(id)
        value = {
            'Id': id,
            'Rating': rating
        }
        data.append(value)

    response = {
        'NumberPages': number_pages,
        'Data': data
    }
    return JsonResponse(response, safe=False)

def news_feed(request, user_id, longitude, latitude, page_number):
    min_sim = request.GET.get('min_sim', 0.1)
    sorted_items = NeighborhoodBasedRecs(min_sim=min_sim).recommend_items(user_id)

    print('DEBUG sorted items len {}'.format(len(sorted_items)))

    number_item_per_page = 5
    paginator = Paginator(sorted_items, number_item_per_page)
    number_pages = paginator.num_pages

    page_items = paginator.page(page_number)
    page_items = page_items.object_list
    data = []
    tz = pytz.timezone('Asia/Saigon')
    current_time = datetime.datetime.now(tz).time()
    week_day = datetime.datetime.today().weekday() + 1

    for item in page_items:
        food_id = item[0]
        food = Food.objects.using('sql_db').filter(id=food_id).first()
        if food == None:
            continue

        menu = food.menuid
        restaurant = menu.restaurantid
        user = Userdetail.objects.using('sql_db').filter(userid=restaurant.userid).first()
        if user == None:
            continue
        rating = calculate_rating(food_id)
        distance = calculate_distance(restaurant.long, restaurant.lat, float(longitude), float(latitude))
        status = (current_time >= restaurant.opentime and current_time <= restaurant.closetime
                  and week_day >= restaurant.openfromday and week_day <= restaurant.opentoday) \
                 and True or False

        value = {
            'Id': food.id,
            'Name': food.name,
            'Address': "status",
            'FoodImage': food.defaultimage,
            'Rating': rating,
            'Status': "status",
            'Distance': "distance"
        }
        data.append(value)

    response = {
        'NumberPages': number_pages,
        'Data': data
    }
    return JsonResponse(response, safe=False)

def calculate_rating(food_id):
    columns = ['food_id', 'rating']
    ratings = Rating.objects.filter(food_id=food_id).values(*columns)
    sum = ratings.aggregate(Sum('rating'))['rating__sum']
    ratings_count = ratings.count()

    if ratings_count == 0:
        return 0
    else:
        return int(sum / ratings_count)

def calculate_distance(res_longitude, res_latitude, customer_long, customer_lat):
    r = 6378137
    d_lat = rad(res_latitude - customer_lat)
    d_long = rad(res_longitude - customer_long)
    a = math.pow(math.sin(d_lat / 2), 2) \
        + math.cos(rad(customer_lat)) \
        * math.cos(rad(res_latitude)) \
        * math.pow(math.sin(d_long / 2), 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = (r * c) / 1000

    return round(d, 1)

def rad(x):
    return x * math.pi / 180

def main():
    print("DEBUG")

if __name__ == '__main__':
    print("DEBUG Recommender.Views")
    main()
