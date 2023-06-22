transcript on

vlib work

vlog -sv +incdir+./ ./src/diffManch.sv
vlog -sv +incdir+./ ./src/diff_cnt_div.sv
vlog -sv +incdir+./ ./src/diff_tdm.sv
vlog -sv +incdir+./ ./tb/tb_diff_tdm.sv

vsim -t 1ns -voptargs="+acc" tb_diff_tdm

add wave tb_ena
add wave tdm_inst/clk2
add wave tdm_inst/clk6
add wave tb_rst
add wave tdm_inst/sel
add wave tdm_inst/syn
add wave tb_a
add wave tb_b
add wave tdm_inst/y
add wave tb_m

run -all
wave zoom full
