from PyQt6.QtGui import * 

import sys 
from PyQt6 import QtWidgets
from PyQt6.QtCore import QThread
import design  
import settings
import pyaudio
import wave
import time
import socket

k=0

class otschet(QThread):
    def __init__(self, mainWindow, parent=None):
        super().__init__()
        self.mainWindow = mainWindow

    def run(self):
        time.sleep(1)
        x=5
        while x>=1:
            
            self.mainWindow.label.setText("Говорите              \r" + str(x))
            x-=1
            time.sleep(1)
        self.mainWindow.label.setText("Идет отправка")
        time.sleep(5)
      



class vizov(QThread):
    def __init__(self, mainWindow, parent=None):
        super().__init__()
        self.mainWindow = mainWindow

    def run(self):
        
        try:
            time.sleep(1)
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 2
            RATE = 44100
            RECORD_SECONDS = 5
            WAVE_OUTPUT_FILENAME = "output.wav"
            p = pyaudio.PyAudio()
            stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=1,
                    frames_per_buffer=CHUNK)
            frames = []
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)
            stream.stop_stream()
            stream.close()
            p.terminate()
            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(("127.0.0.1", 12345))
            # запрашиваем имя файла и отправляем серверу
            f_name = 'output.wav'
            client.send((bytes(f_name, encoding = 'UTF-8')))
            
            # открываем файл в режиме байтового чтения
            f = open (f_name, "rb")
            
            # читаем строку
            l = f.read(1024)
            
            while (l):
                
                client.send(l)
                l = f.read(1024)
            
            f.close()
            client.close()
            self.mainWindow.label.setText("Отправлено\rВоспроизводится")
            k=1
            time.sleep(5)
            self.mainWindow.label.setText("\"Вызов\" что бы вызвать")
            self.mainWindow.pushButton.setEnabled(True)
        except:
            k=0
            self.mainWindow.label.setText("Не удалось отправить, попробуйте снова")
            self.mainWindow.pushButton.setEnabled(True)

class setting(QtWidgets.QMainWindow, settings.Ui_MainWindow,QThread):
    def __init__(self):   
        super().__init__()
        self.setupUi(self)

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):   
        super().__init__()
        self.menuBar().setFont(QFont('Times', 8))
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.record_wav)
        self.vizov_instance = vizov(mainWindow=self)
        self.otschet_instance = otschet(mainWindow=self)
        self.action_3.triggered.connect(self.setting_zapusk)


    def setting_zapusk(self):
        window = setting()  # Создаём объект класса ExampleApp
        window.show()  # Показываем окно


    def record_wav(self):
    	
        self.pushButton.setEnabled(False)
        self.vizov_instance.start()
        self.otschet_instance.start()
      
'''def setting_init():
    app2 = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = setting()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app2.exec()  # и запускаем приложение'''

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение



if __name__ == '__main__':
    main()
