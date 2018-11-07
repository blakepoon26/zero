# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 20:44:37 2018

@author: Dell T7400
"""

import time
import serial
from serial.tools import list_ports

class Pump:
    def __init__(self, SERIAL_ID, USB_VENDOR_ID, BAUDRATE, timeout=1, 
                 syringe_volume=2500., steps=48000., config='3port'):
        """Create a pump object
        
        Args:
            syringe_volume (float): syringe volume in uL
            steps (int): max number of steps for syringe
        
        """
        
        
        # Communication parameters from Hardware ID
        self.USB_VENDOR_ID = USB_VENDOR_ID
        self.SERIAL_ID = SERIAL_ID
        self.BAUDRATE = BAUDRATE
        self.timeout = timeout

        # specs
        self.syringe_volume = syringe_volume
        self.steps = steps
        self.config = config
        
        # Initialize serial connection to create 'pump' connection
        self._initialize()
        
        # Initialize the pump (Not sure if needed so commented out for now)
        #self.initialize_pump()
        
        # Additional parameters needed throughout
        self.valve_map = {'chip': 'O',
                          'c': 'O',
                          'waste': 'I',
                          'w': 'I'}
    
    # Private functions
    #-----------------
    def _initialize(self):
        # Scan serial ports and locate tecan cavro centris pump
        for comport in list_ports.comports():
            if comport.vid != self.USB_VENDOR_ID:
                continue            
            
            # Cross reference serial ID with this device
            print(comport.serial_number, self.SERIAL_ID)
            if comport.serial_number == self.SERIAL_ID:
                # Open serial communication with the tecan pump
                print('found the pump')
                self.pump = serial.Serial(comport.device, baudrate=self.BAUDRATE, parity=serial.PARITY_NONE,
                                          stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=self.timeout)
                return
            else:
                print("There's a problem. Serial number not found")
    
    def _pump_query(self):
        
        while True:
            time.sleep(0.1)
            self.pump.write('/1\r'.encode('ascii'))
            time.sleep(0.1)
            response = list(self.pump.readline())
            #print(response)
            self.pump.reset_input_buffer()
            self.pump.reset_output_buffer()
            if response[2] == 64:
                print("I'm still running. Please be patient")
            elif response[2] == 98:
                print("You provided me with an invalid command")
                self.status = 'Error'
                break
            elif response[2] == 96:
                print("All done.")
                self.status = 'Pass'
                break
    
    
    def _convert_volume(self, volume):
        """ Convert volume(uL) to number of steps for syringe. 
            Returns an int for the number of steps"""
        return int(self.steps*(volume/self.syringe_volume))

    def _convert_flowrate(self, flowrate):
        """ Convert flowrate (uL/sec) to steps/second.
            Return int for steps per second"""
        return int(self.steps*(flowrate/self.syringe_volume))

    # Public functions
    #-----------------
    def initialize_pump(self, steprate=2000):
        """initialize the pump"""        
        
        message = '/1V{}W4R\r'.format(steprate)
        
        #self.pump.write('/~Z2R\r'.encode('ascii'))
        #message = '/Z4R\r'.format(steprate)
        self.pump.write(message.encode('ascii')) # write('/1W5R\r'.encode('ascii'))
        
        
        
        if self.config == '6port':
            self.pump.write('/1~V7R\r'.encode('ascii'))
        elif self.config == '3port':
            self.pump.write('/1~V1R\r'.encode('ascii'))
            
        #self.pump.write('/1~Y1R\r'.encode('ascii'))

        
        time.sleep(0.5)

        # check pump status
       # self._pump_query()
       
    def aspirate(self, valve, volume, flowrate=None):
        """Withdraws liquids out of desired valve
        
        Note:
            Limits for 12.5mL syringe [4.132 - 826491.817 uL/min]
        
        Args:
            valve (str): Valve withdraw fluid from ('chip'/'c' or 'waste'/'w')
            volume (float): Volume to withdraw (uL)
            flowrate (float): flowrate of fluid (uL/minute)
        """
     
        target_steps = self._convert_volume(volume)
        if flowrate:
            target_flowrate = flowrate / 60. # convert to uL/sec
            target_flowrate = round(target_flowrate,3)
            target_steprate = self._convert_flowrate(target_flowrate)
        else:
            target_steprate = 1000
    
        # get the right v0alve
        valve_pos = self.valve_map[valve]
                
        message = '/1{}V{}P{}R\r'.format(valve_pos, target_steprate, target_steps)
        
        #message = '/1o{}V{}P{}R\r'.format(valve_pos, target_steprate, target_steps)

        # sets syringe size to 12.5mL <Not for us>
        #self.pump.write('/1U98R\r'.encode('ascii'))
        #time.sleep(0.1)

        # sends encoded message to run pump at specified valve position, flowrate, and volume
        self.pump.write(message.encode('ascii'))
        time.sleep(0.1)
        self._pump_query()
    
    def dispense(self, valve, volume, flowrate=None):
        """Dispenses the syringe through the desiged valve and flowrate
        
        Note:
            Limits for 12.5mL syringe [4.132 - 826491.817 uL/min]
        
        Args:
            valve (str): Valve dispense fluid to ('chip'/'c' or 'waste'/'w')
            volume (float): volume to dispence
            flowrate (float): flowrate of fluid (uL/minute)
        """

        # Limits for 12.5mL syringe [4.132 - 826491.817 uL/min]
     
        
        target_steps = self._convert_volume(volume)
        
        if flowrate:
             target_flowrate = flowrate / 60. # convert to uL/sec
             target_flowrate = round(target_flowrate,3)
             target_steprate = self._convert_flowrate(target_flowrate)
        else:
            target_steprate = 1000

        # get the right valve
        valve_pos = self.valve_map[valve]

        message = '/1{}V{}D{}R\r'.format(valve_pos,target_steprate, target_steps)
        #message = '/1o{}V{}D{}R\r'.format(valve_pos, target_steprate, target_steps )

        # sets syringe size to 12.5mL
        #self.pump.write('/1U98R\r'.encode('ascii'))
        #time.sleep(0.1)

        # sends encoded message to run pump at specified valve position, flowrate, and volume
        self.pump.write(message.encode('ascii'))
        time.sleep(0.1)

        
        
        self._pump_query()
    
    def empty(self, valve, flowrate=None):
        """Empties the syringe through the desiged valve and flowrate
        
        Note:
            Limits for 12.5mL syringe [4.132 - 826491.817 uL/min]
        
        Args:
            valve (str): Valve dispense fluid to ('chip'/'c' or 'waste'/'w')
            volume (float): volume to dispence
            flowrate (float): flowrate of fluid (uL/minute)
        """
        if flowrate:
             target_flowrate = flowrate / 60. # convert to uL/sec
             target_flowrate = round(target_flowrate,3)
             target_steprate = self._convert_flowrate(target_flowrate)
        else:
            target_steprate = 1000
        valve_pos = self.valve_map[valve]
        message = '/1{}V{}A0R\r'.format(valve_pos, target_steprate)
        
        # sends encoded message to run pump at specified valve position, flowrate, and volume
        self.pump.write(message.encode('ascii'))
        time.sleep(0.1)

        
        
        self._pump_query()
    
    def disconnect(self):
        self.pump.close()
    
    

# helper function
def main():
    global pump
    """This function will fill valve 1 with a certain amount 
    of fluid and then empty it"""
    
    # <FILL IN THESE NUMBERS>
    #SERIAL_ID = '6'
    #SERIAL_ID = '5'
    #USB_VENDOR_ID = 1367
    
    SERIAL_ID = '7'
    USB_VENDOR_ID = 1659
    BAUDRATE = 9600
    
    pump = Pump(SERIAL_ID, USB_VENDOR_ID, BAUDRATE)
    
    # <ADJUST THESE NUMBERS ACCORDINGLY>
    valve_pos = 1
    volume = 50. # Fill in volume
    flowrate = 100. # Fill in flowrate
    
    #my_pump.withdraw(valve_pos, volume, flowrate) 
    #my_pump.empty(valve_pos, flowrate)


if __name__ == '__main__':
    main()