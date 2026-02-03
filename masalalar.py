# 1-masala
# Yechim
# class Transport:
#   def __init__(self, model: str, yil: int) -> None:
#         self.model = model
#         self.yil = yil
#
#     def malumot(self) -> str:
#         return f"Model: {self.model}, Yil: {self.yil}"
#
#
# class Avtomobil(Transport):
#     def __init__(self, model: str, yil: int, yonilgi_turi: str) -> None:
#         super().__init__(model, yil)
#         self.yonilgi_turi = yonilgi_turi
#
#     def malumot(self) -> str:
#         baza = super().malumot()
#         return f"{baza}, Yonilg'i: {self.yonilgi_turi}"
#
#
# class Avtobus(Transport):
#     def __init__(self, model: str, yil: int, orinlar_soni: int) -> None:
#         super().__init__(model, yil)
#         self.orinlar_soni = orinlar_soni
#
#     def malumot(self) -> str:
#         baza = super().malumot()
#         return f"{baza}, O'rinlar: {self.orinlar_soni}"
#
#
# a = Avtomobil("Cobalt", 2022, "benzin")
# print(a.malumot())
#
# b = Avtobus("Isuzu", 2018, 40)
# print(b.malumot())

#
# # 2-masala
# class Kitob:
#     def __init__(self, nom, muallif, yil):
#         self.nom = nom
#         self.muallif = muallif
#         self.yil = yil
#
#     def taqdimot(self) -> str:
#         return f"Nom: {self.nom}, muallif: {self.muallif}, yil: {self.yil}, [Elektron, {fayl_hajmi_mb}MB]"
#
# class ElektronKitob(Kitob):
#     def __init__(self, nom: str, muallif: str, yil: int, fayl_hajmi_mb: int) -> None:
#         super().__init__(nom, muallif, yil)
#         self.fayl_hajmi_mb = fayl_hajmi_mb
#
#     def AudioKitob(Kiob):
#         soat = super().AudioKitob()
#         return f"{soat}, elektron:  {fayl_hajmi_mb}"
#
#
# e = ElektronKitob("Python asoslari", "Ali", 2023, 5)
# a = AudioKitob("O'tkan kunlar", "Abdulla Qodiriy", 2020, 12)
#
# print(e.taqdimot())
# print(a.taqdimot())


#
# # 3-masala
# class Xodim:
#     def __init__(self, ism, asosiy_maosh):
#         self.ism = ism
#         self.asosiy_maosh = asosiy_maosh
#
#
# class Mahsulot:
#     def __init__(self, nom, narx):
#         self.nom = nom
#         self.narx = narx
#
#     def chegirma_narx(self, narx):
#         chegirma = self.narx * foiz // 100
#         return f"Chegirmadan keyin: {self.narx - chegirma}"
#
# class Elektronika(Mahsulot):
#     def __init__(self, nom, narx, Kafolat_oy):
#         super().__init__(nom, narx)
#         self.Kafolat_oy = Kafolat_oy
#
#     def malumot(self):
#         return f"Nom: {self.nom}, Narx: ${self.narx}, Kafolat: {self.Kafolat_oy}"
#
# class OziqOvqat(Mahsulot):
#     def __init__(self, nom, narx, yaroqlilik_kuni):
#         super().__init__(nom, narx)
#         self.yaroqlilik_kuni = yaroqlilik_kuni
#     def malumot(self):
#         return f"Nomi: {self.nom}, Narx: {self.narx}"
#
#
# telefon = Elektronika("Iphone", 1500, 12)
# non = OziqOvqat("non", "3000", 1)
# print(telefon.malumot())
# print(non.malumot())
# print(telefon.chegirma_narx(10))





# 4-masala
























# 5-masala

class Shaxs:
    def __init__(self, ism):
        self.ism = ism

class Talaba(Shaxs):
    def __init__(self, ism, id_raqam):
        super().__init__(ism)
        self.id_raqam = id_raqam

class ImtihonNatijasi(Talaba):
    def __init__(self, ism, id_raqam, baholar):
        super().__init__(ism, id_raqam)
        self.baholar = baholar

    def ortalama(self):
        ortacha = sum(self.baholar) / len(self.baholar)
        return ortacha

    def status(self):
        o = self.ortalama()
        if o >= 86:
            return "A'lo!"
        elif 71 <= o <= 85:
            return "Yaxshi!"
        elif 56 <= o <= 70:
            return "Qoniqarli!"
        else:
            return "Qoniqarsiz!"

natija = ImtihonNatijasi("Sherzodbek", "IT001", [78, 64, 98])

print(natija.ism())
print(natija.id_raqam())
print(natija.ortalama())
print(natija.status())





























# 7-masala

# class Hisob:
#     def __init__(self, raqam, egasi, balans):
#         self.raqam = raqam
#         self.egasi = egasi
#         self.balans = balans
#
#     def kirim(self, summa):
#         self.balans += summa
#
#     def chiqim(self, summa):
#         self.balans -= summa
#
#
# class JamgArmanMixin:
#     def hisobla_foiz(self):
#         return self.balans * self.foiz_stavka / 100
#
# class KreditMixin:
#     def chiqim(self, summa):
#         if self.balans - summa >= -self.limit:
#             self.balans -= summa
#         else:
#             print("Kredit limiti oshib ketdi!")
#
# class VipHisob(JamgArmanMixin, KreditMixin, Hisob):
#     def __init__(self, raqam, egasi, balans, foiz_stavka, limit):
#         super().__init__(raqam, egasi, balans)
#         self.foiz_stavka = foiz_stavka
#         self.limit = limit
#
#
# v = VipHisob("001", "Amirxon", 2_000_000, foiz_stavka=12, limit=1)
# v.chiqim(1000000)
# print(v.balans)



#
# # 7-masala
# class kurs:
#     def __init__(self, nom, davomiylik_hafta, narx):
#         self.nom = nom
#         self.davomiylik_hafta = davomiylik_hafta
#         self.narx = narx
#
#     def malumot(self):

# 8-masala





# 9-masala

from abc import ABC, abstractmethod
from typing import List

class JamoaAzo(ABC):
    def __init__(self, ism):
        self.ism = ism


    @abstractmethod
    def vazifa(self):
        """Har bir rol ucun aniq vazifalarni qaytaradi"""
        return NotImplementedError

class BackendDasturchi(JamoaAzo):
    def vazifa(self):
        return "API va ma'lumotlar bazasi ishlaydi"

class FrontedDasturchi(JamoaAzo):
    def vazifa(self):
        return "UI va foyalanuchi interfeysini yaratadi"

class Tester(JamoaAzo):
    def vazifa(self):
        return "Tizimni test qiladi"

def hisobot(azolar: List[JamoaAzo]):
    for azo in azolar:
        print(f"Ism: {azo.ism}, Vazifa: {azo.vazifa()}")

jamoa = [
    BackendDasturchi("Marjona"),
    FrontedDasturchi("Rayxona"),
    Tester("Maftuna")
]













