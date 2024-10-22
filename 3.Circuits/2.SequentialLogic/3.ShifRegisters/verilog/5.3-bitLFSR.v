module top_module (
		   input [2:0] 	SW, // Reload
		   input [1:0] 	KEY, // Load and clk
		   output [2:0] LEDR);  // Q

   always @(posedge KEY[0]) begin
      if (KEY[1])
	LEDR <= SW;
      else
	LEDR <= { LEDR[2] ^ LEDR[1], LEDR[0], LEDR[2] };
   end

endmodule
