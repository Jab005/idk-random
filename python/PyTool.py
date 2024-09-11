#Logical operator (using function)
class LogicGate:
  
  #Return NAND (True if both statements aren't true at the same time)
  def nand(condition1, condition2):
    return not (condition1 and condition2)
  
  #Return NOR (True if both statements are false at the same time)
  def nor(condition1, condition2):
    return not (condition1 or condition2)
  
  #Return XOR (True if both statements are in the different condition)
  def xor(condition1, condition2):
    return (condition1 or condition2) and (not (condition1 and condition2))
  
  #Return XNOR (True if both statements are in the same condition)
  def xnor(condition1, condition2):
    return not ((condition1 or condition2) and (not (condition1 and condition2)))



#Some extra utilities
class Util:
  
  #User just need to do 'Util()' and they'll be hinted with another help methods
  def __init__(self, method:str=""):
    selection = method.lower()
    match selection:
      case "sqrt":
        print("Return square root of input. Float-integer support based result.\nUsage: sqrt(value:float|int)")
      case "between":
        print("Return boolean of value in between minimum and maximum value.\nUsage: between(minVal:float|int, maxVal:float|int, value:float|int)")
      case "point2da":
        print("Visualizes 2 dimensional coordinate map with pointer. Start from one at top-left to bottom-right. Inputting any pointer to zero or lower will return no pointer.\nUsage: point2DA(locationX:int, locationY:int, maxX:int, maxY:int, point:str='X', empty:str='o')")
      case "point2db":
        print("Visualizes 2 dimensional coordinate map with pointer. Start from one at bottom-left to top-right. Inputting any pointer to zero or lower will return no pointer.\nUsage: point2DB(locationX:int, locationY:int, maxX:int, maxY:int, point:str='X', empty:str='o')")
      case "point2dc":
        print("Visualizes 2 dimensional coordinate map with pointer. Start from zero at top-left to bottom-right. Inputting locationX or locationY lower than zero will return no point.\nUsage: point2DC(locationX:int, locationY:int, maxX:int, maxY:int, point:str='X', empty:str='o')")
      case "point2dd":
        print("Visualizes 2 dimensional coordinate map with pointer. Start from zero at bottom-left to top-right. Inputting locationX or locationY lower than zero will return no point.\nUsage: point2DD(locationX:int, locationY:int, maxX:int, maxY:int, point:str='X', empty:str='o')")
      case "formattext":
        print("Formatting multiple symbols to string array. Any excess of symbols in string (not enough placeholder) will return last placeholder for next symbols.\nUsage: formatText(text:str, symbol:str='@',*placeholder:str)")
      case "factorial":
        print("Return the result of number factorial.\nUsage: factorial(num:int)")
      case "tetra":
        print("Return the result of number tetration. May not working well when the result is too big.\nUsage: tetra(num:int|float, mult:int)")
      case "strremove":
        print("Removes string parts from string.\nUsage: strRemove(text:str, *part:str)")
      case "rate":
        print("Calculates growth rate of starting number by its percentage for amount of loop times.\nUsage: rate(num:int|float=0,percent:int=0,loop:int=1)")
      case _:
        print("Extra utilities for python.\nDo 'Util('method')' for each method info.\nAvailable methods:\n1. sqrt\n2. between\n3. point2DA\n4. point2DB\n5. point2DC\n6. point2DD\n7. formatText\n8. factorial\n9. tetra\n10. strRemove\n11. rate")
  
  #Return value of square root of input. Outputs float or integer based of value return
  def sqrt(value:float|int):
    if (value**0.5) % 1 == 0:
      return int(value**0.5)
    else:
      return value**0.5
  
  #Return True if given value is greater or equal of min value and less or equal of max value (shortcut of double and in between numbers statement). Useful if you're trying to input multi random chance without creating a variable
  def between(minVal:float|int, maxVal:float|int, value:float|int):
    return value >= minVal and value <= maxVal
  
  #Create simple dot mapping visualization of XY coordinate position in 2D. Start from one at top-left to bottom-right. Inputting locationX or locationY zero or lower will return no point
  def point2DA(locationX:int, locationY:int, maxX:int, maxY:int, point:str="X", empty:str="o"):
    for posX in range(maxY):
      notation = ""
      for posY in range(maxX):
        if (posY == locationX-1) and (posX == locationY-1):
          notation += point
        else:
          notation += empty
      print(notation)
  
  #Create simple dot mapping visualization of XY coordinate position in 2D. Start from one at bottom-left to top-right. Inputting locationX or locationY zero or lower will return no point
  def point2DB(locationX:int, locationY:int, maxX:int, maxY:int, point:str="X", empty:str="o"):
    for posX in range(maxY):
      notation = ""
      for posY in range(maxX):
        if (posY == locationX-1) and (posX == maxY-locationY):
          notation += point
        else:
          notation += empty
      print(notation)
  
  #Create simple dot mapping visualization of XY coordinate position in 2D. Start from zero at top-left to bottom-right. Inputting locationX or locationY lower than zero will return no point
  def point2DC(locationX:int, locationY:int, maxX:int, maxY:int, point:str="X", empty:str="o"):
    for posX in range(maxY):
      notation = ""
      for posY in range(maxX):
        if (posY == locationX) and (posX == locationY):
          notation += point
        else:
          notation += empty
      print(notation)
  
  #Create simple dot mapping visualization of XY coordinate position in 2D. Start from zero at bottom-left to top-right. Inputting locationX or locationY lower than zero will return no point
  def point2DD(locationX:int, locationY:int, maxX:int, maxY:int, point:str="X", empty:str="o"):
    for posX in range(maxY):
      notation = ""
      for posY in range(maxX):
        if (posY == locationX) and (posX == maxY-1-locationY):
          notation += point
        else:
          notation += empty
      print(notation)
  
  #Formatting multiple symbols to strings array. Any excess of symbols in string (not enough placeholder) will return last placeholder for next symbols replacement
  def formatText(text:str, symbol:str="@",*placeholder:str):
    raw = text.split(symbol)
    result = ""
    for strl in range(len(raw)-1):
      result += raw[strl] + placeholder[min(strl, len(placeholder)-1)]
    result += raw[len(raw)-1]
    return result
  
  #Return factorial result of number
  def factorial(num:int):
    fNum = 1
    for factor in range(1, num+1):
      fNum *= factor
    return fNum
  
  #Return tetration result of number. May not working well when the result is too big. No pentation bcs fvc you! (not even me can handle it)
  def tetra(num:int|float, mult:int):
    res = num
    for rep in range(mult-1):
      res = num ** res
    return res
  
  #Removes string parts from string
  def strRemove(text:str, *part:str):
    resl = text
    for rep in range(len(part)):
      resl = resl.replace(part[min(rep,len(part)-1)],"")
    return resl
  
  #Calculates growth rate of starting number by its percentage for amount of loop times
  def rate(num:int|float=0,percent:int=0,loop:int=1):
    val = num
    for gl in range(loop):
      val += val*(percent/100)
    return val

