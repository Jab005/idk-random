import random as rnd
listNum = ("0","1","2","3","4","5","6","7","8","9")
listLow = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
listUp = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
listSym = ("`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}",";",":",'"',"'","\\","|",",",".","<",">","/","?")
listNumLow = listNum+listLow
listNumUp = listNum+listUp
listNumSym = listNum+listSym
listLowUp = listLow+listUp
listLowSym = listLow+listSym
listUpSym = listUp+listSym
listNumLowUp = listNumLow+listUp
listNumLowSym = listNumLow+listSym
listNumUpSym = listNumUp+listSym
listLowUpSym = listLowUp+listSym
listMix = listNumLow+listUpSym

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
      case "symbol":
        print("Generates random symbol string.\nUsage: Token.symbol(length:int)")
      case "numlow":
        print("Generates random numbered and lowcased alphabets string.\nUsage: Token.numlow(length:int)")
      case "numup":
        print("Generates random numbered and upcased alphabets string.\nUsage: Token.numup(length:int)")
      case "numsym":
        print("Generates random numbered and symbol string.\nUsage: Token.numsym(length:int)")
      case "lowup":
        print("Generates random lowcased and upcased alphabets string.\nUsage: Token.lowup(length:int)")
      case "lowsym":
        print("Generates random lowcased alphabets and symbol string.\nUsage: Token.lowsym(length:int)")
      case "upsym":
        print("Generates random upcased alphabets and symbol string.\nUsage: Token.upsym(length:int)")
      case "numlowup":
        print("Generates random numbered, lowcased, and upcased alphabets string.\nUsage: Token.numlowup(length:int)")
      case "numlowsym":
        print("Generates random numbered, lowcased alphabets, and symbol string.\nUsage: Token.numlowsym(length:int)")
      case "numupsym":
        print("Generates random numbered, upcased alphabets, and symbol string.\nUsage: Token.numupsym(length:int)")
      case "lowupsym":
        print("Generates random lowcased, upcased alphabets, and symbol string.\nUsage: Token.lowupsym(length:int)")
      case "mix":
        print("Generates random mixed string.\nUsage: Token.mix(length:int)")
      case _:
        print("Generates randomized strings. Do 'Token('selection')' for more info.\nAvailable selection:\n1. Number\n2. Lowcase\n3. Upcase\n4. Symbol\n5. NumLow (Number + Lowcase)\n6. NumUp (Number + Upcase)\n7. NumSym (Number + Symbol)\n8. LowUp (Lowcase + Upcase)\n9. LowSym (Lowcase + Symbol)\n10. UpSym (Upcase + Symbol)\n11. NumLowUp (Number, Lowcase, Upcase)\n12. NumLowSym (Number, Lowcase, Symbol)\n13. NumUpSym (Number, Upcase, Symbol)\n14. LowUpSym (Lowcase, Upcase, Symbol)\n15. mix (All combinations)\n- NOTE: For all tokens has length configuration, but it's limited at 500!\nAlso every token has default 10 characters length by default.")
  
  #Generate random numbered string
  def number(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listNum)
    return result
  
  #Generate random lowercased string
  def lowcase(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listLow)
    return result
  
  #Generate random upcased string
  def upcase(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listUp)
    return result
  
  #Generate random symbol string
  def symbol(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listSym)
    return result
  
  #Generate random numbered + lowcased string
  def numlow(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listNumLow)
    return result
  
  #Generate random numbered + upcased string
  def numup(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listNumUp)
    return result
  
  #Generate random numbered + symbol string
  def numsym(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listNumSym)
    return result
  
  #Generate random low + upcased string
  def lowup(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listLowUp)
    return result
  
  #Generate random lowcased + symbol string
  def lowsym(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listLowSym)
    return result
  
  #Generate random upcased + symbol string
  def upsym(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listUpSym)
    return result
  
  #Generate random numbered + low + upcased string
  def numlowup(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listNumLowUp)
    return result
  
  #Generate random numbered + lowcased + symbol string
  def numlowsym(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listNumLowSym)
    return result
  
  #Generate random numbered + upcased + symbol string
  def numupsym(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listNumUpSym)
    return result
  
  #Generate random low + upcased + symbol string
  def lowupsym(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listLowUpSym)
    return result
  
  #Generate random mixed string
  def mix(length:int=10):
    result = ""
    if length > 500:
      print("Max token length is 500 for safety purpose!\nIf you want it longer, just stack. Current result turned to 500 chars length.")
      length = 500
    else:
      pass
    for rep in range(length):
      result += rnd.choice(listMix)
    return result
  
