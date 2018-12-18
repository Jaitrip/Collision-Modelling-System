import math #imports the library math allowing the use of functions like sin and cos
import time #imports the library time which i require for the tkinter animation
import random #imports the library random which i need for the animation
from tkinter import * #imports tkinter which allows me to create animations and a graphical user interface

#----------------------Error Messgae--------------------------------------------------------------------------------------------------------------------
def invalid():
    GUI = Tk() #creates the user interface
    GUI.title("Error") #title of the interface
    GUI.geometry() #the size of the window, in this case it will be as big as it needs to be for the amount of objects placed within it 

    label  = Label(GUI, text="Invalid Value, please enter a valid value") #creates a label
    label.grid(row=0) #places the label in a certian position on the page
    GUI.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------






#---------------------Main Program----------------------------------------------------------------------------------------------------------------------
def collision():

    def __init__():
        master= Tk()
        master.title("Collision Modelling") #Title of page

        label = Label(master, text="DISCLAMER: in this program mass should be entered in kilograms, velocity in metres per second and angles in degrees")
        label.grid(row=3)

        label1 = Label(master, text="All velocity values must be greater than or equal to 0 and less than or equal to 3x10^8")
        label1.grid(row=4)

        label2 = Label(master, text="All mass values must be greater than 0 and less than or equal to 1x10^14")
        label2.grid(row=5)

        label3 = Label(master, text="All angles must be greater than 0 and less than 90")
        label3.grid(row=6)





