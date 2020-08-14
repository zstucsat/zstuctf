# We will use wave package available in native Python installation to read and write .wav audio file
import wave
# read wave audiaudioo file
song = wave.open("song_embedded.wav", mode='rb')
# Read frames and convert to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))
binstring=''
print(frame_bytes)
for bit in frame_bytes:
   if bit==255:
        binstring=binstring+'1'
   else :
        binstring=binstring+'0'
raw=bytes(int(binstring[i : i + 8], 2) for i in range(0, len(binstring), 8))
f=open("flag.zip","wb")
f.write(raw)
f.close()


