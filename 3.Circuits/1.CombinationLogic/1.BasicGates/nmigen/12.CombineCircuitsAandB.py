#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class A(Elaboratable):
    def __init__(self):
        self.x = Signal()
        self.y = Signal()
        self.z = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.z.eq((self.x ^ self.y) & self.x)
        return m

class B(Elaboratable):
    def __init__(self):
        self.x = Signal()
        self.y = Signal()
        self.z = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.z.eq(~(self.x ^ self.y))
        return m

class CombineCircuitsAandB(Elaboratable):
    def __init__(self):
        self.x = Signal()
        self.y = Signal()
        self.z = Signal()

    def elaborate(self, platform):
        m = Module()

        ia1z = Signal()
        ib1z = Signal()
        ia2z = Signal()
        ib2z = Signal()

        m.submodules.ia1 = ia1 = A()
        m.submodules.ib1 = ib1 = B()
        m.submodules.ia2 = ia2 = A()
        m.submodules.ib2 = ib2 = B()

        m.d.comb += [
            ia1.x.eq(self.x),
            ia1.y.eq(self.y),
            ia1z.eq(ia1.z),
            ib1.x.eq(self.x),
            ib1.y.eq(self.y),
            ib1z.eq(ib1.z),
            ia2.x.eq(self.x),
            ia2.y.eq(self.y),
            ia2z.eq(ia2.z),
            ib2.x.eq(self.x),
            ib2.y.eq(self.y),
            ib2z.eq(ib2.z),
            self.z.eq((ia1z | ib1z) ^ (ia2z & ib2z))
        ]

        return m

if __name__ == "__main__":
    top = CombineCircuitsAandB()
    main(top, ports=[top.x, top.y, top.z])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.x.eq(0)
        yield top.y.eq(0)
        yield Settle()
        assert (yield top.z) == 1, "Test case 1 failed"

        yield top.x.eq(0)
        yield top.y.eq(1)
        yield Settle()
        assert (yield top.z) == 0, "Test case 2 failed"

        yield top.x.eq(1)
        yield top.y.eq(0)
        yield Settle()
        assert (yield top.z) == 1, "Test case 3 failed"

        yield top.x.eq(1)
        yield top.y.eq(1)
        yield Settle()
        assert (yield top.z) == 1, "Test case 4 failed"

    sim.add_process(process)
    sim.run()
