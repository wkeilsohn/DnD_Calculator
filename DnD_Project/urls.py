from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('calculator.urls')), # Just redirects to the first claculator url.
	path('calculator/', include('calculator.urls')),
	path('about/', include('calculator.urls')),
#    path('admin/', admin.site.urls), # Just not necessary for this project.
]

handler_404 = 'calculator.views.handler_404'
handler_500 = 'calculator.views.handler_500'