from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movie.views import home, about, movies_by_year_chart, signup, statistics_page, login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie.urls')),   
    path('news/', include('news.urls')),
    path('statistics/', statistics_page, name='statistics'),
    path('statistics/chart/', movies_by_year_chart, name='movies_by_year_chart'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)