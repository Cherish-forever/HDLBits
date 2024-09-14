module top_module(
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);

   wire 	  cout;
   wire [15:0] 	  sumh, suml;

   add16 lsb(a[15:0], b[15:0], 0, sum[15:0], cout);
   add16 msb1(a[31:16], b[31:16], 0, sumh, 0);
   add16 msb2(a[31:16], b[31:16], 1, suml, 0);

   always @(*)
     case(cout)
       1'b0: sum[31:16] = sumh;
       1'b1: sum[31:16] = suml;
     endcase

endmodule
