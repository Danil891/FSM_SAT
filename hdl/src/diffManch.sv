//------------------------------------------------------
// author:	Boris Belykh
// email:	belyh.ba@spbstu.ru
// project: 	manchester
//------------------------------------------------------
// Manchester Encoder (differnetial)
//------------------------------------------------------

module diffManch (
	clk, rst, d, q
);

input clk, rst;
input d;
output reg q;

reg odd;

always_ff @(posedge clk, negedge rst) begin
    if (~rst) begin // Needs to be reset to start working
        q <= 0;
        odd <= 0;
    end
    else begin 
        if (~d || odd)
            q <= ~q;
        odd <= ~odd;       
    end
end

endmodule
