""" This will parse the data from the unix command echo "Header1 is this~Header2 and that~~Data 1.0~Data 2.0" | tr "~" "\n"
which is:
Header1 is this
Header2 and that

Data 1.0
Data 2.0
"""

tokens = ('CODE', )
# Add in remaining building codes from http://www.utexas.edu/maps/main/buildings/
campus_buildings = {'BAT' : 'Batts Hall', 'CBA' : 'McCombs School of Business', 'CAL' : 'Calhoun Hall', 'GDC' : 'Gates Dell Complex'}

# Tokens
# Use these regular expressions. If input matches this, turn all of it into the specified token
t_CODE  = r'^[A-Za-z]{3}' # A valid building code is 3 letters (case insensitive)

# Ignored characters
t_ignore = " \r\n"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex   # ply.lex comes from the ply folder in the PLY download.
lexer = lex.lex() # PLY looks at everything above this and creates a lexer for you

# Parsing rules

global time_step
time_step = 0

def p_start(t):
    '''start : code
    '''

def p_code(t):
    'code : CODE'
    print("Building code " +  t[1] + " is " + campus_buildings[t[1].upper()])

def p_error(t):
    if t == None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc   # ply.yacc comes from the ply folder in the PLY download.
parser = yacc.yacc()

while True:
    try:
        s = raw_input('')
    except EOFError:
        break
    parser.parse(s)

# To run the parser do the following in a terminal window: echo "CBA~CAL" | tr "~" "\n" | grep -v '^\s*$' | python PLYlookup.py
