from rcsa_dev_kit_edu_python_lib.fly_tello import FlyTello
my_tellos = list()

# Check Serial Tel
# lo EDU
my_tellos.append('0TQDG7BEDB744Y')  # Drone1

mspeed = 50 
mx = 90     
my = 90
mz = 120
mzland = 50

try :
    with FlyTello(my_tellos) as fly:
        while (True):
            try :
                print ("t=takeoff,l=land,b=battery?,s=speed?,h=height,q=exit")
                minput = input("Enter your command : ")
                if minput == 't' :  
                    print('Takeoff')
                    fly.takeoff()
                if minput == 'l' :
                    print('Land')
                    fly.land()
                if minput == 'b' :  
                    print('Battery?')
                    fly.get_battery()
                if minput == 'speed' :  
                    print('Speed?')
                    fly.get_speed()
                if minput == 'h' :
                    print('Height')
                    fly.get_height()
                if minput == "bounce":
                    print('Bounce')
                    fly.bounce(dist=100,times=3) # dist=distance between up and down , times = Number of round bounce
                if minput == 'q' :
                    print('Exit Program')
                    break
                if minput == 'm' :
                    fly.pad_detection_on()

#-------------------------------------------------------------- mission -------------------------------------------------------------------#

                if minput == '1':
                    print ("Mission1")
                    fly.takeoff()
                    with fly.sync_these():
                        fly.jump_between_pads(x=mx,y=0,z=mz,speed=mspeed,yaw=0,pad1='m1',pad2='m2', tello=1)
                    with fly.sync_these():
                        fly.reorient(height=mz, pad='m2', tello=1)

                    """with fly.sync_these():
                        fly.jump_between_pads(x=-mx,y=0,z=mz,speed=mspeed,yaw=0,pad1='m2',pad2='m3', tello=1)
                    with fly.sync_these():
                        fly.reorient(height=mz, pad='m3', tello=1)

                    fly.land()"""
                else :
                    pass
            except KeyboardInterrupt as e:
                break
except KeyboardInterrupt as e:
    fly.Stop()

    #yaw in line 50 =0