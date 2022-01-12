# -*- coding: utf-8 -*-
import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from quickstart import views
from rest_framework import routers

from project import settings

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("quickstart/", include(router.urls)),
    path("", include("snippets.urls")),
    path("api-auth/", include("rest_framework.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("admin/", admin.site.urls),
        path("__debug__/", include(debug_toolbar.urls)),
    ]
