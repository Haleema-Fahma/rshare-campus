from django.urls import path

from .views import (
    explore,
    listing_detail,
    create_listing,
    edit_listing,
    delete_listing,
    my_listings,
)


urlpatterns = [

    path(
        "",
        explore,
        name="explore"
    ),

    path(
        "listing/<int:pk>/",
        listing_detail,
        name="listing_detail"
    ),

    path(
        "create/",
        create_listing,
        name="create_listing"
    ),

    path(
        "listing/<int:pk>/edit/",
        edit_listing,
        name="edit_listing"
    ),

    path(
        "listing/<int:pk>/delete/",
        delete_listing,
        name="delete_listing"
    ),

    path(
        "my/",
        my_listings,
        name="my_listings"
    ),
]