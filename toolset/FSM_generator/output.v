module Moore2
(
	input wire clk, reset, 
	input wire [2:0] in,
	output reg [2:0] out
);
localparam [3:0]
	s0 = 0,
	s1 = 1,
	s2 = 2,
	s3 = 4,
	s4 = 4,
	s5 = 6,
	s5 = 7;

	 reg[4:0] state_reg, state_next;
always @(posedge clk, posedge reset) begin
	 if (reset) begin
		 state_reg <= s0
	end
	 else begin
		 state_reg <= state_next;
	end
end

always @(in, state_reg) begin
	state_next = state_reg;
	case (state_reg)
		s0 : begin
			out = 'b0;
			if (in == 'b010) begin
				 state_next = s0;
			end
			if (in == 'b011) begin
				 state_next = s1;
			end
			else if (in == 'b000) begin
				 state_next = s2;
			end
			else if (in == 'b001) begin
				 state_next = s3;
			end
			else begin
				 state_next = s0;
			end
		end
		s1 : begin
			out = 'b1;
			if (in == 'b000) begin
				 state_next = s0;
			end
			else if (in == 'b110) begin
				 state_next = s3;
			end
			else if (in == 'b101) begin
				 state_next = s2;
			end
			else if (in == 'b100) begin
				 state_next = s5;
			end
			else begin
				 state_next = s1;
			end
		end
		s2 : begin
			out = 'b10;
			if (in == 'b011) begin
				 state_next = s2;
			end
			if (in == 'b100) begin
				 state_next = s5;
			end
			if (in == 'b110) begin
				 state_next = s3;
			end
			else if (in == 'b100) begin
				 state_next = s1;
			end
			else if (in == 'b001) begin
				 state_next = s4;
			end
			else begin
				 state_next = s2;
			end
		end
		s3 : begin
			out = 'b11;
			if (in == 'b110) begin
				 state_next = s5;
			end
			if (in == 'b000) begin
				 state_next = s2;
			end
			if (in == 'b100) begin
				 state_next = s6;
			end
			else if (in == 'b001) begin
				 state_next = s4;
			end
			else begin
				 state_next = s3;
			end
		end
		s4 : begin
			out = 'b100;
			if (in == 'b110) begin
				 state_next = s5;
			end
			if (in == 'b000) begin
				 state_next = s2;
			end
			if (in == 'b100) begin
				 state_next = s6;
			end
			else if (in == 'b001) begin
				 state_next = s4;
			end
			else begin
				 state_next = s4;
			end
		end
        s5 : begin
			out = 'b101;
			if (in == 'b010) begin
				 state_next = s2;
			end
			if (in == 'b000) begin
				 state_next = s6;
			end
			if (in == 'b011) begin
				 state_next = s4;
			end
			else begin
				 state_next = s5;
			end
		end
		s6 : begin
			out = 'b110;
			if (in == 'b010) begin
				 state_next = s4;
			end
			if (in == 'b011) begin
				 state_next = s1;
			end
			if (in == 'b000) begin
				 state_next = s2;
			end
			if (in == 'b001) begin
				 state_next = s5;
			end
			else begin
				 state_next = s2;
			end
		end
	endcase
end

endmodule
