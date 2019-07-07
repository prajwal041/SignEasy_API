from django.conf.urls import url
from django.urls import path
from rest_framework import routers
from myapp.views import books_list,members_list,BookDetail,MemberDetail,ReturnDetail,BorrowDetail
from rest_framework_swagger.views import get_swagger_view
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    url(r'^v1/books', books_list),
    url(r'^v1/members', members_list),
    url(r'^borrow/(?P<pk>\d+)/$', BorrowDetail.as_view(),name='create_Borrow'),
    url(r'^return/(?P<pk>\d+)/$', ReturnDetail.as_view(),name='create_Return'),
    # member & book deletion
    url(r'^book/(?P<pk>\d+)/$', BookDetail.as_view(),name='create_Books'),
    url(r'^member/(?P<pk>\d+)/$', MemberDetail.as_view(),name='create_Member'),
]
