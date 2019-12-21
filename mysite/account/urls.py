from django.urls import re_path
from account import views
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='account/login.html'), name="user_login"),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),
    re_path(r'^register/', views.register, name="user_register"),
    re_path(r'^password-change/$', auth_views.PasswordChangeView.as_view(template_name=
                                                                         'registration/password_change_form.html'),
            name="password_change"),
    re_path(r'^password-change-done/$',
            auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
            name="password_change_done"),
    re_path(r'^password-reset/$', auth_views.PasswordResetView.as_view(template_name="account/password_reset_form.html"
                                                                       ), name="password_reset"),
    re_path(r'^password-reset-done/$',
            auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),
            name="password_reset_done"),

    re_path(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
            auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'
                                                        ), name='password-reset-confirm'),

    re_path(r'^password-reset-complete/$',
            auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
            name="password-reset-complete"),
    re_path(r'^my-information/$', views.myself, name="my_information"),
    re_path(r'^edit-my-information/$', views.myself_edit, name="edit_my_information"),
    re_path(r'^my-image/$', views.my_image, name='my_image'),

]
