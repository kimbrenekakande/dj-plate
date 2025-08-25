from django.urls import path
from .views import Index, Home, Dashboard, List, Billing, Profile, Settings

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("home/", Home.as_view(), name = "home"),
    path("dashboard/", Dashboard.as_view(), name = "dashboard"),
    path("list/", List.as_view(), name = "list"),
    path("billing/", Billing.as_view(), name = "billing"),
    path("profile/", Profile.as_view(), name = "profile"),
    path("settings/", Settings.as_view(), name = "settings"),
]