from django.conf.urls import url


from .views import BlogPostRudView
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name='post-rud')
]   