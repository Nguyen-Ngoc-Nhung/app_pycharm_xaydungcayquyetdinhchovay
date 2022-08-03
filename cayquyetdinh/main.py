from sys import path_hooks

import numpy
import pandas
from sklearn import datasets
import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter import ttk
from sklearn.model_selection import train_test_split
from sklearn import tree
import sklearn.metrics

data = pandas.read_csv("E:/khai thác dl/do an/lamsach.csv",low_memory= False)
data.drop('id', axis=1)

X_train, X_test, y_train, y_test = train_test_split(data[['age','sex','region','income','married','children','car','save_act','current_act','mortgage']].values,data['loan'].values,test_size=0.3, random_state=24)

clf = tree.DecisionTreeClassifier(max_depth=10)
clf = clf.fit(X_train,y_train)

predicted = clf.predict(X_test)
print(predicted)

print(y_test)

conf_ma = sklearn.metrics.confusion_matrix(y_test,predicted)
acc_score = sklearn.metrics.accuracy_score(y_test,predicted)

print(conf_ma)

print(acc_score)

print(clf.predict([[22,1,2,8877.07,0,0,0,0,1,0]]))

def click_me():
    if(var1.get()==1)&(var2.get()==0):
        married = 0
    else:
        married = 1
    if (var3.get() == 1) & (var4.get() == 0):
        car = 0
    else:
        car = 1
    if (var5.get() == 1) & (var6.get() == 0):
        save_act = 0
    else:
        save_act = 1
    if (var7.get() == 1) & (var8.get() == 0):
        current_act = 0
    else:
        current_act = 1
    if (var9.get() == 1) & (var10.get() == 0):
        mortgage = 0
    else:
        mortgage = 1

def tracuu():
    age = int(txt1.get())
    sex = cbb2.get()
    region = cbb3.get()
    income = int(txt4.get())
    children = int(cbb6.get())
    if (var1.get() == 1) & (var2.get() == 0):
        married = 0
    else:
        married = 1
    if (var3.get() == 1) & (var4.get() == 0):
        car = 0
    else:
        car = 1
    if (var5.get() == 1) & (var6.get() == 0):
        save_act = 0
    else:
        save_act = 1
    if (var7.get() == 1) & (var8.get() == 0):
        current_act = 0
    else:
        current_act = 1
    if (var9.get() == 1) & (var10.get() == 0):
        mortgage = 0
    else:
        mortgage = 1
    if sex =="Nữ":
        sex = 0
    if sex=="Nam":
        sex = 1

    if region=="INNER_CITY":
        region = 0
    if region =="TOWN":
        region = 1
    if region=="RURAL":
        region = 2
    else:
        region = 3

    intk = clf.predict([[age, sex, region, income,married, children, car, save_act, current_act, mortgage]])
    if intk[0] == 0:
        lbl12.configure(text="Xin lũiii bạn không đủ điều kiện",foreground='red')
    else:
        lbl12.configure(text="Cho vay nhé !!",foreground='red')


root= Tk()
root.geometry("2000x1000")
root.title("--- ỨNG DỤNG QUYẾT ĐỊNH CHO VAYYYYYY ---")
fts=Font(family='Times', size=16, weight='bold', slant='roman')
#define image
bg= PhotoImage(file="E:/khai thác dl/do an/—Pngtree—white christmas celebration christmas tree_1166172.png")
#create label
my_label=Label(root,image=bg)
my_label.place(x=0,y=0, relwidth=1,relheight=1)
my_label.pack()
my_text1=Label(root,text="                                              ",font=("Times",60))
my_text1.place(x=400, y=60)
my_text=Label(root,text="ỨNG DỤNG QUYẾT ĐỊNH CHO VAY",font=("Times",40))
my_text.place(x=400, y=80)


lbl1 = ttk.Label(root,text="Tuổi:",font=fts)
lbl1.place(x=600,y=200)
txt1 = Entry(root)
txt1.place(x=850, y=200)

