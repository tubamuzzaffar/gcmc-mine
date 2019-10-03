import random
nums = []
for x in range (2000, 2914):
    nums.append(str(x))
f = open("user.txt","w+")
group = ["student","teacher","programmer","parent"]
with open("u.user", "r") as my_file:
	for line in my_file:
		str = line.split()
      		print(str)
		for words in str:
			word = words.split("|")
			print(len(word))
			for i in range(6):
				j=0	
				for el in word:
					print(el)
					if(j<4):
						if(j==3):
							gr = random.choice(group)
							f.write(gr)
						else:
							f.write(el)
						f.write("|")
						j+=1
					
				pc=0
				pc = random.choice(nums)
				print(pc)
				f.write(pc)	
				f.write('\n')
		
	f.close()	
	
