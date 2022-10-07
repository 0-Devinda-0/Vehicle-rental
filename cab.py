from tkinter import *
from tkinter import ttk
mainWindow = Tk()

carList = ["1234","fff","lll"]
vanList = ["kkk","jjj"]
lorryList = []
truckList = []
threewList = []

inJobCar = []
inJobVan = []
injobTruck = []
inJobLorry = []
inJobThree = []

onjob = ["fff"]

categories = ["Car","Van","Lorry","3 Wheels","Truck"]



def refresh():
    Label(mainWindow,text="Cars",borderwidth=1).grid(row=6,column=0)
    Label(mainWindow,text="Vans").grid(row=6,column=1)
    Label(mainWindow,text="3 Wheels").grid(row=6,column=2)
    Label(mainWindow,text="Lorries").grid(row=6,column=3)
    Label(mainWindow,text="Trucks").grid(row=6,column=4)

    cars=Text(mainWindow, width=20, height=15)
    cars.grid(row=7,column=0)

    # Iterate over each item in the list
    for i in carList:
        cars.insert(END, i + '\n')

    #------------------------------------------------
    vans=Text(mainWindow, width=20, height=15)
    vans.grid(row=7,column=1)

    # Iterate over each item in the list
    for i in vanList:
        vans.insert(END, i + '\n')

    #------------------------------------------------
    wheel=Text(mainWindow, width=20, height=15)
    wheel.grid(row=7,column=2)

    # Iterate over each item in the list
    for i in threewList:
        wheel.insert(END, i + '\n')

    #------------------------------------------------
    lorries=Text(mainWindow, width=20, height=15)
    lorries.grid(row=7,column=3)

    # Iterate over each item in the list
    for i in lorryList:
        lorries.insert(END, i + '\n')

    #------------------------------------------------
    trucks=Text(mainWindow, width=20, height=15)
    trucks.grid(row=7,column=4)

    # Iterate over each item in the list
    for i in truckList:
        trucks.insert(END, i + '\n')



def sub_window_add():
    #checking of feald is empty
    if vehicle_id.get() == "":
        Label(add,text="Please enter the vehicle ID!",foreground="red").grid(row=4,column=0,columnspan = 2)

    else:
        #if van
        if smenu.get() == "Van":
            have = 0
            for i in vanList:
                if i == vehicle_id.get():
                    Label(add,text="Vehicle has been registerd!",foreground="red").grid(row=4,column=0,columnspan = 2)
                    have = 1
                    break
                
                else:
                    pass

            if have != 1:
                vanList.append(vehicle_id.get())
                print(vanList)
                Label(add,text="Vehicle registration successful").grid(row=4,column=0,columnspan = 2)
                refresh()

        #if car
        elif smenu.get() == "Car":
            have = 0
            for i in carList:
                if i == vehicle_id.get():
                    Label(add,text="Vehicle has been registerd!",foreground="red").grid(row=4,column=0,columnspan = 2)
                    have = 1
                    break
                
                else:
                    pass

            if have != 1:
                carList.append(vehicle_id.get())
                print(carList)
                Label(add,text="Vehicle registration successful").grid(row=4,column=0,columnspan = 2)
                refresh()

        #if 3wheel
        elif smenu.get() == "3 Wheels":
            have = 0
            for i in threewList:
                if i == vehicle_id.get():
                    Label(add,text="Vehicle has been registerd!",foreground="red").grid(row=4,column=0,columnspan = 2)
                    have = 1
                    break
                
                else:
                    pass

            if have != 1:
                threewList.append(vehicle_id.get())
                print(threewList)
                Label(add,text="Vehicle registration successful").grid(row=4,column=0,columnspan = 2)
                refresh()

        #if lorry
        elif smenu.get() == "Lorry":
            have = 0
            for i in lorryList:
                if i == vehicle_id.get():
                    Label(add,text="Vehicle has been registerd!",foreground="red").grid(row=4,column=0,columnspan = 2)
                    have = 1
                    break
                
                else:
                    pass

            if have != 1:
                lorryList.append(vehicle_id.get())
                print(lorryList)
                Label(add,text="Vehicle registration successful").grid(row=4,column=0,columnspan = 2)
                refresh()

        #if truck 
        elif smenu.get() == "Truck":
            have = 0
            for i in truckList:
                if i == vehicle_id.get():
                    Label(add,text="Vehicle has been registerd!",foreground="red").grid(row=4,column=0,columnspan = 2)
                    have = 1
                    break
                
                else:
                    pass

            if have != 1:
                truckList.append(vehicle_id.get())
                print(truckList)
                Label(add,text="Vehicle registration successful").grid(row=4,column=0,columnspan = 2)
                refresh()

