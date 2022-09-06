a = int(input("Masukkan nilai ujian teori"))
b = int(input("Masukkan nilai ujian praktek"))
c = 70
if a>c and b>c:
    print("Selamat, anda lulus!")
elif a>c and b<c:
    print("Anda harus mengulang ujian praktek.")
elif a<c and b>c:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")