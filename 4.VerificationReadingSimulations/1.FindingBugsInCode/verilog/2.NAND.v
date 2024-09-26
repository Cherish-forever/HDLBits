module top_module (input a, input b, input c, output out);//

   wire andgate_out;

   andgate inst1 ( .a(a), .b(b), .c(c), .d(1), .e(1), .out(andgate_out) );

   assign out = ~andgate_out;

endmodule
