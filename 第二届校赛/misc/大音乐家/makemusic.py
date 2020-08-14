import wave
zipfile='''
50 4B 03 04 14 03 00 00 08 00 28 65 06 51 CC A6
37 A9 9E 00 00 00 D1 00 00 00 08 00 00 00 66 6C
61 67 2E 74 78 74 1D 8D C1 0E C2 20 10 44 EF 7E
C5 DC AA 49 63 E4 56 8F F6 A8 1F D1 AC 65 2D C4
16 1A A0 22 1A FF 5D E0 B6 D9 99 F7 A6 4F 60 72
73 82 E8 44 87 9E 39 28 FB 62 D3 78 28 A6 39 28
28 92 D0 CB EA F2 57 B6 20 23 A1 B4 87 E1 55 71
C4 2D A3 2D 8C 8D A0 89 25 84 68 B1 E4 62 26 0C
A2 2E B4 5E CA 7D 25 B3 91 4B 2D F6 C5 69 B7 49
D5 38 27 84 94 F7 AB A8 F1 19 0E 8A 5D DD 8C D6
54 FA 4E E3 B3 28 72 80 D1 6E 2E F8 C3 71 F7 F1
61 1B C3 E3 BB 8A CB 7B 38 0D 67 6B E5 B0 68 AF
C7 DF EE 0F 50 4B 01 02 3F 03 14 03 01 00 08 00
28 65 06 51 CC A6 37 A9 9E 00 00 00 D1 00 00 00
08 00 24 00 00 00 00 00 00 00 20 80 A4 81 00 00
00 00 66 6C 61 67 2E 74 78 74 0A 00 20 00 00 00
00 00 01 00 18 00 80 27 5B D1 AB 6B D6 01 00 E3
75 A3 AB 6B D6 01 80 27 5B D1 AB 6B D6 01 50 4B
05 06 00 00 00 00 01 00 01 00 5A 00 00 00 C4 00
00 00 00 00

'''
miscraw=bytes.fromhex(zipfile)


frame_bytes = bytearray()

bits = list(map(int, ''.join(['{0:08b}'.format(i) for i in miscraw])))
print(bits)
for i,bit in enumerate(bits):
    print("[",bit,"]",end = '')
    frame_bytes.append(bit*255)
    print("[",bit*255,"]")
frame_modified = bytes(frame_bytes)

# Write bytes to a new wave audio file
with wave.open('song_embedded.wav', 'wb') as fd:
    fd.setparams((1, 1, 44100, 44100, 'NONE', 'not compressed'))
    fd.writeframes(frame_modified)
