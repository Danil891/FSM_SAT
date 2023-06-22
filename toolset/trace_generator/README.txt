How to run:

Put three (a, b, m) .csv files or one .dat file to folder input/
For testing purposes input/ contains files TRC01.CSV, TRC02.CSV, TRC03.CSV, a, b, m, tb_diff_TDM.dat

Open CMD

Browse: [...]\trace_generator

For .csv files: java -jar trace_generator.jar csv [file name for a] [file name for b] [file name for m]
For .dat files: java -jar trace_generator.jar dat [file name]

TIP: You may not write the file names with their extension.
Example1: java -jar trace_generator.jar csv a b m
Example2: java -jar trace_generator.jar dat tb_diff_TDM

Check the folder output_trace/ and see the formed_trace.txt file
You can compare it with the input (analog_waveform.txt, created only for csv input) and its binary form (digital_waveform.txt)

