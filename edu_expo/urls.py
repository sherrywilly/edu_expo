"""edu_expo URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from edu_expo.views import home
from apps.student.views import StudentRegistrationView

# django admin customization settings
admin.site.site_header = "edu_expo Admin"
admin.site.site_title = "edu_expo Admin Portal"
admin.site.index_title = "Welcome to edu_expo Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('test', home, name='home'),
    path('', StudentRegistrationView.as_view(), name='student_registration'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:
#     try:
#         import debug_toolbar
#     except ImportError:
#         """The debug toolbar was not installed. Ignore the error.
#         settings.py should already have warned the user about it."""
#     else:
#         urlpatterns += [path("^__debug__/", include(debug_toolbar.urls))]
