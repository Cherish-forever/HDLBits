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
        self.a = Signal(3)
        self.b = Signal(3)
        self.cin = Signal()
        self.cout = Signal()
        self.sum_ = Signal(3)

    def elaborate(self, platform):
        m = Module()

        m.submodules.adder = adder = Fulladder(3);

        m.d.comb += [
            adder.a.eq(self.a),
            adder.b.eq(self.b),
            adder.cin.eq(self.cin),
            self.cout.eq(adder.cout),
            self.sum_.eq(adder.o)
        ]
        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.cin, top.cout, top.sum_])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(4)
        yield top.b.eq(3)
        yield top.cin.eq(0)
        yield Settle()
        assert (yield top.sum_) == 7, "Test case 1.1 failed"
        assert (yield top.cout) == 0, "Test case 1.2 failed"

        yield top.a.eq(4)
        yield top.b.eq(3)
        yield top.cin.eq(1)
        yield Settle()
        assert (yield top.sum_) == 0, "Test case 2.1 failed"
        assert (yield top.cout) == 1, "Test case 2.2 failed"

        yield top.a.eq(4)
        yield top.b.eq(4)
        yield top.cin.eq(1)
        yield Settle()
        assert (yield top.sum_) == 1, "Test case 3.1 failed"
        assert (yield top.cout) == 1, "Test case 3.2 failed"

    sim.add_process(process)
    sim.run()
