import os
import contextlib, io
import importlib
import random
import ruamel.yaml

yaml = ruamel.yaml.YAML()

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

# load functionality defined in sample solution
module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.nl.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def write_yaml( data:list ):
    """ A function to write YAML file"""
    with open(os.path.join('..', 'evaluation', 'tests.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(data, f)

# generate test data
ntests= 20
cases = [ [[4,3,1,2], 
          [-1,0,3,4], 
          [0,4,2,1] ],
         [[9, 4], 
          [9, -2],
          [-3, 9]],
         [[0, -1, -3, -1], 
          [-1, -1, -2, 0]],
         [[-3, 4, 4, 2, -3, -3]],
         [[-3, -1, -1, -7]]]

while len( cases ) < ntests:
    nrow = random.randint(1,6)
    ncol = random.randint(1,6)
    m = []
    for _ in range( nrow ):
        row = []
        for _ in range( ncol ):
            row.append(random.randint( -5, 5 ))
        m.append( row )
    cases.append( m )

# generate unit tests for functions
yamldata = []
yamldata.append( {'tab': 'Feedback', 'testcases': []})
# input, expression, statement or stdin?
input = 'expression'
# output, stdout or return?
output = 'stdout'
for test in cases:
    # generate test expression
    expression_name = 'aantal_max( {} )'.format( test )
    
    f = io.StringIO()
    with contextlib.redirect_stdout( f ):
        module.aantal_max( test )
    
    result = f.getvalue().strip() 
    
    # setup for return expressions
    testcase = { input: expression_name, output: ''+ result }
    yamldata[0]['testcases'].append( testcase )

write_yaml(yamldata)