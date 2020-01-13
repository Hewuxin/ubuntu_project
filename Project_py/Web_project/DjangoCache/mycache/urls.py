from django.conf.urls import url

from mycache import views

urlpatterns = [
    url('^index/', views.index, name="index"),
    url('^news/', views.news, name='news'),
    url('^jokers/', views.joker, name='jokers'),
    url('^add/', views.adds, name='adds'),
    url('^ticket/', views.ticket, name="ticket"),
    url('^blank/', views.blank, name="blank"),
]