def addVehiPop():
    global add
    add = Toplevel(mainWindow)
    add.geometry("350x250")
    add.title("Add a Vehicle")

    Label(add, text="Please fill the following infromations about new vehicle").grid(row=0,column=0,columnspan = 2)

    #vehicle Id input
    Label(add, text="Vehicle Id").grid(row=1,column=0)
    global vehicle_id
    vehicle_id = Entry(add, width=25, borderwidth=1)
    vehicle_id.grid(row=1,column=1)

    #vehicle type/ dropdown for sub window
    global smenu
    smenu = StringVar()
    smenu.set(categories[1])

    vehicle_type = OptionMenu(add, smenu, *categories, )
    vehicle_type.grid(row=2,column=0)

    
    #creating buttons
    Button(add, text = "Add", command = sub_window_add).grid(row = 3,column = 0,columnspan=2)

#list appending logic
    
def deleteVehiPop():
    global delete
    delete = Toplevel(mainWindow)
    delete.geometry("350x250")
    delete.title("Add a Vehicle")
    Label(delete, text="Please fill the following infromations about new vehicle").grid(row=0,column=0,columnspan = 2)

    #vehicle Id input
    Label(delete, text="Vehicle Id").grid(row=1,column=0)
    global vehicle_id_del
    vehicle_id_del = Entry(delete, width=25, borderwidth=1)
    vehicle_id_del.grid(row=1,column=1)

    #vehicle type/ dropdown for sub window
    global delmenu
    delmenu = StringVar()
    delmenu.set(categories[1])

    vehicle_type = OptionMenu(delete, delmenu, *categories, )
    vehicle_type.grid(row=2,column=0)

    
    #creating buttons
    Button(delete, text = "Delete", command = sub_window_delete).grid(row = 3,column = 0,columnspan=2)

#list popping logic

def sub_window_delete():
    #chicikng if vehicle id is empty?
    
    if vehicle_id_del.get() == "":
        Label(delete,text="Please enter the vehicle ID!",foreground="red").grid(row=4,column=0,columnspan = 2)

    else:
        #checking if the vehicle is currntly hired
        injob = 0
        for i in onjob:
            if i == vehicle_id_del.get():
                injob = 1
            else:
                pass

        if injob == 1:
            Label(delete,text="The vehicle is currntly hired",foreground="red").grid(row=4,column=0,columnspan = 2)
            
        else:
            try:
                #if van
                if delmenu.get() == "Van":
                    vanList.remove(vehicle_id_del.get())
                    print(vanList)
                    Label(delete,text="Vehicle deleted").grid(row=4,column=0,columnspan = 2)
                    refresh()
                    
                elif delmenu.get() == "Car":
                    carList.remove(vehicle_id_del.get())
                    print(carList)
                    Label(delete,text="Vehicle deleted").grid(row=4,column=0,columnspan = 2)
                    refresh()

                elif delmenu.get() == "Lorry":
                    lorryList.remove(vehicle_id_del.get())
                    print(lorryList)
                    Label(delete,text="Vehicle deleted").grid(row=4,column=0,columnspan = 2)
                    refresh()

                elif delmenu.get() == "3 Wheel":
                    threewList.remove(vehicle_id_del.get())
                    print(threewList)
                    Label(delete,text="Vehicle deleted").grid(row=4,column=0,columnspan = 2)
                    refresh()

                elif delmenu.get() == "Truck":
                    truckList.remove(vehicle_id_del.get())
                    print(truckList)
                    Label(delete,text="Vehicle deleted").grid(row=4,column=0,columnspan = 2)
                    refresh()

            except:
                Label(delete,text="Couldn't find the vehicle. Check vehicle ID and try again",foreground="red").grid(row=4,column=0,columnspan = 2)
            

