# Racal-Dana 1992 GPIB Notes

* SK4 must be plugged in on the GPIB board.

  My unit had the jumper in the one parallel to it! @#$%!@$%

* There's a buffer in the instrument in which values get written whenever
  there's a new measurement.
* *all* messages read from instrument are 21 bytes long. No exceptions.
* When you issue a command that requests data back, the buffer
  gets cleared.

  For example, you will only get the data for RGS if you do:

  ```python
    write("RMS")
    write("RGS")
    read_bytes(21)
   ```

  You will still get RMS if you do this:

  ```python
    write("RMS")
    write("PA")
    read_bytes(21)
  ```

  Concatenation doesn't work. This only returns RGS:

  ```
	write("RMS RGS")
  ```

    You will get the data for RMS, because PA doesn't ask for data.

  Switching from one measurement mode to another also clears the
  buffer.

* read data commands:
  * RGS: GPIB SW version
  * RLA: channel A trigger or peak level
  * RLB: channel B trigger or peak level
  * RMS: software version
  * RMX: math constant X
  * RMZ: math constant Z
  * RRS: resolution
  * RSF: special function
  * RUT: unit type

* If there is no data, pyvisa will time out. 
* Configure SRQ and use `wait_for_srq`, however, that gives the
  following error with `pyvisa_py`:

```
  File "/home/tom/projects/racal1992/./racal.py", line 39, in <module>
    inst.wait_for_srq()
  File "/home/tom/.local/lib/python3.10/site-packages/pyvisa/resources/gpib.py", line 65, in wait_for_srq
    self.enable_event(
  File "/home/tom/.local/lib/python3.10/site-packages/pyvisa/resources/resource.py", line 511, in enable_event
    self.visalib.enable_event(self.session, event_type, mechanism, context)
  File "/home/tom/.local/lib/python3.10/site-packages/pyvisa/highlevel.py", line 909, in enable_event
    raise NotImplementedError
NotImplementedError
```

* Only way to avoid timeouts is to set larger timeout values?



