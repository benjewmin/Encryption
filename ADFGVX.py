import random
import string
import sys
from math import ceil as roundup
from math import floor as rounddown

#searches through rows in the grid for the value and returns the 2 Letters corresponding to the location
def encrypt(grid,crypt):
	Letters=''
	ADFGVX='ADFGVX'
	for i in crypt:
		for row in range(6):
			try:
				col=grid[row].index(i)
				Letters+=ADFGVX[row]+ADFGVX[col]
			except:
				continue	
	return Letters

#from the grid and crypt, returns unencrypted message. 
def decrypt(grid,crypt):
	Letters=''
	LetterDict = dict(zip('ADFGVX', range(6)))
	for i in range(len(crypt)/2):
		x=crypt[i*2]
		y=crypt[i*2+1]
		Letters+=grid[LetterDict[x]][LetterDict[y]]
	return Letters


#give a list and 2d list, puts columns in encrypted positions
def bubbleSort(alist,d):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                templist=d[i]
                
                alist[i] = alist[i+1]
                d[i] = d[i+1] 
                
                alist[i+1] = temp
                d[i+1] = templist
    return d

#give crypt and key, returns 2d list of crypt with len(key) columns
def Listify(crypt,key):
	keyl=list(key)
	length=len(key)

	#gets numbers of each letter
	keyln=[]
	for index in range(len(keyl)):
		keyln.append(ord(keyl[index]))

	m = [[] for x in range(length)]
	
	#puts crypt into 2D array
	i = 0
	for row in range(int(roundup(len(unshuffledString)/length))+1):
		for col in range(length):
			try:
				m[col].append(crypt[i])
			except:
				continue
			i+=1
	return m

def printarray(arr,beginning):
	ADFGVX='ADFGVX'
	if beginning:
		print '   A D F G V X'
		print ''
	for x in range(len(arr[0])+1):
		try:
			if beginning:
				sys.stdout.write(ADFGVX[x])
				sys.stdout.write('  ')
		except:
			continue
		for y in range(len(arr)+1):
			try:
				print arr[y][x],
			except:
				if y==0:
					sys.stdout.write('  ')
				else:
					sys.stdout.write(' ')
		print ""
	print ""
	return -1

raws = string.ascii_uppercase + string.digits
ranl=list(raws)

random.shuffle(ranl)

ranm = [['0' for x in range(6)] for i in range(6)]

for i in range(0,6):
	ranm[i]=ranl[i*6:i*6+6]


istrs='INVADE FROM THE WEST AT 8'
istr=istrs.replace(" ", "")

print 'PlainText: ',istrs

printarray(ranm,True)

unshuffledString = encrypt(ranm,istr)
print 'UnShuffled Crypt: ',unshuffledString

k='GERMAN'

c=Listify(list(unshuffledString),k)
printarray(c,False)

print 'Encryption Key: ',k
#gets numbers of key
keyln=[ord(j) for j in k]


#Shuffles 2d array  to key
d=bubbleSort(keyln,c)
printarray(d,False)

encryptedString=''
for x in range(len(k)):
	encryptedString+=''.join(d[x])

print 'Encrypted String: ',encryptedString
print 'Straight Decryption: ', decrypt(ranm,encryptedString)

k="GERMAN"
print 'Decryption Key: ',k

SmallerCol=int(rounddown(len(encryptedString)/len(k)))

#makes dictionary key=letters,value=original position
keyd=dict(enumerate(k))
keydSorted = {y:x for x,y in keyd.iteritems()}
DesignatedSpot=keydSorted.values()

dnew = [[] for x in range(len(k))]

extra=len(encryptedString) % len(k)

# Takes crypt and starting from the beggining removes either a short or long column for the next method 
# i is the place of the starting column extra is how many long columns there are 
# SmallerCol is how long the smaller columns are 
# var is true[1] if the New Position is a long column
i=0
for col in range(len(k)):
	var = DesignatedSpot[col]<extra
	dnew[DesignatedSpot[col]]=encryptedString[i:i+SmallerCol+var]
	i+=var + SmallerCol

printarray(dnew,False)

DecryptedString=''
for col in range(SmallerCol+1):
	for row in range(len(k)):
		try:
			DecryptedString+=dnew[row][col]
		except:
			continue

print 'Decrypted Crypt', DecryptedString
print 'Decrypted PlainText: ',decrypt(ranm,DecryptedString)
