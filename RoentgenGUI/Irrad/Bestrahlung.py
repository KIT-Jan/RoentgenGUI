import time
import numpy as np
import ConfigParser #python2?
import io
import sys
from XrayTubeCommands import *
from mcl2 import MCL2

def main():

    """get settings from config file"""
    
    config = ConfigParser.ConfigParser() #python2? #TODO
    config.readfp(io.open("irradiation.cfg", "r"))
    R = float(config.get("Geometry", "spot_radius")) #in mm
    sensor_size_x = int(config.get("Geometry", "sensor_size_x")) #in mm
    sensor_size_y= int(config.get("Geometry", "sensor_size_y")) #in mm
    #beamtime_at_distance = float(config.get("Calibration", "beamtime_at_distance"))
    dose_at_distance = float(config.get("Calibration", "dose_at_distance"))
    required_dose = float(config.get("Calibration", "required_dose"))
    number_of_scans = int(config.get("Calibration", "number_of_scans"))
    #v = float(config.get("Calibration", "motor_speed"))
    print("Config initialised")

    """initialise motor and xraytube"""
    
    try:
        motor = MCL2()
    except Exception:
        sys.exit("Motor could not be initialized!")

    try:
        xray = XrayTubeCommands(config.get("XrayTube","serialport"))
        shutter = int(config.get("XrayTube","shutter"))
        tubewait = int(config.get("XrayTube","tubewait"))
    except:
        sys.exit("Xray tube could not be initialized!")


    """calculate delta_y"""
    
    y = dose_at_distance*number_of_scans*np.pi*R**2/required_dose
    y = y/3.6 #convert in mm*mum/s
    delta_y = int(y/motor_speed_to_velocity(10)) #has to be int for motor.move
    delta_y_float = y/motor_speed_to_velocity(10)
    print("delta_y: " + str(delta_y))
    print("real best delta_y: " + str(delta_y_float))
    #, delta_y, difference = best_product_performant(y, 1, 20, 30, int(R/2*1000))

    """execution"""
    
    motor.setSpeed(10) #set correct speed
    motor.center() #should be centered already
    print("motor in center!")
    #input("Make sure that the alignment of the sensor is correct!\n"   + "Press Enter to continue and start irradiation procedure")
    motor.move(int(R*1000), int(R*1000)) #get the beamspot on the upper left of the sensor
    print("30 seconds till start!")
    time.sleep(30)

    #XrayTube
    xray.setVoltage(60)
    xray.setCurrent(30)
    time.sleep(tubewait)
    xray.openShutter(shutter)
    
    initial_position = motor.getPos()
    print("Initial position x: " + str(initial_position[0]) + " initial position y: " + str(initial_position[1]))
    xstep = int((sensor_size_x + R*2)*1000)
    y_total = int((sensor_size_y + R*2)*1000)
    number_of_y_steps = int(y_total/delta_y)
    print("number of y steps: " + str(number_of_y_steps))

    for i in range(number_of_scans):
        start_time = time.time()
        for iy in range(0,number_of_y_steps,1):
            if iy%2==0:
                motor.move(-xstep,0)
                print("Drive in negative x direction")
            elif iy%2!=0:
                motor.move(xstep,0)
                print("Drive in positive x direction")
            motor.move(0,-delta_y) #? 1mm in y fahren
            print("Drive delta_y upwards")
        end_time = time.time()
        motor.moveAbs(initial_position[0]/4,initial_position[1]/4) #care getPos() is in motor ticks
        print("Scan " + str(i) + " done!")
        print("Time per scan: " + str(end_time-start_time) + "s")
        print("Time per scan in hours: " + str((end_time-start_time)/3600))
    
    print("Irradiation procedure finished!")
    xray.Shutdown()
    motor.center()


def motor_speed_to_velocity(x):
    m = 0.0965
    b = 0.046
    return m*x+b

"""
def best_product_performant(y, amin, amax, bmin, bmax):
    #Find product of two numbers a, b in the given intervals that comes
    #closest to the value of y (performant version)

    #if amax - amin > bmax - bmin:
        #return best_product_performant(y, bmin, bmax, amin, amax)

    best_deviation = abs(amin * bmin - y)
    best_a, best_b = amin, bmin

    imin = max(amin, math.floor(y / bmax))
    imax = min(amax, math.ceil(y / bmin))

    for a in range(imin, imax+1):
        b = max(bmin, min(bmax, round(y / a)))
        deviation = abs(a*b - y)
        if deviation < best_deviation:
            best_deviation = deviation
            best_a, best_b = a, b

    return best_a, best_b, best_deviation
"""
if __name__ == '__main__':
    main()

