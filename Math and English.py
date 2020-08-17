mscore = int(input ("What's your math score:"))
escore = int(input("What's your English score:"))
if (mscore >= 0 and mscore <= 100) and (escore >= 0 and escore <= 100):
    if mscore>=90 and escore >= 90:
        print("You get a prize!")
    elif (escore >= 60 and mscore <=60) or (escore <=60 and mscore >= 60):
        print("Keep studying")
    elif mscore <= 60 and escore <= 60:
        print ("Please wait for your punishment", "This score is unacceptable")
    else:
        print ("You get nothing")
else:
    print("Can you even type?")
