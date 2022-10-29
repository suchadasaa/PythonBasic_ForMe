import Tank_module as t

#class
'''class Tank:   #ฝ่ายขาย
    def __init__(self, name, ammo): #ทีมวิศวกรขี้อาย  #self คือแขกVIP => ตัวใส่ข้อมูลให้รถถัง และคืนค่าข้อมูลทั้งหมดกลับไปให้เจ้าของที่สั่งซื้อรถถังมา 
        self.name = name  #self.name ชื่อรถถัง = name คือparamitor ที่ส่งเข้ามา
        self.ammo = ammo

    
    #method => function ที่ถูกสร้างขึ้นมาในclass และเรียกใช้ได้ผ่าน obj
    def add_ammo(self, ammo):
        if self.ammo + ammo <= 10:
            self.ammo += ammo

    def fire_ammo(self):
        if self.ammo > 0:
            self.ammo -= 1
'''


#object  #self คืนค่า name, ammo มาให้ first_tank เลยไม่ต้องใส่self   #self คล้ายreturn มั้ย?
first_tank = t.Tank('กรุ้มกริ่ม', 3)  #ติดต่อฝ่ายขาย ว่าอยากได้รถถัง ชื่อ กรุ้มกริ่ม จำนวน 3 กระสุน
# first_tank.add_ammo(2)
first_tank.fire_ammo()
print(first_tank.ammo)

first_tank.fire_ammo()
first_tank.fire_ammo()
print(first_tank.ammo)

first_tank.add_ammo(6)
print(first_tank.ammo)


second_tank = t.Tank('ฟ๊องแฟ๊ง',6)
second_tank.add_ammo(3)
# second_tank.add_ammo(2) #if ไม่ผ่าน
print(second_tank.name)