# ----------------------------------------------------------------
# This is a library to use the SKR Pico as a development board,
# it does have dependecies on code I cloned from kjk25 which is an
# adaptation of Chr157i4n's
# ----------------------------------------------------------------

from machine import Pin, PWM, I2C, UART
from TMC_2209_StepperDriver import *
from time import sleep


tmc = TMC_2209(11, 10, 12)

tmc.setMicrosteppingResolution(1)
micro_stepping			= 1
steps_per_revolution	= 200 * micro_stepping


FAN1 = Pin(17, Pin.OUT)
FAN2 = Pin(18, Pin.OUT)
FAN3 = Pin(20, Pin.OUT)

X_EN = Pin(12, Pin.OUT)	 # Enable Pin for motor connected to X
X_ST = Pin(11, Pin,OUT)	 # Step Pin for motor connected to X
X_DR = Pin(10, Pin.OUT)	 # Direction Pin for motor connected to X

Y_EN = Pin(07, Pin.OUT)	 # Enable Pin for motor connected to Y
Y_ST = Pin(06, Pin.OUT)	 # Step Pin for motor connected to Y
Y_DR = Pin(05, Pin.OUT)	 # Direction Pin for motor connected to Y

Z_EN = Pin(02, Pin.OUT)	 # Enable Pin for up to 2 motor connected to Z
Z_ST = Pin(19, Pin.OUT)	 # Step Pin for motors connected to Z
Z_DR = Pin(28, Pin.OUT)	 # Direction Pin for motors connected to Z

E_EN = Pin(15, Pin.OUT)	 # Enable Pin for motor connected to E0
E_ST = Pin(14, Pin.OUT)	 # Step Pin for motor connected to E0
E_DR = Pin(13, Pin.OUT)	 # Direction Pin for motor connected to E0

class General:
    
    def set_current(mA):
        tmc.setCurrent(mA)
        
        
    def set_microstepping(fraction):
        global micro_stepping, steps_per_revolution
        tmc.setMicrosteppingResolution(fraction)
        micro_stepping = fraction
        steps_per_revolution	= 200 * micro_stepping
        
        
class Fans:
    
    def enable(port):        
        if port == 1:
            FAN1.high()
        
        elif port == 2:
            FAN2.high()
            
        elif port == 3:
            FAN3.high()
            
        elif port == all:
            FAN1.high()
            FAN2.high()
            FAN3.high()
        
        else:
            pass
        
    def disable(port):        
        if port == 1:
            FAN1.low()
        
        elif port == 2:
            FAN2.low()
            
        elif port == 3:
            FAN3.low()
            
        elif port == all:
            FAN1.low()
            FAN2.low()
            FAN3.low()
        
        else:
            pass
        
        
class X :
    
    def enable():
        X_EN.low()

    def disable():
        X_EN.high()
    
    def step():
        X_ST = Pin(11, Pin.OUT)
        X_ST.high()
        sleep(0.01)
        X_ST.low()
        
    def steps(amount):
        X.enable()
        for i in range(amount):
            X.step()
        
    def run_pwm(freq):
        X.enable()
        X_ST = PWM(Pin(11))
        X_ST.freq(freq)
        X_ST.duty_u16(2**15)
        
    def run_sleep(sleep_time):
        X_ST = Pin(11, Pin.OUT)
        X_ST.high()
        sleep(sleep_time)
        X_ST.low()
        
    def run_rpm(RPM):
        X_ST = PWM(Pin(11))
        X_ST.freq(int((RPM*steps_per_revolution)/60))
        X_ST.duty_u16(2**15)
        
    def stop():
        X_ST = PWM(Pin(11))
        X_ST.freq(100)
        X_ST.duty_u16(0)
    
    def e_stop():
        X.disable()
        X_ST = PWM(Pin(11))
        X_ST.freq(100)
        X_ST.duty_u16(0)
        
    def toggle_direction():
        X_DR.toggle()
        
   
    def ramp(ramp_time, final_rpm):
        X.enable()
        start_rpm = 10
        for i in range(256):
            X.rpm(start_rpm)
            sleep(ramp_time/256)
            start_rpm += (final_rpm/256)
        print("Ramp Finished")
        
    
