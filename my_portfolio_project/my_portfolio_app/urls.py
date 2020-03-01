from django.contrib import admin
from django.urls import path
from my_portfolio_app import views

app_name = "my_portfolio_app"

urlpatterns = [
    path('my_first_page', views.my_first_view,name='my_first_url'),
    path('my_second_page',views.my_second_view,name='my_second_url'),
    path('my_third_page',views.my_third_view,name='my_third_url'),
    path('contact_form_submit',views.contact_form_submit,name='contact_form_submit'),
    path('contact_data',views.contact_form_data,name='my_forth_url'),
]