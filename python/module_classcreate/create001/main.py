#import CalculationDataClass
from CalculationDataClass import CCalcData

obj = CCalcData("sample.txt")
obj.read()

print(obj.data)
print(obj.calc())

obj.update(lambda x: int(x * 2), True)
print(obj.data)

print(obj.calc())

obj.write()

print("end.")
