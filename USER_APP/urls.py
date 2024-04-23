from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user, name='booking'),
    path('about/', views.about, name='about'),
    path('review/', views.review, name='review'),
    path('login/', views.login, name='login'),
    path('offer/', views.offer, name='offer'),
    path('package/', views.package, name='package'),
    path('package_filter/', views.package_filter, name='package_filter'),
    path('package_preview/<int:package_id>/', package_preview, name='package_preview'),
    # path('display_hotels/', views.display_hotels, name='display_hotels'),
    path('profile/', views.profile, name='profile'),
    path('add_wishlist/<int:package_id>/', views.add_wishlist, name='add_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('remove_from_wishlist/<int:package_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('package_review/<int:package_id>/', views.package_review, name='feedback_form'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    # path('hotel_preview/', views.hotel_preview, name='hotel_preview'),
    # path('package_payment/', views.package_payment, name='package_payment'),
    path('logout/', views.logout, name='logout'),
    path('history_page/', views.history_page, name='history_page'),
    path('hotel_select/<int:package_split_id>/', views.hotel_select, name='hotel_select'),
    path('booking_user/', views.booking_user, name='booking_user'),


    # path('manage_bookings/', views.manage_bookings, name='manage_bookings'),
    # path('approve_booking/<int:booking_id>/', views.history_page, name='approve_booking'),
    # path('deny_booking//<int:booking_id>/', views.history_page, name='deny_booking')



]
