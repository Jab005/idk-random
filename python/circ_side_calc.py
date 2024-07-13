#Circular Side Geometry Calculator python program created by Jab005! This very simple program is training program by Jab005 to learn his beginner skill.
#NOTE: This program has quiet much inaccuracies due to float value instead of integer!
#If you're feels helped or satisfied, thank you!

#———————————————————————————#

print("Hello dear user, welcome!\nThis python program is created by Jab005 to help you to count the Circular Side Geometry Calculator!\nThere are several geometries:\n1. Tube(has 5 more sub side calculations)\n2. Cone(has 5 more sub side calculations)\n3. Ball(has 4 more sub side calculations)\n\nNote: This calculation program only supporting float, for integer just convert it by yourself, sorry...")
geo_type = str(input("Enter geometry selection by number(available selection: 1. Tube, 2. Cone, 3. Ball): "))
pi = 3.14 #or pi = 22/7 => float result aren't simplified version

if geo_type == "1":
  print("\nYou just have chosen calculation of a Tube\nPlease enter sub side calculation selection to choose side that you want to be calculated\n\nAvailable sub side selections:\n1. Base Area\n2. Blanket Size\n3. Surface Area\n4. Surface Area(without lid)\n5. Volume")
  sub_side = str(input("Enter sub side selection by number input: "))
  
  if sub_side == "1":
    print("\nYou just have chosen Base Area calculation.")
    r = float(input("Please enter radius: "))
    print("\nThe Base Area of tube is: ",pi * r ** 2)

  elif sub_side == "2":
    print("\nYou just have chosen Blanket Size calculation.")
    r = float(input("Please enter radius: "))
    h = float(input("Please enter height: "))
    print("\nThe Blanket Size of tube is: ",2 * pi * r * h)

  elif sub_side == "3":
    print("\nYou just have chosen Surface Area calculation.")
    r = float(input("Please enter radius: "))
    h = float(input("Please enter height: "))
    print("\nThe Surface Area of tube is: ",2 * pi * r * (r + h))

  elif sub_side == "4":
    print("\nYou just have chosen Surface Area(without lid) calculation.")
    r = float(input("Please enter radius: "))
    h = float(input("Please enter height: "))
    print("\nThe Surface Area(without lid) of tube is: ",pi * r ** 2 + 2 * pi * r * h)

  elif sub_side == "5":
    print("\nYou just have chosen Volume calculation.")
    r = float(input("Please enter radius: "))
    h = float(input("Please enter height: "))
    print("\nThe Volume of tube is: ",pi * r ** 2 * h)

  else:
    print("\nSorry dear user... But your sub side selection input isn't available selection to be chosen!\nPlease confirm there's no any mistype happened, and only '1' until '5' is available selection to be selected.")

elif geo_type == "2":
  print("\nYou just have chosen calculation of a Cone\nPlease enter sub side calculation selection to choose side that you want to be calculated\n\nAvailable sub side selections:\n1. Painter Line\n2. Base Area\n3. Surface Area\n4. Blanket Size\n5. Volume")
  sub_side = str(input("Enter sub side selection by number input: "))
  
  if sub_side == "1":
    print("\nYou just have chosen Painter Line calculation.")
    r = float(input("Please enter radius: "))
    h = float(input("Please enter height: "))
    print("\nThe Painter Line of cone is: ",(r ** 2 + h ** 2) ** 0.5)

  elif sub_side == "2":
    print("\nYou just have chosen Base Area calculation.")
    r = float(input("Please enter radius: "))
    print("\nThe Base Area of cone is: ",pi * r ** 2)

  elif sub_side == "3":
    print("\nYou just have chosen Conical Surface calculation.")
    r = float(input("Please enter radius: "))
    h = float(input("Please enter height: "))
    print("\nThe Conical Surface of cone is: ",pi * r * (((r ** 2 + h ** 2) ** 0.5) + r))

  elif sub_side == "4":
    print("\nYou just have chosen Blanket Size calculation.")
    r = float(input("Please enter radius: "))
    h = float(input("Please enter height: "))
    print("\nThe Blanket Size of cone is: ",pi * r * ((r ** 2 + h ** 2) ** 0.5))

  elif sub_side == "5":
    print("\nYou just have chosen Volume calculation.")
    r = float(input("Please enter radius: "))
    h = float(input("Please enter height: "))
    print("\nThe Volume of cone is: ",0.33 * pi * r ** 2 * h)

  else:
    print("\nSorry dear user... But your sub side selection input isn't available selection to be chosen!\nPlease confirm there's no any mistype happened, and only '1' until '5' is available selection to be selected.")

elif geo_type == "3":
  print("\nYou just have chosen calculation of a Ball\nPlease enter sub side calculation selection to choose side that you want to be calculated\n\nAvailable sub side selections:\n1. Surface Area\n2. Half Surface Area(hollow)\n3. Half Surface Area(congested)\n4. Volume")
  sub_side = str(input("Enter sub side selection by number input: "))
  
  if sub_side == "1":
    print("\nYou just have chosen Surface Area calculation.")
    r = float(input("Please enter radius: "))
    print("\nThe Surface Area of ball is: ",4 * pi * r ** 2)

  elif sub_side == "2":
    print("\nYou just have chosen Half Surface Area(hollow) calculation.")
    r = float(input("Please enter radius: "))
    print("\nThe Half Surface Area(hollow) of ball is: ",2 * pi * r ** 2)

  elif sub_side == "3":
    print("\nYou just have chosen Half Surface Area(congested) calculation.")
    r = float(input("Please enter radius: "))
    print("\nThe Half Surface Area(congested) of ball is: ",3 * pi * r ** 2)

  elif sub_side == "4":
    print("\nYou just have chosen Volume calculation.")
    r = float(input("Please enter radius: "))
    print("\nThe Volume of ball is: ",1.33 * pi * r ** 3)

  else:
    print("\nSorry dear user... But your sub side selection input isn't available selection to be chosen!\nPlease confirm there's no any mistype happened, and only '1' until '4' is available selection to be selected.")

else:
  print("\nSorry dear user... But your input method isn't available geometry selection to be chosen!\nPlease confirm there's no any mistype happened, and only '1', '2', or '3' is available method to be used.")

print("\n© By Jab005.")

#NOTE ON 2024: Meh, now I've learned some new improvements, but i dont want to change it. Let this becoming my legacy training.