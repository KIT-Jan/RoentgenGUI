import traceback, sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Window import Ui_MainWindow
from mcl2 import MCL2
#from XrayTubeCommands import *
import os
import json
import numpy as np


"""Multithreading Tests!!!"""

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        `tuple` (exctype, value, traceback.format_exc() )

    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


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
        self.Start.clicked.connect(self.execute_fn)

        """
        try:
            xray = XrayTubeCommands(str(config["XrayTube"]["serialport"]))
            shutter = int(config["XrayTube"]["shutter"])
        except:
            sys.exit("Xray tube could not be initialized!")
		"""

        """NEW START!!!"""
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def progress_fn(self, n):
        print("%d%% done" % n)

    def execute_this_fn(self, progress_callback):
        for n in range(0, 5):
            time.sleep(1)
            progress_callback.emit(n*100/4)

        return "Done."

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    """NEW END"""

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

    def execute_fn(self):

        # Pass the function to execute
        worker = Worker(self.execute) # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)

    def execute(self, progress_callback):
        print("Executing")
        time.sleep(10)
        print("Slept")

        """
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

        self.center()"""
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

    APP = QApplication(sys.argv)
    QApplication.setStyle("Fusion")
    PARENT = QMainWindow()

    PROG = Gose_Irradiation(PARENT)

    PARENT.show()
    sys.exit(APP.exec_())
