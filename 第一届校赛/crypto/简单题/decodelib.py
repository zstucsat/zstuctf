#decodes integers to the original message bytes
def decode(aiPlaintext, iNumBits):
		#bytes array will hold the decoded original message bytes
		bytes_array = []

		#same deal as in the encode function.
		#each encoded integer is a linear combination of k message bytes
		#k must be the number of bits in the prime divided by 8 because each
		#message byte is 8 bits long
		k = iNumBits//8

		#num is an integer in list aiPlaintext
		for num in aiPlaintext:
				#get the k message bytes from the integer, i counts from 0 to k-1
				for i in range(k):
						#temporary integer
						temp = num
						#j goes from i+1 to k-1
						for j in range(i+1, k):
								#get remainder from dividing integer by 2^(8*j)
								temp = temp % (2**(8*j))
						#message byte representing a letter is equal to temp divided by 2^(8*i)
						letter = temp // (2**(8*i))
						#add the message byte letter to the byte array
						bytes_array.append(letter)
						#subtract the letter multiplied by the power of two from num so
						#so the next message byte can be found
						num = num - (letter*(2**(8*i)))

		#example
		#if "You" were encoded.
		#Letter        #ASCII
		#Y              89
		#o              111
		#u              117
		#if the encoded integer is 7696217 and k = 3
		#m[0] = 7696217 % 256 % 65536 / (2^(8*0)) = 89 = 'Y'
		#7696217 - (89 * (2^(8*0))) = 7696128
		#m[1] = 7696128 % 65536 / (2^(8*1)) = 111 = 'o'
		#7696128 - (111 * (2^(8*1))) = 7667712
		#m[2] = 7667712 / (2^(8*2)) = 117 = 'u'

		decodedText = bytearray(b for b in bytes_array).decode('utf-16')

		return decodedText
