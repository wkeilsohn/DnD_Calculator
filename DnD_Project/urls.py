from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('calculator.urls')), # Just redirects to the first claculator url.
	path('calculator/', include('calculator.urls')),
	path('about/', include('calculator.urls')),
    path('admin/', admin.site.urls),
]
