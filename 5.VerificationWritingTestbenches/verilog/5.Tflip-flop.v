`timescale 1ps/1ps

module top_module();
   reg clk;
   reg reset;
   reg t;
   wire q;

   initial begin
      clk   = 1'b0;
      reset = 1'b1;
      t     = 1'b0;
      #10;
      reset = 1'b0;
      t     = 1'b1;
   end

   always #5 clk = ~clk;

   tff u_tff(
	     .clk(clk),
	     .reset(reset),
	     .t(t),
	     .q(q)
	     );

endmodule
