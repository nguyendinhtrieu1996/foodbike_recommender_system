import django
import os
import datetime
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prs_project.settings')

django.setup()

from collector.models import Log

SEED = 0
MAX_FOOD_ID = 100

class User:
    userId = ""
    events = {}

    def __init__(self, user_id):
        self.userId = user_id
        self.events = []

def select_food():
    return random.randrange(0, MAX_FOOD_ID)

def select_action(user):
    actions = {'details': 55, 'moreDetails': 29, 'addToList': 15, 'buy': 1}
    return sample(actions)

def sample(dictionary):
    random_number = random.randint(0, 100)
    index = 0
    for key, value in dictionary.items():
        index += value

        if random_number <= index:
            return key

def main():
    Log.objects.all().delete()
    random.seed(SEED)

    number_of_event = 10000

    print("Generating Data")
    users = [
        User("400001"),
        User("400002"),
        User("400003"),
        User("400004"),
        User("400005"),
        User("400006"),
        User("400007"),
    ]

    print("Simulating " + str(len(users)) + " visitors")

    for x in range(0, number_of_event):
        randomuser_id = random.randint(0, len(users) - 1)
        user = users[randomuser_id]
        selected_food = select_food()
        action = select_action(user)
        # if action == 'buy':
        # user.events[user.userId].append(selected_food)
        print("=================================")
        print("user id " + user.userId)
        print("selected id " + str(selected_food))
        print(action)
        print("action " + action)
        # print("user id " + user.userId + " selects food " + str(selected_food) + " and " + action)

        l = Log(user_id=user.userId,
                content_id=selected_food,
                event=action,
                created=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                )
        l.save()

    # print("users\n")
    # for u in users:
    #     print("user with id {} \n".format(u.userId))
    #     for key, value in u.events.items():
    #         if len(value) > 0:
    #             print(" {}: {}".format(key, value))

if __name__ == '__main__':
    print("Starting FoodBike Log Population script")
    main()