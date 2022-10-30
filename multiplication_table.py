import tkinter as tk


def showOutput():
    number = 0

    # number = int(number_input.get())  #เพราะget จะreturn ค่ากลับมาเป็น str จึงต้องแปลงให้เป็นint
    # if number == 0:
    #     output_label.configure(text='ผิดที่ไว้ใจ')
    #     return

    try:
        number = int(number_input.get())  #เพราะget จะreturn ค่ากลับมาเป็น str จึงต้องแปลงให้เป็นint 
        if number == 0:
            raise Exception()
    except:
        output_label.configure(text='ผิดที่ไว้ใจ')
        return

    output = ''

    #คำนวณสูตรคูณ
    for i in range(1,13):
        output += str(number) + ' x ' + str(i) + ' = '
        output += str(number * i) + '\n'


    #update text in output
    output_label.configure(text=output)



window = tk.Tk()
window.title('JustPython')
window.minsize(width=400, height=400)


title_label = tk.Label(master=window, text="สูตรคูณแม่")
title_label.pack(pady=20) #pady = pad y เพิ่มพื้นที่ว่างด้านล่าง

number_input = tk.Entry(master=window, width=15)
number_input.pack(pady=5)

go_button = tk.Button(master=window, text="ได้แก่", command=showOutput, width=10, height=2)
go_button.pack()


output_label = tk.Label(master=window)
output_label.pack(pady=20)


window.mainloop()