#---------------------One Dimensional Collision---------------------------------------------------------------------------------------------------------
        def onedimension():
            keyGUI = Toplevel()#Top level means it is constantly updating 
            keyGUI.title("1D collision")
            keyGUI.geometry()

            label1 = Label(keyGUI, text="Mass Of Object 1")
            label1.grid(row=0, sticky=W)
            
            v1= DoubleVar() #DoubleVar = float
            e1 = Entry(keyGUI, textvariable= v1) #creates an entry box
            e1.grid(row=0, column=1)
            
            
            label2 = Label(keyGUI, text="Velocity Of Object 1")
            label2.grid(row=1, sticky=W)
            
            v2= DoubleVar()
            e2= Entry(keyGUI, textvariable= v2)
            e2.grid(row=1, column=1)
            

            label3 = Label(keyGUI, text="Mass Of Object 2")
            label3.grid(row=2, sticky=W)
            
            v3= DoubleVar()
            e3= Entry(keyGUI, textvariable= v3)
            e3.grid(row=2, column=1)
            

            label4 = Label(keyGUI, text="Velocity Of Object 2")
            label4.grid(row=3, sticky=W)
            
            v4= DoubleVar()
            e4 = Entry(keyGUI, textvariable= v4)
            e4.grid(row=3, column=1)
            
            
            
        
            label6 = Label(keyGUI, text="Is the collision elastic or inelastic?")
            label6.grid(row=4, sticky=W)
            
            v6= StringVar() #String variable
            e6 = Entry(keyGUI, textvariable= v6)
            e6.grid(row=4, column=1)

            photo4 = PhotoImage(file="oned.png") #Brings a photo from specified area in storage into the gui 
            label25 = Label(keyGUI, image=photo4) #Places the images as a label onto the gui
            label25.image = photo4
            label25.grid(row=6, column=3)
            
        

            def calculate ():

                a=2
                #Validation Tests


                try:
                    mass1=v1.get() 
                    if (mass1 > 0) and (mass1 <= 100000000000000000):
                        a=2
                    else:
                        a=1
                        invalid()
                except ValueError:
                    a=1
                    invalid()
                #If mass is greater than 0 and less or equal to 1x10^14 the value will be stored and the program will be continue
                #Other wise the program will display a error message

                

                if a==2:

            
                    try:
                        velocity1=v2.get()  #If velocity is greater than or equal to 0 and less than or equal to 3x10^8 tests passed
                        if (velocity1 >=0) and (velocity1 <= 300000000):
                            a=2
                        else:
                            a=1
                            invalid()
                    except ValueError:
                        a=1
                        invalid() #If test is not passed then error message page shown
                else:
                    invalid()


                if a==2:
            
                    try:
                        mass2=v3.get() #If mass is greater than 0 and less than 1x10^14 test passed
                        if (mass2 > 0) and (mass2 <= 100000000000000000):
                            a=2
                        else:
                            a=1
                            invalid()
                    except ValueError:
                        a=1
                        invalid()
                else:
                    invalid()

                if a==2:

            
                    try:
                        velocity2=v4.get() #if velocity is greater than -3x10^8 and less than 0 test passed. Value is -ve as its traveling in the negative direction
                        if (velocity2 <=0) and (velocity2 >=-300000000):
                            a=2
                        else:
                            a=1
                            invalid()
                    except ValueError:
                        a=1
                        invalid()
                else:
                    invalid()


                if a==2:

                    collision = v6.get()
                    if (collision.lower() == "elastic") or (collision.lower() == "inelastic"): #if the variable is "elastic" or "inelastic" passed
                        a=2
                    else:
                        a=1
                        invalid()
                else:
                    c=1

                #If the variable contains a string with one of the two words then the program will continue, other wise it will display an error


                



                if a==2:
                #If the inputs pass the validation tests the program carrys out the required function

                    GUI3 = Tk()
                    GUI3.title("1D collision")
                    GUI3.geometry()

            
                    momentum1=(mass1*velocity1) #momentum = mass * velocity
                    momentum2=(mass2*velocity2)
                    KineticE1=(mass1*velocity1*velocity1*1/2) #Kinetic energy = 1/2 * mass * velocity^2
                    KineticE2=(mass2*velocity2*velocity2*1/2)
                    totalmo=(momentum1+momentum2)
                    d=0
                    c=0

                            


                    if collision==("elastic"):
                    #Depending on the string variable the program will carry out one of the two functions
                        d=1
                        #New velocities, momentums and kinetic energies after the collision is calculated
                        newVelocity1 = (((mass1-mass2)*velocity1)/(mass1+mass2))+((2*mass2*velocity2)/(mass1+mass2))
                        newVelocity2 = ((2*mass1*velocity1)/(mass1+mass2))-(((mass1-mass2)*velocity2)/(mass1+mass2))
                        NewKE1 = (((mass1)*(newVelocity1)*(newVelocity1))/2)
                        NewKE2 = (((mass2)*(newVelocity2)*(newVelocity1))/2)
                        newMomentum1=(mass1*newVelocity1)
                        newMomentum2=(mass2*newVelocity2)
                        
                           

                    if collision==("inelastic"):
                            c=1
                            #Depending on the string variable the program will carry out one of the two functions
                            newVelocity1=((mass1*velocity1)+(mass2*velocity2))/(mass1+mass2)
                            #New velocity and kinetic energy calculated
                            NewKE1=((mass1+mass2)*(newVelocity1*newVelocity1))/2
                            
                                
                                

                    label7 = Label(GUI3, text="Before The Collision")
                    label7.grid(row=0)

                    label8 = Label(GUI3, text="")
                    label8.grid(row=1)

                    label9 = Label(GUI3, text="Momentum Of Object 1")
                    label9.grid(row=2, sticky=W) #Labels and objects put in this window

                    e7 = Entry(GUI3)
                    e7.grid(row=2, column=1)
                    e7.insert(0,momentum1)


                    label10 = Label(GUI3, text="Kinetic Energy Of Object 1")
                    label10.grid(row=3, sticky=W) #Variable is inserted into the entry box

                    e8 = Entry(GUI3)
                    e8.grid(row=3, column=1)
                    e8.insert(0,KineticE1)


                    label11 = Label(GUI3, text="Momentum Of Object 2")
                    label11.grid(row=4, sticky=W)

                    e9 = Entry(GUI3)
                    e9.grid(row=4, column=1)
                    e9.insert(0,momentum2)


                    label12 = Label(GUI3, text="Kinetic Energy Of Object 2")
                    label12.grid(row=5, sticky=W)

                    e10 = Entry(GUI3)
                    e10.grid(row=5, column=1)
                    e10.insert(0,KineticE2)


                    

                    label15 = Label(GUI3, text="")
                    label15.grid(row=8)

                    label16 = Label(GUI3, text="After The Collision")
                    label16.grid(row=9)

                    label17 = Label(GUI3, text="")
                    label17.grid(row=10)

                   


                    if c==1:
                    #Depending on the string variable the program will change the interface created
                        label18 = Label(GUI3, text="New Velocity Of Object 1")
                        label18.grid(row=11, sticky=W)

                        e13 = Entry(GUI3)
                        e13.grid(row=11, column=1)
                        e13.insert(0,newVelocity1)


                        
                        label21 = Label(GUI3, text="Kinetic Energy Of Object 1")
                        label21.grid(row=14, sticky=W)

                        e16 = Entry(GUI3)
                        e16.grid(row=14, column=1)
                        e16.insert(0,NewKE1)

                        def animation():
                            anim1 = Tk()
                            anim1.title("Inelastic collision animation")
                            canvas = Canvas(anim1, width = 700, height = 300) #Creates a canvas
                            canvas.pack()

                            if totalmo < 0: #if total momentum is less than 0 this code is done
                                x0 = 10	#top left hand corner of shapes x coordinate	
                                y0 = 100 #top left hand corner of shapes y coordinate		
                                x1 = 60	 #Bottom right hand corner of shapes x coordinate 
                                y1 = 150 #Bottom right hand corner of shapes y coordinate 

                                x2 = 650 #top right hand corner of shapes x coordinate		
                                y2 = 100 #top left hand corner of shapes y coordinate	
                                x3 = 700 #Bottom right hand corner of shapes x coordinate 		
                                y3 = 150 #Bottom right hand corner of shapes y coordinate 

                                dx = 2 #X component of speed 
                                dy = 0 #Y component of speed

                                d2x = -2 #X component of speed
                                d2y = 0 #Y component of speed
                        
                                ball1 = canvas.create_oval(x0, y0, x1, y1, fill="blue", tag='blueBall') #Creates ball 1 with the following attributes
                                ball2 = canvas.create_oval(x2, y2, x3, y3, fill="red", tag='redBall') #Creates ball 2 with the following attributes

                                while True:

                                    canvas.move('blueBall', dx, dy) #Makes ball move with those speeds
                                    canvas.move('redBall', d2x, d2y)

                                    pos = canvas.coords(ball1)
                                    pos1 = canvas.coords(ball2)

                                    canvas.after(20)
                                    canvas.update()

                                    if pos[2] >= 360:
                                        dx = -2
                                        dy = 0

                            if totalmo > 0: #if total momentum is greater than 0 this code is done
                                x0 = 10		
                                y0 = 100		
                                x1 = 60	
                                y1 = 150

                                x2 = 650		
                                y2 = 100	
                                x3 = 700		
                                y3 = 150

                                dx = 2
                                dy = 0

                                d2x = -2
                                d2y = 0
                        
                                ball1 = canvas.create_oval(x0, y0, x1, y1, fill="blue", tag='blueBall')
                                ball2 = canvas.create_oval(x2, y2, x3, y3, fill="red", tag='redBall')

                                while True:

                                    canvas.move('blueBall', dx, dy)
                                    canvas.move('redBall', d2x, d2y)

                                    pos = canvas.coords(ball1)
                                    pos1 = canvas.coords(ball2)

                                    canvas.after(20)
                                    canvas.update()

                                    if pos1[0] <= 350:
                                        d2x = 2
                                        d2y = 0

                            if totalmo == 0: #if total momentum = 0 this is carried out
                                x0 = 10		
                                y0 = 100		
                                x1 = 60	
                                y1 = 150

                                x2 = 650		
                                y2 = 100	
                                x3 = 700		
                                y3 = 150

                                dx = 2
                                dy = 0

                                d2x = -2
                                d2y = 0
                        
                                ball1 = canvas.create_oval(x0, y0, x1, y1, fill="blue", tag='blueBall')
                                ball2 = canvas.create_oval(x2, y2, x3, y3, fill="red", tag='redBall')

                                while True:

                                    canvas.move('blueBall', dx, dy)
                                    canvas.move('redBall', d2x, d2y)

                                    pos = canvas.coords(ball1)
                                    pos1 = canvas.coords(ball2)

                                    canvas.after(20)
                                    canvas.update()

                                    if pos[2] >= 350:
                                        dx = 0
                                        dy = 0

                                    if pos1[0] <= 350:
                                        d2x = 0
                                        d2y = 0




                            anim1.mainloop


                        animation_button = Button(GUI3, text="General Animation", command=animation)
                        animation_button.grid(row=15)



                    if d==1:

                        label18 = Label(GUI3, text="New Velocity Of Object 1")
                        label18.grid(row=11, sticky=W)

                        e13 = Entry(GUI3)
                        e13.grid(row=11, column=1)
                        e13.insert(0,newVelocity1)
                            
                        label19 = Label(GUI3, text="New Velocity Of Object 2")
                        label19.grid(row=12, sticky=W)

                        e14 = Entry(GUI3)
                        e14.grid(row=12, column=1)
                        e14.insert(0,newVelocity2)


                        label20 = Label(GUI3, text="Momentum Of Object 1")
                        label20.grid(row=13, sticky=W)

                        e15 = Entry(GUI3)
                        e15.grid(row=13, column=1)
                        e15.insert(0,newMomentum1)


                        label21 = Label(GUI3, text="Kinetic Energy Of Object 1")
                        label21.grid(row=14, sticky=W)

                        e16 = Entry(GUI3)
                        e16.grid(row=14, column=1)
                        e16.insert(0,NewKE1)


                        label22 = Label(GUI3, text="Momentum Of Object 2")
                        label22.grid(row=15, sticky=W)

                        e17 = Entry(GUI3)
                        e17.grid(row=15, column=1)
                        e17.insert(0,newMomentum2)


                        label23 = Label(GUI3, text="Kinetic Energy Of Object 2")
                        label23.grid(row=16, sticky=W)

                        e18 = Entry(GUI3)
                        e18.grid(row=16, column=1)
                        e18.insert(0,NewKE2)

                        def animation():
                            anim1 = Tk()
                            anim1.title("Elastic collision animation")
                            canvas = Canvas(anim1, width = 700, height = 300)
                            canvas.pack()
                            x0 = 10 # dimensions of all the balls		
                            y0 = 100		
                            x1 = 60	
                            y1 = 150

                            x2 = 650		
                            y2 = 100	
                            x3 = 700	    
                            y3 = 150

                            dx = 2
                            dy = 0

                            d2x = -2
                            d2y = 0
                    
                            ball1 = canvas.create_oval(x0, y0, x1, y1, fill="blue", tag='blueBall')
                            ball2 = canvas.create_oval(x2, y2, x3, y3, fill="red", tag='redBall')

                            while True:

                                canvas.move('blueBall', dx, dy)
                                canvas.move('redBall', d2x, d2y)

                                pos = canvas.coords(ball1)
                                pos1 = canvas.coords(ball2)

                                canvas.after(20)
                                canvas.update()

                                if pos[2] >= 360: #if position is 360 or greater then attributes changed 
                                    dx = -2
                                    dy = 0

                                if pos1[2] <= 400:
                                    d2x = 2
                                    dy = 0


                            anim1.mainloop


                        animation_button = Button(GUI3, text="General Animation", command=animation)
                        animation_button.grid(row=18)



            calculate_button = Button(keyGUI, text="Calculate", command=calculate)
            calculate_button.grid(row=6)#function calculate is attributed with the button
        
            
        


