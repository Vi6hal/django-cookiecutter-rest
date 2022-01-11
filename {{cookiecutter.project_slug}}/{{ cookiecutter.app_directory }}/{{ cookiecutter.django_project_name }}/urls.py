from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="{{ cookiecutter.project_slug }}",
        default_version="v0.0.1",
        description="API Spec Documentation",
        terms_of_service="/usr/dev/null",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="No License"),
    ),
    public=True,
    #    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("", include("djoser.urls.base")),
    path("manage/", admin.site.urls),
    path("", include("djoser.urls.jwt")),
]
