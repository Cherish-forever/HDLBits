module top_module ( );

   reg clk;

   initial begin
      clk = 0;
   end

   always #5 clk = ~clk;

   dut dut1(clk);

endmodule
