import tkinter as tk
from tkinter.filedialog import askopenfilename
import random

print('Select a file you want mixed')
print('Remember to stick to the syntax!')

root = tk.Tk()
root.withdraw()
filename = askopenfilename()

lines = []
shell = []

with open(filename) as infile:
    for line in infile:
        line = line.strip()
        if line == '--BREAK--':
            shell.append(lines)
            lines = []
        else:
            lines.append(line + '\n')
            random.shuffle(lines)

with open('output.txt', 'w') as outfile:
    for n in shell:
        outfile.writelines(n)
        outfile.write('--BREAK--' + '\n')

print('all done!')
