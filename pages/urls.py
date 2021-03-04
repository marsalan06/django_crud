from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from pages.views import home,contact,home_oop, index_home,team,member
from pages.views import cat_mem, q_view, index_home,about_page
from pages.views import contact_page

urlpatterns=[
    path('home/',home),
    path('contact/',contact),
    path('home_oop/',home_oop.as_view()),
    path('members/',team,name="team"), #static url
    path('member/<int:id>',member,name="member"),#dynamic url
                    #we declared this as a fixed data type
    path('cat/<str:cat_id>/mem/<int:mem_id>',cat_mem),
    #dynamic url passed 
    path('q_view/',q_view),
    path('index_home/',index_home),
    path('about_page/',about_page),
    path('contact_form/',contact_page),
]

