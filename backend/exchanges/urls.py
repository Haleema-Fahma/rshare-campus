from django.urls import path

from .views import (
    create_request,
    my_requests,
    received_requests,
    approve_request,
    reject_request,
)


urlpatterns = [
    path(
        "request/<int:listing_id>/",
        create_request,
        name="create_request"
    ),

    path(
        "my-requests/",
        my_requests,
        name="my_requests"
    ),

    path(
        "received/",
        received_requests,
        name="received_requests"
    ),

    path(
        "approve/<int:request_id>/",
        approve_request,
        name="approve_request"
    ),

    path(
        "reject/<int:request_id>/",
        reject_request,
        name="reject_request"
    ),
]