`timescale 1ps/1ps

module top_module();
   reg clk;
   reg in;
   reg [2:0] s;
   wire      out;

   initial begin
      clk = 1'b0;
      in = 1'b0;
      s = 2;
   end

   initial begin
      #20; in = 1'b1;
      #10; in = 1'b0;
      #10; in = 1'b1;
      #30; in = 1'b0;
      // #10; $finish; /* no need finish */
   end

   initial begin
      #10; s = 6;
      #10; s = 2;
      #10; s = 7;
      #10; s = 0;
   end

   always #5 clk = ~clk;

   q7 u_q7(
    	   .clk(clk),
           .in(in),
           .s(s),
           .out(out)
    	   );

endmodule
