//------------------------------------------------------
// author:	Boris Belykh
// email:	belyh.ba@spbstu.ru
// project: 	manchester
//------------------------------------------------------
// Time Division Multiplexing for Manchester Encoder (differnetial)
//------------------------------------------------------

`timescale 1ns/1ns
module diff_tdm (
    rst, clk, a, b, m
);

input rst, clk, a, b;
output m;
reg y;
wire [2:0] sel, syn;
wire clk2, clk6;

diff_cnt_div #(2) cnt_div_2 ( // Makes clk2 = 1 every 2 clk cycles
    .clk(clk),
    .reset(rst),
    .q_cout(clk2) // Frequency of clk2 is clk / 2
);

diff_cnt_div #(6) cnt_div_6 ( // Makes clk6 = 1 every 6 clk cycles
    .clk(clk),
    .reset(rst),
    .q_cout(clk6) // Frequency of clk6 is clk / 6
);

diff_cnt_div #(3) cnt2_inst_1 ( // Assigns new value to sel every clk2 (two clk cycles)
    .clk(clk2),
    .reset(rst),
    .q(sel) // sel = 0 || sel = 1 || sel = 3
);

diff_cnt_div #(2) cnt2_inst_2 ( // Assigns new value to syn every clk6 (six clk cycles)
    .clk(clk6),
    .reset(rst),
    .q(syn) // syn = 0 || syn = 1
);

diffManch manchester_inst ( 
    .clk(clk),
    .rst(rst),
    .d(y), 
    .q(m) // y encoded to differential Manchester code
);

always_ff @(posedge clk2, negedge rst) begin
    if (~rst) begin
        y <= 1'b0;
    end
    else
        case(sel) // mux with data inputs syn, a, b; select input sel; data output y
            2'b001: y <= a;
            2'b010: y <= b;
            default: y <=  syn[0:0];
        endcase
end
endmodule