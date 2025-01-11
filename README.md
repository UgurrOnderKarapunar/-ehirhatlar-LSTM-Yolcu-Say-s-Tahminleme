İBB Şehir Hatları LSTM Modeli ile Yolcu Sayısı Tahminleme 






![Açıklama](https://pbs.twimg.com/profile_images/1670793732264796167/5x0JMUSN_400x400.jpg)                                    



![Açıklama](https://i.pinimg.com/originals/e6/6f/be/e66fbe79ce5ed5427f775fdf944d3c17.png)


Bu proje, İstanbul Büyükşehir Belediyesi (İBB) Şehir Hatları'na bağlı gemilerin hatlara ve saatlere göre yolcu sayılarının tahminlemesi için LSTM modelleme projesidir.
Bu projede:
*Şehirhatları hizmetinin sürdürülebilirliğini ve kârlılığını analiz etmek,
*Operasyonel giderler, bakım maliyetleri, yakıt giderleri gibi kalemleri inceleyerek seferler başına ortalama günlük maliyetleri hesaplamak,
*Yolcu başına gelir ve sefer sayılarına göre gelir analizi yapmak,






******************************************************************************
Kullanılan Veri Seti
Bu projede kullanılan veri seti 2024 Ocak-Ekim ayları baz alınarak oluşturulmuş olup ücretlendirme ilgili ayları baz alınarak kullanılmıştır, İBB Şehir Hatları seferleri, bilet satışları, yakıt gibi operasyonel verilerden oluşmaktadır. Veri setinde yer alan ana değişkenler şunlardır:

Sefer Tarihi ve Saati: Yapılan seferin hangi tarihte ve saatte olduğunu belirtmektedir.​

Hat: Seferin hangi iskeleden/iskelelerden ulaşıma başladığı ve hangi iskele/iskelelere uğradığı ifade eder.​

Mil: Hattın tek seferdeki mesafesini belirtir.​

Yolcu Sayısı: Hatta ne kadar yolcu olduğunu belirtir.​

Ortalama Kullanılan Yakıt(Lt): Hat için kullanılan ortalama yakıt.​

Tek Seferde Kullanılan Toplam Yakıt(Lt): Hat için tek seferde kullanılan toplam yakıt.​

Yakıt Masrafı: Toplam yakıt masrafını belirtir.​

Saatlik Yolcu Ücreti: Saatlik ücretlendirmeyi belirtir



***************************************************************************************
Proje Adımları
Veri Toplama ve Temizleme:
Sefer, yolcu ve maliyet bilgilerini içeren veri seti düzenlenmiş ve eksik/veri hatalı olan kayıtlar temizlenmiştir.
Keşifsel Veri Analizi (EDA):
Veri setinde yer alan değişkenler incelenmiş, sefer başına ortalama gelir ve maliyet dağılımları analiz edilmiştir.
Kar/Zarar Analizi:
Şehirhatları başına günlük ortalama gelir ve maliyet hesaplanarak net kârlılık oranı bulunmuştur.
Öneriler:
Analiz sonuçlarına dayanarak, seferlerin karlılığını artırmak için operasyonel süreçlerde iyileştirme önerileri geliştirilmiştir.
*******************************
Teknolojiler ve İstatistiki Yöntemler
Bu projede kullanılan ana teknolojiler ve İstatistiki araçlar araçlar:

Python: Veri analizi ve hesaplamalar için temel programlama dili.
Pandas: Veri manipülasyonu ve analiz.
Matplotlib & Seaborn: Veri görselleştirme için kullanıldı.
Jupyter Notebook: Proje geliştirimi ve analizlerin yürütülmesi için.
Power BI:Veri görselleştirme için Kullanıldı.
LSTM Modeli:Derin Ağ tahmin modellemesi için kullanıldı.
Shapiro-Wilk Testi: Normalllik Testi
Kolmogorov-Smirnov (K-S) Testi:Bir örneklem ile belirli bir dağılımın (genellikle normal dağılım) veya iki örneklem arasındaki farkın istatistiksel olarak anlamlı olup olmadığını test etmek için kullanılan bir non-parametrik testtir.
Anderson-Darling Testi:Bir veri setinin belirli bir dağılıma (genellikle normal dağılım) ne kadar iyi uyduğunu test etmek için kullanılan bir güçlendirilmiş goodness-of-fit testidir.
Kruskal-Wallis H Testi:Bir veya daha fazla bağımsız gruptan gelen sıralı verilerin medyanlarının karşılaştırılmasını amaçlayan parametrik olmayan bir istatistiksel testtir.
Üç veya daha fazla bağımsız grubun medyanları arasında istatistiksel olarak anlamlı bir fark olup olmadığını test etmek için kullanılır.
Dunn's Testi:Kruskal-Wallis H Testi'nde bulunan anlamlı farklılıkları daha spesifik gruplar arasında incelemek için kullanılan post-hoc (sonrası) bir istatistiksel testtir. Bu test, farklı gruplar arasındaki medyanların karşılaştırılmasını sağlar ve hangi gruplar arasında anlamlı farklar olduğunu belirler.
Kruskal-Wallis H Testi sonucunda eğer anlamlı bir fark bulunursa, bu farkın hangi gruplar arasında olduğunu belirlemek için kullanılır.
*********************************************






**************************************************************************
Gelecekteki Geliştirme Fırsatları
Bu proje, seferlerin mali performansını analiz etmek için ilk adımdır. Gelecekte, daha kapsamlı bir tahmin modeli geliştirilebilir ve farklı sezonlara göre talep tahminleri yapılabilir. Ayrıca:

Talep Tahmini Modelleri: Mevsimsel ve saatlik yolcu talebi tahminleri için makine öğrenmesi modelleri geliştirilebilir.
Maliyet Optimizasyonu: Yakıt tüketimini giderlerini azaltacak optimizasyon yöntemleri araştırılabilir.



*************************************

NOT:Kodların tamamı PAYLAŞILMAMIŞTIR.
