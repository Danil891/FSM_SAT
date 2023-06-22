import subprocess
import os
import shutil

shutil.copy('trace_generator/output_trace/formed_trace.txt', 'SAT_invocator/formed_trace.txt')

os.chdir('SAT_invocator')
subprocess.Popen("python main2.py", shell=True)
os.chdir('../')

shutil.copy('SAT_invocator/sat_to_genFSM.txt', 'FSM_generator/input.txt')

os.chdir('FSM_generator')
subprocess.Popen("python main.py", shell=True)
os.chdir('../')
