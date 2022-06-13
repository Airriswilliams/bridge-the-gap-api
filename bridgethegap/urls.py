from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from bridgethegapapi.views import register_user, login_user, TutorView, SessionView, ParentView, LanguageView, ReviewView
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tutors', TutorView, 'tutor')
router.register(r'sessions', SessionView, 'session')
router.register(r'parents', ParentView, 'parent')
router.register(r'languages', LanguageView, 'language')
router.register(r'reviews', ReviewView, 'review')




urlpatterns = [
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Notice that the register_user and login_user functions are imported into the module. 
#  Then they are used to map a route to  that view.