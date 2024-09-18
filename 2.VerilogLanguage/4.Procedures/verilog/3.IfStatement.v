module top_module(
		  input       a,
		  input       b,
		  input       sel_b1,
		  input       sel_b2,
		  output wire out_assign,
		  output reg  out_always   );

   /* assign left-hand-side type is wire */
   assign out_assign = (sel_b1 & sel_b2) ? b : a;

   /* always left-hand-side type is reg */
   always @ (*) begin
      if (sel_b1 & sel_b2) begin
         out_always = b;
      end
      else begin
         out_always = a;
      end
   end

endmodule
