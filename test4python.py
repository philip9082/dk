if "4" in ['1','2','3','4']:
     print("4 is included.")
else: print("4 is not included")

languages = ['python','perl','c','java']

for lang in languages:
    if lang in ['python','perl']:
        print("%10s need interpreter" % lang)
    elif lang in ['c','java']:
        print("%10s need compiler" % lang)
    else:
        print("should not reach here")


print(1+1)

print(3/2.4)

a=1
b=3
print(a+b)

while a<=b:
    print("while:"+ str(a))
    a+=1
    
print(4.2e-02 * 10000000)

print(str(3%7) + '__' + str(3//7))

print('''philip's mac''')
print("""philip's iPhone
philip want to get a new iPhone14 pro
""")

a = "a,b,c,d"
b = a.split(',')
print(len(b))

for i in b:
    print(i)

print("")
dica = {'a' : ['a','b','d'],'b':1,'c':'kim'}
print(len(dica))

for i in dica :
    print(i)

print(dica['c'])