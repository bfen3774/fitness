from django.forms import ModelForm
from workouts.models import Plan

class PlanForm(ModelForm):
    class Meta:
        model = Plan
