from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views
router = DefaultRouter()
router.register('list',views.PatientVewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.UserRegistrationViewSet.as_view(),name='register'),
    path('login/',views.userloginApiView.as_view(),name='login'),
    path('logout/',views.userlogoutView.as_view(),name='logout'),
    path('active/<uid64>/<token>/',views.activate,name='activate')
    
   
]