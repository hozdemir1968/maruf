from django.shortcuts import render, get_object_or_404, redirect, Http404
from .models import Announce
from .forms import AnnounceForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def announce_index(request):
    announce_list = Announce.objects.all()
    # filter
    query = request.GET.get("search")
    if query:
        announce_list = announce_list.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(user__first_name__icontains=query)
        ).distinct()
    
    paginator = Paginator(announce_list, 10)
    page_number = request.GET.get("page")
    announces = paginator.get_page(page_number)
    context = {"announces": announces}
    return render(request, "announce/index.html", context)


def announce_create(request):
    if not request.user.is_authenticated and request.user.is_superuser:
        return Http404
    form = AnnounceForm(request.POST or None)
    if form.is_valid():
        announce = form.save(commit=False)
        announce.user = request.user
        announce.save()
        messages.success(request, "Başarılı bir şekilde oluşturuldu!")
        return render(request, "announce/detail.html", {"announce": announce})
    context = {
        "form": form,
    }
    return render(request, "announce/form.html", context)


def announce_detail(request, id):
    announce = get_object_or_404(Announce, id=id)
    context = {
        "announce": announce,
    }
    return render(request, "announce/detail.html", context)


def announce_update(request, id):
    if not request.user.is_authenticated:
        return Http404
    announce = get_object_or_404(Announce, id=id)
    form = AnnounceForm(request.POST or None, instance=announce)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde değiştirildi!")
        return render(request, "announce/detail.html", {"announce": announce})
    context = {
        "form": form,
    }
    return render(request, "announce/form.html", context)


def announce_delete(request, id):
    if not request.user.is_authenticated:
        return Http404
    announce = get_object_or_404(Announce, id=id)
    announce.delete()
    return redirect("announce:index")
