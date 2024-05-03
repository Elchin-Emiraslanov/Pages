from django.urls import path
from .views import *
"""
#- Bu 2 ferqli url ucun isdifade olunmasi 

#- daha doqrusu /users/create/
# ve /advertisement/create/



"""
app_name = "switch" 

urlpatterns = [
    path(
        '',
        home,
        name="home-anasehife" 
    ),
    path(
        '/card-details',
        card_details,
        name="card-details" 
    ),
    # path(
    #     'create/',
    #     home,
    #     name="create" 
    # ),
]
