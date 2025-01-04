"""spark_api_drf_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),


    
    path("Subscriptions/", include("abonnement_app.api.urls")),
    path("Payments/", include("abonnement_app.api.urls")),
    
    path("Schools/", include("academy_app.api.urls")),
    path("Teachers/", include("academy_app.api.urls")),
    path("Students/", include("academy_app.api.urls")),
    path("Sections/", include("academy_app.api.urls")),
    path("Chapters/", include("academy_app.api.urls")),
    path("Courses/", include("academy_app.api.urls")),
    
    
    path("Members/", include("association_app.api.urls")),
    path("Sport_events/", include("association_app.api.urls")),
    path("Promotions/", include("association_app.api.urls")),
    path("SubscriptionsAssoc/", include("association_app.api.urls")),
    
    
    
    path("scc/", include("association_configuration_app.api.urls")),
    path("chats/", include("chat_app.api.urls")),
    path("contacts/", include("contact_app.api.urls")),
    path("useractions/", include("comportement_app.api.urls")),
    
    
    path("market/", include("ecommerce.api.urls")),
    path("images_app/", include("images_app.api.urls")),
    path("team_app/", include("equipe_app.api.urls")),
    path("images/", include("images_app.api.urls")),
    path("advert_app/", include("publicite_app.api.urls")),

    path("localisation_app/", include("localisation_app.api.urls")),
    path("codes_app/", include("qr_codes_app.api.urls")),
    path("user_config/", include("user_config.api.urls")),
    path("employment_app/", include("employment_app.api.urls")),
    # path("api/", include("service_app.api.urls")),
    path("blog_app/", include("post_and_comment_app.api.urls")),
    path("invitation_app/", include("invitation_app.api.urls")),
    path("interests_app/", include("interests_app.api.urls")),
    
    path("user_app/", include("user_app.api.urls")),
    path("sport_app/", include("sport_app.api.urls")),
    
    path("profile_app/", include("profile_app.api.urls")),

    
    
]
