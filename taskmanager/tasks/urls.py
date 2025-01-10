from django.contrib import admin
from django.urls import path
from tasks import views as tasks_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', tasks_views.login_view, name='login'),
    path('profile/', tasks_views.profile_view, name='profile'),
    path('signup/', tasks_views.signup, name='signup'),
    path('subscribe/', tasks_views.subscription_view, name='subscribe'),
    path('create/',tasks_views.create),
    path('create-username/', tasks_views.create_username_view, name='create_username'),
    path('about/', tasks_views.about, name='about'),
    path('faq/', tasks_views.faq, name='faq'),
    path('contact/', tasks_views.contact, name='contact'),
    path('dashboard/<int:patient_id>/', tasks_views.patient_dashboard, name='patient_dashboard'),
    path('', tasks_views.index, name='home'),
    
]
 