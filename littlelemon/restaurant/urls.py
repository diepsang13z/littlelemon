from django.urls import path

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'table', views.BookingViewSet)


urlpatterns = [
	path('', views.index, name='home'),
	path('menu/', views.MenuItemView.as_view()),
	path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
