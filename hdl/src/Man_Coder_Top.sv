module Man_Coder_Top (
	input dataA, input dataB, input clk, input reset, output out_top, output out_top_2, output out_top_3,
	output out_a, output out_b, output out_pin_1, output out_pin_2, output out_pin_3, output divided_clk);
	wire mux_encoder, div, cnt_syn;
	wire [1:0] cnt_mux;

Man_Coder_Mux coder_mux(.syn (cnt_syn), .dataA (dataA), .dataB (dataB), .sel (cnt_mux), .out (mux_encoder));
Man_Coder_Counter counter(.clk (div), .reset(reset), .out (cnt_mux), .syn(cnt_syn));
Man_Coder_Thomas encoder(.clk (div), .reset(reset), .data (mux_encoder), .out (out_top));
Man_Coder_IEEE ieee_encoder(.clk (div), .reset(reset), .data (mux_encoder), .out (out_top_2));
diffManch diff_encoder(.clk(div), .rst(~reset), .d(mux_encoder), .q(out_top_3));
divider_by_16 divider(.clk_in(clk), .reset(reset), .clk_out(div));
//divider_by_3 div3(.clk_in (clk), .reset(reset), .clk_out(div3_div2));
//divider_by_2 div2(.clk_in (div3_div2), .reset(reset), .clk_out(clk2_syn));
assign out_a = dataA;
assign out_b = dataB;
assign out_pin_1 = out_top;
assign out_pin_2 = out_top_2;
assign out_pin_3 = out_top_3;
assign divided_clk = div;
endmodule
