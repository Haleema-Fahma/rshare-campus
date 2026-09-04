from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ListingForm
from .models import Listing


def explore(request):

    listings = Listing.objects.filter(
        is_available=True
    ).select_related("owner")

    search = request.GET.get("search", "")
    listing_type = request.GET.get("type", "")
    category = request.GET.get("category", "")

    if search:
        listings = listings.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(category__icontains=search)
        )

    if listing_type:
        listings = listings.filter(
            listing_type=listing_type
        )

    if category:
        listings = listings.filter(
            category=category
        )

    context = {
        "listings": listings,
        "search": search,
        "selected_type": listing_type,
        "selected_category": category,
    }

    return render(
        request,
        "listings/explore.html",
        context
    )


def listing_detail(request, pk):

    listing = get_object_or_404(
        Listing,
        pk=pk
    )

    return render(
        request,
        "listings/detail.html",
        {"listing": listing}
    )


@login_required
def create_listing(request):

    if request.method == "POST":

        form = ListingForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            listing = form.save(
                commit=False
            )

            listing.owner = request.user

            listing.save()

            return redirect(
                "listing_detail",
                pk=listing.pk
            )

    else:

        form = ListingForm()

    return render(
        request,
        "listings/form.html",
        {
            "form": form,
            "page_title": "Share Something"
        }
    )


@login_required
def edit_listing(request, pk):

    listing = get_object_or_404(
        Listing,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":

        form = ListingForm(
            request.POST,
            request.FILES,
            instance=listing
        )

        if form.is_valid():

            form.save()

            return redirect(
                "listing_detail",
                pk=listing.pk
            )

    else:

        form = ListingForm(
            instance=listing
        )

    return render(
        request,
        "listings/form.html",
        {
            "form": form,
            "page_title": "Edit Listing"
        }
    )


@login_required
def delete_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk, owner=request.user)

    if request.method == "POST":
        listing.delete()
        return redirect("explore")

    return render(request, "listings/delete.html", {"listing": listing})


@login_required
def my_listings(request):

    listings = Listing.objects.filter(
        owner=request.user
    ).order_by("-created_at")

    return render(
        request,
        "listings/my_listings.html",
        {"listings": listings}
    )