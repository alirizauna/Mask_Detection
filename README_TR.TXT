KURULUM:

Mask_Detection dosyası proje dosyası olduğundan istediğiniz herhangi bir dizine atın.
Pycharm'da FILE OPEN dedikten  sonra Mask_Detection'u seçebilir ve projeyi içeri alabilirsiniz.
Kullanmak istedğiniz webcam ile maske tespiti ise MaskeTespit-PcWebcam.py dosyasını açmanız yeterlidir.
Eğer telefon kamerasını kullanmak istiyorsanız telefona IP Webcam uygulamasını indirin.
178. satırdaki url değerine IP Webcam servisi başlatıldığında altta yazan ip değerini girin


BAŞLATIRKEN:

Kullanmak istedğiniz kamera,webcam ise MaskeTespit-PcWebcam.py dosyasını çalıştırmanız yeterlidir.
Eğer telefon kamerasını kullanmak istiyorsanız telefondaki IP Webcam uygulamasının servisini başlatmalısınız ve bilgisayarla aynı ağda olduğuna emin olmalısınız.
Ardından MaskeTespit_TelefonKamerasi_Tr.py dosyasını çalıştırmanız yeterli olacaktır.

Not:Kütüphanelerden kaynaklı sorun yaşarsanız yeniden yüklemenizi tavsiye ederiz.Projenin ana dosyasında farklı dosyalar denendiğinden farklı kütüphanelerde yüklendi.
Program yazılırken kullanılan Python Sürümü:3.7.6 ,Pycharm Sürümü:2020.2 ,Pip version=20.2.2

ÇALIŞIRKEN:

Orta ekranda anlık Webcam Görüntüsü belirir.Programın seçtiği yüzler mavi dikdörtgen ile çizilir. Tespit edilen yüzün x,y noktası yukardaki iki yeşil çizgi arasına girerse fotoğraf çekilir.
Çekilen fotoğrafta maske tespit edilemediyse C://screen/Maskesiz dosyasına kaydedilir.
Screen klasörü ve içerisindeki Maskeli,Maskesiz klasörü yoksa C dizini içerisinde bu dosyalar oluşturulur. 
Eğer belirlenen yüzün içerisinde maske var ise maske açık mavi dikdörtgenler ile çizilir. 
İki yeşil çizgi arasına girilen yüzde maske varsa fotoğraf çekilir ve C://screen/Maskeli dosyasına kaydedilir.

Çekilen son fotoğraflar sırasıyla ekranın sağ ve sol bölgesindeki çerçevelerde gösterilir.
Sol tarafta maskesizken çekilen fotoğraflar,sağda maskeliyken çekilen fotoğraflar yer alır.