#----------------------------Two Dimensional Collision-----------------------------------------------------------------------------------------
        def twodimension():
            GUI2 = Toplevel()
            GUI2.title("2D Collision")
            GUI2.geometry()

            label24 = Label(GUI2, text="Welcome to 2D collisions please select a scenario")
            label24.grid(row=0, sticky=W)

            label= Label(GUI2, text="Scenario 1")
            label.grid(row=1, column=0)

            photo = PhotoImage(file="Scenario1.png")
            label25 = Label(GUI2, image=photo)
            label25.image = photo
            label25.grid(row=1, column=1)

            label= Label(GUI2, text="Scenario 2")
            label.grid(row=2, column=0)

            photo1 = PhotoImage(file="Scenario2.png")
            label25 = Label(GUI2, image=photo1)
            label25.image = photo1
            label25.grid(row=2, column=1)





#-------------------------Scenario 1----------------------------------------------------------------------------------------------------------
            def sone():
                GUI3 = Toplevel()
                GUI3.title("2D Collision Scenario 1")
                GUI3.geometry()

                photo2 = PhotoImage(file="Scenario1.png")
                label25 = Label(GUI3, image=photo)
                label25.image = photo2
                label25.grid(row=3, column=2)

                label= Label(GUI3, text="Initial Velocity v01")
                label.grid(row=0, sticky=W)

                v7= DoubleVar()
                e19 = Entry(GUI3, textvariable= v7)
                e19.grid(row=0, column=1, sticky=W)

                label= Label(GUI3, text="Angle θ1")
                label.grid(row=1, sticky=W)

                v8= DoubleVar()
                e20 = Entry(GUI3, textvariable= v8)
                e20.grid(row=1, column=1, sticky=W)

                label= Label(GUI3, text="Angle θ2")
                label.grid(row=2, sticky=W)

                v9= DoubleVar()
                e21 = Entry(GUI3, textvariable= v9)
                e21.grid(row=2, column=1, sticky=W)

                def calone():
                    #Validation tests

                    b=2


                    try:
                        velocityi1=v7.get() #if velocity is greater than 0 and less than 3x10^8 then validation is passed
                        if (velocityi1 > 0) and (velocityi1 <= 300000000):
                            b=2
                        else:
                            b=1
                            invalid() #if failed then the error message is starte
                    except ValueError:
                        b=1
                        invalid()

                    if b==2:

                
                        try:
                            theta1=v8.get() #If angle is greater than 0 and less than 90 validation passed 
                            if (theta1 > 0) and (theta1 < 90):
                                b=2
                            else:
                                b=1
                                invalid() #if failed then the error message is opened
                        except ValueError:
                            b=1
                            invalid()
                    else:
                        b=1


                    if b==2:
                
                        try:
                            theta2=v9.get() #If angle is greater than 0 and less than 90 validation passed
                            if (theta2 > 0) and (theta2 < 90):
                                b=2
                            else:
                                b=1
                                invalid() #if failed then the error message is opened
                        except ValueError:
                            b=1
                            invalid()
                    else:
                        b=1

                    if b==2:
                        #If validation tests are passed the program will carry out the calculation
                        GUI5= Tk()
                        GUI5.title("2D Collision Scenario 1")
                        GUI5.geometry()

                        velocityf1=(velocityi1/(math.cos(math.radians(theta1))+(math.sin(math.radians(theta1))/math.tan(math.radians(theta2)))))
                        #velocity final 1 = velocity initial / cos(theta1) + sin(theta1)/tan(theta2)

                        velocityf2=((velocityf1*math.sin(math.radians(theta1)))/math.sin(math.radians(theta2)))
                        #velocity final 2 = Velocity final 1 * sin(theta1)/sin(theta2)

                        label10 = Label(GUI5, text="Final Velocity 1 (vf1)")
                        label10.grid(row=0, sticky=W)

                        e26 = Entry(GUI5)
                        e26.grid(row=0, column=1)
                        e26.insert(0,velocityf1)

                        label10 = Label(GUI5, text="Final Velocity 1 (vf2)")
                        label10.grid(row=1, sticky=W)

                        e27 = Entry(GUI5)
                        e27.grid(row=1, column=1)
                        e27.insert(0,velocityf2)

                        def animtwo():
                            anim1 = Tk()
                            anim1.title("2D collision scenario 1 animation")
                            canvas = Canvas(anim1, width = 900, height = 800)
                            canvas.pack()
                            x0 = 10		
                            y0 = 400		
                            x1 = 60	
                            y1 = 450

                            x2 = 250		
                            y2 = 400	
                            x3 = 300		
                            y3 = 450

                            dx = 4
                            dy = 0

                            d2x = 0
                            d2y = 0
                    
                            ball1 = canvas.create_oval(x0, y0, x1, y1, fill="blue", tag='blueBall')
                            ball2 = canvas.create_oval(x2, y2, x3, y3, fill="red", tag='redBall')

                            while True:

                                canvas.move('blueBall', dx, dy)
                                canvas.move('redBall', d2x, d2y)

                                pos = canvas.coords(ball1)
                                pos1 = canvas.coords(ball2)

                                canvas.after(20)
                                canvas.update()

                                if pos[2] >= 251:
                                    dx = 1
                                    dy = 2

                                    d2x = 1 
                                    d2y = -2



                            anim1.mainloop


                        animation_button = Button(GUI5, text="General Animation", command=animtwo)
                        animation_button.grid(row=18)

                calculate_button = Button(GUI3, text="Calculate", command=calone)
                calculate_button.grid(row=3)







