module Moore2
(
	input wire clk, reset, 
	input wire [1:0] in,
	output reg [1:0] out 
);
localparam [3:0]
	s0 = 0,
	s1 = 1,
	s2 = 2;

	 reg[4:0] state_reg, state_next;
always @(posedge clk, posedge reset) begin
	 if (reset) begin
		 state_reg <= s1
	end
	 else begin
		 state_reg <= state_next;
	end
end

always @(in, state_reg) begin
	state_next = state_reg;
	case (state_reg)
		s0 : begin
			out = 'b1;
			if (in == 'b0) begin
				 state_next = s1;
			end
			else if (in == 'b10) begin
				 state_next = s2;
			end
			else begin
				 state_next = s0;
			end
		end
		s1 : begin
			out = 'b0;
			if (in == 'b11) begin
				 state_next = s1;
			end
			else if (in == 'b10) begin
				 state_next = s2;
			end
			else begin
				 state_next = s1;
			end
		end
		s2 : begin
			out = 'b0;
			if (in == 'b0) begin
				 state_next = s0;
			end
			if (in == 'b11) begin
				 state_next = s0;
			end
			else begin
				 state_next = s2;
			end
		end
	endcase
end

endmodule
