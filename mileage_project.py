import tkinter as tk
import pickle

#model loaded
with open('mileage.pkl', 'rb') as fp:
    model = pickle.load(fp)
    fp.close()

root=tk.Tk()
cdr = tk.IntVar()
disp = tk.DoubleVar()
hp = tk.DoubleVar()
wt = tk.DoubleVar()

#function to clear input
def clear():
    cdr.set('')
    disp.set('')
    hp.set('')
    wt.set('')
clear()

#frame 1
f1 = tk.Frame(root,bg='#eeeeee')
l1=tk.Label(f1,text="Cylinders:".center(20))
l1.config(bg='#eeeeee', fg='#333333', font=('monospace', 12, 'bold'))
l1.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

e1 = tk.Entry(f1, textvariable=cdr)
e1.config(bg='#eeeeee', fg='#333333', font=('monospace', 12, 'bold'))
e1.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
e1.focus()
f1.config(height=5)
f1.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=5)

#frame 2
f2 = tk.Frame(root)
l2=tk.Label(f2,text="Displacement:".center(20))
l2.config(bg='#eeeeee', fg='#333333', font=('monospace', 12, 'bold'))
l2.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

e2 = tk.Entry(f2, textvariable=disp)
e2.config(bg='#eeeeee', fg='#333333', font=('monospace', 12, 'bold'))
e2.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
f2.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=5)

#frame 3
f3 = tk.Frame(root)
l3=tk.Label(f3,text="Horse Power:".center(20))
l3.config(bg='#eeeeee', fg='#333333', font=('monospace', 12, 'bold'))
l3.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

e3 = tk.Entry(f3, textvariable=hp)
e3.config(bg='#eeeeee', fg='#333333', font=('monospace', 12, 'bold'))
e3.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
f3.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=5)

#frame 4
f4 = tk.Frame(root)
l4=tk.Label(f4,text="Weight:".center(20))
l4.config(bg='#eeeeee', fg='#333333', font=('monospace', 12, 'bold'))
l4.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

e4 = tk.Entry(f4, textvariable=wt)
e4.config(bg='#eeeeee', fg='#333333', font=('monospace', 12, 'bold'))
e4.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
f4.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=5)

#frame 5 to display output
f5=tk.Frame(root)
l5=tk.Label(f5,text="""
 Prediction






""",height=10,font=('monospace', 18, 'bold'))
l5.pack()
f5.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=5)

def show(mil):
    global l5
    l5.pack_forget()
    l5=tk.Label(f5,text=f"""
Prediction
________________________________
Cylinders     : {float(cdr.get()):.2f}
Displacement  : {float(disp.get()):.2f}
Horse Power   : {float(hp.get()):.2f}
Weight        : {float(wt.get()):.2f}
_________________________________
Mileage       : {float(mil):2f}""",height=10,font=('monospace', 18, 'bold'))   
    
    l5.pack()


def predict():
    c = cdr.get()
    d = disp.get()
    h = hp.get()
    w = wt.get()
    features = [ [ c,d,h,w ] ]
    mil = model.predict(features)[0]
    show(mil)
    
#buttons
cal_b=tk.Button(root,text="Calculate",command=predict)
cal_b.config(bg='white', fg='red', font=('monospace', 20, 'bold'))
cal_b.pack(side=tk.LEFT,padx=20,pady=20)

exit_b=tk.Button(root,text="Quit",command=root.destroy)
exit_b.config(bg='white', fg='red', font=('monospace', 20, 'bold'))
exit_b.pack(side=tk.RIGHT,padx=20,pady=20)

#root.iconbitmap('images/chrysler.ico')
root.title("Mileage Calculator")
root.wm_minsize(700, 700)
root.resizable(0,0)
root.config(bg='#cc2900')
root.mainloop()