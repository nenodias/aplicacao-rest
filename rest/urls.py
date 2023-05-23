# *-* coding:utf-8 *-*
import os
from django.urls import include, re_path
from django.views.generic import TemplateView

from rest_framework.authtoken.views import obtain_auth_token

from rest.core.urls import router

urlpatterns = [
    re_path(r'^api/token/', obtain_auth_token, name='api-token'),
    re_path(r'^api/', include(router.urls)),
    re_path(r'^$', TemplateView.as_view(template_name='core'+os.sep+'index.html'))
]
