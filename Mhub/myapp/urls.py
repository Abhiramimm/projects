from django.urls import path

from myapp import views

urlpatterns=[
    
    path('movie/all/',views.MovieListView.as_view(),name="movie-list"),

    path('movie/add/',views.MovieCreateView.as_view(),name="movie-create"),

    path('movie/<int:pk>/',views.MovieDetailView.as_view(),name="movie-detail"),

    path('movie/<int:pk>/delete/',views.MovieDeleteView.as_view(),name="movie-delete"),

    path('movie/<int:pk>/change/',views.MovieUpdateView.as_view(),name="movie-edit"),
]
