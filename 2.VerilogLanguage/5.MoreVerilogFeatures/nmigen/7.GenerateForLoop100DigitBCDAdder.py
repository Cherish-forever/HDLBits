#!/usr/bin/python3

# no test, generate by chartgpt

from nmigen import *
from nmigen.cli import main

class BCDAdder(Elaboratable):
    def __init__(self):
        self.a = Signal(4)  # 4位 BCD 输入
        self.b = Signal(4)  # 4位 BCD 输入
        self.cin = Signal()  # 进位输入
        self.cout = Signal()  # 进位输出
        self.sum = Signal(4)  # 4位 BCD 和

    def elaborate(self, platform):
        m = Module()

        # 中间和（5位）
        sum_temp = Signal(5)

        # 计算和
        m.d.comb += sum_temp.eq(self.a + self.b + self.cin)

        # BCD 校正
        with m.If(sum_temp > 9):
            m.d.comb += [
                self.sum.eq(sum_temp + 6),
                self.cout.eq(1)
            ]
        with m.Else():
            m.d.comb += [
                self.sum.eq(sum_temp),
                self.cout.eq(0)
            ]

        return m


class BCDRippleCarryAdder(Elaboratable):
    def __init__(self):
        self.a = Signal(400)  # 100位 BCD 数字 A
        self.b = Signal(400)  # 100位 BCD 数字 B
        self.cin = Signal()  # 进位输入
        self.cout = Signal()  # 进位输出
        self.sum = Signal(400)  # 100位 BCD 和

    def elaborate(self, platform):
        m = Module()

        carry = self.cin  # 初始化进位
        for i in range(100):
            bcd_fadd_inst = BCDAdder()
            m.submodules[f'bcd_fadd_{i}'] = bcd_fadd_inst

            # 将信号连接到 BCD 加法器实例
            m.d.comb += [
                bcd_fadd_inst.a.eq(self.a[i*4:(i+1)*4]),
                bcd_fadd_inst.b.eq(self.b[i*4:(i+1)*4]),
                bcd_fadd_inst.cin.eq(carry),
                self.sum[i*4:(i+1)*4].eq(bcd_fadd_inst.sum),
            ]
            carry = bcd_fadd_inst.cout  # 更新进位

        m.d.comb += self.cout.eq(carry)  # 最终进位输出

        return m

class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal(400)  # 100位 BCD 输入
        self.b = Signal(400)  # 100位 BCD 输入
        self.cin = Signal()  # 进位输入
        self.cout = Signal()  # 进位输出
        self.sum = Signal(400)  # 100位 BCD 输出

    def elaborate(self, platform):
        m = Module()
        bcd_adder = BCDRippleCarryAdder()
        m.submodules.bcd_adder = bcd_adder

        # 连接信号
        m.d.comb += [
            bcd_adder.a.eq(self.a),
            bcd_adder.b.eq(self.b),
            bcd_adder.cin.eq(self.cin),
            self.cout.eq(bcd_adder.cout),
            self.sum.eq(bcd_adder.sum)
        ]

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.cin, top.cout, top.sum])
