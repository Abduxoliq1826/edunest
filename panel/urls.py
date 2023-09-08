from django.urls import path
from .views import *

urlpatterns = [

    path('dashboard', admin_dashboard, name='admin_dashboard'),
    path('page_404', page_404, name='page_404'),
    path('', login_view, name='login'),
    path('logout_view', logout_view, name='logout'),
    path('profile', profile, name='profile'),
    path('reset_password', reset_password, name='reset_password'),



    path('course', Course_views, name='course'),
    path('course_single/<int:pk>/', course_single, name='course_single'),
    path('add_course', add_course, name='add_course'),
    path('update_curse/<int:pk>/', update_curse, name='update_course'),
    path('delete_course/<int:pk>/', delete_course, name='delete_course'),
    path('delete_student/<int:pk>/', delete_student, name='delete_student'),

    #     # Student
    path('student', Student_views, name='student'),
    path('new_student', Student_views_new, name='student_new'),
    path('deleted_student', Student_views_deleted, name='student_deleted'),
    path('finished_student', Student_views_finished, name='student_finished'),
    path('add_student', add_student, name='add_student'),
    path('finished_student/<int:pk>/', finished_student, name='finished_student'),
    path('deleted_student/<int:pk>/', deleted_student, name='deleted_student'),


    # Link
    path('link', Link_views, name='link'),
    path('add_link', add_link, name='add_link'),
    path('update_link/<int:pk>/', update_link, name='update_link'),
    path('delete_link/<int:pk>/', delete_link, name='delete_link'),


    # Mock
    path('mock', Mock_views, name='mock'),
    path('add_mock', add_mock, name='add_mock'),
    path('disactive_mock/<int:pk>/', disactive_mock, name='disactive_mock'),
    path('student_mock/<int:pk>/', student_mock, name='student_mock'),
    path('active_mock/<int:pk>/', active_mock, name='active_mock'),
    path('update_mock/<int:pk>/', update_mock, name='update_mock'),
    path('delete_mock/<int:pk>/', delete_mock, name='delete_mock'),
    ]