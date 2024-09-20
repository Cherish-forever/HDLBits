module A(input x, input y, output z);

   assign z = (x ^ y) & x;

endmodule

module B(input x, input y, output z);

   assign z = ~(x ^ y);

endmodule

module top_module (input x, input y, output z);

   wire ia1z, ib1z, ia2z, ib2z;

   A IA1(x, y, ia1z);
   B IB1(x, y, ib1z);
   A IA2(x, y, ia2z);
   B IB2(x, y, ib2z);

   assign z = (ia1z | ib1z) ^ (ia2z & ib2z);

endmodule
