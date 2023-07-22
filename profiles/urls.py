from django.urls import path

from .views import ProfileListView, ProfileDetailView, ProfileRegistrationView

urlpatterns = [
    path('', ProfileListView.as_view(), name = 'profile-list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name = 'profile-details'),
    path('profiles/sign-up/', ProfileRegistrationView.as_view(), name = 'profile-registration')
]