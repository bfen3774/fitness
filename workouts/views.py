from django.shortcuts import render
from workouts.models import Plan

# Create your views here.


def index(request):
    results = Plan.objects.all()
    form_dict = {}
    if request.GET.get('min_age'):
        min_age = request.GET.get('min_age')
        form_dict['min_age'] = min_age
        results = results.filter(user_age__gte=min_age)
    if request.GET.get('max_age'): 
        max_age = request.GET.get('max_age')
        form_dict['max_age'] = max_age
        results = results.filter(user_age__lte=max_age)
    if request.GET.get('min_starting_weight'): 
        min_starting_weight = request.GET.get('min_starting_weight')
        form_dict['min_starting_weight'] = min_starting_weight
        results = results.filter(user_starting_weight__gte=min_starting_weight)
    if request.GET.get('max_starting_weight'): 
        max_starting_weight = request.GET.get('max_starting_weight')
        form_dict['max_starting_weight'] = max_starting_weight
        results = results.filter(user_starting_weight__lte=max_starting_weight)
    if request.GET.get('sexRadio'): 
        sex = request.GET.get('sexRadio')
        form_dict['sex'] = sex
        if sex == "None":
            results
        else:
            results = results.filter(user_sex__startswith=sex)
    return render(request, 'workouts/index.html', {"results": results, 'form_dict': form_dict})