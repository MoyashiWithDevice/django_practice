from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Equip
from .forms import EquipForm

# Create your views here.
@login_required
def equip_list(request):
    equips = Equip.objects.alive()
    filtered_equips = equips.filter(user=request.user)
    deleted_equips = Equip.objects.dead()
    filtered_deleted_equips = deleted_equips.filter(user=request.user)

    return render(
        request,
        "equip/equip_list.html",
        {"equips": filtered_equips, "deleted_equips": filtered_deleted_equips}
    )

@login_required
def equip_create(request):
    if request.method == "POST":
        form = EquipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equip_list")
    else:
        form = EquipForm()
    
    return render(request, "equip/equip_form.html", {"form": form})

@login_required
def equip_update(request, equip_id):
    equip = get_object_or_404(Equip, id=equip_id, user=request.user,)
    if request.method == "POST":
        form = EquipForm(
            request.POST,
            instance=equip
        )
        if form.is_valid():
            form.save()
            return redirect("equip_list")
    else:
        form = EquipForm(instance=equip)
    
    return render(request, "equip/equip_form.html",{"form": form})

@login_required
def equip_delete(request, equip_id):
    equip = get_object_or_404(Equip, id=equip_id, user=request.user,)
    if request.method == "POST":
        equip.delete()
        return redirect("equip_list")
    
    return render(request, "equip/equip_confirm_delete.html",{"equip": equip})

@login_required
def equip_restore(request, equip_id):
    if request.method == "POST":
        equips = Equip.objects.dead()
        filtered_equips = equips.filter(user=request.user)
        for equip in filtered_equips:
            if equip.id == equip_id:
                equip.deleted_at = None
                equip.save()
                return redirect("equip_list")
    
    return render(request, "equip/equip_list.html")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"