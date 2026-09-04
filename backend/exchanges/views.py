from datetime import timedelta
import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from listings.models import Listing
from .forms import ExchangeRequestForm
from .models import ExchangeRequest, Exchange


@login_required
def create_request(request, listing_id):
    listing = get_object_or_404(
        Listing,
        id=listing_id,
        is_available=True
    )

    if listing.owner == request.user:
        return redirect("listing_detail", pk=listing.id)

    existing_request = ExchangeRequest.objects.filter(
        listing=listing,
        requester=request.user,
        status="pending"
    ).first()

    if existing_request:
        return redirect("my_requests")

    if request.method == "POST":
        form = ExchangeRequestForm(request.POST)

        if form.is_valid():
            exchange_request = form.save(commit=False)
            exchange_request.listing = listing
            exchange_request.requester = request.user
            exchange_request.save()

            return redirect("my_requests")

    else:
        form = ExchangeRequestForm()

    return render(
        request,
        "exchanges/request_form.html",
        {
            "form": form,
            "listing": listing
        }
    )


@login_required
def my_requests(request):
    requests = ExchangeRequest.objects.filter(
        requester=request.user
    ).select_related(
        "listing",
        "listing__owner"
    ).order_by("-created_at")

    return render(
        request,
        "exchanges/my_requests.html",
        {"requests": requests}
    )


@login_required
def received_requests(request):
    requests = ExchangeRequest.objects.filter(
        listing__owner=request.user
    ).select_related(
        "listing",
        "requester"
    ).order_by("-created_at")

    return render(
        request,
        "exchanges/received_requests.html",
        {"requests": requests}
    )


@login_required
def approve_request(request, request_id):
    exchange_request = get_object_or_404(
        ExchangeRequest,
        id=request_id,
        listing__owner=request.user
    )

    if request.method == "POST" and exchange_request.status == "pending":

        exchange_request.status = "approved"
        exchange_request.save()

        due_date = timezone.now().date() + timedelta(
            days=exchange_request.listing.duration_days
        )

        handover_code = str(random.randint(100000, 999999))

        Exchange.objects.create(
            request=exchange_request,
            borrower=exchange_request.requester,
            owner=exchange_request.listing.owner,
            status="approved",
            due_date=due_date,
            handover_code=handover_code
        )

    return redirect("received_requests")


@login_required
def reject_request(request, request_id):
    exchange_request = get_object_or_404(
        ExchangeRequest,
        id=request_id,
        listing__owner=request.user
    )

    if request.method == "POST" and exchange_request.status == "pending":
        exchange_request.status = "rejected"
        exchange_request.save()

    return redirect("received_requests")