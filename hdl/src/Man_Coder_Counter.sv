module Man_Coder_Counter
#(parameter N = 2)
(
	input clk, reset,
	output reg [N-1:0] out,
	output reg syn
	);
always @(negedge clk) begin
	if (reset) begin
		out <= 2'b0;
		syn <= 1'b0;
	end
	else if (out <= N - 1) begin
		out <= out + 1'b1;
	end
	else begin
		out <= 2'b0;
		syn <= ~syn;
	end
end
endmodule	