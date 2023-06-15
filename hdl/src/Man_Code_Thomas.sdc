//Copyright (C)2014-2022 GOWIN Semiconductor Corporation.
//All rights reserved.
//File Title: Timing Constraints file
//GOWIN Version: 1.9.8.06-1 
//Created Time: 2022-07-01 14:59:18
create_clock -name clk -period 20 -waveform {0 10} [get_ports {clk}]
