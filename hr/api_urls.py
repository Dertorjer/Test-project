from django.urls import (
    include,
    path,
)
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from hr.api_views import (
    EmployeeViewSet,
    PositionViewSet,
    SalaryCalculatorView,
)


router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'positions', PositionViewSet , basename='position')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('calculate_salary/', SalaryCalculatorView.as_view(), name='calculate_salary'),
]
