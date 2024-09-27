#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal(16)
        self.b = Signal(16)
        self.c = Signal(16)
        self.d = Signal(16)
        self.e = Signal(16)
        self.f = Signal(16)
        self.g = Signal(16)
        self.h = Signal(16)
        self.i = Signal(16)
        self.sel = Signal(4)
        self.out = Signal(16)

    def elaborate(self, platform):
        m = Module()
        with m.Switch(self.sel):
            with m.Case(0):
                m.d.comb += self.out.eq(self.a)
            with m.Case(1):
                m.d.comb += self.out.eq(self.b)
            with m.Case(2):
                m.d.comb += self.out.eq(self.c)
            with m.Case(3):
                m.d.comb += self.out.eq(self.d)
            with m.Case(4):
                m.d.comb += self.out.eq(self.e)
            with m.Case(5):
                m.d.comb += self.out.eq(self.f)
            with m.Case(6):
                m.d.comb += self.out.eq(self.g)
            with m.Case(7):
                m.d.comb += self.out.eq(self.h)
            with m.Case(8):
                m.d.comb += self.out.eq(self.i)
            with m.Default():
                m.d.comb += self.out.eq(0xffff)
        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.c,
                     top.d, top.e, top.f,
                     top.g, top.h, top.i,
                     top.sel, top.out])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(111)
        yield top.b.eq(222)
        yield top.c.eq(333)
        yield top.d.eq(444)
        yield top.e.eq(555)
        yield top.f.eq(666)
        yield top.g.eq(777)
        yield top.h.eq(888)
        yield top.i.eq(999)
        yield top.sel.eq(0)
        yield Settle()
        assert (yield top.out) == 111, "Test case 1 failed"

        yield top.sel.eq(1)
        yield Settle()
        assert (yield top.out) == 222, "Test case 2 failed"

        yield top.sel.eq(2)
        yield Settle()
        assert (yield top.out) == 333, "Test case 3 failed"

        yield top.sel.eq(3)
        yield Settle()
        assert (yield top.out) == 444, "Test case 4 failed"

        yield top.sel.eq(4)
        yield Settle()
        assert (yield top.out) == 555, "Test case 5 failed"

        yield top.sel.eq(5)
        yield Settle()
        assert (yield top.out) == 666, "Test case 6 failed"

        yield top.sel.eq(6)
        yield Settle()
        assert (yield top.out) == 777, "Test case 7 failed"

        yield top.sel.eq(7)
        yield Settle()
        assert (yield top.out) == 888, "Test case 8 failed"

        yield top.sel.eq(8)
        yield Settle()
        assert (yield top.out) == 999, "Test case 9 failed"

        yield top.sel.eq(9)
        yield Settle()
        assert (yield top.out) == 0xffff, "Test case 10 failed"

    sim.add_process(process)
    sim.run()
