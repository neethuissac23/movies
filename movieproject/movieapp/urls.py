from . import views
from django.urls import path

app_name = 'movieapp'

urlpatterns = [
    path('', views.index, name="index"),
    path("movie/<int:movie_id>/", views.detail, name="detail"),
    path("add/", views.add_movie, name="add"),
    path("update/<int:id>/", views.update_movie, name="update"),
    path("delete/<int:id>/", views.delete_movie, name="delete"),


    # path('', views.index, name="index"),
    # path('', views.base, name="base"),
    # path("movie/<int:movie_id>/", views.page2, name="page2"),
    # path("add/", views.page3, name="page3"),
    # path("update/<int:id>/", views.page4, name="update"),
    # path("delete/<int:id>/", views.page5, name="delete"),
    # path("movie/<int:movie_id>/", views.detail, name="detail"),
]
