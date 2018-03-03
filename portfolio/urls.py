from django.urls import path
from portfolio import views
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('', views.Index, name='index'),
    path('collegeCareerReadiness/', views.CollegeCareerReadiness, name='collegeCareerReadiness'),
    path('communityConnections/', views.CommunityConnections, name='communityConnections'),
    path('interdisciplinaryConnections/', views.InterdisciplinaryConnections, name='interdisciplinaryConnections'),
    path('rigorousThinking/', views.RigorousThinking, name='rigorousThinking'),
]
