def AddZeros(num,s):
        l=num-len(s)
        for i in range (l): 
            s="0"+s
        return s
class volts:
    def __init__(self,volt=0.0,max_volts=0,bit_num=0):
        self.volt=volt
        self.max_volts=max_volts
        self.bit_num=bit_num
    def ToDigital(self):
        if self.volt>self.max_volts or self.volt <0:
            return ("volts out of range")
        num_of_bits = int((self.volt/self.max_volts)*1023)
        return(AddZeros(self.max_volts,str(bin(num_of_bits)[2:])))
    def SetDigitalValue(self,value):
         if (len(value)==self.bit_num):
              bits=int(value,2)
              self.volt=round(self.max_volts*(bits/1023),2)
              
        

volt=volts(10,10,10)
print(volt.ToDigital())
volt.SetDigitalValue("1000111011")
print(volt.volt)
