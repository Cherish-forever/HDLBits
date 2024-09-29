#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal(signed(8))
        self.b = Signal(signed(8))
        self.s = Signal(signed(8))
        self.overflow = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += [
            self.s.eq(self.a + self.b),
            self.overflow.eq(~(self.a[7] ^ self.b[7]) & (self.a[7] != self.s[7]))
        ]
        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.s])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(4)
        yield top.b.eq(-3)
        yield Settle()
        assert (yield top.s) == 1, "Test case 1.1 failed"
        assert (yield top.overflow) == 0, "Test case 1.2 failed"

        yield top.a.eq(8)
        yield top.b.eq(-16)
        yield Settle()
        assert (yield top.s) == -8, "Test case 2.1 failed"
        assert (yield top.overflow) == 0, "Test case 2.2 failed"


        # 0x70 eq 112
        # 112 + 112 = 224, overflow 128
        # hex(224) = 0xe0 : 1110_0000 - 1 = 1101_1111 ~ = 0010_0000 = 32
        yield top.a.eq(0x70)
        yield top.b.eq(0x70)
        yield Settle()
        assert (yield top.s) == -32, "Test case 3.1 failed"
        assert (yield top.overflow) == 1, "Test case 3.2 failed"

    sim.add_process(process)
    sim.run()
