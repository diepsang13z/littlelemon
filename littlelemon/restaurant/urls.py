from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken import views as rest_framework_views

from . import views


router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
	path('', views.index, name='home'),
	path('api-token-auth/', rest_framework_views.obtain_auth_token),
	path('menu/', views.MenuItemView.as_view()),
	path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
]
