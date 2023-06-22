transcript on

vlib work

vlog -sv +incdir+./ ./src/diffManch.sv
vlog -sv +incdir+./ ./tb/tb_diffManch.sv

vsim -t 1ns -voptargs="+acc" tb_diffManch

add wave tb_clk
add wave tb_rst
add wave tb_d
add wave tb_q
run -all
wave zoom full
