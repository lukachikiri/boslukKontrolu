kullaniciAdi=input("Kullanıcı Adınızı Giriniz: ")
sifre=input("Şifrenizi Giriniz: ")

if(kullaniciAdi!=""or sifre!=""):
    if(kullaniciAdi=="ali"and sifre=="123"):
        print("Hoşgeldiniz",kullaniciAdi)
    else:
        print("Kullanıcı Adı veya Şifre Hatalı")
else:
    print("Kullanıcı Adı veya Şifre Boş Bırakılamaz")