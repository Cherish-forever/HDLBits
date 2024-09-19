module top_module(
		  input [254:0] in,
		  output [7:0] 	out );

   integer 			i;

   always @ (*) begin
      out = 0;
      for (i=0; i<$bits(in); i++) begin
	 out = out + in[i];
      end
   end

endmodule
