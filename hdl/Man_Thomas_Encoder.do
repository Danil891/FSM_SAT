transcript on

vlib work

vlog -sv +incdir+./ ./src/Man_Coder_Thomas.sv
vlog -sv +incdir+./ ./src/Man_Coder_Mux.sv
vlog -sv +incdir+./ ./src/Man_Coder_Counter.sv
vlog -sv +incdir+./ ./src/Man_Coder_Top_ModelSim.sv
vlog -sv +incdir+./ ./src/Man_Coder_IEEE.sv
vlog -sv +incdir+./ ./src/diffManch.sv
vlog -sv +incdir+./ ./tb/tb_Man_Coder_Thomas.sv

vsim -t 1ns -voptargs="+acc" tb_Man_Coder_Thomas

add wave dataA
add wave dataB
add wave clk
add wave reset
add wave out_top
add wave out_top_2
add wave out_top_3
add wave out_a
add wave out_b
add wave out_pin_1
add wave out_pin_2
add wave out_pin_3

run -all
wave zoom full
