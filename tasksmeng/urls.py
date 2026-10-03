from rest_framework.routers import DefaultRouter
from .views import TaskView


router = DefaultRouter()

router.register(
    "tasks",
    TaskView,
    basename="tasks",
)

urlpatterns = router.urls