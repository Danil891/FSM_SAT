`timescale 1ns/1ps

module tb_Man_Coder_Thomas();

logic dataA, dataB, clk, reset;

logic out_top, out_top_2, out_top_3, out_a, out_b, out_pin_1, out_pin_2, out_pin_3;

//bit test_in [0:22];

//int i;

Man_Coder_Top_ModelSim Man_Coder_Top_ModelSim_inst(.*);

always #10 clk = ~clk;
	
//initial begin
	//$readmemh("test_in.txt", test_in);
//end

initial begin
	#0
	clk = 0;
	reset = 1;
	dataA = 0;
	#0
	dataB = 1;
	#5
	reset = 0;
	#120
	dataA = 0;
	#120
	dataB = 1;
	#120
	dataA = 0;
	#120
	dataB = 1;
	#120
	dataA = 0;
	#120
	dataB = 0;
	#120
	dataA = 0;
	#120
	dataB = 0;
	#120
	dataA = 0;
	#120
	dataB = 0;
	#120
	dataA = 1;
	#120
	dataB = 1;
	#120
	dataA = 1;
	#120
	dataB = 1;
	#120
	dataA = 1;
	#120
	dataB = 1;
	#120
	dataA = 0;
	#120
	dataB = 1;
	#120
	dataA = 1;
	#120
	dataB = 0;
	//for (i = 0; i < 23; i ++) begin
		//data = test_in[i];
	//end
	#1500 $stop;
end

endmodule 