from rcsa_dev_kit_edu_python_lib.fly_tello import FlyTello
my_tellos = list()

# Check Serial Tello EDU
my_tellos.append('') # Drone1

try :
    with FlyTello(my_tellos) as fly:
        while (True):
            try :
                print ("ap = setAP for NAME")
                minput = input("Enter your command : ")
                if minput == 'ap':
                    print ("Set AP for NAME")
                    fly.set_ap_wifi(ssid='RCSA_DL',password= 'RCSA1804')
                else :
                    pass
            except KeyboardInterrupt as e:
                break
except KeyboardInterrupt as e:
    fly.Stop()