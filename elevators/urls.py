from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElevatorViewSet, ElevatorSystemViewSet

router = DefaultRouter()
router.register(r'elevators', ElevatorViewSet, basename='elevator')

elevator_system_router = DefaultRouter()
elevator_system_router.register(
    r'elevators', ElevatorSystemViewSet, basename='elevator-system')

urlpatterns = [
    path('', include(router.urls)),
    path('elevator-system/', ElevatorSystemViewSet.as_view({'get': 'requests'})),
    path('elevators/<int:pk>/requests/',
         ElevatorViewSet.as_view({'get': 'requests'}), name='elevator-requests'),
    path('elevators/<int:pk>/next_destination/', ElevatorViewSet.as_view(
        {'get': 'next_destination'}), name='elevator-next-destination'),
    path('elevators/<int:pk>/is_moving_up/',
         ElevatorViewSet.as_view({'get': 'is_moving_up'}), name='elevator-is-moving-up'),
    path('elevators/<int:pk>/save_request/',
         ElevatorViewSet.as_view({'post': 'save_request'}), name='elevator-save-request'),
    path('elevators/<int:pk>/mark_not_working/', ElevatorViewSet.as_view(
        {'post': 'mark_not_working'}), name='elevator-mark-not-working'),
    path('elevators/<int:pk>/open_door/',
         ElevatorViewSet.as_view({'post': 'open_door'}), name='elevator-open-door'),
    path('elevators/<int:pk>/close_door/',
         ElevatorViewSet.as_view({'post': 'close_door'}), name='elevator-close-door'),
]
