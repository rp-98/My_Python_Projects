import tkinter
from PyDictionary import PyDictionary
from tkinter import Entry,LEFT,Button,Tk,Label
global data
def search(dict_entry,results):
    dictionary=PyDictionary()
    try:
        data=dictionary.meaning(dict_entry.get())
        data=data['Noun']
        text=''
        for data_ in data:
            text=text+'\n\n'+str(data_)
        results.configure(text=text,wraplength=300,justify=LEFT)
    except:
        results.configure(text='Check the spelling \n''check your connnection\n',wraplength=300,justify=LEFT)
def ui():
    root=Tk()
    root.title('Dictionary | Ravi Prakash')
    heading=Label(root,text="Ravi's Dictionary",font=('Times',40))
    dict_entry=Entry(root)
    results=Label(root)
    search_button=Button(root,text='Search',command=lambda:search(dict_entry,results))
    #gui
    heading.pack()
    dict_entry.pack()
    search_button.pack()
    results.pack()
    root.mainloop()
if __name__=='__main__':
    ui()