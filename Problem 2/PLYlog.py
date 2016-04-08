tokens = ('IP', 'DATETIME', 'COMMAND', 'VERSION', 'CODE', 'BYTES' )
#literals = ['.',  ]

# Tokens
t_IP  = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
t_DATETIME = r'^[0-9]{2}\/[A-Za-z]{3}\/[0-9]{4}\s[0-9]{2}:[0-9]{2}:[0-9]{2}'
#t_DATE = r'^[0-9]{2}\/[A-Za-z]{3}\/[0-9]{4}'
#t_TIME = r'^[0-9]{2}:[0-9]{2}:[0-9]{2}'
t_COMMAND = r'^\".*\"'
t_VERSION = r'^HTTP\/[0-9].[0-9]'
t_CODE = r'^[0-9]{3}'
t_BYTES = r'^[0-9]{1,5}'

'''def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t'''

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
    '''start : entry
    '''
    print "Saw: ", t[1]

'''def p_datetime(t):
    'datetime : DATE ":" INTEGER ":" INTEGER ":" INTEGER'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7])

def p_time(t):
    'time : INTEGER ":" INTEGER ":" INTEGER'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])'''

'''def p_badRequest(t):
    'badRequest : IP DATETIME CODE'
    if int(t[3]) != 200:
        print "BAD"'''

'''def p_entry(t):
    'entry : IP DATETIME CODE'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])
    if int(t[3]) == 401:
        print "Error found"'''

def p_entry(t):
    'entry : IP CODE'
    t[0] = str(t[1]) + str(t[2])
    if int(t[2]) == 401:
        print "Error found"

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

# To run the parser do the following in a terminal window: echo "Header1 is this~Header2 and that~~Data 1.0~Data 2.0" | tr "~" "\n" | grep -v '^\s*$' | python PLYstarter.py | sed "s/_~_/ which is a float./"
# head -3 mpstat.out | grep -v "^\s*$" | python PLYmpstat.py