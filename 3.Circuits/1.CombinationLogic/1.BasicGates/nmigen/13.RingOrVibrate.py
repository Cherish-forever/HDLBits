#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class RingOrVibrate(Elaboratable):
    def __init__(self):
        self.ring = Signal()
        self.vibrate_mode = Signal()
        self.ringer = Signal()
        self.motor = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += [
            self.ringer.eq(self.ring & (~self.vibrate_mode)),
            self.motor.eq(self.ring & self.vibrate_mode)
        ]
        return m

if __name__ == "__main__":
    top = RingOrVibrate()
    main(top, ports=[top.ring, top.vibrate_mode, top.ringer, top.motor])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.ring.eq(0)
        yield top.vibrate_mode.eq(0)
        yield Settle()
        assert (yield top.ringer) == 0, "Test case 1.1 failed"
        assert (yield top.motor) == 0, "Test case 1.2 failed"

        yield top.ring.eq(0)
        yield top.vibrate_mode.eq(1)
        yield Settle()
        assert (yield top.ringer) == 0, "Test case 2.1 failed"
        assert (yield top.motor) == 0, "Test case 2.2 failed"

        yield top.ring.eq(1)
        yield top.vibrate_mode.eq(0)
        yield Settle()
        assert (yield top.ringer) == 1, "Test case 3.1 failed"
        assert (yield top.motor) == 0, "Test case 3.2 failed"

        yield top.ring.eq(1)
        yield top.vibrate_mode.eq(1)
        yield Settle()
        assert (yield top.ringer) == 0, "Test case 4.1 failed"
        assert (yield top.motor) == 1, "Test case 4.2 failed"

    sim.add_process(process)
    sim.run()
