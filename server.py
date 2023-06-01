import socket
import pyaudio
import wave
import sys
import traceback
CHUNK = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))

server.listen(3)


def main():
	while True:
		conn, addr = server.accept()
		print(('connected:', addr))
		name_f = (conn.recv(1024)).decode ('UTF-8')
		f = open('sent/output'+str(addr)+'.wav','wb')
	
		while True:
			l = conn.recv(1024)
			f.write(l)
			if not l:
				break
		f.close()
		conn.close()
		print('File received')
	
def play_on_recieve():	
	wf = wave.open('sent/output'+str(addr)+'.wav', 'rb')
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