//------------------------------------------------------
// author:	Boris Belykh
// email:	belyh.ba@spbstu.ru
// project: 	manchester
//------------------------------------------------------
// Counter from 0 to div-1 with Cout signal
//------------------------------------------------------

module diff_cnt_div
 #(parameter div = 2)
(input clk,
 input reset,
 output [2:0] q, 
output q_cout );	

reg [2:0] cnt;
reg cout;
wire cycle;

always_ff @(posedge clk, negedge reset)
	if (~reset | cycle) 
		cnt <= 0;
	else 
		cnt <= cnt + 1'b1;

assign cycle = (cnt == (div-1));

always_ff @(posedge clk, negedge reset)
	if (~reset) 
		cout <= 1'b0;
	else 
		if (cycle)
			cout <= 1'b1;
		else
			cout <= 1'b0;

assign q_cout = cout;
assign q = cnt;

endmodule

