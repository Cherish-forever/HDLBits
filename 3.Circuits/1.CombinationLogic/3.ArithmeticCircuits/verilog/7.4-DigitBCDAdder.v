module top_module (
                   input [15:0] a, b,
                   input        cin,
                   output       cout,
                   output [15:0] sum );

   wire [3:0]                    co;
   bcd_fadd x(a[3:0], b[3:0], cin, co[0], sum[3:0]);

   generate
      genvar                     i;
      for (i=1; i<4; i++) begin: adding
         bcd_fadd y(
                    a[3 + i * 4:i * 4],
                    b[3 + i * 4:i * 4],
                    co[i -1],
                    co[i],
                    sum[3 + i * 4:i * 4]);
      end
   endgenerate

   assign cout = co[3];

endmodule
