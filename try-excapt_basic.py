try: #คือเซฟโซน ถ้าเซฟโซนเกิดอะไรขึ้น เช่น สายฟ้าฟาด ก็จะส่งไปยังสายดิน
    x = int(input('X = '))
    y = int(input('Y = '))
    if x == 0:
        raise Exception()  #โยนความผิดลง except บรรทัด6-7 ไม่ต้องรันต่อ  #()จะใส่ข้อความข้างในก็ได้
    z = x/y
    print(z)
except: #สายดิน
    print('ผิดที่ไว้ใจ')
print('เส้นทางลูกผู้ชาย')