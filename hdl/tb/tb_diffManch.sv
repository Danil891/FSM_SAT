//------------------------------------------------------
// author:	Boris Belykh
// email:	belyh.ba@spbstu.ru
// project: 	manchester
//------------------------------------------------------
// Manchester Encoder (differnetial), testbench
//------------------------------------------------------
`timescale 1ns/1ns
module tb_diffManch();
bit tb_clk, tb_d, tb_q, tb_rst;

initial begin
	tb_clk = 1'b0; //0?
	while (1) #10 tb_clk = ~tb_clk;
end

initial begin
    tb_rst = 0;
    #1 tb_rst = 1;
    #900 tb_rst = 0;
end

diffManch man_inst(
	.clk(tb_clk),
    .rst(tb_rst),
	.d(tb_d),
	.q(tb_q)
);

initial begin
	tb_d = 0;
	#40 tb_d = 1;
	#40 tb_d = 0;
	#40 tb_d = 1;
	#40 tb_d = 0;
	#40 tb_d = 1;
	#40 tb_d = 0;
	#240 tb_d = 1;
	#240 tb_d = 0;
	#40 tb_d = 1;
	#80 tb_d = 0;
	#50 $stop;
end

endmodule