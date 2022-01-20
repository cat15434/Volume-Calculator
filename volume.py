import math
from math import pi
import tkinter as tk

#OPTION MENU STUFF
#_______________________________________________
#Create List with List options
shapelist=[
"Sphere",
"Cylinder",
"Cone",
"Cube",
"Rectangular Prism",
"Pyramid",

]
#STart Tkinter loop
w=tk.Tk()
#Create Optionmenu
shape1=tk.StringVar(w)
#Create Option menu default text
shape1.set("Select A Shape")
#Place the option menu
shapechoice=tk.OptionMenu(w,shape1,*shapelist)
shapechoice.pack()
#___________________________________________________




#VARIABLE STUFF
#___________________________________________________________________________
#Make height entry
height1=tk.Entry(w)
#Make radius entry
radius1=tk.Entry(w)
width1=tk.Entry(w)
length1=tk.Entry(w)
#Create labels for raidus/height/width/length info
heightlabel=tk.Label(text="Height^; needed for Cylinder, cone, Rectangular prism, Pyramid, Cube")
radiuslabel=tk.Label(text="Radius^; needed for all round shapes")
widthLabel=tk.Label(text="Width^; needed for cuboid objects(Cube,Rectangular prism,Pyramid)")
lengthlabel=tk.Label(text="Length^; needed for cuboid objects(Cube,Rectangular prism,Pyramid)")
coollabel=tk.Label(text="Cube is L*W*H or x^3 so we only need width")
coollabel.pack()
#place labels and packs
radius1.pack(),radiuslabel.pack()
height1.pack(),heightlabel.pack()  
length1.pack(),lengthlabel.pack()
width1.pack(),widthLabel.pack()  
#___________________________________________________________________________    

#CALCULATE STUFF    
#______________________________________________________________
#define calculate loop
def calculate():
    #get chosen shape from shape menu
    shape=shape1.get()
    #Spehe math
    if shape=='Sphere':
        
        radius=float(radius1.get())
        v=4/3*pi*radius**3
        
        
        print(v)
     #Cylinder Math   
    elif shape=='Cylinder':
        
        radius=float(radius1.get())
        height=float(height1.get())
        v=pi*radius**2*height
        print(v)
    #Cone math
    elif shape=='Cone':
     
        
        radius=float(radius1.get())
        height=float(height1.get())
        v=[(pi*radius**2*height)/3]
        print(v)
    #Cube math
    elif shape== 'Cube':
        width=float(width1.get())


        v=width**3


    elif shape=='Rectangular Prism':
        width=float(width1.get())
        height=float(height1.get())
        length=float(length1.get())
        v=length *width* height
        print(v)
    elif shape=='Pyramid':
        width=float(width1.get())
        height=float(height1.get())
        length=float(length1.get())
        v=(length *width* height)/3




    
    #Create answer label
        
    answ=tk.Label(text="The answer is {}".format(v))
    answ.pack()
    w.after(2500,answ.destroy)
#_______________________________________________________________________




#Calculate button
calculatebutton=tk.Button(w,text="Calculate",command=calculate)
calculatebutton.pack()
w.mainloop()