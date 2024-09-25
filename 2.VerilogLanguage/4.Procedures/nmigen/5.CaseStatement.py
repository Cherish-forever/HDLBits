#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.sel    = Signal(3)
        self.data0 = Signal(4)
        self.data1 = Signal(4)
        self.data2 = Signal(4)
        self.data3 = Signal(4)
        self.data4 = Signal(4)
        self.data5 = Signal(4)
        self.out = Signal(4)

    def elaborate(self, platform):
        m = Module()

        with m.Switch(self.sel):
            with m.Case(0):
                m.d.comb += self.out.eq(self.data0)
            with m.Case(1):
                m.d.comb += self.out.eq(self.data1)
            with m.Case(2):
                m.d.comb += self.out.eq(self.data2)
            with m.Case(3):
                m.d.comb += self.out.eq(self.data3)
            with m.Case(4):
                m.d.comb += self.out.eq(self.data4)
            with m.Case(5):
                m.d.comb += self.out.eq(self.data5)
            with m.Default():
                m.d.comb += self.out.eq(0)

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.data0, top.data1, top.data2, top.data3,
                     top.data4, top.data5, top.out, top.sel])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
         yield top.data0.eq(1)
         yield top.data1.eq(2)
         yield top.data2.eq(4)
         yield top.data3.eq(8)
         yield top.data4.eq(15)
         yield top.data5.eq(10)

         yield top.sel.eq(0)
         yield Settle()
         assert (yield top.out) == 1, "Test case 1 failed"

         yield top.sel.eq(1)
         yield Settle()
         assert (yield top.out) == 2, "Test case 2 failed"

         yield top.sel.eq(2)
         yield Settle()
         assert (yield top.out) == 4, "Test case 3 failed"

         yield top.sel.eq(3)
         yield Settle()
         assert (yield top.out) == 8, "Test case 4 failed"

         yield top.sel.eq(4)
         yield Settle()
         assert (yield top.out) == 15, "Test case 5 failed"

         yield top.sel.eq(5)
         yield Settle()
         assert (yield top.out) == 10, "Test case 6 failed"

    sim.add_process(process)
    sim.run()
