module counter
  #(parameter RST = 0,
    parameter LOAD = 0,
    parameter OVER = 12)
   (
    input 	     clk,
    input 	     reset,
    input 	     ena,
    output reg [7:0] out
    );

   always @(posedge clk) begin
      if(reset) begin
         out <= RST;
      end
      else if (ena) begin
         if (out == OVER) begin
            out <= LOAD;
         end
         else if (out[3:0] == 9) begin
            out[7:4] <= out[7:4] + 1;
            out[3:0] <= 0;
         end
         else begin
            out[3:0] <= out[3:0] + 1;
         end
      end
      else begin
         out <= out;
      end
   end

endmodule

module top_module(
                  input        clk,
                  input        reset,
                  input        ena,
                  output       pm,
                  output [7:0] hh,
                  output [7:0] mm,
                  output [7:0] ss);

   wire                        ss_over;
   wire                        mm_over;
   reg 			       pm_reg;

   assign ss_over = (ss == 8'h59);
   assign mm_over = (ss == 8'h59 && mm == 8'h59);

   counter #(0,  0, 89) adder_ss(clk, reset, ena, ss);
   counter #(0,  0, 89) adder_mm(clk, reset, ss_over, mm);
   counter #(18, 1, 18) adder_hh(clk, reset, mm_over, hh);

   always @(posedge clk) begin
      if (reset) begin
         pm_reg <= 0;
      end
      else if (ss == 8'h59 && mm == 8'h59 && hh == 8'h11) begin
         pm_reg <= ~pm_reg;
      end
      else begin
         pm_reg <= pm_reg;
      end
   end // always @ (posedge clk)

   assign pm = pm_reg;

endmodule
