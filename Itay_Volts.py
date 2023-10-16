def AddZeros(s):
        l=10-len(s)
        for i in range (l): 
            s="0"+s
        return s
class volts:
    def __init__(self,volt=0.0):
        self.volt=volt
    def ToDigital(self):
        if self.volt>5 or self.volt <0:
            return ("volts out of range")
        num_of_bits = int((self.volt/5)*1023)
        return(AddZeros(str(bin(num_of_bits)[2:])))
    def SetDigitalValue(self,value):
         if (len(value)==10):
              bits=int(value,2)
              self.volt=round(5*(bits/1023),2)
              
        

volt=volts(2)
print(volt.ToDigital())
volt.SetDigitalValue("1001111010")
print(volt.volt)