lbl2 = ttk.Label(root,text="Giới tính:",font=fts)
lbl2.place(x=600,y=250)
cbb2 = ttk.Combobox(root)
cbb2['values'] = ("Nam", "Nữ")
cbb2.place(x=850, y=250)


lbl3 = ttk.Label(root,text="Nơi ở:",font=fts)
lbl3.place(x=600,y=300)
cbb3 = ttk.Combobox(root)
cbb3['values'] = ("INNER_CITY", "TOWN", "RURAL", "SUBURBAN")
cbb3.place(x=850, y=300)


lbl4 = ttk.Label(root,text="Thu nhập:",font=fts)
lbl4.place(x=600,y=350)
txt4 = Entry(root)
txt4.place(x=850, y=350)

var1 = tk.IntVar()
var2 = tk.IntVar()
lbl5 = ttk.Label(root,text="Đã kết hôn:",font=fts)
lbl5.place(x=600,y=400)
c1 = tk.Checkbutton(root, text='NO',variable=var1, onvalue=1, offvalue=0,command=click_me)
c1.pack()
c2 = tk.Checkbutton(root, text='YES',variable=var2, onvalue=1, offvalue=0,command=click_me)
c2.pack()
c1.place(x=850, y=400)
c2.place(x=950, y=400)

lbl6 = ttk.Label(root,text="Con cái:",font=fts)
lbl6.place(x=600,y=450)
cbb6 = ttk.Combobox(root)
cbb6['values'] = ("0", "1", "2", "3")
cbb6.place(x=850, y=450)

var3 = tk.IntVar()
var4 = tk.IntVar()
lbl7 = ttk.Label(root,text="Xe hơi:",font=fts)
lbl7.place(x=600,y=500)
c3 = tk.Checkbutton(root, text='NO',variable=var3, onvalue=1, offvalue=0,command=click_me)
c3.pack()
c4 = tk.Checkbutton(root, text='YES',variable=var4, onvalue=1, offvalue=0,command=click_me)
c4.pack()
c3.place(x=850, y=500)
c4.place(x=950, y=500)

var5 = tk.IntVar()
var6 = tk.IntVar()
lbl8 = ttk.Label(root,text="Tài khoản tiết kiệm:",font=fts)
lbl8.place(x=600,y=550)
c5 = tk.Checkbutton(root, text='NO',variable=var5, onvalue=1, offvalue=0,command=click_me)
c5.pack()
c6 = tk.Checkbutton(root, text='YES',variable=var6, onvalue=1, offvalue=0,command=click_me)
c6.pack()
c5.place(x=850, y=550)
c6.place(x=950, y=550)

var7 = tk.IntVar()
var8 = tk.IntVar()
lbl9 = ttk.Label(root,text="Tài khoản vãng lai:",font=fts)
lbl9.place(x=600,y=600)
c7 = tk.Checkbutton(root, text='NO',variable=var7, onvalue=1, offvalue=0,command=click_me)
c7.pack()
c8 = tk.Checkbutton(root, text='YES',variable=var8, onvalue=1, offvalue=0,command=click_me)
c8.pack()
c7.place(x=850, y=600)
c8.place(x=950, y=600)

var9 = tk.IntVar()
var10 = tk.IntVar()
lbl10 = ttk.Label(root,text="Thế chấp tài sản:",font=fts)
lbl10.place(x=600,y=650)
c9 = tk.Checkbutton(root, text='NO',variable=var9, onvalue=1, offvalue=0,command=click_me)
c9.pack()
c10 = tk.Checkbutton(root, text='YES',variable=var10, onvalue=1, offvalue=0,command=click_me)
c10.pack()
c9.place(x=850, y=650)
c10.place(x=950, y=650)

btn = ttk.Button(root,text="Tra cứu", comman=lambda:tracuu())
btn.place(x=800,y=720)


lbl11 = ttk.Label(root,text="Kết quả:",font=fts)
lbl11.place(x=600,y=790)
lbl12 = ttk.Label(root,text="",font=fts)
lbl12.place(x=850,y=790)

root.mainloop()
