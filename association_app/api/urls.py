from django.urls import path
from . import views

urlpatterns = [
    path("membersCreateList/", views.MemberListCreateView.as_view(), name="member_create"),
    path("member/<int:pk>/", views.MemberRetrieveUpdateDestroyView.as_view(), name="member_detail"),

    path("sport_eventsCreateList/", views.SportEventListCreateView.as_view(), name="sport_event_create"),
    path("sport_event/<int:pk>/", views.SportEventRetrieveUpdateDestroyView.as_view(), name="sport_event_detail"),

    path("promotionCreateList/", views.PromotionListCreateView.as_view(), name="promotion_create"),
    path("promotion/<int:pk>/", views.PromotionRetrieveUpdateDestroyView.as_view(), name="promotion_detail"),

    path("subscriptionsAssocCreateList/", views.SubscriptionListCreateView.as_view(), name="subscription_create"),
    path("subscriptionAssoc/<int:pk>/", views.SubscriptionRetrieveUpdateDestroyView.as_view(), name="subscription_detail"),
]