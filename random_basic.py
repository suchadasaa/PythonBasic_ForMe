import random
from time import perf_counter

damage =  random.randint(50 ,60) #(ค่าต่ำสุด, ค่าสูงสุด)
print(damage)

percent = random.uniform(0, 100) #random float
print(percent)


#random member in list
moneys = [0,20,50,100]
money = random.choice(moneys)
print(money)