def assignJob():
    if inOne == "":
        Label(mainWindow,text="Feald is empty..!", foreground="red").grid(row=0,column=2,columnspan=2)
    else:
        try:
            if menu.get() == "Car":
                onjob.append(inOne.get())
                inJobCar.append(inOne.get())
                carList.remove(inOne.get())
            
            elif menu.get() == "Van":
                inJobVan.append(inOne.get())
                vanList.remove(inOne.get())
                onjob.append(inOne.get())
            
            elif menu.get() == "3Wheel":
                inJobThree.append(inOne.get())
                threewList.remove(inOne.get())
                onjob.append(inOne.get())
            
            elif menu.get() == "Lorry":
                inJobLorry.append(inOne.get())
                lorryList.remove(inOne.get())
                onjob.append(inOne.get())
            
            elif menu.get() == "Truck":
                injobTruck.append(inOne.get())
                truckList.remove(inOne.get())
                onjob.append(inOne.get())

            refresh()    

        except:
            Label(mainWindow,text="Can not find the vehicle..", foreground="red").grid(row=0,column=2,columnspan=2)
            
def removeJob():
    if inOne == "":
        Label(mainWindow,text="Feald is empty..!", foreground="red").grid(row=0,column=2,columnspan=2)
    else:
        try:
            if menu.get() == "Car":
                
                carList.append(inOne.get())
                inJobCar.remove(inOne.get())
                onjob.remove(inOne.get())
            
            elif menu.get() == "Van":
                vanList.append(inOne.get())
                inJobVan.remove(inOne.get())
                onjob.remove(inOne.get())
            
            elif menu.get() == "3Wheel":
                threewList.append(inOne.get())
                inJobThree.remove(inOne.get())
                onjob.remove(inOne.get())
            
            elif menu.get() == "Lorry":
                lorryList.append(inOne.get())
                inJobLorry.remove(inOne.get())
                onjob.remove(inOne.get())
            
            elif menu.get() == "Truck":
                truckList.append(inOne.get())
                injobTruck.remove(inOne.get())
                onjob.remove(inOne.get())

            refresh()   

        except:
            Label(mainWindow,text="Can not find the vehicle..", foreground="red").grid(row=0,column=2,columnspan=2)

# Label(mainWindow, text = "Vehicle type").grid(row=0,column=0)
Label(mainWindow, text = "Enter the vehicle Id").grid(row=1,column=0)


menu = StringVar()
menu.set(categories[1])
#drop down lists
vehicle_type = OptionMenu(mainWindow, menu,*categories, )
vehicle_type.grid(row=4,column=0)
#text input
inOne = Entry(mainWindow, width= 25, borderwidth = 1)
inOne.grid(row=1,column=1)

refresh()
#button 


Button(mainWindow, text = "Hire", command = assignJob).grid(row = 3,column = 0)
Button(mainWindow, text = "Add Vehicle", command = addVehiPop).grid(row = 3,column = 4)
Button(mainWindow, text = "Delete Vehicle", command = deleteVehiPop).grid(row = 4,column = 4)
Button(mainWindow, text = "Avalable Vehicles", command = refresh).grid(row = 5,column = 4)
Button(mainWindow, text = "Returned", command = removeJob).grid(row = 3,column = 1)

mainWindow.mainloop()