//------------------------------------------------------
// author:	Boris Belykh
// email:	belyh.ba@spbstu.ru
// project: 	manchester
//------------------------------------------------------
// Time Division Multiplexing for Manchester Encoder (differnetial), testbench
//------------------------------------------------------
`timescale 1ns/1ns
module tb_diff_tdm();
bit tb_ena, tb_rst, tb_a, tb_b, tb_m;
int data;

initial begin
	tb_ena = 1'b0; //0?
	while (1) #10 tb_ena = ~tb_ena;
end

initial begin
    tb_rst = 0;
    #1 tb_rst = 1;
    #3000 tb_rst = 0;
end

diff_tdm tdm_inst(
	.clk(tb_ena),
    .rst(tb_rst),
	.a(tb_a),
	.b(tb_b),
    .m(tb_m)
);

initial begin
	data = $fopen("tb_diff_TDM.dat", "w");
    while (1) #1 $fdisplay(data,
	"time=%1t tb_a=%b tb_b=%b tb_m=%b",
	$time, tb_a, tb_b, tb_m);
end

initial begin
	tb_a = 0;
	#120 tb_a = 1;
	#120 tb_a = 0;
	#120 tb_a = 1;
	#120 tb_a = 0;
	#120 tb_a = 1;
	#120 tb_a = 0;
	#720 tb_a = 1;
	#720 tb_a = 0;
	#120 tb_a = 1;
	#240 tb_a = 0;
	#150 $fclose(data); $stop;
end

initial begin
	tb_b = 1;
	#120 tb_b = 0;
	#120 tb_b = 1;
	#120 tb_b = 0;
	#120 tb_b = 1;
	#120 tb_b = 0;
	#120 tb_b = 1;
	#720 tb_b = 0;
	#720 tb_b = 1;
	#120 tb_b = 0;
	#240 tb_b = 1;
	#150 $stop;
end

endmodule