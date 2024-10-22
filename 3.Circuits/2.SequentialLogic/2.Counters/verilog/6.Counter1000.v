module top_module (
		   input 	clk,
		   input 	reset,
		   output 	OneHertz,
		   output [2:0] c_enable
		   ); //

   wire [3:0] 			Q1, Q2, Q3;

   bcdcount counter0 (clk, reset, c_enable[0], Q1);
   bcdcount counter1 (clk, reset, c_enable[1], Q2);
   bcdcount counter2 (clk, reset, c_enable[2], Q3);

   assign c_enable[1] = (Q1 == 4'd9) ? 1 : 0;
   assign c_enable[2] = (Q2 == 4'd9 && Q1 == 4'd9) ? 1 : 0;
   assign OneHertz    = (Q3 == 4'd9 && Q2 == 4'd9 && Q1 == 4'd9) ? 1 : 0;

   always @(posedge clk) begin
      if (!reset) begin
         c_enable[0] = 1'b1;
      end
   end

endmodule
