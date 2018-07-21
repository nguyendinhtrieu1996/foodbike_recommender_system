import decimal
import json
import time
from datetime import datetime

from django.db import connection
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from gensim import models

from analytics.models import Rating, Cluster
from collector.models import Log

def index(request):
    context_dict = {}
    return render(request, 'analytics/index.html', context_dict)
