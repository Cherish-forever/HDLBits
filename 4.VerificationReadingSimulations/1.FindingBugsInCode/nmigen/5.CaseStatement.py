#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.code  = Signal(8)
        self.out   = Signal(8)
        self.valid = Signal(reset=1)

    def elaborate(self, platform):
        m = Module()

        with m.Switch(self.code):
            m.d.comb += self.valid.eq(1)
            with m.Case(0x45):
                m.d.comb += self.out.eq(0)
            with m.Case(0x16):
                m.d.comb += self.out.eq(1)
            with m.Case(0x1e):
                m.d.comb += self.out.eq(2)
            with m.Case(0x26):
                m.d.comb += self.out.eq(3)
            with m.Case(0x25):
                m.d.comb += self.out.eq(4)
            with m.Case(0x2e):
                m.d.comb += self.out.eq(5)
            with m.Case(0x36):
                m.d.comb += self.out.eq(6)
            with m.Case(0x3d):
                m.d.comb += self.out.eq(7)
            with m.Case(0x3e):
                m.d.comb += self.out.eq(8)
            with m.Case(0x46):
                m.d.comb += self.out.eq(9)
            with m.Default():
                m.d.comb += [
                    self.out.eq(0),
                    self.valid.eq(0)
                ]

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.code, top.out, top.valid])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.code.eq(0x45)
        yield Settle()
        assert (yield top.out) == 0, "Test case 1.1 failed"
        assert (yield top.valid) == 1, "Test case 1.2 failed"

        yield top.code.eq(0x16)
        yield Settle()
        assert (yield top.out) == 1, "Test case 2.1 failed"
        assert (yield top.valid) == 1, "Test case 2.2 failed"

        yield top.code.eq(0x1e)
        yield Settle()
        assert (yield top.out) == 2, "Test case 3.1 failed"
        assert (yield top.valid) == 1, "Test case 3.2 failed"

        yield top.code.eq(0x26)
        yield Settle()
        assert (yield top.out) == 3, "Test case 4.1 failed"
        assert (yield top.valid) == 1, "Test case 4.2 failed"

        yield top.code.eq(0x25)
        yield Settle()
        assert (yield top.out) == 4, "Test case 5.1 failed"
        assert (yield top.valid) == 1, "Test case 5.2 failed"

        yield top.code.eq(0x2e)
        yield Settle()
        assert (yield top.out) == 5, "Test case 6.1 failed"
        assert (yield top.valid) == 1, "Test case 6.2 failed"

        yield top.code.eq(0x36)
        yield Settle()
        assert (yield top.out) == 6, "Test case 7.1 failed"
        assert (yield top.valid) == 1, "Test case 7.2 failed"

        yield top.code.eq(0x3d)
        yield Settle()
        assert (yield top.out) == 7, "Test case 8.1 failed"
        assert (yield top.valid) == 1, "Test case 8.2 failed"

        yield top.code.eq(0x3e)
        yield Settle()
        assert (yield top.out) == 8, "Test case 9.1 failed"
        assert (yield top.valid) == 1, "Test case 9.2 failed"

        yield top.code.eq(0x46)
        yield Settle()
        assert (yield top.out) == 9, "Test case 10.1 failed"
        assert (yield top.valid) == 1, "Test case 10.2 failed"

        yield top.code.eq(0xff)
        yield Settle()
        assert (yield top.out) == 0, "Test case 11.1 failed"
        assert (yield top.valid) == 0, "Test case 11.2 failed"

    sim.add_process(process)
    sim.run()
