from rest_framework.routers import DefaultRouter
from .views import (
    TeacherListAPIView,
    StudentListAPIView,
    StaffListAPIView
)

router = DefaultRouter()
router.register('teachers', TeacherListAPIView)
router.register('students', StudentListAPIView)
router.register('staffs', StaffListAPIView)