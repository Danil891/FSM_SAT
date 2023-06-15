import subprocess
import os
import shutil

os.chdir('trace_generator')
subprocess.call(['java', '-jar', 'trace_generator.jar', 'dat', 'tb_diff_TDM'])
os.chdir('../')

shutil.copy('trace_generator/output_trace/formed_trace.txt', 'SAT_invocator/formed_trace.txt')

os.chdir('SAT_invocator')
subprocess.Popen("python main.py", shell=True)
os.chdir('../')

shutil.copy('SAT_invocator/sat_to_genFSM.txt', 'FSM_generator/input.txt')

os.chdir('FSM_generator')
subprocess.Popen("python main.py", shell=True)
os.chdir('../')
