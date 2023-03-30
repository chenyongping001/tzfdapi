# from rest_framework.routers import DefaultRouter
# from .views import EmployeePhoneViewSet

# router = DefaultRouter()
# router.register("employeephones", EmployeePhoneViewSet)
# urlpatterns = router.urls


from rest_framework.routers import DefaultRouter
from .views import EmployeePhoneViewSet

router = DefaultRouter()
router.register('employeephones', EmployeePhoneViewSet)
urlpatterns = router.urls
