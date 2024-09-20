module top_module(
		   input  a, b,
		   output out_and,
		   output out_or,
		   output out_xor,
		   output out_nand,
		   output out_nor,
		   output out_xnor,
		   output out_anotb
		   );

   assign out_and  = a & b;       /* 与 */
   assign out_or   = a | b;       /* 或 */
   assign out_xor  = a ^ b;       /* 异或 */
   assign out_nand = ~(a & b);    /* 与非 */
   assign out_nor  = ~(a | b);    /* 或非 */
   assign out_xnor = ~(a ^ b);    /* 异或非 */
   assign out_anotb = a & (~b);

endmodule
