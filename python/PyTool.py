#Did i need to import something? #

# MAIN CLASSES #
#Logical operator (using function)
class LogicGate:
  
  #Return NAND (True if both statements aren't true at the same time)
  def nand(condition1,condition2):
    return not (condition1 and condition2)
  
  #Return NOR (True if both statements are false at the same time)
  def nor(condition1,condition2):
    return not (condition1 or condition2)
  
  #Return XOR (True if both statements are in the different condition)
  def xor(condition1,condition2):
    return (condition1 or condition2) and (not (condition1 and condition2))
  
  #Return XNOR (True if both statements are in the same condition)
  def xnor(condition1,condition2):
    return not ((condition1 or condition2) and (not (condition1 and condition2)))



#Some extra utilities
class Utilities:
  
  #User just need to do 'Utilities()' and they'll be redirected to use 'Utilities.info()''
  def __init__(self):
    print("Utility and Tool packages by Jab005 successfully active!\n> Please do 'Utilities.info()' for more info!")
  
  #These two are still unfinished, will be updated later...
  
  #Help list
  #def info(method=""):
    #if method == "":
      
    #elif :
  
  #Return value of square root of input. Outputs float or integer based of value return.
  def sqrt(value):
    if (value**0.5) % 1 == 0:
      return int(value**0.5)
    else:
      return value**0.5
  
  #Return True if given value is greater or equal of min value and less or equal of max value (shortcut of double and statements). Useful if you're trying to input multi random chance without creating a variable.
  def between(minVal:float, maxVal:float, value:float):
    return value >= minVal and value <= maxVal
  
  #Create simple dot mapping visualization of XY coordinate position in 2D. Start from one at top-left to bottom-right. Inputting locationX or locationY zero will return no point.
  def point2DA(locationX:int, locationY:int, maxX:int, maxY:int, point:str="X", empty:str="o"):
    for posX in range(maxY):
      notation = ""
      for posY in range(maxX):
        if (posY == locationX-1) and (posX == locationY-1):
          notation += point
        else:
          notation += empty
      print(notation)
  
  #Create simple dot mapping visualization of XY coordinate position in 2D. Start from one at bottom-left to top-right. Inputting locationX or locationY zero will return no point.
  def point2DB(locationX:int, locationY:int, maxX:int, maxY:int, point:str="X", empty:str="o"):
    for posX in range(maxY):
      notation = ""
      for posY in range(maxX):
        if (posY == locationX-1) and (posX == maxY-locationY):
          notation += point
        else:
          notation += empty
      print(notation)
  
  #Create simple dot mapping visualization of XY coordinate position in 2D. Start from zero at top-left to bottom-right.
  def point2DC(locationX:int, locationY:int, maxX:int, maxY:int, point:str="X", empty:str="o"):
    for posX in range(maxY):
      notation = ""
      for posY in range(maxX):
        if (posY == locationX) and (posX == locationY):
          notation += point
        else:
          notation += empty
      print(notation)
  
  #Create simple dot mapping visualization of XY coordinate position in 2D. Start from zero at bottom-left to top-right.
  def point2DD(locationX:int, locationY:int, maxX:int, maxY:int, point:str="X", empty:str="o"):
    for posX in range(maxY):
      notation = ""
      for posY in range(maxX):
        if (posY == locationX) and (posX == maxY-1-locationY):
          notation += point
        else:
          notation += empty
      print(notation)
