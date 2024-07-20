import random as rnd
listNum = ("0","1","2","3","4","5","6","7","8","9")
listLow = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
listUp = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
listLowUp = listLow+listUp
listNumUp = listNum+listUp
listNumLow = listNum+listLow
listMix = listNum+listLow+listUp

class Token:
  
  #User just need to do 'Token()'
  def __init__(self,sel:str=""):
    chs = sel.lower()
    match chs:
      case "number":
        print("Generates random numbered string.\nUsage: Token.number(length:int)")
      case "lowcase":
        print("Generates random lowcased alphabets string.\nUsage: Token.lowcase(length:int)")
      case "upcase":
        print("Generates random upcased alphabets string.\nUsage: Token.upcase(length:int)")
      case "numlow":
        print("Generates random numbered and lowcased alphabets string.\nUsage: Token.numlow(length:int)")
      case "numup":
        print("Generates random numbered and upcased alphabets string.\nUsage: Token.numup(length:int)")
      case "lowup":
        print("Generates random lowcased and upcased alphabets string.\nUsage: Token.lowup(length:int)")
      case "mix":
        print("Generates random mixed string.\nUsage: Token.mix(length:int)")
      case _:
        print("Generates randomized strings. Do 'Token('selection')' for more info.\nAvailable selection:\n1. Number\n2. Lowcase\n3. Upcase\n4. NumLow (Number + Lowcase)\n5. NumUp (Number + Upcase)\n6. LowUp (Lowcase + Upcase)\n7. Mix (All mixed version)\n- NOTE: For all tokens has length configuration, but it's limited at 500!\nAlso every token has default 10 characters length by default.")
  
  #Generate random numbered string
  def number(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500!\nIf you want longer token, just stack. And here, this generated token is 500 characters length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listNum)
    print("Token result:\n"+result)
  
  #Generate random lowercased string
  def lowcase(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500!\nIf you want longer token, just stack. And here, this generated token is 500 characters length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listLow)
    print("Token result:\n"+result)
  
  #Generate random upcased string
  def upcase(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500!\nIf you want longer token, just stack. And here, this generated token is 500 characters length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listUp)
    print("Token result:\n"+result)
  
  #Generate random numbered + lowcased string
  def numlow(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500!\nIf you want longer token, just stack. And here, this generated token is 500 characters length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listNumLow)
    print("Token result:\n"+result)
  
  #Generate random numbered + upcased string
  def numup(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500!\nIf you want longer token, just stack. And here, this generated token is 500 characters length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listNumUp)
    print("Token result:\n"+result)
  
  #Generate random low + upcased string
  def lowup(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500!\nIf you want longer token, just stack. And here, this generated token is 500 characters length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listLowUp)
    print("Token result:\n"+result)
  
  #Generate random mixed string
  def mix(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500!\nIf you want longer token, just stack. And here, this generated token is 500 characters length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listMix)
    print("Token result:\n"+result)
  
