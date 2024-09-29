#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.c = Signal()
        self.d = Signal()
        self.mux_in = Signal(4)


    def elaborate(self, platform):
        m = Module()
        m.d.comb += [
            self.mux_in[0].eq(self.c | self.d),
            self.mux_in[1].eq(0),
            self.mux_in[2].eq(~self.d),
            self.mux_in[3].eq(self.c & self.d),
        ]
        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.c, top.d, top.mux_in])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.c.eq(0)
        yield top.d.eq(0)
        yield Settle()
        assert (yield top.mux_in) == 4, "Test case 1 failed"

        yield top.c.eq(0)
        yield top.d.eq(1)
        yield Settle()
        assert (yield top.mux_in) == 1, "Test case 2 failed"

        yield top.c.eq(1)
        yield top.d.eq(0)
        yield Settle()
        assert (yield top.mux_in) == 5, "Test case 3 failed"

        yield top.c.eq(1)
        yield top.d.eq(1)
        yield Settle()
        assert (yield top.mux_in) == 9, "Test case 4 failed"

    sim.add_process(process)
    sim.run()
