
# -----------------------------------------------------------------
# Project settings
# -----------------------------------------------------------------
#

set_device -name "GW2A-55C" "GW2A-LV55PG484C8/I7"

set_option -output_base_name "manchester"
set_option -top_module "Man_Coder_Top"
set_option -verilog_std "sysv2017"
set_option -use_sspi_as_gpio 1

add_file -type cst "./src/Man_Code_Thomas.cst"
add_file -type sdc "./src/Man_Code_Thomas.sdc"
add_file -type verilog "./src/diffManch.sv"
add_file -type verilog "./src/Man_Coder_Counter.sv"
add_file -type verilog "./src/Man_Coder_IEEE.sv"
add_file -type verilog "./src/Man_Coder_Mux.sv"
add_file -type verilog "./src/Man_Coder_Thomas.sv"
add_file -type verilog "./src/divider_by_16.sv"
add_file -type verilog "./src/Man_Coder_Top.sv"


run all
