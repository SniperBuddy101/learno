import sys
import os
import subprocess

if len(sys.argv) == 1:
    print("Enter an argument")

runner = subprocess.run(["ls"], capture_output=True, text=True, check=True)

print("stdout: ", runner.stdout)
print("stderr: ", runner.stderr)
print("returncode: ", runner.returncode)
print("args: ", runner.args)
