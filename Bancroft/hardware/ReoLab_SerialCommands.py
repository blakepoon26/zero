# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:12:37 2018

@author: Dell T7400
"""

import PumpSerialCommands as psc
import MagCommands as mc
import ReoLabImageCapture as ric
import time
import os

# Syringe Commands
#=================

def play(SERIAL_ID = '7', USB_VENDOR_ID = 1659, BAUDRATE = 9600):
    pump = psc.Pump(SERIAL_ID, USB_VENDOR_ID, BAUDRATE)
    return pump

def initialize_pump(SERIAL_ID = '7', USB_VENDOR_ID = 1659, BAUDRATE = 9600):
    """
    Home the syringe
    
    Args:
            SERIAL_ID (str): Serial ID for connection
            USB_VENDOR_ID (int): Vendor ID to connect to pump 
            BAUDRATE (int): Baudrate for syrine
    """
    
    
    pump = psc.Pump(SERIAL_ID, USB_VENDOR_ID, BAUDRATE)
    pump.initialize_pump()
    pump.disconnect()

def fill(vol=360, flowrate=200, valve_pos='chip', SERIAL_ID = '7', USB_VENDOR_ID = 1659, BAUDRATE = 9600):
    """
    fill the syringe
    
    Args:
            vol (float): volume (uL) to fill syringe to
            flowrate (float): flowrate (uL/min) for syring fill
            valve_pos (str, 'I'/'O'): set valve position for input ('I') 
                or output ('O'). Defaults to 'I'
            SERIAL_ID (str): Serial ID for connection
            USB_VENDOR_ID (int): Vendor ID to connect to pump 
            BAUDRATE (int): Baudrate for syrine
    """
    
    pump = psc.Pump(SERIAL_ID, USB_VENDOR_ID, BAUDRATE)
    pump.aspirate(valve_pos, vol, flowrate=flowrate)
    pump.disconnect()

def fast_fill(vol=360, flowrate=1000, valve_pos = 'chip', SERIAL_ID = '7', USB_VENDOR_ID = 1659, BAUDRATE = 9600):
    """
    fast fill the syringe
    
    Args:
            vol (float): volume (uL) to fill syringe to
            flowrate (float): flowrate (uL/min) for syring fill
            valve_pos (str, 'I'/'O'): set valve position for input ('I') 
                or output ('O'). Defaults to 'I'
            SERIAL_ID (str): Serial ID for connection
            USB_VENDOR_ID (int): Vendor ID to connect to pump 
            BAUDRATE (int): Baudrate for syrine
    """
    
    pump = psc.Pump(SERIAL_ID, USB_VENDOR_ID, BAUDRATE)
    pump.aspirate(valve_pos, vol, flowrate=flowrate)
    pump.disconnect()

def shift_to_trapping(vol=275, flowrate=200, valve_pos = 'chip', SERIAL_ID = '7', USB_VENDOR_ID = 1659, BAUDRATE = 9600):
    """
    Shift to trapping
    
    Args:
            vol (float): volume (uL) to fill syringe to
            flowrate (float): flowrate (uL/min) for syring fill
            valve_pos (str, 'I'/'O'): set valve position for input ('I') 
                or output ('O'). Defaults to 'I'
            SERIAL_ID (str): Serial ID for connection
            USB_VENDOR_ID (int): Vendor ID to connect to pump 
            BAUDRATE (int): Baudrate for syringe
    """
    
    pump = psc.Pump(SERIAL_ID, USB_VENDOR_ID, BAUDRATE)
    pump.aspirate(valve_pos, vol, flowrate=flowrate)
    pump.disconnect()
    
def shift_to_syringe(vol=2000, flowrate=1000, valve_pos = 'chip', SERIAL_ID = '7', USB_VENDOR_ID = 1659, BAUDRATE = 9600):
    """
    Shift to syringe
    
    Args:
            vol (float): volume (uL) to fill syringe to
            flowrate (float): flowrate (uL/min) for syring fill
            valve_pos (str, 'I'/'O'): set valve position for input ('I') 
                or output ('O'). Defaults to 'I'
            SERIAL_ID (str): Serial ID for connection
            USB_VENDOR_ID (int): Vendor ID to connect to pump 
            BAUDRATE (int): Baudrate for syringe
    """
    
    pump = psc.Pump(SERIAL_ID, USB_VENDOR_ID, BAUDRATE)
    pump.aspirate(valve_pos, vol, flowrate=flowrate)
    pump.disconnect()    

def shift_to_detection(vol=75, flowrate=200, valve_pos = 'chip', SERIAL_ID = '7', USB_VENDOR_ID = 1659, BAUDRATE = 9600):
    """
    Shift to detection
    
    Args:
            vol (float): volume (uL) to fill syringe to
            flowrate (float): flowrate (uL/min) for syring fill
            valve_pos (str, 'I'/'O'): set valve position for input ('I') 
                or output ('O'). Defaults to 'I'
            SERIAL_ID (str): Serial ID for connection
            USB_VENDOR_ID (int): Vendor ID to connect to pump 
            BAUDRATE (int): Baudrate for syringe
    """
    
    pump = psc.Pump(SERIAL_ID, USB_VENDOR_ID, BAUDRATE)
    pump.aspirate(valve_pos, vol, flowrate=flowrate)
    pump.disconnect()

def empty_syringe(valve_pos='waste', flowrate=1000, SERIAL_ID = '7', USB_VENDOR_ID = 1659, BAUDRATE = 9600):
    """
    Empty the syringe
    
    Args:
            valve_pos (str, 'I'/'O'): set valve position for input ('I') 
                or output ('O'). Defaults to 'O'
            SERIAL_ID (str): Serial ID for connection
            USB_VENDOR_ID (int): Vendor ID to connect to pump 
            BAUDRATE (int): Baudrate for syringe
    """
    
    pump = psc.Pump(SERIAL_ID, USB_VENDOR_ID, BAUDRATE)
    pump.empty(valve_pos, flowrate=flowrate)
    pump.disconnect()
    
    
    
# Magnet Commands
#================
def engage_top(board_num = 0):
    """
    Turn top magnet on
    
    Args:
            board_num (int): board number for magnet connection
    """
    
    con = mc.MagMover(board_num)
    con.turn_on(mag_pos='top')
    print('Turned on top magnet')

def release_top(board_num = 0):
    """
    Turn top magnet off
    
    Args:
            board_num (int): board number for magnet connection
    """
    
    con = mc.MagMover(board_num)
    con.turn_off(mag_pos='top')
    print('Turned off top magnet')

def engage_bottom(board_num = 0):
    """
    Turn bottom magnet on
    
    Args:
            board_num (int): board number for magnet connection
    """
    
    con = mc.MagMover(board_num)
    con.turn_on(mag_pos='bottom')
    print('Turned on bottom magnet')

def release_bottom(board_num = 0):
    """
    Turn bottom magnet off
    
    Args:
            board_num (int): board number for magnet connection
    """
    
    con = mc.MagMover(board_num)
    con.turn_off(mag_pos='bottom')
    print('Turned off bottom magnet')
    
def engage_both(board_num = 0):
    """
    Turn both top and bottom magnet on
    
    Args:
            board_num (int): board number for magnet connection
    """
    
    con = mc.MagMover(board_num)
    con.turn_on(mag_pos='top')
    con.turn_on(mag_pos='bottom')
    print('Turned on both top and bottom magnet')

def release_both(board_num = 0):
    """
    Turn both top and bottom magnet off
    
    Args:
            board_num (int): board number for magnet connection
    """
    
    con = mc.MagMover(board_num)
    con.turn_off(mag_pos='top')
    con.turn_off(mag_pos='bottom')
    print('Turned off both top and bottom magnet')

def homogenize(n, magnet='top', period=0.5, board_num = 0):
    """
    Cycle top/bottom/both magnets for n number of cycle
    
    Args:
            n (int): number of cycles
            magnet (str): The magnet to cycle. Options: top, bottom, both
            period (float): number of seconds between on/off cycle
            board_num (int): board number for magnet connection
    """
    
    con = mc.MagMover(board_num)
    tic = time.time()
    for i in range(n):
        if magnet == 'top':
             con.turn_on(mag_pos='top')
             time.sleep(period)
             con.turn_off(mag_pos='top')
             time.sleep(period)
        elif magnet == 'bottom':
            con.turn_on(mag_pos='bottom')
            time.sleep(period)
            con.turn_off(mag_pos='bottom')
            time.sleep(period)
        elif magnet == 'both':
            con.turn_on(mag_pos='top')
            con.turn_on(mag_pos='bottom')
            time.sleep(period)
            con.turn_off(mag_pos='top')
            con.turn_off(mag_pos='bottom')
            time.sleep(period)
    toc = time.time()
    
    print('Finished %s cycles in %0.3f seconds' % (n, toc-tic))

def incubate(t, magnet='top', period=0.5, board_num = 0):
    """
    Cycle top/bottom/both magnets for t seconds
    
    Args:
            t (float): length of time (seconds) to cycle magnets
            magnet (str): The magnet to cycle. Options: top, bottom, both
            period (float): number of seconds between on/off cycle
            board_num (int): board number for magnet connection
    """
    con = mc.MagMover(board_num)
    tic = time.time()
    n = 0
    while time.time() - tic < t:
        if magnet == 'top':
             con.turn_on(mag_pos='top')
             time.sleep(period)
             con.turn_off(mag_pos='top')
             time.sleep(period)
        elif magnet == 'bottom':
            con.turn_on(mag_pos='bottom')
            time.sleep(period)
            con.turn_off(mag_pos='bottom')
            time.sleep(period)
        elif magnet == 'both':
            con.turn_on(mag_pos='top')
            con.turn_on(mag_pos='bottom')
            time.sleep(period)
            con.turn_off(mag_pos='top')
            con.turn_off(mag_pos='bottom')
            time.sleep(period)
        n += 1
    toc = time.time()
    
    print('Finished %s cycles in %0.3f seconds' % (n, toc-tic))


# Image Commands
#================
def image_capture(fname, fdir=os.getcwd()):
    ric.Capture(os.path.join(fdir, fname))
    
    
    
    
    
    