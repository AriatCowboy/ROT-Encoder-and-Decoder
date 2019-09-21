#Author Ghost
#Variables
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
output = ""
#Data to decode
encodedData = input("What do you want decoded?")
#Rotatation Amount
rotNum = int(input('What ROT number do you want?'))
#DeCoder
for i in range(len(encodedData)):
	for j in range(len(alphabet)):
		if encodedData[i] == alphabet[j]:
			if j + rotNum > 25:
				diff = (j + rotNum) - 25
				output = output + (alphabet[diff -1])
			else:	
				output = output + (alphabet[j + rotNum])
print(output)