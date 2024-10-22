module coutn10(
	       input 	    clk,
	       input 	    reset,
	       input 	    ena,
	       output [3:0] q);

   always @(posedge clk) begin
      if (reset)
        q <= 0;
      else if (ena)
        if (q == 4'd9)
          q <= 0;
        else
          q <= q + 1;
      else
        q <= q;
   end
endmodule

module top_module (
		   input 	 clk,
		   input 	 reset, // Synchronous active-high reset
		   output [3:1]  ena,
		   output [15:0] q);

   coutn10 c1(clk, reset, 1'b1, q[3:0]);
   coutn10 c2(clk, reset, ena[1], q[7:4]);
   coutn10 c3(clk, reset, ena[2], q[11:8]);
   coutn10 c4(clk, reset, ena[3], q[15:12]);

   assign ena[1] = (q[3:0] == 9);
   assign ena[2] = (q[3:0] == 9 && q[7:4] == 9);
   assign ena[3] = (q[3:0] == 9 && q[7:4] == 9 && q[11:8] == 9);
