from django.urls import path, include
from .views import SignupView
from .api.urls import router

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupView.as_view(), name='signup')
]