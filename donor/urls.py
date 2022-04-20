from django.urls import include, path
from . import views
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register('donor', views.DonorView)
router.register('hospital', views.HospitalView)
router.register('user', views.UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('donor/', views.DonorView.as_view()),
   
]