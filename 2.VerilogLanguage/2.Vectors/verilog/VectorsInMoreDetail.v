module top_module (
                   input wire [15:0] in,
                   output wire [7:0] out_hi,
                   output wire [7:0] out_lo
                   );

   assign out_hi = in[8:15];
   assign out_lo = in[0:7];

endmodule
