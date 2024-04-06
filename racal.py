#! /usr/bin/env python3

import pyvisa
import Gpib
from pymeasure.instruments.racal import Racal1992

if False:
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource("GPIB::14")

    #print("0x%02x" % inst.stb)

    inst.write_termination='\r\n'   # Default pyvisa termination
    inst.write("RUT")
    if (inst.stb & 0x7) == 5:
        inst.write_termination='\n\r'
        inst.write("RUT")
    if (inst.stb & 0x7) == 5:
        raise Exception("Can't find working write termination!")
    else:
        unit_type = inst.read_bytes(21)

        print(unit_type)

    inst.write("IP")    # Default settings
    inst.write("CK")    # Self-check mode
    inst.write("SRS 8")

    while True:
        while (inst.stb & 0x10) == 0:
            print(".", end='', flush=True)
            pass
        print(inst.read_bytes(21))


if False:
    rm = pyvisa.ResourceManager()

    # Prints all GPIB traffic...
    pyvisa.log_to_screen()
    #print(rm.list_resources())

    inst = rm.open_resource("GPIB::14")
    inst.chunk_size=21
    inst.max_count_read=21
    #inst.write_termination='\n\r'
    inst.write_termination='\n\r'

    # Reset to default settings
    #print(inst.write("IP"))

    # Switch to self-test mode: internal 10MHz clock is measured.
    #print(inst.write("CK"))

    inst.write("RGS")
    print(inst.read_bytes(21))
    inst.write("RLA")
    print(inst.read_bytes(21))
    inst.write("RLB")
    print(inst.read_bytes(21))
    inst.write("RMS")
    print(inst.read_bytes(21))
    inst.write("RMX")
    print(inst.read_bytes(21))
    inst.write("RMZ")
    print(inst.read_bytes(21))
    inst.write("RRS")
    print(inst.read_bytes(21))
    inst.write("RSF")
    print(inst.read_bytes(21))
    inst.write("RUT")
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
    pyvisa.log_to_screen()
    inst = Racal1992("GPIB::14", timeout=10000)
    inst.resolution=7
    #print(inst.resolution)
    #print(inst.unit)

    inst.channel_settings('A', 
                coupling="DC", 
                impedance='1M', 
                slope='neg',
                trigger='auto',
                filtering=False,
                trigger_level=1.5)
    print("0x%02x" % inst.adapter.read_stb())
    print(inst.trigger_level('A'))
    inst.operating_mode('frequency_a')
    inst.math_mode(False)
    inst.math_x = 1000
    inst.math_z = 2


    for i in range(10):
        inst.wait_for_measurement(timeout=2)
        print(inst.measured_value)

