from rcsa_dev_kit_edu_python_lib.fly_tello import FlyTello
my_tellos = list()

# Check Serial Tello EDU
my_tellos.append('') # Drone1

mx = 150 #cm
my = 150 #cm
mz = 80  #cm
mspeed = 70 #10-100 cm/s

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
                    pass
                 
                else :
                    pass        
            except KeyboardInterrupt as e:
                break
except KeyboardInterrupt as e:
    fly.Stop()