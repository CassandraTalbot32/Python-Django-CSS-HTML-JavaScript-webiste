from django.contrib import admin
from django.urls import include, path
from entry.views import home_view, contact_view, about_view, projects_view, search_view, events_view

urlpatterns = [
	path('blog/', include('blog.urls')),
	path('challenges/', include('challenges.urls')),
	path('products/', include('products.urls')),
	path('admin/', admin.site.urls),
   	path('', home_view, name='home'),
	path('contact/', contact_view),
	path('projects/', projects_view),
	path('search/', search_view),
	path('events/', events_view),
	path('about/', about_view),
	]
