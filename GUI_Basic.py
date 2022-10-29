from cgitb import text
import tkinter as tk

window = tk.Tk()
window.title('JustPython')
window.minsize(width=400, height=400)


def set_message():
    text = text_input.get()  #ดึงข้อความที่กรอก เอามาใช้งานได้
    title_level.configure(text=text)  #กำหนดค่าให้เป็นไปตาม text(text_input)

#UI label
title_level = tk.Label(master=window, text="เมื่อรักฉันเกิด") #master บอกว่าLabelนี้จะถูกใส่ในwindow อะไร
title_level.pack()  #เอามาแปะในแอพของเรา


#UI ช่องกรอบข้อความ
text_input = tk.Entry(master=window)
text_input.pack()

#UI button
ok_button = tk.Button(master=window, text="Okey", command=set_message)  #command เมื่อกดแล้วเรียกใช้ฟังก์ชัน **ระวังอย่าเผลอใส่() เพราะฟังก์ชัน อาจจะถูกรันก่อนถูกกด
ok_button.pack()


window.mainloop()  #start app