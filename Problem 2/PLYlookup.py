tokens = ('CODE', )
# Add in remaining building codes from http://www.utexas.edu/maps/main/buildings/
campus_buildings = {'ACA' : 'Academic Annex', 'ADH' : 'Almetris Duren Hall', 'AFP' : 'Athletic Fields Pavilion', 'AHG' : 'Anna Hiss Gymnasium', 'ANB' : 'Arno Nowotny Building', 'AND' : 'Andrews Dormitory', 'ARC' : 'Animal Resources Center', 'ART' : 'Art Building and Museum', 'ATT' : 'AT&T Executive Education and Conference Center',
                    'BAT' : 'Batts Hall', 'BEL' : 'L. Theo Bellmont Hall', 'BEN' : 'Benedict Hall', 'BHD' : 'Brackenridge Hall Dormitory', 'BIO' : 'Biological Laboratories', 'BLD' : 'Blanton Dormitory', 'BMA' : 'Blanton Museum of Art', 'BMC' : 'Belo Center for New Media', 'BME' : 'Biomedical Engineering Building', 'BOT' : 'Biological Greenhouse', 'BRB' : 'Bernard and Audre Rapoport Building', 'BRG' : 'Brazos Garage', 'BTL' : 'Battle Hall', 'BUR' : 'Burdine Hall', 'BWY' : '2616 Wichita',
                    'CAL' : 'Calhoun Hall', 'CBA' : 'McCombs School of Business', 'CCG' : 'Conference Center Garage', 'CCJ' : 'John B. Connally Center for Justice', 'CDA' : 'Comal Child Development Center Annex', 'CDL' : 'Collections Deposit Library', 'CEE' : 'Continuing Engineering Education', 'CCF' : 'Caven Lacrosse and Sports Center at Clark Field', 'CLA' : 'Liberal Arts Building', 'CLK' : 'Caven Clark Field Support Building', 'CMA' : 'Jesse H. Jones Communication Center - Building A',
                    'CMB' : 'Jesse H. Jones Communication Center - Building B', 'CML' : '	Child Development Center', 'COM' : 'Computation Center', 'CPE' : 'Chemical and Petroleum Engineering Building', 'CRB' : 'Computational Resource Building', 'CRD' : 'Carothers Dormitory', 'CRH' : 'Creekside Residence Hall', 'CS3' : 'Chilling Station No. 3', 'CS4' : 'Chilling Station No. 4', 'CS5' : 'Chilling Station No. 5',
                    'DEV' : 'Development Office Building', 'DCP' : 'Denton A. Cooley Pavilion', 'DFA' : 'E. William Doty Fine Arts Building', 'DFF' : '	UFCU Disch-Falk Field',
                    'EAS' : 'Edgar A. Smith Building', 'ECJ' : 'Ernest Cockrell Jr. Hall', 'ENS' : 'Engineering-Science Building', 'EPS' : 'E. P. Schoch Building', 'ERC' : 'Frank C. Erwin Jr. Special Events Center', 'ESS' : 'Engineering Student Services Building', 'ETC' : 'Engineering Teaching Center II',
                    'FAC' : 'Peter T. Flawn Academic Center', 'FC1' : 'Facilities Complex Building 1', 'FC2' : 'Facilities Complex Building 2', 'FC3' : 'Facilities Complex Building 3', 'FC4' : 'Facilities Complex Building 4', 'FC5' : 'Facilities Complex Building 5', 'FC6' : 'Facilities Complex Building 6', 'FC7' : 'Facilities Complex Building 7', 'FC8' : 'Facilities Complex Building 8', 'FDF' : 'Frank Denius Fields', 'FDH' : 'J. Frank Dobie House', 'FNT' : 'Larry R. Faulkner Nano Science and Technology Building', 'FPC' : 'OFPC Field Staff Office',
                    'GAR' : 'Garrison Hall', 'GDC' : 'Gates Dell Complex', 'GEA' : 'Mary E. Gearing Hall', 'GEB' : 'Dorothy L. Gebauer Building', 'GOL' : 'Goldsmith Hall', 'GRE' : 'Gregory Gymnasium', 'GSB' : 'Graduate School of Business Building', 'GUG' : 'UT Administration Parking Garage', 'GWB' : 'Gordon-White Building',
                    'HMA' : 'Hogg Memorial Auditorium', 'HRC' : 'Harry Ransom Center', 'HRH' : 'Homer Rainey Hall', 'HSM' : '	William Randolph Hearst Building',
                    'INT' : 'International Office', 'IPF' : 'Indoor Practice Facility',
                    'JCD' : 'Jester Dormitory', 'JES' : 'Beauford H. Jester Center', 'JGB' : 'Jackson Geological Sciences Building', 'JHH' : 'John W. Hargis Hall', 'JON' : 'Jesse H. Jones Hall',
                    'KIN' : 'Kinsolving Dormitory',
                    'LBJ' : 'Lyndon B. Johnson Library', 'LCH' : 'Littlefield Carriage House', 'LDH' : 'Longhorn Dining Facility', 'LFH' : 'Littlefield Home', 'LLA' : 'LLA Living Learning Center', 'LLB' : 'LLB Living Learning Center', 'LLC' : 'LLC Living Learning Center', 'LLD' : 'LLD Living Learning Center', 'LLE' : 'LLE Living Learning Center', 'LLF' : 'LLF Living Learning Center', 'LTD' : 'Littlefield Dormitory', 'LTH' : 'Laboratory Theater Building',
                    'MAG' : 'Manor Garage', 'MAI' : 'Main Building', 'MBB' : 'Louise and James Robert Moffett Molecular Biology Building', 'MEZ' : 'Mezes Hall', 'MFH' : 'Richard Mithoff Track and Soccer Fieldhouse', 'MHD' : 'Moore-Hill Dormitory', 'MMS' : 'Mike A. Myers Track and Soccer Stadium', 'MNC' :'Moncrief-Neuhaus Athletics Center', 'MRH' : 'Music Building East and Music Building/Recital Hall', 'MSB' : 'Mail Services Building',
                    'NEZ' : 'North End Zone', 'NHB' : 'Norman Hackerman Building', 'NMS' : 'Neural Molecular Science Building', 'NOA' : 'North Office Building A', 'NUR' : 'Nursing School',
                    'PAC' : 'Performing Arts Center', 'PAI' : 'T. S. Painter Hall', 'PAR' : 'Parlin Hall', 'PAT' : 'J. T. Patterson Laboratories Building', 'PCL' : 'Perry-Castaneda Library', 'PHD' : 'Prather Hall Dormitory', 'PHR' : 'Pharmacy Building', 'POB' : 'Peter O\'Donnell Jr. Building', 'PPA' : 'Hal C. Weaver Power Plant Annex', 'PPB' : 'Printing and Press Building', 'PPE' : 'Hal C. Weaver Power Plant Expansion', 'PPL' : 'Hal C. Weaver Power Plant'
}
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
