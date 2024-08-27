import tkinter as tk


#* Первичная Настройка
root = tk.Tk()   
root.geometry("285x400")
root.title("Calculator")
root.resizable(False,False)
display = tk.StringVar()
display.set("0")


#* Создание кнопок и Окно вывода
display_label = tk.Label(root, textvariable=display, font=("Arial", 24), anchor="e", background="white")
display_label.grid(row=0, column=0, columnspan=4)

#* Кнопки ввиде массива
buttons = [
   "7", "8", "9", "/",
   "4", "5", "6", "*",
   "1", "2", "3", "-",
   "0", ".", "=", "+"]

row_val = 1
col_val = 0

for button in buttons:
   tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda b=button: update_display(b) if b != "=" else calculate()).grid(row=row_val, column=col_val)
   col_val += 1
   if col_val > 3:
      col_val = 0
      row_val += 1

#* Проверка на ошибку или если все цифра 0 
def update_display(value):
   current_text = display.get()
   if current_text == "0" or current_text == "Error":
      display.set(value)
   else:
      display.set(current_text + value)

#* Выполнения расчетов
def calculate():
   try:
      result = eval(display.get())
      display.set(result)
   except:
      display.set("Error")
root.mainloop()