from django.urls import path
from .api import *

urlpatterns = [
    path('admincreate/', AdminCreateAPI.as_view()),
    path('country/', CountryCreateAPI.as_view()),
    path('state/', StateCreateAPI.as_view()),
    path('city/', CityCreateAPI.as_view()),

    path('user/logout/', LogoutAPI.as_view()),

    # path()
]