module top_module(
                   input [99:0] a, b,
                   input        cin,
                   output       cout,
                   output [99:0] sum );

   /* verilog will auto expand the overflow bit in arithmetic operation */
   assign {cout, sum} = a + b + cin;

endmodule
