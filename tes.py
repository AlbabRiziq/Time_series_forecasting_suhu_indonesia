# hehe = False

# while not hehe:
#     angka = int(input("Masukkan angka: "))
#     if angka < 50:
#         if angka % 2 == 0:
#             print("Benar")
#             hehe = True
#         else:
#             print("Salah")
#     else:
#         print("Salah")


daftar_kota = ["Jakarta", "Suarabaya", "Bandung",
               "Semarang", "Tegal", "Kebumen", "Purwakarta"]

i = 0

print(len(daftar_kota))
while i < len(daftar_kota):
    print(daftar_kota[i])
    i += 1
print("\n")
while daftar_kota:
    print(daftar_kota.pop())
    print("\n")
