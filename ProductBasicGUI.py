# is All Library (tkinter packageAll GUI Python)
from tkinter import * 
from tkinter import ttk

def Addproduct():
	pd = product.get() #String %s
	pc = float(price.get()) # float %f
	qt = int(quantity.get()) # int %d
	cal = pc * qt

    #Calculate Summary
	#print(pd,pc,qt,cal)
	resulttext = "Product: %s Price: %.2f Quantity: %d \nTotal Payment: %.2f Baht"%(pd,pc,qt,cal)
	#print(resulttext)
	result.set(resulttext)

#------- GEOMETRY-------------
GUI =Tk()
GUI.geometry('500x500')
GUI.title('Shopping Cart By Peter')
#------------------------------

product = StringVar()
price = StringVar()
quantity = StringVar()

Logo = PhotoImage(file='drink.jpg')
GUILogo = Label(GUI, image=Logo)

#------- Label and Entry of Product ---------------------------------
LProduct = Label(GUI, text='Product', font=('Aagsana New',16))
LProduct.pack(padx=5,pady=5)

EProduct = ttk.Entry(GUI, textvariable=product,font=('Aagsana New',16))
EProduct.pack(padx=5,pady=5)

#------- Label and Entry of Price ---------------------------------
LPrice = Label(GUI, text='Price', font=('Aagsana New',16))
LPrice.pack(padx=5,pady=5)

EPrice = ttk.Entry(GUI, textvariable=price,font=('Aagsana New',16))
EPrice.pack(padx=5,pady=5)

#------- Label and Entry of Quantity ---------------------------------
LQuantity = Label(GUI, text='Quantity', font=('Aagsana New',16))
LQuantity.pack(padx=5,pady=5)

EQuantity = ttk.Entry(GUI, textvariable=quantity,font=('Aagsana New',16))
EQuantity.pack(padx=5,pady=5)


#------------ Button Add Product-------
BAddproduct = ttk.Button(GUI, text='Add',command=Addproduct)
BAddproduct.pack(padx=5,pady=5,ipadx=10,ipady=10)

#----------Result Labal-------------------
result = StringVar() # Show Display
LResult = Label(GUI, textvariable=result, font=('Angsana New',16))
LResult.pack(padx=10,pady=10)

#----------------------
GUI.mainloop()
#----------------------