module top_module (
		   input  clk,
		   input  w, R, E, L,
		   output Q
		   );

   wire 		  x;
   assign x = (E) ? w : Q;

   always @ (posedge clk) begin
      if (L) begin
         Q <= R;
      end
      else begin
         Q <= x;
      end
   end

endmodule
