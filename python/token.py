import random

print("Welcome dear user!, this simple python program called 'Token Generator' is coded by Jab005 himself at school for no reason. This program can be used to enter random site url or something else...")

list_num = ["0","1","2","3","4","5","6","7","8","9"]
list_low = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list_up = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
list_mix_numlow = list_num + list_low
list_mix_numup = list_num + list_up
list_mix_lowup = list_low + list_up
list_multi_mix = list_num + list_low + list_up
result = "Here is the result: \n"

print("\nAll available token type:\n1. Number\n2. Lowcase\n3. Upcase\n4. Number + Lowcase\n5. Number + Upcase\n6. Lowcase + Upcase\n7. All Combinations")
sel = str(input("Enter your token type by number selection: "))

if sel == "1":
  lgt = int(input("Enter token length(integer number only!): "))
  for loop in range(lgt):
    result = result + random.choice(list_num)
  print("Number token generation completed!\n",result)

elif sel == "2":
  lgt = int(input("Enter token length(integer number only!): "))
  for loop in range(lgt):
    result = result + random.choice(list_low)
  print("Lowcase token generation completed!\n",result)

elif sel == "3":
  lgt = int(input("Enter token length(integer number only!): "))
  for loop in range(lgt):
    result = result + random.choice(list_up)
  print("Upcase token generation completed!\n",result)

elif sel == "4":
  lgt = int(input("Enter token length(integer number only!): "))
  for loop in range(lgt):
    result = result + random.choice(list_mix_numlow)
  print("Lowcase + Number token generation completed!\n",result)

elif sel == "5":
  lgt = int(input("Enter token length(integer number only!): "))
  for loop in range(lgt):
    result = result + random.choice(list_mix_numup)
  print("Upcase + Number token generation completed!\n",result)

elif sel == "6":
  lgt = int(input("Enter token length(integer number only!): "))
  for loop in range(lgt):
    result = result + random.choice(list_mix_lowup)
  print("Lowcase + Upcase token generation completed!\n",result)

elif sel == "7":
  lgt = int(input("Enter token length(integer number only!): "))
  for loop in range(lgt):
    result = result + random.choice(list_multi_mix)
  print("Multi Mix token generation completed!\n",result)

else:
  print("\nSorry, but your input type isn't match of any available type selection!\nPlease be carefully if there's mistype happens and only available type selection it's just '1' until '7'.")

#NOTE ON 2024: This is execute-input version, see token_gen.py for Class-Function Method.
