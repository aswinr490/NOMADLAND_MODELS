from . import views
from django.urls import path

urlpatterns = [

    path('admin/', views.admin_login, name='admin_login'),
    path('welcome_admin/', views.welcome_admin, name='welcome_admin'),
    path('agent_remove/', views.agent_remove, name='agent_remove'),
    path('agent_remove_fun/<int:agent_id>/', views.agent_remove_fun, name='agent_remove_fun'),
    path('user_remove/', views.user_remove, name='user_remove'),
    path('user_remove_fun/<int:user_id>/', views.user_remove_fun, name='user_remove_fun'),
    path('action_pending_agents/<int:agent_id>/', views.action_pending_agents, name='action_pending_agents'),
    path('pending_agents/', views.pending_agents, name='pending_agents'),
    path('notifications/', views.notification_list, name='notification_list'),

]