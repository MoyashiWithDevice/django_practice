from django.shortcuts import render, redirect, get_object_or_404
from .models import Equip
from .forms import EquipForm

# Create your views here.
def equip_list(request):
    equips = Equip.objects.alive()
    deleted_equips = Equip.objects.dead()
    return render(
        request,
        "equip/equip_list.html",
        {"equips": equips, "deleted_equips": deleted_equips}
    )

def equip_create(request):
    if request.method == "POST":
        form = EquipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equip_list")
    else:
        form = EquipForm()
    
    return render(request, "equip/equip_form.html", {"form": form})

def equip_update(request, equip_id):
    equip = get_object_or_404(Equip, id=equip_id)
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

def equip_delete(request, equip_id):
    equip = get_object_or_404(Equip, id=equip_id)
    if request.method == "POST":
        equip.delete()
        return redirect("equip_list")
    
    return render(request, "equip/equip_confirm_delete.html",{"equip": equip})

def equip_restore(request, equip_id):
    if request.method == "POST":
        equips = Equip.objects.dead()
        for equip in equips:
            if equip.id == equip_id:
                equip.deleted_at = None
                equip.save()
                return redirect("equip_list")
    
    return render(request, "equip/equip_list.html")