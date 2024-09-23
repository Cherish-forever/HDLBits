# HDLBits
Verilog Practice

# Install

`$ pip3 install nmigen`

`$ sudo apt insatll yosys`

# Generate

default file type is verilog

`$ ./1.GettingStarted/python/GettingStared.py generate`

## for verilog
`$ ./1.GettingStarted/python/GettingStared.py generate -t v`

## for RTLIL
`$ ./1.GettingStarted/python/GettingStared.py generate -t il`


# Simulate

## for VCD file

default period is 1e-6 = 1us

`$ ./1.GettingStarted/python/Counter.py simulate -v counter.vcd -c 1000`

## for gtkware file

change period to 1 second

`$ ./1.GettingStarted/python/Counter.py simulate -v counter.vcd -w counter.gtkw -p 1 -c 1000`
