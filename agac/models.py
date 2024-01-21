from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

class Sele(Base):
    sele_ismi = models.CharField(max_length=100)
    renk = models.CharField(max_length=100)
    kod = models.CharField(max_length=100)
    tedarikci = models.CharField(max_length=100)
    skt = models.CharField(max_length=100)
    gelis_tarihi = models.CharField(max_length=100)
    baglantili_parcalar = models.CharField(max_length=100)

class Tekerlek(Base):
    teker_ismi = models.CharField(max_length=100)
    jant = models.CharField(max_length=100)
    lastik = models.CharField(max_length=100)
    olcu = models.CharField(max_length=100)
    kod = models.CharField(max_length=100)
    tedarikci = models.CharField(max_length=100)
    skt = models.CharField(max_length=100)
    gelis_tarihi = models.CharField(max_length=100)
    baglantili_parcalar = models.CharField(max_length=100)


class Govde(Base):
    govde_ismi = models.CharField(max_length=100)
    kadro = models.CharField(max_length=100)
    vites = models.CharField(max_length=100)
    kod = models.CharField(max_length=100)
    tedarikci = models.CharField(max_length=100)
    skt = models.CharField(max_length=100)
    gelis_tarihi = models.CharField(max_length=100)
    baglantili_parcalar = models.CharField(max_length=100)


#Bisiklet Ürün Agacı
class Bisiklet(Base):
    sele_ismi = models.CharField(max_length=100, null=True)
    renk = models.CharField(max_length=100, null=True)
    sele_kod = models.CharField(max_length=100, null=True)
    sele_tedarikci = models.CharField(max_length=100, null=True)
    sele_skt = models.CharField(max_length=100, null=True)
    sele_gelis_tarihi = models.CharField(max_length=100, null=True)
    sele_baglantili_parcalar = models.CharField(max_length=100, null=True)
    teker_ismi = models.CharField(max_length=100, null=True)
    jant = models.CharField(max_length=100, null=True)
    lastik = models.CharField(max_length=100, null=True)
    olcu = models.CharField(max_length=100, null=True)
    teker_kod = models.CharField(max_length=100, null=True)
    teker_tedarikci = models.CharField(max_length=100, null=True)
    teker_skt = models.CharField(max_length=100, null=True)
    teker_gelis_tarihi = models.CharField(max_length=100, null=True)
    teker_baglantili_parcalar = models.CharField(max_length=100, null=True)
    govde_ismi = models.CharField(max_length=100, null=True)
    kadro = models.CharField(max_length=100, null=True)
    vites = models.CharField(max_length=100, null=True)
    govde_kod = models.CharField(max_length=100, null=True)
    govde_tedarikci = models.CharField(max_length=100, null=True)
    govde_skt = models.CharField(max_length=100, null=True)
    govde_gelis_tarihi = models.CharField(max_length=100, null=True)
    govde_baglantili_parcalar = models.CharField(max_length=100, null=True)


#1. Asama Kendisi Ham maddeleri İle
#2 Parca Birlesince Yarı Mamul 2. Asama
#Hepsi Birlesinde Bisiklet 3. Asama