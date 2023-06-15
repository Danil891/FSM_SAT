module divider_by_16 (
    clk_in, reset, clk_out
);

input clk_in, reset;
output clk_out;

reg [3:0] pos_cnt;
reg [3:0] neg_cnt;

always @ (posedge clk_in)
if (reset) begin
             pos_cnt <= 0;
            end else begin
                          pos_cnt <= (pos_cnt == 15) ? 0 : pos_cnt + 1;
                          end

always @ (negedge clk_in)
if (reset) begin
              neg_cnt <= 0;
              end else begin
                            neg_cnt <= (neg_cnt == 15) ? 0 : neg_cnt + 1;
                            end
assign clk_out = !((pos_cnt != 15) && (neg_cnt != 15));
endmodule
