mscore = int(input ("What's your math score:"))
if mscore >= 0 and mscore <= 100:
    if mscore >= 90:
        print("Yay! You're smart!")
    elif mscore >= 75:
        print("You passed, not bad.")
    elif mscore >= 60:
        print("You passed, but work harder.")
    elif mscore >= 45:
        print("Didn't pass, keep trying." )
    elif mscore >= 30:
        print("Seriously, you need to study.")
    else:
        print("There is no hope for you now.", "You are a massive failure.", "Haha!")
else:
    print("Can you even type?", "Yeah, I'm talking to you.")
escore = int(input("What's your English score:"))
if escore >= 0 and mscore <= 100:
    if escore >= 90:
        print("Yay! You're smart!")
    elif escore >= 80:
        print("Okay, if you think this is a good score, then you're wrong. Haha!")
    elif escore >= 60:
        print("You passed, but work harder.")
    elif escore >= 45:
        print("Didn't pass, keep trying." )
    elif escore >= 30:
        print("Seriously, you need to study.")
    else:
        print("There is no hope for you now.", "You are a massive failure.", "Haha!")
else:
    print("Can you even type?")
cscore = int(input ("What's your Mandarin score?"))
if (mscore >= 0 and mscore <= 100) and (escore >= 0 and escore <= 100):
    if mscore>=90 and escore >= 90:
        print("Final score: You get a prize for being awesome!!")
    elif (escore >= 60 and mscore <=60) or (escore <=60 and mscore >= 60):
        print("Final score: Keep studying, keep trying.")
    elif mscore <= 60 and escore <= 60:
        print ("Final score: Please wait for your punishment.", "This score is unacceptable.")
    else:
        print ("Final score: Haha, you are not very bright.")
else:
    print("Can you even type?")
a = input("Would you like to see your average?")
if a = "yes"
ay = cscore+mscore+escore
    print:("Average:",ay)