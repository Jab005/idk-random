import random

list_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
list_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
list_up = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list_mix_numlow = list_num + list_low
list_mix_numup = list_num + list_up
list_mix_lowup = list_low + list_up
list_multi_mix = list_num + list_low + list_up
result = ""

class Token:
    def help():
        print("<Token Generator Help Page>\nBy Jab005\nList of available help:\n1. Number\n2. Lowcase\n3. Upcase\n4. Number + Lowcase\n5. Number + Upcase\n6. Lowcase + Upcase\n7. All Combination\n\nImportant info: Max token length is 500, why?\nLimitation of token length is set in order to avoid lag. If you want to make longer digits, just stack with new generation.")
        sel = str(input("\nEnter your selection: "))
        if sel == "1":
            print("<Token Number>\n- Generates random number list. Length of list is set in <token_length> in function.\n\nToken.number([TOKEN_LENGTH])\n\nExample:\nToken.number(10)")
        elif sel == "2":
            print("<Token Lowcase>\n- Generates random lowcase alphabet list. Length of list is set in <token_length> in function.\n\nToken.lowcase([TOKEN_LENGTH])\n\nExample:\nToken.lowcase(7)")
        elif sel == "3":
            print("<Token Upcase>\n- Generates random upcase alphabet list. Length of list is set in <token_length> in function.\n\nToken.upcase([TOKEN_LENGTH])\n\nExample:\nToken.upcase(8)")
        elif sel == "4":
            print("<Token Number + Lowcase>\n- Generates random number with lowcase alphabet combination list. Length of list is set in <token_length> in function.\n\nToken.numlow([TOKEN_LENGTH])\n\nExample:\nToken.numlow(13)")
        elif sel == "5":
            print("<Token Number + Upcase>\n- Generates random number with upcase alphabet combination list. Length of list is set in <token_length> in function.\n\nToken.numup([TOKEN_LENGTH])\n\nExample:\nToken.numup(16)")
        elif sel == "6":
            print("<Token Lowcase + Upcase>\n- Generates random lowcase with upcase alphabet combination list. Length of list is set in <token_length> in function.\n\nToken.lowup([TOKEN_LENGTH])\n\nExample:\nToken.lowup(24)")
        elif sel == "7":
            print("<Token All Combination>\n- Generates random number, lowcase, and upcase alphabet combination list. Length of list is set in <token_length> in function.\n\nToken.mix([TOKEN_LENGTH])\n\nExample:\nToken.mix(35)")
        else:
            print("Sorry, your input wasn't listed here! Please check if there was a typo or make sure your input is between '1' until '7' only!")

    def number(l):
        if l > 500:
            print("Sorry, but max token length is 500 digits!\n")
            l = 500
        else:
            pass
        for gen in range(l):
            global result
            result = result + random.choice(list_num)
        print("Here's the token generation result: \n",result)

    def lowcase(l):
        if l > 500:
            print("Sorry, but max token length is 500 digits!\n")
            l = 500
        else:
            pass
        for gen in range(l):
            global result
            result = result + random.choice(list_low)
        print("Here's the token generation result: \n",result)

    def upcase(l):
        if l > 500:
            print("Sorry, but max token length is 500 digits!\n")
            l = 500
        else:
            pass
        for gen in range(l):
            global result
            result = result + random.choice(list_up)
        print("Here's the token generation result: \n",result)

    def numlow(l):
        if l > 500:
            print("Sorry, but max token length is 500 digits!\n")
            l = 500
        else:
            pass
        for gen in range(l):
            global result
            result = result + random.choice(list_mix_numlow)
        print("Here's the token generation result: \n",result)

    def numup(l):
        if l > 500:
            print("Sorry, but max token length is 500 digits!\n")
            l = 500
        else:
            pass
        for gen in range(l):
            global result
            result = result + random.choice(list_mix_numup)
        print("Here's the token generation result: \n",result)

    def lowup(l):
        if l > 500:
            print("Sorry, but max token length is 500 digits!\n")
            l = 500
        else:
            pass
        for gen in range(l):
            global result
            result = result + random.choice(list_mix_lowup)
        print("Here's the token generation result: \n",result)

    def mix(l):
        if l > 500:
            print("Sorry, but max token length is 500 digits!\n")
            l = 500
        else:
            pass
        for gen in range(l):
            global result
            result = result + random.choice(list_multi_mix)
        print("Here's the token generation result: \n",result)
