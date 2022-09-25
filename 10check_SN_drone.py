from rcsa_dev_kit_edu_python_lib.fly_tello import FlyTello

my_tellos = list()

# Check Serial Tello EDU
my_tellos.append('0TQDG7BEDB744Y') # Drone1

try:
    with FlyTello(my_tellos) as fly:
        pass
except :
    pass
    