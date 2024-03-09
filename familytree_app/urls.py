#/home/keyurjoshi/familytree_project/familytree_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views  # Import auth_views



app_name = 'familytree_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('family-members/', views.family_member_list, name='family_member_list'),
    path('family-members/create/', views.family_member_create, name='family_member_create'),
    path('family-members/<int:pk>/', views.family_member_detail, name='family_member_detail'),
    path('family-members/<int:pk>/update/', views.family_member_update, name='family_member_update'),
    path('family-members/<int:pk>/delete/', views.family_member_delete, name='family_member_delete'),
    path('family-members/<int:pk>/add-child/', views.family_member_add_child, name='family_member_add_child'),
    path('view_all_roots/', views.view_all_roots, name='view_all_roots'),
    path('view_all_leaves/', views.view_all_leaves, name='view_all_leaves'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),



    path('search-by-name/', views.search_by_name, name='search_by_name'),  # New URL mapping


    path('filter/gender/', views.filter_by_gender, name='filter_by_gender'),


    path('view_child_tree/<int:member_id>/', views.view_child_tree, name='view_child_tree'),



    path('msgk-list/', views.msgk_list, name='msgk_list'),
    path('msgkind-entries/<int:msgkind_id>/', views.msgkind_entries, name='msgkind_entries'),
    path('sandesha-detail/<int:sandesha_id>/', views.sandesha_detail, name='sandesha_detail'),
    path('instructions/', views.instructions_view, name='instructions'),  # Update the name here






]






