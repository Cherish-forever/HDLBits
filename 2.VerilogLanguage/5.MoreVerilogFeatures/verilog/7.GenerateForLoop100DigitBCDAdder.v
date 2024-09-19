module top_module(
		  input [399:0]  a, b,
		  input 	 cin,
		  output 	 cout,
		  output [399:0] sum );

   wire [99:0] 			 wcout;
   genvar 			 i;

   generate
      bcd_fadd(a[3:0], b[3:0], cin, wcout[0], sum[3:0]);

      /* generate block need a name */
      for(i=4; i<400; i=i+4) begin: bcd_adder_instances
	 bcd_fadd bcd_adder(a[i+3:i], b[i+3:i], wcout[i/4 - 1], wcout[i/4], sum[i+3:i]);
      end
   endgenerate

   assign cout = wcout[99];

endmodule
