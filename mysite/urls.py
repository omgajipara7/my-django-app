from django.contrib import admin
from django.urls import path,include
from Portfolio.views import portfolio_view,om
from emailapp.views import contact,contact_success


urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('',om, name='om'),  # Assuming 'om' is the view you want to map to the root URL
    path('contact/',contact, name='contact'),
    path('contact_success/', contact_success, name='contact_success'),
    path('djangohelp/',include("djangohelp.urls"))
]