#--------------------------Scenario 2---------------------------------------------------------------------------------------------------------
            def stwo():
                GUI4 = Toplevel()
                GUI4.title("2D Collision Scenario 2")
                GUI4.geometry()

                photo3 = PhotoImage(file="Scenario2.png")
                label25 = Label(GUI4, image=photo3)
                label25.image = photo3
                label25.grid(row=4, column=2)

                label= Label(GUI4, text="Mass Of Object 1 (m1)")
                label.grid(row=0, sticky=W)

                v10= DoubleVar()
                e22 = Entry(GUI4, textvariable= v10)
                e22.grid(row=0, column=1, sticky=W)

                label= Label(GUI4, text="Initial Velocity Of Object 1 (v01)")
                label.grid(row=1, sticky=W)

                v11= DoubleVar()
                e23 = Entry(GUI4, textvariable= v11)
                e23.grid(row=1, column=1, sticky=W)

                label= Label(GUI4, text="Mass Of Object 2 (m2)")
                label.grid(row=2, sticky=W)

                v12= DoubleVar()
                e24 = Entry(GUI4, textvariable= v12)
                e24.grid(row=2, column=1, sticky=W)

                label= Label(GUI4, text="Initial Velocity Of Object 2 (v02)")
                label.grid(row=3, sticky=W)

                v13= DoubleVar()
                e25 = Entry(GUI4, textvariable= v13)
                e25.grid(row=3, column=1, sticky=W)

                def caltwo():
                    #Validation tests

                    c=2


                    try:
                        mass01=v10.get() #If mass is greater than 0 and less than 1x10^14 validation passed
                        if (mass01 > 0) and (mass01 <= 100000000000000000):
                            c=2 #If c=2 then validation passed and program continues
                        else:
                            c=1
                            invalid() #If c=1 then error message is shown
                    except ValueError:
                        c=1 #if value error the error message is displayed
                        invalid()

                    if c==2:
                        

                
                        try:
                            velocity01=v11.get() #If velocity is greater than 0 and less than 3x10^8 validation passed 
                            if (velocity01 >0) and (velocity01 <= 300000000):
                                c=2 #If c=2 then validation passed and program continues
                            else:
                                c=1
                                invalid() #If c=1 then error message is shown
                        except ValueError:
                            c=1
                            invalid() #if value error the error message is displayed
                    else:
                        c=1

                    if c==2:
                        

                    
                
                        try:
                            mass02=v12.get()
                            if (mass02 > 0) and (mass02 <= 100000000000000000): #If mass is greater than 0 and less than 1x10^14 validation passed
                                c=2
                            else:
                                c=1
                                invalid()
                        except ValueError:
                            c=1
                            invalid()
                    else:
                        c=1

                    if c==2:

                
                        try:
                            velocity02=v13.get() #If velocity is greater than 0 and less than 3x10^8 validation passed
                            if (velocity02 >0) and (velocity02 <=300000000):
                                c=2 #If c=2 then validation passed and program continues
                            else:
                                c=1 #If c=1 then error message is shown
                                invalid()
                        except ValueError:
                            c=1 #if value error the error message is displayed
                            invalid()
                    else:
                        c=1

                    if c==2:
                        #If validation tests are passed the program will carry out the calculation

                        GUI6= Tk()
                        GUI6.title("2D Collision Scenario 2")
                        GUI6.geometry()
                        

                        vFinalx=((mass01*velocity01)/(mass01+mass02)) #vfinalx = mass1*velocity1 / mass1 + mass2 
                        vFinaly=((mass02*velocity02)/(mass01+mass02)) #vfinalx = mass1*velocity1 / mass1 + mass2 
                        vFinalsq=((vFinalx*vFinalx)+(vFinaly*vFinaly)) #vfinal = vfinalx^2 + vfinaly^2
                        vFinal= math.sqrt(vFinalsq) #square root of vfinalsq
                        thetarad= math.atan((vFinaly/vFinalx)) #arc tan 
                        theta= math.degrees(thetarad) #conversion of angle

                        label10 = Label(GUI6, text="Final Velocity Of Object (vf)")
                        label10.grid(row=0, sticky=W)

                        e28 = Entry(GUI6)
                        e28.grid(row=0, column=1)
                        e28.insert(0,vFinal)

                        label10 = Label(GUI6, text="Angle θ1")
                        label10.grid(row=1, sticky=W)

                        e29 = Entry(GUI6)
                        e29.grid(row=1, column=1)
                        e29.insert(0,theta)

                        def animtwo():
                            anim2 = Tk()
                            anim2.title("2D collision scenario 2 animation")
                            canvas = Canvas(anim2, width = 900, height = 800)
                            canvas.pack()
                            x0 = 10		
                            y0 = 400		
                            x1 = 60	
                            y1 = 450

                            x2 = 250		
                            y2 = 750	
                            x3 = 300		
                            y3 = 800

                            dx = 2
                            dy = 0

                            d2x = 0
                            d2y = -3
                    
                            ball1 = canvas.create_oval(x0, y0, x1, y1, fill="blue", tag='blueBall')
                            ball2 = canvas.create_oval(x2, y2, x3, y3, fill="red", tag='redBall')

                            while True:

                                canvas.move('blueBall', dx, dy)
                                canvas.move('redBall', d2x, d2y)

                                pos = canvas.coords(ball1)
                                pos1 = canvas.coords(ball2)

                                canvas.after(20)
                                canvas.update()

                                if pos[2] >= 310:
                                    dx = 2 
                                    dy = -3

                                if pos1[1] <= 400:
                                    d2x = 2
                                    d2y = -3


                            anim2.mainloop


                        animation_button = Button(GUI6, text="General Animation", command=animtwo)
                        animation_button.grid(row=18)
                
    

                calculatetwo_button = Button(GUI4, text="Calculate", command=caltwo)
                calculatetwo_button.grid(row=4, column=0)

                



            scenarioone_button = Button(GUI2, text="Scenario 1", command=sone)
            scenarioone_button.grid(row=3, column=0)

            scenariotwo_button = Button(GUI2, text="Scenario 2", command=stwo)
            scenariotwo_button.grid(row=3, column=1)
            
            

            

            

            

        onedimension_button = Button(master, text="1D Collision", command=onedimension)
        onedimension_button.grid(row=1)

        twodimension_button = Button(master, text="2D Collision", command=twodimension)
        twodimension_button.grid(row=2)
        master.mainloop()



    __init__()
collision()
