from django.urls import path
from .views import homeView,newView,detailView,portfolioView
urlpatterns = [
	# path('',loginView.as_view(),name="login"),
    path('',homeView.as_view(),name="home"),
    path('create/',newView.as_view(),name="create"),
    path('detail/<int:pk>',detailView.as_view(),name="detail"),
    path("portfolio/",portfolioView.as_view(),name="portfolio"),
]
