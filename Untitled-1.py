
    

while True :
    a=input("exact date of birth ")

    b=a.split("/")
#print (b)
    d=(int(b[2])) 

    c=2025

    if int(b[0]) > 31 or int(b[1]) >12 or int(b[2]) >2025 :
        print("invalid date") 
        continue

    if int(b[1])== 2 and int(b[0]) > 30 :
        print("invalid date") 
        continue

    if (int(b[1])== 1 or int(b[1])== 3 or int(b[1])== 5 or int(b[1])== 7 or int(b[1])== 9 or int(b[1])== 11) and int(b[0]) >30 :
        print("invalid date")
        continue

    break


print("your age is "+str(c-d))

#zodiac=(int(int(b[0])+int (b[1])))
if (int(b[1]))== 1 : 
    if (int(b[0])) in range(20, 32) :
        print("you're an Aquarius")
    else: 
        print("you're a Capricorn")
if (int(b[1]))== 2 :
    if int(b[0]) in range(19, 30) :
        print ("you're aPisces")
    else:
        print ("you're an Aquarius")
if int(b[1])== 3 :
    if int(b[0]) in range (21, 32) :
        print ("you're an Aries")
    else:
        print ("you're a Pisces")    
if int(b[1])== 4 :
    if int(b[0]) in range (20, 31) :
        print ("you're a Taurus")
    else:
        print ("you're an Aries")    
if int(b[1])== 5 :
    if int(b[0]) in range (21, 32) :
        print ("you're a Gemini")
    else:
        print ("you're a Taurus")
if int(b[1])== 6 :
    if int(b[0]) in range (22, 31) :
        print ("you're a Cancer")
    else:
        print ("you're a Gemini")    
if int(b[1])== 7 :
    if int(b[0]) in range (23,32) :
        print ("you're a Leo")
    else:
        print ("you're a Cancer")
if int(b[1])== 8 :
    if int(b[0]) in range (23, 32) :
        print ("you're a virgo")
    else:
         print ("you're a Leo")
if int(b[1])== 9 :
    if int(b[0]) in range (23, 31) :
        print ("you're a Libra")
    else: 
        print ("you're a Virgo")
if int(b[1])== 10 :
    if int(b[0]) in range (24, 32) :
        print ("you're a Scorpio")
    else:
        print ("you're a Libra")
if int(b[1])== 11 :
    if int(b[0]) in range (22, 31) :
        print ("you're a saggitarius")
    else: 
        print ("you're a Scorpio")
if int(b[1])== 12 :
    if int(b[0]) in range (22, 32) :
        print ("you're a Capricorn")
    else: 
        print ("you're a Saggitarius")

