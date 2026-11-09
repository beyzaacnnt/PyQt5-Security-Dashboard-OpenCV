Bu proje, ESP32-CAM ve OpenCV tabanlı yüz tanıma özellikli bir yoklama sistemi için geliştirilmekte olan masaüstü arayüz (GUI) prototipidir. Şu anki aşamada uygulamanın modern kullanıcı arayüzü PyQt5 (Qt Designer) kullanılarak tasarlanmış olup, donanım ve veritabanı entegrasyonları geliştirilme aşamasındadır.

🌟 Mevcut Durum (Sadece Arayüz)
Modern Masaüstü Paneli: Qt Designer ve PyQt5 kullanılarak tasarlanmış kullanıcı dostu arayüz.

Kamera Akış Ekranı: Görüntü işleme çıktılarının yansıtılacağı ana vizör tasarımı.

Kontrol ve Kayıt Menüleri: Yoklama listelerinin ve manuel kayıt işlemlerinin yapılacağı UI bileşenleri.

🗺️ Yol Haritası (Planlanan Özellikler)
[ ] Görüntü İşleme: OpenCV entegrasyonu ile kamera akışının arayüze aktarılması.

[ ] Donanım Entegrasyonu: ESP32-CAM üzerinden Wi-Fi ile anlık görüntü alınması.

[ ] Yüz Tanıma: Yüz hatlarının analiz edilerek kişilerin otomatik tespiti.

[ ] Veritabanı (SQLite): Tanınan kişilerin giriş-çıkış verilerinin SQLite ile kaydedilmesi.
Kullanılan Teknolojiler (Şu anki aşama)
Arayüz (GUI): Python, PyQt5, Qt Designer

Planlanan Teknolojiler: OpenCV, SQLite, ESP32-CAM (C++)

This project is a desktop Graphical User Interface (GUI) prototype currently in development for an ESP32-CAM and OpenCV-based facial recognition attendance system. At this stage, the modern desktop panel has been built using PyQt5 and Qt Designer, while the hardware and database integrations are actively in the pipeline.Current State (UI Only)
Modern Desktop Panel: A user-friendly layout designed with Qt Designer and PyQt5.

Camera Feed Viewport: UI placeholders for the upcoming live OpenCV video stream.

Control Menus: Interface components designed for manual registration and attendance logs.

🗺️ Roadmap (Upcoming Features)
[ ] Computer Vision: Integrating OpenCV to feed the live camera stream into the GUI.

[ ] Hardware Integration: Connecting the ESP32-CAM via Wi-Fi to capture real-time footage.

[ ] Facial Recognition: Implementing automated detection and identification algorithms.

[ ] Database (SQLite): Logging entry/exit times securely into a local SQLite database.Tech Stack (Current)
GUI Development: Python, PyQt5, Qt Designer

Planned Tech: OpenCV, SQLite, ESP32-CAM (C++)
