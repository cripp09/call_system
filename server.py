import socket
import pyaudio
import wave

CHUNK = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('10.16.20.165', 12345))
server.listen(3)

"""Основной цикл программы"""
def main():
    while True:
        conn, addr = server.accept()
        print(('connected:', addr))
        f = open('sent/output'+str(addr)+'.wav','wb')
        while True:
            l = conn.recv(1024)
            f.write(l)
            if not l:
                break
        f.close()
        conn.close()
        print('File received')

"""Воспроизведение полученных данных"""
def play_on_recieve():  
    wf = wave.open('sent/output'+'.wav', 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output_device_index=3,
                    output=True)
    data = wf.readframes(CHUNK)
    while len(data):
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as ex:
            print(ex)
