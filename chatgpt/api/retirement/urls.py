from django.urls import path

from .views import RetirementCreate, RetirementRetrieve

urlpatterns = [
    path("retirement/set/<str:pk>", RetirementCreate.as_view(), name="RetirementCreate"),
    path("retirement/get/<str:pk>", RetirementRetrieve.as_view(), name="RetirementRetrieve"),
]
