# OOP TEMEL PRENSİPLERİ VE İLİŞKİLER
# KALITIM
# ÇOK BİÇİMLİLİK
# KAPSÜLLEME
# SOYUTLAMA

"""
OOP Prensiplerinde amaç
-> Bir kodun yeniden kullanılabilirliğini sağlama
-> Kodun  tekrar etmesini önleme
-> Sınıflar birbiri ile ilişki kurarken olabilidğince esnek olmalı
-> Sınıflar birbirlerine bağımlı olmamalıdır
"""

"""
Kalıtımın Dezavantajları
-> Kalıtım bir sınıfa tamamen bağımlı yapar. 
-> Kalıtım esnek bir yapı sunmaz
-> Çünkü kalıtım sebebiyle base classın gerekli gereksiz tüm özelliklerine erişmiş oluruz.
-> Base classta yapılan bir değişiklik miras alan tüm sınıflara etki eder
-> O yüzden kalıtımı olabilidğince az ve gerekli durumlarda kullanmalıyız.
!!! Mesela base classı miras alan 5 tane sınıfımız var diyelim. Baseclassımıza sonradan id
ekledik ama bu id değişkeni sadece miras alan 2 sınıfın işine yarıyor. Bu durumda sadece o iki sınıfta 
değil diğer tüm sınıfların super fonksiyonunda bu id yi tanımlamamız lazım. İŞİMİZ ZORLAŞTI
ESNEKLİK BOZULDU. O yüzden olabilidğince kalıtımı gerekli durumlarda kullanmalıyız
"""


