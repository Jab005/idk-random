#Pythagoras Calculator python program created by Jab005! This very simple program is training program by Jab005 to learn his beginner skill.
#If you're feels helped or satisfied, thank you!
#This program is 100% pure coded by Jab005 himself at school for a limited time.

#———————————————————————————#

print("Hello dear user, welcome!\nThis python program is created by Jab005 to help you to count the Pythagoras triangle side length!\nThere are several sides:\n1. A = √(C² - B²)\n2. B = √(C² - A²)\n3. C = √(A² + B²)")
method = str(input("Please enter counting method by number selection: "))

if method == "1":
  c = float(input("Please enter C value: "))
  b = float(input("Please enter B value: "))
  print("The value of A is: ",(c ** 2 - b ** 2) ** 0.5)
elif method == "2":
  c = float(input("Please enter C value: "))
  a = float(input("Please enter A value: "))
 print("The value of B is: ",(c ** 2 - a ** 2) ** 0.5)
elif method == "3":
  a = float(input("Please enter A value: "))
  b = float(input("Please enter B value: "))
  print("The value of C is: ",(a ** 2 + b ** 2) ** 0.5)
else:
  print("Sorry dear user... But your input method is not available method to be used!\nPlease confirm there's no any mistype happened, and only '1', '2', or '3' is available method to be used.")

print("\n© By Jab005.")

#NOTE ON 2024: I've understand more things i should use here, but let this becomes legacy history training.