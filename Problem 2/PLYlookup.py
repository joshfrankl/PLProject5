tokens = ('CODE', )
# Add in remaining building codes from http://www.utexas.edu/maps/main/buildings/
campus_buildings = {'ACA' : 'Academic Annex', 'ADH' : 'Almetris Duren Hall', 'AFP' : 'Athletic Fields Pavilion', 'AHG' : 'Anna Hiss Gymnasium', 'ANB' : 'Arno Nowotny Building', 'AND' : 'Andrews Dormitory', 'ARC' : 'Animal Resources Center', 'ART' : 'Art Building and Museum', 'ATT' : 'AT&T Executive Education and Conference Center',
                    'BAT' : 'Batts Hall', 'BEL' : 'L. Theo Bellmont Hall', 'BEN' : 'Benedict Hall', 'BHD' : 'Brackenridge Hall Dormitory', 'BIO' : 'Biological Laboratories', 'BLD' : 'Blanton Dormitory', 'BMA' : 'Blanton Museum of Art', 'BMC' : 'Belo Center for New Media', 'BME' : 'Biomedical Engineering Building', 'BOT' : 'Biological Greenhouse', 'BRB' : 'Bernard and Audre Rapoport Building', 'BRG' : 'Brazos Garage', 'BTL' : 'Battle Hall', 'BUR' : 'Burdine Hall', 'BWY' : '2616 Wichita',
                    'CAL' : 'Calhoun Hall', 'CBA' : 'McCombs School of Business', 'CCG' : 'Conference Center Garage',
                    'GDC' : 'Gates Dell Complex'}

# Tokens
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
    try:
        print("Building code " +  t[1] + " is " + campus_buildings[t[1].upper()])
    except KeyError:
        print("Building code " + t[1] + " does not exist at the UT campus or is not in the database")

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

# To run the parser do the following in a terminal window: cat plyParserInputs/parser.out | python PLYlookup.py
