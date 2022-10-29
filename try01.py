# return คือ คืนค่ากลับไปยังตำแหน่งที่เรียกใช้มัน
            # ดังนั้น เราจึงสามารถสร้างตัวแปร เพื่อมารับค่าที่return กลับมาจากตำแหน่งนั้นได้
            # ถ้าอยากรู้คำตอบเมื่อไร ก็print ตำแปรที่สร้างขึ้นมาใหม่
            # ไม่ใช่บอกทุกครั้งที่เรียกใช้def เหมือนprint
            # และเมื่อเจอreturn ในdef เมื่อไร มันจะหยุดการทำงานของ def นั้นทันที

def get_box_area(width, length, height):
    if width < 0 or length < 0 or height < 0:
        return 0
    box_area = width * length * height
    return box_area

box1 = get_box_area(4,-4,0)
box2 = get_box_area(width=4, length=4, height=0)

print(box1)