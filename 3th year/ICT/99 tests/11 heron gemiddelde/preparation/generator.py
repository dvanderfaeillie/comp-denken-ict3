import os
import random
import subprocess
from typing import Text

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# configuration settings
tab_name = 'Feedback'
settings = f'''
tab name: {tab_name}
python input without prompt: true
block count: multi
input block size: 2
output block size: ends with
comparison: exact match
'''

# generate test data
ntests= 20
cases = [(4,25), (0,3) ]
while len(cases) < ntests:
    a = random.randint( 0, 15 )
    b = random.randint( 0, 15 )
    cases.append( (a, b) )

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w')
outfile = open(os.path.join(evaldir, '0.out'), 'w')

# generate unit tests
for stdin in cases:

    # add input to input file
    stdin = '\n'.join(f'{line}' for line in stdin)
    print(stdin, file=infile)

    # generate output to output file
    script = os.path.join(solutiondir, 'solution.nl.py')
    process= subprocess.run(
        ['python', script],
        input=stdin,
        encoding='utf-8',
        capture_output=True
    )
    
    result_lines = process.stdout.split("\n")
    for line in result_lines:
        if not(line.startswith( 'Geef' )):
            print(line)
            print(line, file=outfile)

    # add stdout to output file
    # print(process.stdout, file=outfile, end='')

# add settings to output file
print('-' * 41 + settings, file=outfile, end='')
