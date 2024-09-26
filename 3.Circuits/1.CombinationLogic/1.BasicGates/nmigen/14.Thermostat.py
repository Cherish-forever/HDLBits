#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class Thermostat(Elaboratable):
    def __init__(self):
        self.too_code = Signal()
        self.too_hot = Signal()
        self.mode = Signal()
        self.fan_on = Signal()
        self.heater = Signal()
        self.aircon = Signal()
        self.fan = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += [
            self.heater.eq(self.too_code & self.mode),
            self.aircon.eq(self.too_hot & (~self.mode)),
            self.fan.eq(self.fan_on | self.heater | self.aircon)
        ]
        return m

if __name__ == "__main__":
    top = Thermostat()
    main(top, ports=[top.too_code, top.too_hot, top.mode,
                     top.fan_on, top.heater, top.aircon, top.fan])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.mode.eq(0)
        yield top.too_code.eq(0)
        yield top.too_hot.eq(0)
        yield top.fan_on.eq(1) # only enable fan
        yield Settle()
        assert (yield top.heater) == 0, "Test case 1.1 failed"
        assert (yield top.aircon) == 0, "Test case 1.2 failed"
        assert (yield top.fan) == 1, "Test case 1.3 failed"

        yield top.mode.eq(0)
        yield top.too_code.eq(0)
        yield top.too_hot.eq(1)
        yield top.fan_on.eq(0)
        yield Settle()
        assert (yield top.heater) == 0, "Test case 2.1 failed"
        assert (yield top.aircon) == 1, "Test case 2.2 failed"
        assert (yield top.fan) == 1, "Test case 2.3 failed"

        yield top.mode.eq(1)
        yield top.too_code.eq(1)
        yield top.too_hot.eq(0)
        yield top.fan_on.eq(0)
        yield Settle()
        assert (yield top.heater) == 1, "Test case 3.1 failed"
        assert (yield top.aircon) == 0, "Test case 3.2 failed"
        assert (yield top.fan) == 1, "Test case 3.3 failed"

        yield top.mode.eq(1)
        yield top.too_code.eq(1)
        yield top.too_hot.eq(1)
        yield top.fan_on.eq(1)
        yield Settle()
        assert (yield top.heater) == 1, "Test case 4.1 failed"
        assert (yield top.aircon) == 0, "Test case 4.2 failed"
        assert (yield top.fan) == 1, "Test case 4.3 failed"


    sim.add_process(process)
    sim.run()
