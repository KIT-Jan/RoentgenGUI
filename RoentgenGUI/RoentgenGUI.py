from PyQt5 import QtCore, QtWidgets
from Window import Ui_MainWindow
from mcl2 import MCL2
#from XrayTubeCommands import *
import sys
import time
import os
import json
import numpy as np

class Gose_Irradiation(Ui_MainWindow, MCL2):
    """Homogeneous x-ray irradiation"""

    def __init__(self, parent):
        """Initializes GUI"""

        super().__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(parent)
        config = read_config("irrad_config.cfg")
        self.shutter = int(config["XrayTube"]["shutter"])
        self.xray_port = config["XrayTube"]["serialport"]
        self.set_def_values(config)
        self.center()
        self.log_text.append("Motor in center")
        self.update_button.clicked.connect(self.update)
        self.Start.clicked.connect(self.execute)
    
        """
        try:
            xray = XrayTubeCommands(str(config["XrayTube"]["serialport"]))
            shutter = int(config["XrayTube"]["shutter"])
        except:
            sys.exit("Xray tube could not be initialized!")
		"""

    def set_def_values(self, config):
        self.NoS_line.setText(str(config["Irradiation"]["number_of_scans"]))
        self.radius.setText(str(config["Geometry"]["spot_radius"]))
        self.width.setText(str(config["Geometry"]["sensor_size_x"]))
        self.height.setText(str(config["Geometry"]["sensor_size_y"]))
        self.doserate_line.setText(str(config["Irradiation"]["dose_at_distance"]))
        self.rdose_line.setText(str(config["Irradiation"]["required_dose"]))


    def calculate_stepsize(self):
        y = self.rate*self.number_of_scans*np.pi*self.spot_radius**2/self.dose
        y = y/3.6 #convert in mm*mum/s
        delta_y = int(y/motor_speed_to_velocity(10)) #has to be int for self.move
        delta_y_float = y/motor_speed_to_velocity(10)
        print("delta_y: " + str(delta_y))
        print("real best delta_y: " + str(delta_y_float))
        return delta_y

    def update(self):
        self.number_of_scans = int(self.NoS_line.text())
        self.spot_radius = float(self.radius.text())
        self.sample_x = float(self.width.text())
        self.sample_y = float(self.height.text())
        self.rate = float(self.doserate_line.text())
        self.dose = float(self.rdose_line.text())
        A_total = (self.sample_x+self.spot_radius*2)*(self.sample_y+self.spot_radius*2)

        self.delta_y = self.calculate_stepsize()
        self.stepsize_line.setText(str(self.delta_y))
        total_time = self.calculate_time(A_total)
        print("total time in minutes: " + str(total_time))
        self.time_lcd.display(str(total_time))
        self.log_text.append("Properties updated")


    def execute(self):
        time.sleep(3)

        self.setSpeed(10) #set correct speed
        self.center() #should be centered already
        print("Motor in center!")
        #input("Make sure that the alignment of the sensor is correct!\n"   + "Press Enter to continue and start irradiation procedure")
        self.move(int(self.spot_radius*1000), int(self.spot_radius*1000)) #get the beamspot on the upper left of the sensor
        print("30 seconds till start!")
        time.sleep(30)

        #XrayTube
        xray.setVoltage(60)
        xray.setCurrent(30)
        time.sleep(3)
        xray.openShutter(self.shutter)

        initial_position = self.getPos()
        print("Initial position x: " + str(initial_position[0]) + " initial position y: " + str(initial_position[1]))
        xstep = int((self.sample_x + self.spot_radius*2)*1000)
        y_total = int((self.sample_y + self.spot_radius*2)*1000)
        number_of_y_steps = int(y_total/self.delta_y)
        print("number of y steps: " + str(number_of_y_steps))

        for i in range(number_of_scans):
            start_time = time.time()
            for iy in range(0,number_of_y_steps,1):
                if iy%2==0:
                    self.move(-xstep,0)
                    print("Drive in negative x direction")
                elif iy%2!=0:
                    self.move(xstep,0)
                    print("Drive in positive x direction")
                self.move(0,-delta_y) #? 1mm in y fahren
                print("Drive delta_y upwards")
            end_time = time.time()
            self.moveAbs(initial_position[0]/4,initial_position[1]/4) #care getPos() is in self ticks
            print("Scan " + str(i) + " done!")
            print("Time per scan: " + str(end_time-start_time) + "s")
            print("Time per scan in hours: " + str((end_time-start_time)/3600))

        print("Irradiation procedure finished!")
        xray.Shutdown()

        self.center()
        self.log_text.append("Execution finished")

    def calculate_time(self, A_tot):
        A_beam = np.pi * self.spot_radius **2
        # time in h
        time = A_tot/A_beam *self.dose/self.rate
        minutes = int(time*60)
        return minutes

def read_config(cfg):
    config = json.load(open(cfg))
    return config

def motor_speed_to_velocity(x):
    m = 0.0965
    b = 0.046
    return m*x+b

if __name__ == '__main__':

    APP = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setStyle("Fusion")
    PARENT = QtWidgets.QMainWindow()

    PROG = Gose_Irradiation(PARENT)

    PARENT.show()
    sys.exit(APP.exec_())
