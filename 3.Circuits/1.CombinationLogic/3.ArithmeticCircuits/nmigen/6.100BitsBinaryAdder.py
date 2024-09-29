#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal(100)
        self.b = Signal(100)
        self.cin = Signal()
        self.cout = Signal()
        self.sum_ = Signal(100)

    def elaborate(self, platform):
        m = Module()

        s = Signal(101)

        m.d.comb += [
            s.eq(self.a + self.b + self.cin),
            self.sum_.eq(s[:-1]), # eq s[0:99]
            self.cout.eq(s[-1])   # eq s[101]
        ]
        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.cin, top.cout, top.sum_])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(32768)
        yield top.b.eq(32768)
        yield Settle()
        assert (yield top.sum_) == 65536, "Test case 1.1 failed"
        assert (yield top.cout) == 0, "Test case 1.2 failed"

        yield top.a.eq(0xfffffffffffffffffffffffff)
        yield top.b.eq(100)
        yield Settle()
        assert (yield top.sum_) == 99, "Test case 2.1 failed"
        assert (yield top.cout) == 1, "Test case 2.2 failed"

    sim.add_process(process)
    sim.run()
