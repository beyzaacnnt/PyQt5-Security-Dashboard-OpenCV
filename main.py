import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap

class SecurityDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Security Dashboard - Face Recognition")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #2b2b2b; color: #ffffff;") # Koyu granit renk paleti
        
        # Kamera veya Video Kaynağı
        self.capture = cv2.VideoCapture(0)
        
        # Asenkron arayüz güncellemeleri için QTimer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        
        self.video_label = QLabel("Kamera bekleniyor...")
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setStyleSheet("border: 2px solid #5c5c5c; background-color: #1e1e1e;")
        self.layout.addWidget(self.video_label)
        
        self.toggle_btn = QPushButton("Sistemi Başlat")
        self.toggle_btn.setStyleSheet("background-color: #3a3a3a; padding: 10px; font-weight: bold;")
        self.toggle_btn.clicked.connect(self.toggle_feed)
        self.layout.addWidget(self.toggle_btn)
        
        self.central_widget.setLayout(self.layout)

    def toggle_feed(self):
        if not self.timer.isActive():
            self.timer.start(30)  # ~30 FPS asenkron güncelleme
            self.toggle_btn.setText("Sistemi Durdur")
        else:
            self.timer.stop()
            self.toggle_btn.setText("Sistemi Başlat")
            self.video_label.setText("Sistem Duraklatıldı")

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            # OpenCV işlemleri (Gerçek projede yüz tanıma algoritması buraya gelir)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Görüntüyü PyQt5'in gösterebileceği formata çevirme
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.video_label.setPixmap(QPixmap.fromImage(q_img).scaled(
                self.video_label.width(), self.video_label.height(), Qt.KeepAspectRatio))

    def closeEvent(self, event):
        self.capture.release()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SecurityDashboard()
    window.show()
    sys.exit(app.exec_())
