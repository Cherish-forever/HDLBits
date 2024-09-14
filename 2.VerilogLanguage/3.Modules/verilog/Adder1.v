module top_module(
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);

   wire 	  cout;

   add16 lsb(a[15:0], b[15:0], 0, sum[15:0], cout);
   add16 msb(a[31:16], b[31:16], cout, sum[31:16], 0);

endmodule
