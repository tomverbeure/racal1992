#! /usr/bin/env python3

import pyvisa
import Gpib
from pymeasure.instruments.racal import Racal1992

if False:
    rm = pyvisa.ResourceManager()

    # Prints all GPIB traffic...
    pyvisa.log_to_screen()
    #print(rm.list_resources())

    inst = rm.open_resource("GPIB::14")
    inst.chunk_size=21
    inst.max_count_read=21
    inst.read_termination='\n'

    # Reset to default settings
    #print(inst.write("IP"))

    # Switch to self-test mode: internal 10MHz clock is measured.
    #print(inst.write("CK"))

    print(inst.write("RGS"))
    print(inst.read_bytes(21))
    print(inst.write("RLA"))
    print(inst.read_bytes(21))
    print(inst.write("RLB"))
    print(inst.read_bytes(21))
    print(inst.write("RMS"))
    print(inst.read_bytes(21))
    print(inst.write("RMX"))
    print(inst.read_bytes(21))
    print(inst.write("RMZ"))
    print(inst.read_bytes(21))
    print(inst.write("RRS"))
    print(inst.read_bytes(21))
    print(inst.write("RSF"))
    print(inst.read_bytes(21))
    print(inst.write("RUT"))
    print(inst.read_bytes(21))

    print(inst.write("CK"))
    inst.timeout=10000
    print(inst.timeout)
    #print(inst.write("PA ADC AHI APS AAD BCS SLA1.5 T0 Q7"))
    print(inst.read_bytes(21))

    # Doesn't work: not implemented
    #print(inst.write("Q7"))
    #inst.wait_for_srq()
    #print(inst.read_bytes(21))

if True:
    # Future pymeasure support?
    #pyvisa.log_to_screen()
    inst = Racal1992("GPIB::14", timeout=10000)
    inst.resolution=7
    print(inst.resolution)
    print(inst.unit)
    for i in range(10):
        print(inst.measured_value)

if False:
    print(Gpib.gpib.listener(0,14))
    dev = Gpib.gpib.dev(0,1)

