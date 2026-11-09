import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5 import uic

class GuvenlikSistemi(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Tasarım dosyanı doğrudan okuyoruz
        uic.loadUi(r"C:\Users\Lenovo\Desktop\gömülü\arayuz.ui", self)
        
        # --- GÜNCEL RENK PALETİ (Antrasit, Siyah ve Siber Mavi) ---
        self.setStyleSheet("""
            QMainWindow {
                background-color: #070a10;
            }
            QGroupBox {
                border: 1px solid #3a3f4c;
                border-radius: 8px;
                margin-top: 15px;
                color: #00a8ff;
                font-weight: bold;
                background-color: #1a1e24;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 5px;
                left: 15px;
            }
            QLabel {
                color: #d1d5db;
                font-size: 13px;
                font-weight: bold;
            }
            QLabel#baslik_etiketi {
                color: #00a8ff;
                margin-bottom: 10px;
            }
            QLabel#kamera_ekrani {
                border: 2px dashed #00a8ff;
                background-color: #000000;
                color: #555555;
            }
            QPushButton {
                background-color: #111827;
                color: #ffffff;
                border: 1px solid #00a8ff;
                border-radius: 6px;
                padding: 12px;
                font-size: 13px;
                font-weight: bold;
                margin-bottom: 5px;
            }
            QPushButton:hover {
                background-color: #00a8ff;
                color: #ffffff;
            }
            QListWidget {
                background-color: #000000;
                color: #e6e6e6;
                border: 1px solid #3a3f4c;
                border-radius: 5px;
                padding: 10px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 13px;
            }
        """)
        # -------------------------------------------------------------------------------
        
        self.kamera = None
        self.zamanlayici = QTimer()
        self.zamanlayici.timeout.connect(self.kare_guncelle)
        
        self.baslat_butonu.clicked.connect(self.kamera_baslat)
        self.cikis_butonu.clicked.connect(self.cikis_yap)
        
        self.yuz_algilayici = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.son_yuz_zamani = 0  
        
        self.log_ekle("Sistem başlatıldı, komut bekleniyor.")

    def kamera_baslat(self):
        if not self.zamanlayici.isActive():
            self.kamera = cv2.VideoCapture(0)
            self.zamanlayici.start(30)
            self.baslat_butonu.setText("Kamerayı Durdur")
            self.log_ekle("Kamera açıldı. Yüz taraması yapılıyor...")
        else:
            self.zamanlayici.stop()
            if self.kamera:
                self.kamera.release()
            self.kamera_ekrani.clear()
            self.kamera_ekrani.setText("Kamera bağlantısı bekleniyor...")
            self.baslat_butonu.setText("Kamerayı Başlat")
            self.log_ekle("Kamera durduruldu.")

    def kare_guncelle(self):
        ret, frame = self.kamera.read()
        if ret:
            gri_kare = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            yuzler = self.yuz_algilayici.detectMultiScale(gri_kare, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
            
            for (x, y, w, h) in yuzler:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            if len(yuzler) > 0:
                su_an = QDateTime.currentMSecsSinceEpoch()
                if su_an - self.son_yuz_zamani > 3000:
                    self.log_ekle(f"🔵 BİLGİ: Ekranda {len(yuzler)} kişi tespit edildi!")
                    self.son_yuz_zamani = su_an

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qt_resim = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            
            esnetilmis_resim = qt_resim.scaled(self.kamera_ekrani.width(), self.kamera_ekrani.height())
            self.kamera_ekrani.setPixmap(QPixmap.fromImage(esnetilmis_resim))

    def log_ekle(self, mesaj):
        zaman = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.log_ekrani.addItem(f"[{zaman}] - {mesaj}")
        self.log_ekrani.scrollToBottom()

    def cikis_yap(self):
        if self.kamera:
            self.kamera.release()
        self.log_ekle("Sistem kapatılıyor...")
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = GuvenlikSistemi()
    pencere.show()
    sys.exit(app.exec_())