from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from main.views import IndexPageView, RetirementPageView

urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("me/", RetirementPageView.as_view(), name="me"),
    path("accounts/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
