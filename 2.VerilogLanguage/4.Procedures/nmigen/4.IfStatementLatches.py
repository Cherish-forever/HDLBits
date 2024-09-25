#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.cpu_overheated    = Signal()
        self.shut_off_computer = Signal()
        self.arrived           = Signal()
        self.gas_tank_empty    = Signal()
        self.keep_driving      = Signal()

    def elaborate(self, platform):
        m = Module()

        with m.If(self.cpu_overheated):
            m.d.comb += self.shut_off_computer.eq(1)
        with m.Else():
            m.d.comb += self.shut_off_computer.eq(0)

        with m.If(self.arrived):
            m.d.comb += self.keep_driving.eq(0)
        with m.Else():
            m.d.comb += self.keep_driving.eq(~self.gas_tank_empty)

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.cpu_overheated, top.shut_off_computer,
                     top.arrived, top.gas_tank_empty,
                     top.keep_driving])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.arrived.eq(0)
        yield top.gas_tank_empty.eq(0)
        yield Settle()
        assert (yield top.keep_driving) == 1, "Does`t arrived and gas not empty, keep_driving must eq 1"

        yield top.arrived.eq(0)
        yield top.gas_tank_empty.eq(1)
        yield Settle()
        assert (yield top.keep_driving) == 0, "Gas empty, keep_driving must eq 0"

        yield top.arrived.eq(1)
        yield top.gas_tank_empty.eq(0)
        yield Settle()
        assert (yield top.keep_driving) == 0, "arrived and Gas not empty, keep_driving must eq 0"

        yield top.arrived.eq(0)
        yield top.gas_tank_empty.eq(1)
        yield Settle()
        assert (yield top.keep_driving) == 0, "Does`t arrived and gas empty, keep_driving must eq 0"

        yield top.cpu_overheated.eq(0)
        yield Settle()
        assert (yield top.shut_off_computer) == 0, "cpu is not overheated, shut_off_computer must eq 0"

        yield top.cpu_overheated.eq(1)
        yield Settle()
        assert (yield top.shut_off_computer) == 1, "cpu overheated, shut_off_computer must eq 1"


    sim.add_process(process)
    sim.run()
