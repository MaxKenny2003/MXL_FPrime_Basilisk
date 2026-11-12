from Basilisk.utilities import SimulationBaseClass
from Basilisk.utilities import macros
from Basilisk.moduleTemplates import cModuleTemplate
from Basilisk.moduleTemplates import cppModuleTemplate
from Basilisk.architecture import sysModel
from Basilisk.architecture import bskLogging
from Basilisk.architecture import messaging

import numpy as np
import socket   # used to do UDP

UDP_IP = "127.0.0.1"    # Talk to myself. String for weird reasons
UDP_PORT = 9021     # Fantastic 4

class TestPythonModule(sysModel.SysModel):
    has_sent = False
    def __init__(self, *args):
        super().__init__(*args)

    def Reset(self, CurrentSimNanos):
        pass

    def UpdateState(self, CurrentSimNanos):
        #print("Testing", CurrentSimNanos * 1e-9)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create an IPv4 socket that uses UDP (Dgram)
        
        msg = f"Hello from Basilisk. Current sim time is {CurrentSimNanos * 1e-9}"
        sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
        print(f"Sent: {msg}")