#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class BCDAdder(Elaboratable):
    def __init__(self):
        self.a = Signal(4)
        self.b = Signal(4)
        self.cin = Signal()
        self.cout = Signal()
        self.sum_ = Signal(4)

    def elaborate(self, platform):
        m = Module()

        sum_temp = Signal(5)

        m.d.comb += sum_temp.eq(self.a + self.b + self.cin)

        with m.If(sum_temp > 9):
            m.d.comb += [
                self.sum_.eq(sum_temp + 6),
                self.cout.eq(1)
            ]
        with m.Else():
            m.d.comb += [
                self.sum_.eq(sum_temp),
                self.cout.eq(0)
            ]

        return m

class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal(16)
        self.b = Signal(16)
        self.cin = Signal()
        self.cout = Signal()
        self.sum_ = Signal(16)

    def elaborate(self, platform):
        m = Module()

        co = Signal(5)

        m.d.comb += co[0].eq(self.cin)

        for i in range(4):
            m.submodules[f'bcdadder_{i}'] = bcd_adder = BCDAdder()
            m.d.comb += [
                bcd_adder.a.eq(self.a[i * 4:i*4 + 4]),
                bcd_adder.b.eq(self.b[i * 4:i*4 + 4]),
                bcd_adder.cin.eq(co[i]),
                co[i + 1].eq(bcd_adder.cout),
                self.sum_[i * 4:i*4 + 4].eq(bcd_adder.sum_)
            ]

        m.d.comb += self.cout.eq(co[4])

        return m

def to_bcd(value):
    bcd = 0
    for i in range(4):
        digit = value % 10
        bcd |= (digit << (i * 4))
        value //= 10
    return bcd

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.cin, top.cout, top.sum_])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(to_bcd(111))
        yield top.b.eq(to_bcd(222))
        yield top.cin.eq(0)
        yield Settle()
        assert (yield top.sum_) == to_bcd(333), "Test case 1.1 failed"
        assert (yield top.cout) == 0, "Test case 1.2 failed"

        yield top.a.eq(to_bcd(9999))
        yield top.b.eq(to_bcd(1))
        yield top.cin.eq(0)
        yield Settle()
        assert (yield top.sum_) == 0, "Test case 2.1 failed"
        assert (yield top.cout) == 1, "Test case 2.2 failed"

        yield top.a.eq(to_bcd(4444))
        yield top.b.eq(to_bcd(5555))
        yield top.cin.eq(1)
        yield Settle()
        assert (yield top.sum_) == 0, "Test case 3.1 failed"
        assert (yield top.cout) == 1, "Test case 3.2 failed"

    sim.add_process(process)
    sim.run()
