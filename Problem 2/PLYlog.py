'''
Purpose: to parse a server log file and print out any entries with error code 4xx (client error) or 5xx (server error)
    A full list of error codes can be found at: http://www.restapitutorial.com/httpstatuscodes.html
'''

# To run this program, enter the following in Terminal: cat plyParserInputs/serverlog.out | python PLYlog.py

tokens = ('IP', 'DATE', 'TIME', 'COMMAND', 'CODE' )
literals = ['-', ]

# Tokens
t_IP  = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' # Example: 192.168.1.154
t_DATE = r'[0-9]{2}\/[A-Za-z]{3}\/[0-9]{4}' # Example: 07/Mar/2004
t_TIME = r'[0-9]{2}:[0-9]{2}:[0-9]{2}' # Example: 16:23:56
t_COMMAND = r'\".*\"' # Example: "GET /twiki/bin/edit/Main/Double_bounce_sender?topicparent=Main.ConfigurationVariables HTTP/1.1"
t_CODE = r'[0-9]{3}' # Example: 404

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
lexer = lex.lex()

# Parsing rules

global time_step
time_step = 0

def p_start(t):
    '''start : line
    '''

def p_line(t):
    'line : IP "-" "-" DATE TIME COMMAND CODE'
    t[0] = str(t[1]) + " " + str(t[4]) + " " + str(t[5]) + " " + str(t[6]) + " " + str(t[7])
    if (str(t[7])[0] == "4") or (str(t[7][0]) == "5"): # Client or Server error code
        print t[0] + "\n"

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