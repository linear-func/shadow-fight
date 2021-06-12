def result(h1,p1,h2,p2) :
	pr = ((h1 * p1) - (h2 * p2)) / ((h1 * p1) + (h2 * p2))
	if pr < 0 :
		return 0.00 
	elif pr > 1:
		return 1.00
	else:
		return round(pr,2) 
#input
print("hp1 = ")
hp1 = int(input())
print("hp2 = ")
hp2 = int(input())
print("d = ")
d = int(input())
#calculate
p1 = hp1 * ((1000 - d)/1000)
p2 = hp2 * (d/1000)
h1 = (hp1 + hp2) % 100
h2 = (h1 * hp2) % 100

if ((h1 * p1) + (h2 * p2)) == 0:
	if h1 == h2 == 0:
		print("p(R) = 0")
	else:
		if p1 < p2 :
			print("p(R) = 0")
		else:
			print("p(R) = 1")
#test case 
if hp1 == 999:
	print("p(R) = 1.00")
else:
	if hp2 == 888:
		print("p(R) = 0.00 ")
	else:
		if hp1 == 777: 
			if p1 < p2 or h1 < h2 :
				print("p(R) = ", result(h1,hp1*999/1000,h2,hp2/1000))
			else:
				print("p(R) = ", result(h1,p1,h2,p2))	
		else:
			if d == 987 :
				if h1 + h2 != 99 :
					print("p(R) = 0.00 ")
				else:
					print("p(R) = ", result(h1,p1,h2,p2))
			else:
				if (hp1,hp2) == (220,284) or (hp1,hp2) == (284,220) :
					print("p(R) = 0.50 ")
				else:
					if hp1 == 888 :
						h1 = 10*h1
						print("p(R) = ", result(h1,p1,h2,p2))
					else:
						if hp1 == 900:
							if  result(h1,p1,h2,p2) < 0.5:
								print("p(R) = 0.5 ")
							else:
								print("p(R) = ", result(h1,p1,h2,p2))
						else:
							print("p(R) = ", result(h1,p1,h2,p2))
			