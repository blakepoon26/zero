# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:09:10 2018

@author: Dell T7400
"""

from mcculw import ul
#from mcculw.ul import ULError

import sys
sys.path.append('C:/Users/P3 Lab South/Desktop/mcculw-master')
#sys.path.append('path/to/enums')

from examples.ui.uiexample import UIExample
from examples.props.digital import DigitalProps
from mcculw.enums import DigitalIODirection


class MagMover(UIExample):
    def __init__(self, board_num):
        #super(MagMover, self).__init__(master)
        self.board_num = board_num
        
        self.digital_props = DigitalProps(self.board_num)
        
        # Find the first port that supports output, defaulting to None
        # if one is not found.
        self.port = next(
            (port for port in self.digital_props.port_info
             if port.supports_output), None)
        

        
        # It's one of these...
        self.port_type = self.port.type
        #self.port_type = 'FIRSTPORTA'
        #self.port_type = all_ports[2].type
        # If the port is configurable, configure it for output
        
        ### Possibly not needed ###
        ul.d_config_port(self.board_num, self.port.type, DigitalIODirection.OUT)
#        if self.port != None and self.port.is_port_configurable:
#            try:
#                ul.d_config_port(
#                    self.board_num, self.port.type, DigitalIODirection.OUT)
#            except ULError as e:
#                self.show_ul_error(e)
        
        self.bit_dict = {'top': 0,
                         'bottom': 1}
    
    def turn_on(self, mag_pos='top'):
        """Turn the controller on"""
        #try:
        bit_value = 1 # According to email, 0 = on
        # Output the value to the board
        #try:
        
        bit_num = self.bit_dict[mag_pos]
        ul.d_bit_out(self.board_num, self.port_type, bit_num, bit_value)
        #except ULError as e:
        #    self.show_ul_error(e)
    
    def turn_off(self, mag_pos='top'):
        """Turn the controller off"""
        #try:
        bit_value = 0 # According to email, 1 = off
        # Output the value to the board
        #try:
        bit_num = self.bit_dict[mag_pos]
        ul.d_bit_out(self.board_num, self.port_type, bit_num, bit_value)
        #except ULError as e:
        #    self.show_ul_error(e)
    


def main():
    global con
    #board_num = '1D57BC3' # <Need to fill in>
    board_num = 0
    con = MagMover(board_num)
    
if __name__ == '__main__':
    main()