from django.shortcuts import render, get_object_or_404
from .models import *
from .qr import qr_olustur
import qrcode


def qrkod_sele(request, id):
    sele = Sele.objects.filter(id=id)
    string = str(sele.get().id) + " " + \
             sele.get().sele_ismi + " " + \
             sele.get().renk + " " + \
             sele.get().kod + " " + \
             sele.get().tedarikci + " " + \
             sele.get().skt + " " + \
             sele.get().gelis_tarihi + " " + \
             sele.get().baglantili_parcalar
    code = qrcode.make(string)
    code.save('static/qr/qr.png')

    context = {

    }

    return render(request, "qr.html", context)


def qrkod_tekerlek(request, id):
    tekerlek = Tekerlek.objects.filter(id=id)
    string = str(tekerlek.get().id) + " " + \
             tekerlek.get().teker_ismi + " " + \
             tekerlek.get().jant + " " + \
             tekerlek.get().lastik + " " + \
             tekerlek.get().olcu + " " + \
             tekerlek.get().kod + " " + \
             tekerlek.get().tedarikci + " " + \
             tekerlek.get().skt + " " + \
             tekerlek.get().gelis_tarihi + " " + \
             tekerlek.get().baglantili_parcalar
    code = qrcode.make(string)
    code.save('static/qr/qr.png')

    context = {

    }

    return render(request, "qr.html", context)


def qrkod_govde(request, id):
    govde = Govde.objects.filter(id=id)
    string = str(govde.get().id) + " " + \
             govde.get().govde_ismi + " " + \
             govde.get().kadro + " " + \
             govde.get().vites + " " + \
             govde.get().kod + " " + \
             govde.get().tedarikci + " " + \
             govde.get().skt + " " + \
             govde.get().gelis_tarihi + " " + \
             govde.get().baglantili_parcalar
    code = qrcode.make(string)
    code.save('static/qr/qr.png')

    context = {

    }

    return render(request, "qr.html", context)


def qrkod_bisiklet(request, id):
    bisiklet = Bisiklet.objects.filter(id=id)
    string = str(bisiklet.get().id) + " " + \
             bisiklet.get().sele_ismi + " " + \
             bisiklet.get().renk + " " + \
             bisiklet.get().sele_kod + " " + \
             bisiklet.get().sele_tedarikci + " " + \
             bisiklet.get().sele_skt + " " + \
             bisiklet.get().sele_gelis_tarihi + " " + \
             bisiklet.get().sele_baglantili_parcalar + " " + \
             bisiklet.get().teker_ismi + " " + \
             bisiklet.get().jant + " " + \
             bisiklet.get().lastik + " " + \
             bisiklet.get().olcu + " " + \
             bisiklet.get().teker_kod + " " + \
             bisiklet.get().teker_tedarikci + " " + \
             bisiklet.get().teker_skt + " " + \
             bisiklet.get().teker_gelis_tarihi + " " + \
             bisiklet.get().teker_baglantili_parcalar + " " + \
             bisiklet.get().govde_ismi + " " + \
             bisiklet.get().kadro + " " + \
             bisiklet.get().vites + " " + \
             bisiklet.get().govde_kod + " " + \
             bisiklet.get().govde_tedarikci + " " + \
             bisiklet.get().govde_skt + " " + \
             bisiklet.get().govde_gelis_tarihi + " " + \
             bisiklet.get().govde_baglantili_parcalar
    code = qrcode.make(string)
    code.save('static/qr/qr.png')

    context = {

    }

    return render(request, "qr.html", context)


def index(request):
    seleler = Sele.objects.all()
    tekerlekler = Tekerlek.objects.all()
    govdeler = Govde.objects.all()
    bisikletler = Bisiklet.objects.all()

    context = {
        "seleler": seleler,
        "tekerlekler": tekerlekler,
        "govdeler": govdeler,
        "bisikletler": bisikletler
    }

    if request.method == "POST":
        seleid = request.POST.get('seleid')
        tekerlekid = request.POST.get('tekerlekid')
        govdeid = request.POST.get('govdeid')

        sele = get_object_or_404(Sele, id = seleid)
        tekerlek = get_object_or_404(Tekerlek, id = tekerlekid)
        govde = get_object_or_404(Govde, id = govdeid)

        bisiklet = Bisiklet.objects.create(
            sele_ismi=sele.sele_ismi,
            renk=sele.renk,
            sele_kod=sele.kod,
            sele_tedarikci=sele.tedarikci,
            sele_skt=sele.skt,
            sele_gelis_tarihi=sele.gelis_tarihi,
            sele_baglantili_parcalar=sele.baglantili_parcalar,
            teker_ismi=tekerlek.teker_ismi,
            jant=tekerlek.jant,
            lastik=tekerlek.lastik,
            olcu=tekerlek.olcu,
            teker_kod=tekerlek.kod,
            teker_tedarikci=tekerlek.tedarikci,
            teker_skt=tekerlek.skt,
            teker_gelis_tarihi=tekerlek.gelis_tarihi,
            teker_baglantili_parcalar=tekerlek.baglantili_parcalar,
            govde_ismi=govde.govde_ismi,
            kadro=govde.kadro,
            vites=govde.vites,
            govde_kod=govde.kod,
            govde_tedarikci=govde.tedarikci,
            govde_skt=govde.skt,
            govde_gelis_tarihi=govde.gelis_tarihi,
            govde_baglantili_parcalar=govde.baglantili_parcalar
        )
        bisiklet.save()

    return render(request, "anasayfa.html", context)