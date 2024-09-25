#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.scancode = Signal(16)
        self.left = Signal()
        self.down = Signal()
        self.right = Signal()
        self.up = Signal()

    def elaborate(self, platform):
        m = Module()

        with m.Switch(self.scancode):
            with m.Case(0xe60b):
                m.d.comb += self.left.eq(1)
            with m.Case(0xe072):
                m.d.comb += self.down.eq(1)
            with m.Case(0xe074):
                m.d.comb += self.right.eq(1)
            with m.Case(0xe075):
                m.d.comb += self.up.eq(1)
            with m.Default():
                m.d.comb += [self.left.eq(0),
                             self.down.eq(0),
                             self.right.eq(0),
                             self.up.eq(0),]
        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.scancode, top.left, top.down, top.right, top.up])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
         yield top.scancode.eq(0xe60b)
         yield Settle()
         assert (yield top.left) == 1, "Test case 1.1 failed"
         assert (yield top.down) == 0, "Test case 1.2 failed"
         assert (yield top.right) == 0, "Test case 1.3 failed"
         assert (yield top.up) == 0, "Test case 1.4 failed"

         yield top.scancode.eq(0xe072)
         yield Settle()
         assert (yield top.left) == 0, "Test case 2.1 failed"
         assert (yield top.down) == 1, "Test case 2.2 failed"
         assert (yield top.right) == 0, "Test case 2.3 failed"
         assert (yield top.up) == 0, "Test case 2.4 failed"

         yield top.scancode.eq(0xe074)
         yield Settle()
         assert (yield top.left) == 0, "Test case 3.1 failed"
         assert (yield top.down) == 0, "Test case 3.2 failed"
         assert (yield top.right) == 1, "Test case 3.3 failed"
         assert (yield top.up) == 0, "Test case 3.4 failed"

         yield top.scancode.eq(0xe075)
         yield Settle()
         assert (yield top.left) == 0, "Test case 4.1 failed"
         assert (yield top.down) == 0, "Test case 4.2 failed"
         assert (yield top.right) == 0, "Test case 4.3 failed"
         assert (yield top.up) == 1, "Test case 4.4 failed"

         yield top.scancode.eq(0xffff)
         yield Settle()
         assert (yield top.left) == 0, "Test case 5.1 failed"
         assert (yield top.down) == 0, "Test case 5.2 failed"
         assert (yield top.right) == 0, "Test case 5.3 failed"
         assert (yield top.up) == 0, "Test case 5.4 failed"

    sim.add_process(process)
    sim.run()
