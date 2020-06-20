from django.urls import path, include
from rest_framework.authtoken import views
from .views import SignupView
from .api.views import CurrentUserView
from .api.urls import router

urlpatterns = [
    path('', include(router.urls)),
    path('me/', CurrentUserView.as_view(), name='current-user'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('auth-token/', views.obtain_auth_token),
]