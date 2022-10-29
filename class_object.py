#class
class Tank:   #ฝ่ายขาย
    def __init__(self, name, ammo): #ทีมวิศวกรขี้อาย  #self คือแขกVIP => ตัวใส่ข้อมูลให้รถถัง และคืนค่าข้อมูลทั้งหมดกลับไปให้เจ้าของที่สั่งซื้อรถถังมา 
        self.name = name  #self.name ชื่อรถถัง = name คือparamitor ที่ส่งเข้ามา
        self.ammo = ammo


#object  #self คืนค่า name, ammo มาให้ first_tank เลยไม่ต้องใส่self   #self คล้ายreturn มั้ย?
first_tank = Tank('กรุ้มกริ่ม', 3)  #ติดต่อฝ่ายขาย ว่าอยากได้รถถัง ชื่อ กรุ้มกริ่ม จำนวน 3 กระสุน
print(first_tank.ammo)