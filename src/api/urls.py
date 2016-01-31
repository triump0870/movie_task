from django.conf.urls import url, patterns
from api.views import MovieListView, MovieDetailView, UserList, UserDetial, api_root

urlpatterns = [
    url(r'^$', api_root, name='api-root'),
    url(r'^movies/', MovieListView.as_view(), name='movie-list'),
    url(r'^movies/(?P<pk>)/$', MovieDetailView.as_view, name='movie-detail'),
    url(r'^users/$',UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>)/$', UserDetial.as_view(), name='user-detail'),
]