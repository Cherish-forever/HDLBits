module top_module(
		  input       a,
		  input       b,
		  output wire out_assign,
		  output reg  out_alwaysblock);

   /* assign left-hand-side type is wire */
   assign out_assign = a & b;

   /* always left-hand-side type is reg */
   always @ (*) begin
      out_alwaysblock = a & b;
   end

endmodule
