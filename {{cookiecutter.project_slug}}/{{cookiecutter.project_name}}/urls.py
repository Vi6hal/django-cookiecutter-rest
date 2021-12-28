from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Proto APIs",
        default_version='v1',
        description="API Documentation",
        terms_of_service="/usr/dev/null",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="No License"),
    ),
    public=True,
    #    permission_classes=(permissions.AllowAny,),
)

swaggerd = [
    path('api', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = [
    path('', include("djoser.urls.base")),
    path('manage/', admin.site.urls),
    path('', include("djoser.urls.jwt")),
]

urlpatterns = urlpatterns + swaggerd
