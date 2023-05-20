import tkinter
# Вызывается в момент нажатия на кнопку:
def click():
  # Получаем строковое содержимое поля ввода с помощью метода get()
  # C помощью config() можем изменить отображаемый текст
  converter.set('{:.2f}'.format((5/9*(float(entry.get())-32))))
  window = tkinter.Tk()
  frame = tkinter.Frame(window)
  frame.pack()
  # Модель: создаем объект класса IntVar
  converter = tkinter.IntVar()
  # Обнуляем созданный объект с помощью метода set()
  #converter.set(0)
  entry = tkinter.Entry(frame)
  entry.pack()
  label = tkinter.Label(frame, textvariable=converter)
  label.pack()
  # Привязываем обработчик нажатия на кнопку к функции click()а
  button = tkinter.Button(frame, text='CONVERT', command=click)
  button.pack()
  window.mainloop()