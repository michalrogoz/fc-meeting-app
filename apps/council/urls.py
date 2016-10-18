from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^meetinglist$', views.MeetingListView.as_view(), name='meeting_list'),
    url(r'^addmeeting$', views.MeetingCreateView.as_view(), name='add_meeting'),
    url(r'^meetingdetail/(?P<pk>\d+)/$', views.MeetingDetailView.as_view(),
        name='meeting_detail'),
    url(r'^meetingdetail/(?P<pk>\d+)/addpoint$', views.PointCreateView.as_view(),
        name='add_point'),
    url(r'^pointdetail/(?P<pk>\d+)/$', views.PointDetailView.as_view(),
        name='point_detail'),
]