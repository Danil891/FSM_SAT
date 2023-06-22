module Man_Coder_Thomas (
	input clk, reset, data,
	output logic out
);

logic inner_clk;
always_ff @(negedge clk) begin
	if (reset) begin
		out <= 1'b0;
        inner_clk <= 1'b0;
	end
	else begin
        if (inner_clk ^ data) begin
            out <= 1'b1;
        end
        else begin
            out <= 1'b0;
        end
        inner_clk <= ~inner_clk;
    end
end

endmodule
