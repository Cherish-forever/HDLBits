#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class MoreLogicGate(Elaboratable):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.out_and   = Signal()
        self.out_or    = Signal()
        self.out_xor   = Signal()
        self.out_nand  = Signal()
        self.out_nor   = Signal()
        self.out_xnor   = Signal()
        self.out_anoth = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += [
            self.out_and.eq(self.a & self.b),
            self.out_or.eq(self.a | self.b),
            self.out_xor.eq(self.a ^ self.b),
            self.out_nand.eq(~(self.a & self.b)),
            self.out_nor.eq(~(self.a | self.b)),
            self.out_xnor.eq(~(self.a ^ self.b)),
            self.out_anoth.eq(self.a & (~self.b))
        ]
        return m

if __name__ == "__main__":
    top = MoreLogicGate()
    main(top, ports=[top.a, top.b,
                     top.out_and, top.out_or,
                     top.out_xor, top.out_nand,
                     top.out_nor, top.out_anoth])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(0)
        yield top.b.eq(0)
        yield Settle()
        assert (yield top.out_and) == 0, "Test case 1.1 failed"
        assert (yield top.out_or) == 0, "Test case 1.2 failed"
        assert (yield top.out_xor) == 0, "Test case 1.3 failed"
        assert (yield top.out_nand) == 1, "Test case 1.4 failed"
        assert (yield top.out_nor) == 1, "Test case 1.5 failed"
        assert (yield top.out_xnor) == 1, "Test case 1.6 failed"
        assert (yield top.out_anoth) == 0, "Test case 1.7 failed"

        yield top.a.eq(0)
        yield top.b.eq(1)
        yield Settle()
        assert (yield top.out_and) == 0, "Test case 2.1 failed"
        assert (yield top.out_or) == 1, "Test case 2.2 failed"
        assert (yield top.out_xor) == 1, "Test case 2.3 failed"
        assert (yield top.out_nand) == 1, "Test case 2.4 failed"
        assert (yield top.out_nor) == 0, "Test case 2.5 failed"
        assert (yield top.out_xnor) == 0, "Test case 2.6 failed"
        assert (yield top.out_anoth) == 0, "Test case 2.7 failed"

        yield top.a.eq(1)
        yield top.b.eq(0)
        yield Settle()
        assert (yield top.out_and) == 0, "Test case 3.1 failed"
        assert (yield top.out_or) == 1, "Test case 3.2 failed"
        assert (yield top.out_xor) == 1, "Test case 3.3 failed"
        assert (yield top.out_nand) == 1, "Test case 3.4 failed"
        assert (yield top.out_nor) == 0, "Test case 3.5 failed"
        assert (yield top.out_xnor) == 0, "Test case 3.6 failed"
        assert (yield top.out_anoth) == 1, "Test case 3.7 failed"

        yield top.a.eq(1)
        yield top.b.eq(1)
        yield Settle()
        assert (yield top.out_and) == 1, "Test case 4.1 failed"
        assert (yield top.out_or) == 1, "Test case 4.2 failed"
        assert (yield top.out_xor) == 0, "Test case 4.3 failed"
        assert (yield top.out_nand) == 0, "Test case 4.4 failed"
        assert (yield top.out_nor) == 0, "Test case 4.5 failed"
        assert (yield top.out_xnor) == 1, "Test case 4.6 failed"
        assert (yield top.out_anoth) == 0, "Test case 4.7 failed"

    sim.add_process(process)
    sim.run()
