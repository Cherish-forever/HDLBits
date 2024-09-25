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
        self.a = Signal(100)
        self.b = Signal(100)
        self.o = Signal(100)

    def elaborate(self, platform):
        m = Module()

        adder = Fulladder(100)
        m.submodules.adder = adder

        m.d.comb += [
            adder.cin.eq(0),
            adder.a.eq(self.a),
            adder.b.eq(self.b),
            self.o.eq(adder.o)
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
