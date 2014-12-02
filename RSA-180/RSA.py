import math
import binascii
from itertools import combinations

p = 1398023584459
q = 29065965967667
N = 40634905927881125837687153 #p * q
r = 40634905927850661848135028 #(p - 1) * (q - 1)

def powerMod(x , p , N):
	# Finds x ^ p mod N
	A = 1
	m = p
	t = x
	while(m > 0):
		k = math.floor(m / 2)
		r = m - 2 * k
		if (r == 1):
			A = (A * t) % N
		t = (t * t) % N
		m = k
	return A

print("p: 		" + str(p))
print("q: 		" + str(q))
print("N: 		" + str(N))
print("r: 		" + str(r))

#Message = Cipher ** d % N
cipher = int("ac470f7350ea67d7a0696" , 16)

#Try 1: use r + 1
#Factors = 7 , 349 , 16633199315534450203903

#Try 2: use 2r + 1
#Factors = 139 , 5635373 , 260393671 , 398438561

#Try 3: use 3r + 1
#Factors = 968930987 , 2541455999 , 9 , 1100101 , 5

#Try 4: use 4r + 1
#Factors = 3089 , 5851089594680350369 , 17 , 23 , 23

#Try 5: use 5r + 1
#Factors = 97 , 475 , 4583332122070277002429

#Try 6: use 6r + 1
#Factors: 7 , 12101 , 231671101 , 12423940003681

#Try 7: use 7r + 1
#Factors: 5 , 13 , 19 , 31 , 48337 , 11416753 , 13463139607

f = open('RSA.out' , 'w')
possibleFactors = [5 , 13 , 19 , 31 , 48337 , 11416753 , 13463139607]
fstreamOutput = ""

for L in range(0 , len(possibleFactors)):
	for subset in combinations(possibleFactors , L):
		d = 1
		for num in subset:
			d = d * num
		message = powerMod(cipher , d , N)
		#print("c:		" + str(cipher))
		#print("m: 		" + str(message))
		#print("d:		" + str(d))
		message = str(hex(message).split('x')[1])
		#print("Hexify(m):	" + str(message))
		try:
			x = binascii.unhexlify(''.join(message[:-1].split()))
			print("Unhexlify(m):		" + str(x))
			fstreamOutput += str(x) + "\n"
		except:
			print("Returned error:		" + str(subset))

f.write(fstreamOutput)
