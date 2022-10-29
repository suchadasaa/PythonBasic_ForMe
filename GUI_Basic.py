import tkinter as tk

window = tk.Tk()
window.title('JustPython')
window.minsize(width=400, height=400)


#UI label
title_level = tk.Label(master=window, text="เมื่อรักฉันเกิด") #master บอกว่าLabelนี้จะถูกใส่ในwindow อะไร
title_level.pack()  #เอามาแปะในแอพของเรา


#UI ช่องกรอบข้อความ
text_input = tk.Entry(master=window)
text_input.pack()

#UI button
ok_button = tk.Button(master=window, text="Okey")
ok_button.pack()


window.mainloop()  #start app