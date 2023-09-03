#volume balok
print ("menghitung volume balok versi Python")
panjang = int(input('masukan panjang balok'))
lebar = int(input('masukan lebar balok'))
tinggi = int(input('masukan tinggi balok'))
volume = int(panjang*lebar*tinggi)

print("---------------hasil volume balok---------------")
print ("hasilnya ialah =", volume)

#volume tabung

print("menghitung volume tabung")

pi = 22/7
jarijari = float(input("masukan jari-jarinya : "))
tinggi = float(input("masukan tinggi : "))
volume = pi*jarijari*jarijari*tinggi

print("---------------hasil volume tabung---------------")
print ( "volume tabung = " , volume)

#volume bola

print("menghitung volume bola")

pi = 22/7
jarijari = float(input("masukan jari-jarinya : "))
volume = 4/3*pi*(jarijari*jarijari*jarijari)
print("---------------hasil volume tabung---------------")
print ("volume bola =", volume)
