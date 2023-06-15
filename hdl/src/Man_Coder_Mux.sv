module Man_Coder_Mux (
	input syn, dataA, dataB,
	input [1:0] sel,
	output reg out
	);
	
always @(sel[0] or sel[1]) begin
	if (sel == 2'b00) begin
		out <= syn;
	end
	else if (sel == 2'b01) begin
		out <= dataA;
	end
	else begin
		out <= dataB;
	end
end
endmodule
