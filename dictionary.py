import json
import tkinter

window=tkinter.Tk()
window.title('Dictionary')

left_frame=tkinter.Frame(window)
left_frame.grid(row=0, column=0)
label=tkinter.Label(left_frame, text="ENTER WORD : ").grid(row=0,column=0)
input_field=tkinter.Entry(left_frame,font=("times",15))
input_field.grid(row=1,column=0)
label1=tkinter.Label(left_frame, text="MEANING : ").grid(row=2,column=0)
result=tkinter.Text(left_frame, width=50, height=20)
result.grid()

f=open('dict.json',encoding='utf-8')
data=json.load(f)

def find_meaning():
    result.delete(1.0,tkinter.END)
    word=input_field.get()
    word=word.lower()
    if word in data:
        result.insert(tkinter.END,data[word])
        result.insert(tkinter.END, '\n\n' + "If you think the above meaning is incorrect, then modify the meaning and then click on edit button" )
    else:
        result.insert(tkinter.END,"No such word found in dictionary!! You can add this word by writing its meaning in this box and then click on add button")

def edit_meaning():
    word=input_field.get()
    new_meaning=result.get(1.0,tkinter.END)
    data[word]=new_meaning
    with open('dict.json','w',encoding='utf-8') as file:
      json.dump(data,file)

def add_word():
    word=input_field.get()
    if word in data:
        result.insert(tkinter.END,"\nError! Word already exists in dictionary. You cannot add same word again.")
    else:
     new_meaning = result.get(1.0, tkinter.END)
     data[word] = new_meaning
     with open('dict.json', 'w', encoding='utf-8') as file:
       json.dump(data, file)

right_frame=tkinter.Frame(window)
right_frame.grid(row=0, column=1)
btn=tkinter.Button(right_frame, text="Search", width=20, height=5, command=find_meaning)
btn.grid(row=0,column=0)
btn1=tkinter.Button(right_frame, text="add", width=20, height=5, command=add_word)
btn1.grid(row=1,column=0)
btn2=tkinter.Button(right_frame, text="edit", width=20, height=5, command=edit_meaning)
btn2.grid(row=2,column=0)

window.mainloop()

