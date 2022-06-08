from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from bridgethegapapi.views import register_user, login_user, TutorView, SessionView
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tutors', TutorView, 'tutor')
router.register(r'sessions', SessionView, 'session')


urlpatterns = [
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]


# Notice that the register_user and login_user functions are imported into the module. 
#  Then they are used to map a route to  that view.