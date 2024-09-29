module top_module (
                   input [3:0] x,
                   input [3:0] y,
                   output [4:0] sum);

   /* sum is 5bits, x and y is 4bits */
   /* verilog will auto expand the overflow bit in arithmetic operation */
   /* sum is 5bits, it has been expanded */
   assign sum = x + y;

endmodule
