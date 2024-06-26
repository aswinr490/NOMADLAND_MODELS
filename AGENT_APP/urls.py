from . import views
from django.urls import path

from .views import *

urlpatterns = [

    path('agent_login/', views.agent_login, name='agent_login'),
    path('welcome_agent/', views.welcome_agent, name='welcome_agent'),
    path('agent_manage/', views.agent_manage, name='agent_manage'),
    path('manage_package/', views.manage_package, name='manage_package'),
    path('agent_communication/', views.agent_communication,name='agent_communication'),
    path('agent_analyticgraph',views.agent_analyticgraph, name='agent_analyticgraph'),
    path('activities/', views.activities, name='activities'),
    path('add_hotel/', views.add_hotels, name='add_hotel'),
    path('logout/', views.logout, name='logout'),
    path('agent_offer/', views.agent_offer, name='agent_offer'),
    path('package_update/<int:package_id>/', views.package_update, name='package_update'),
    path('package_remove/<int:package_id>/', views.package_remove, name='package_remove'),
    path('hotel_img_del/<int:hotel_image_id>/',views.hotel_img_del,name='hotel_img_del'),
    path('pack_img_del/<int:image_id>/', views.pack_img_del, name='pack_img_del'),
    # path('agent_booking/',views.booking_approval, name='booking-approval'),
    # path('agent_booking/<int:booking_id>/', views.agent_booking, name='agent_booking'),
]