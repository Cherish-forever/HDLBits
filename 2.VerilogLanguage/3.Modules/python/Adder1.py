#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class Fulladder(Elaboratable):
    def __init__(self, width):
        self.a = Signal(width)
        self.b = Signal(width)
        self.o = Signal(width)
        self.cin = Signal()
        self.cout = Signal()
        self.width = width

    def elaborate(self, platform):
        m = Module()

        carry = Signal(self.width + 1)
        m.d.comb += carry[0].eq(self.cin)

        for i in range(self.width):
            m.d.comb += [
                self.o[i].eq(self.a[i] ^ self.b[i] ^ carry[i]),
                carry[i + 1].eq((self.a[i] & self.b[i]) | (carry[i] & (self.a[i] ^ self.b[i])))
            ]

        m.d.comb += self.cout.eq(carry[self.width])

        return m


class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal(32)
        self.b = Signal(32)
        self.o = Signal(32)

    def elaborate(self, platform):
        m = Module()

        low = Fulladder(16)
        high = Fulladder(16)

        m.submodules.low = low
        m.submodules.high = high

        m.d.comb += [
            low.cin.eq(0),
            low.a.eq(self.a[0:16]),
            low.b.eq(self.b[0:16]),
            high.a.eq(self.a[16:32]),
            high.b.eq(self.b[16:32]),
            low.cin.eq(0),
            high.cin.eq(low.cout),
            self.o.eq(Cat(low.o, high.o))
        ]

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.o])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(5)
        yield top.b.eq(10)
        yield Settle()
        assert (yield top.o) == 15, "Test case 1 failed"

        yield top.a.eq(65535)
        yield top.b.eq(65535)
        yield Settle()
        assert (yield top.o) == 131070, "Test case 2 failed"

    sim.add_process(process)
    sim.run()
