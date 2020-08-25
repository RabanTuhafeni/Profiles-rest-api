from django.conf.urls import url

from . import views


urlpattens = [
    url(r'^hello-view/', views.HelloApiView.as_view()),

]
