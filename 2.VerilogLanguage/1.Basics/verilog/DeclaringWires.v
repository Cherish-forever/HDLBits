module top_module(
                  input a, b, c, d,
                  output out, out_n
                  );

   assign out = (a & b) | (c & d);
   assign out_n = ~out;

endmodule
