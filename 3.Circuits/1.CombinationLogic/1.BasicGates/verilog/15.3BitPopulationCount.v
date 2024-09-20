module top_module(
		   input [2:0] 	in,
		   output [1:0] out );

   integer i, count;

   always @ (*) begin
      count = 0;
      for (i=0; i<$bits(in);i++) begin
	 count = count + in[i];
      end
      out = count;
   end

endmodule
