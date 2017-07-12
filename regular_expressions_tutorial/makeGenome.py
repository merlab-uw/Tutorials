
import random

count = 0

values = ["A", "C", "G", "T"]

for i in range(1000):
	print ">unicorn_scaffold", i
	for j in range(50):
		tmp = ''
		for k in range(80):
			tmp += values[random.randrange(0,4,1)]
		print tmp	
