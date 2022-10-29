class Tank:   #ฝ่ายขาย
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