from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

#Text
description_text = Label(text="is equal to   ", font=('Arial', 12, 'normal'))
description_text.grid(row=1, column=0)

miles_text = Label(text="  Miles", font=('Arial', 12, 'normal'))
miles_text.grid(row=0, column=2)

km_text = Label(text="Km", font=('Arial', 12, 'normal'))
km_text.grid(row=1, column=2)
km_text.config(pady=30)



#Miles input
miles_input = Entry(textvariable='0', width=10)
miles_input.grid(row=0, column=1)


#Km output
km_output = Label(text="0", font=('Arial', 12, 'normal'))
km_output.grid(row=1, column=1)


#Calculate button
def button_click():
    mile = int(miles_input.get())
    output = round((mile * 1.60934),2)
    km_output.config(text=f'{output}')


calculate_button = Button(text='Calculate', command=button_click)
calculate_button.grid(row=2, column=1)


window.mainloop()