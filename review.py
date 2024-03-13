#GIATSOS GEORGIOS 3202 


import sys, re, os  

from collections import OrderedDict

progtk = 'program'
idtk = ''
leftCurlyBrackettk = '{'
rightCurlyBrackettk = '}'
leftRoundBrackettk = '('
rightRoundBrackettk = ')'
leftBoxBrackettk = '['
rightBoxBrackettk = ']'
declaretk = 'declare'
notdeclaretk = 'notdeclare'
greekqmtk = ';'
functiontk = 'function'
proceduretk = 'procedure'
formalparstk = 'formalist'
definetk = ':='
formalparitemtk = 'formalparitem'
intk = 'in'
inouttk = 'inout'
assignmenttk = 'assignment'
calltk = 'call'
printtk = 'print'
inputtk = 'input'
iftk = 'if'
thentk = 'then'
elsetk = 'else'
whiletk = 'while'
doublewhiletk = 'doublewhiletk'
looptk = 'loop'
exittk = 'exit'
actualparitemtk = 'actualparitem'
booltermtk = 'booleterm'
ortk = 'or'
andtk = 'and'
forcasetk = 'forcase'
updowntk = ':'
defaulttk = 'default'
incasetk = 'incase'
reutnrtk = 'return'
boolfactortk = 'boolfactor'
whentk = 'when'
nottk = 'not'
addopertk = 'addo-oper'
termtk = 'term'
mulopertk = 'mul-oper'
factortk = 'factor'
equaltk = '='
minequaltk = '<='
maxequaltk = '>='
mintk = '<'
maxtk = '>'
minmaxtk = '<>'
plustk = '+'
minustk = '-'
multtk = '*'
devidetk = '/'
komatk = ','

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=[0,1,2,3,4,5,6,7,8,9]
math_symbols=['+','-','*','/']
relations=['<','>','=','<=','>=','<>']
delimeters=[';',',',':']
operators=['(',')','{','}','[',']']
comments=['/*','*/','//']
commited_words=['program','declare','function','procedure','in','inout','if','else','while','doublewhile','loop','exit','forcase','incase','when','default','not','and','or','call','return','input','print']

math_operations = ('add', 'sub', 'mul', 'div')
branches = ('beq', 'bne', 'blt', 'ble', 'bgt', 'bge')


#useful globals
lextotokens = []
InterCarray = []
scope_count = 0
scope_array = [] 
mainframelength=-1
nextquad = 0  
vartemp = dict() 
nextvartemp = 1

quads = []
counterformips = 0


counter=0
tokens = []
string = []
L_counter=0
lines_counter = 0
token_index = 0

last_token = []
quads_inside_block=[] #used for putting quads from a block in function:from_quad_to_assembly
flag_while = 0 # gia emfwleumenes while
flag_if = 0 # gia emfwleumenes if
flag_dowhile = 0  # gia emfwleumenes dowhile
flag_loop = 0 # gia emfwleumenes loop
flag_forcase = 0  # gia emfwleumenes forcase
flag_incase = 0 # gia emfwleumenes incase
flag_function = 0 # gia emfwleumenes function
default_flag=0
number_of_functions_mips=0; #counter gia na auksanoume ton arithmo twn function ston assembly
function_name=[]



def changed_lines():

  char_c = 0 # metrhths gia ton pinaka char_p
  char_p = [] # pinakas poy periexei ton arithmo twn grammatwn apo ka8e grammh toyu pinaka string

  global last_token 

  for i in string:
    for x in i:
      if x != ' ':
        char_c+=1
    char_p.append(char_c)
    char_c=0
  
  met = 0 # topikos athroisths gia ta tokens
  counter = 0 # metrhths gai ton pinaka char_p
  thesh = -1 # metrhths gia na 3eroume se poio token briskomaste
 
  for i in tokens:
    while char_p[counter] == 0:  # periptwsh poy exoume sunexwmena kena
      if counter == len(char_p)-1: # periptwsh pou eimaste sto teleutaio token
        thesh+=1
        last_token.append(thesh)
        break
      counter+=1
    thesh+=1
    met+=len(i[1])
    if met < char_p[counter]:
      continue
    elif met == char_p[counter]:
      last_token.append(thesh)
      counter+=1
      met = 0

 
  #print (tokens)
  #print(last_token)

    

def main():
    global default_flag
    content = ""
    "Press 1 if you want to put a specific input file else will read text.stl files"
    default_flag=1
    if len(sys.argv)<2:
        print('Please put file name')
    if sys.argv[1][-4:]!='.stl':
        print('wrong file type,expected .stl')
    with open(sys.argv[1], 'r') as file:
        content = file.read() 
   

    lex=Lexer(content) 
    tokens=lex.tokenize()

    changed_lines()

    syntax(tokens)
    create_int_file()
    create_c_code_file()
    main()





class Scope:

    def _init_(self, nestlvl=0, enclosescope = None):
        global scope_count
        self.scope_count = scope_count
        self.entities=[]
        self.nestlvl=nested_level 
        self.enclosescope = enclosescope
        self.temp_offset = 12

    def addEntity(self,entity):
      self.entities.append(entity)


    def getOffset(self):
        self.temp_offset+=4
        return (self.tmp_offset-4)


    def _str_(self):
        return self._repr_() + ': (' + str(self.nestlvl) + ', ' + self.enclosescope._repr_() + ')'
        


class Argument():

    def _init_(self, partype, next_arg = None):
        self.partype = partype
        self.next_arg = next_arg


    def setnext(self,next_arg):
        self.next_arg = next_arg

    def _str_(self):
        return self._repr_() + ': (' + self.parMode + ',\t' + self.next_argument.__repr__() + ')'



class Entity():

    def _init_(self,name, elemtype):
        self.name = name
        self.elemtype = elemtype
        self.next = None


    def _str_(self):
        return self.elemtype + ': ' + self.name



class Variable(Entity):

    def _init_(self, name, offset=-1):
        super()._init_(name,"VARIABLE")
        self.offset = offset


    def _str_(self):
        return super()._str_() + ', Offset: ' + str(self.offset)


class Function(Entity):

    def _init_(self, name, startquad=-1):
        super()._init_(name,"FUNCTION")
        self.startquad = startquad
        self.arguments = []
        self.framelength=-1


    def add_arguments(self,arg):
        self.arguments.append(arg)


    def setframelength(self,framelength):
        self.framelength = framelength


    def setstartquad(self, startquad):
        self.startquad = startquad


    def _str_(self):
        return super()._str_() + ', startquad: ' + str(self.startquad) + ', framelength: ' +str(self.frame_length)



class TempVariable(Entity):


    def _init_(self, name, offset=-1):
        super()._init_(name,"TEMPVAR")
        self.offset = offset


    def _str_(self):
        return super()._str_() + ', Offset: ' + str(self.offset)


class Parameter(Entity):

    def _init_(self, name, partype, offset=-1):
        super()._init_(name, "PARAMETER")
        self.partype = partype 
        self.offset = offset

    def _str_(self):
        return super()._str_() + ', type: ' + self.partype \
            + ', Osffset: ' + str(self.offset)






    def addscope():
        global scope_count
        scope_count += 1
        enclosescope = scope_array[-1]
        curr_scope = Scope[enclosescope.nestlvl +1, enclosescope]
        scope_array.append(curr_scope)
        

    def addparentity(name, partype):
        nestlvl = scope_array[-1].nestlvl
        paroffset = scope_array[-1].getOffset()
        if not unique_entity(name, "PARAMETER", nestlvl):
            print("Error: Add parameter entity")
            quit()
        scope_array[-1].addEntity(Parameter(name, partype, paroffset))

        
    def addfunctentity(name):
        nestlvl = scope_array[-1].enclosescope.nestlvl
        if not unique_entity(name, "FUNCTION", nestlvl):
            print("Error: Add function entity")
            quit()
        scope_array[-2].addEntity(Function(name))


    def updatequad_functentity(name):
        startquad = nextquad()
        if (name == tokens[1][1]):
            return startquad
        funct_entity = search_entity(name, "FUNCTION")[0]
        funct_entity.setstartquad(startquad)
        return startquad



    def updateframelength_functentity(name, framelength):
        global mainframelength
        if (name == tokens[1][1]):
            mainframelength = framelength
            return
        funct_entity = search_entity(name, "FUNCTION")[0]
        funct_entity.setframelength(framelength)



    def addvarentity(name):
        nestlvl = scope_array[-1].netslvl
        varoffset = scope_array[-1].getOffset()
        if not unique_entity(name, "VARIABLE", nestlvl):
            print("Error: Add variable entity")
            quit()
        if varispar(name, nestlvl):
            print("Error: Variable is parameter")
            quit()
        scope_array[-1].addEntity(Variable(name, varoffset))



    def addfunctarg(funct_name, partype):
        if (partype == 'in'):
            new_arg = Argument('CV')
        elif (partype == 'inout'):
            new_arg = Argument('REF')
        elif (partype == 'inandout'):
            new_arg =Argument('INANDOUT')
            funct_entity = search_entity(funct_name, "FUNCTION")[0]
        if funct_entity == None:
            print("Error: Add function argument")
            quit()
        if funct_entity.arguments != list():
            funct_entity.arguments[-1].setnext(new_arg)
        funct_entity.add_arguments(new_arg)


    def search_entity(name, elemtype):
        if (scope_array == list()):
            return
        temp_scope = scope_array[-1]
        while (temp_scope != None):
            for entity in temp_scope.entities:
                if (entity.name == name and entity.elemtype == elemtype):
                    return entity, tmp_scope.nestlvl
            temp_scope = temp_scope.enclosescope
        temp_scope = scope_array[0]
        for entity in temp_scope.entities:
            if (entity.name == name and entity.type == elemtype):
                return entity, temp_scope.nestlvl


    def search_entity_by_name(name):
        if scope_array == list():
            return
        temp_scope = scope_array[-1]
        while temp_scope != None:
            for entity in temp_scope.entities:
                if entity.name == name:
                    return entity, temp_scope.nestlvl

            temp_scope = temp_scope.enclosescope
        temp_scope = scopes_array[0]
        for entity in temp_scope.entities:
            if entity.name == name:
                return entity, temp_scope.nestlvl



    def unique_entity(name, enttype, nestlvl):
        if scope_array[-1].nestlvl < nestlvl:
           return
        scope = scope_array[nestlvl]
        list_len = len(scope.entities)
        for i in range(list_len):
            for j in range(list_len):
                ent1 = scope.entities[i]
                ent2 = scope.entities[j]
            if (ent1.name == ent2.name and ent1.enttype == ent2.enttype and ent1.name == name and ent1.enttype == enttype):
                return False
        return True


    def varispar(name, nestlvl):
        if scope_array[-1].nestlvl < nestlvl:
            return
        scope = scope_array[nestlvl]
        list_len = len(scope.entities)
        for i in range(list_len):
            ent = scope.entities[i]
            if ent.type == "PARAMETER" and ent.name == name:
                return True
        return False

    def printscope():
        print("* Printing main scope:\n|")
        for scope in scope_array:
            nestlvl = scope.nestlnl + 1
            print('\t' * nestlvl + str(scope))
            for entity in scope.entities:
                print('|\t' * nestlvl + str(entity))
                if isinstance(entity, Function):
                    for arg in entity.arguments:
                        print('|\t' * nestlvl + '|\t' + str(arg))
        print('\n')


class Quads():

    def _init_(self, quad, p, x, y, z):
        self.quad = quad
        self.p = p
        self.x = x
        self.y = y
        self.z = z


    def _str_(self):
        return '(' + str(self.quad) + ': ' + str(self.p)+ ', ' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'


    def makefile(self):
        return str(self.quad) + ': ' + str(self.p)+ ', ' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
        


def nextquad():
        global nextquad
        return nextquad


def genquad(p, x, y, z):
        global nextquad
        newquad = Quad(nextquad, p, x, y, z)
        quadList.append(newquad)
        nextquad += 1


def newtemp():
    global vartemp, nextvartemp
    varkey = 'T_' + str(nextvartemp)
    vartemp[varkey] = None
    scope_array[-1].addEntity(TempVariable(varkey, scope_array[-1].getOffset()))
    nextvarkey += 1
    return varkey
    

def emptyList():
    emptyL = []
    return emptyL


def makelist(x):
    m = list()
    m.append(x)
    return m


def merge(l1,l2):
    ml = []
    ml = l1+l2
    return ml


def backpatch(l1,z):
    for quad in InterCarray:
        if quad.quad in l1:
            quad.z = z


def writetofile_int():
    file = filename + '.int'
    wfile = open(file,"w")
    for quad in InterCarray:
        wfile.write(quad.makefile() + '\n')
    wfile.close()


def vardeclare(quad):
    var = vartemp()
    array = InterCarray.array(quad) + 1
    while True:
        arg = InterCarray[array]
        if arg.p == 'end_block' :
            break
        if arg.y not in ('CV', 'REF', 'RET') and arg.p != 'call':
            if isinstance(arg.x, str):
                if (arg.x.numbers() == False):
                    var[arg.x] = 'int'
            if isinstance(arg.y, str):
                if (arg.y.numbers() == False):
                    var[arg.y] = 'int'
            if isinstance(arg.z, str):
                if (arg.z.numbers() == False):
                    var[arg.z] = 'int'
        array += 1
    return


def changedeclare(var):
    flag = False
    temp = '\n\int'
    for i in var:
        flag = True
        temp += v + ', '
    if flag == True:
        return temp[:-2] + ';'
    else:
        return ''



def convert_c(quad):
    mode = True
    if quad.p == 'jump':
        temp = 'jump to' + str(quad.z) + ';'
    elif quad.p in ('=', '<>', '<', '<=', '>', '>='):
        p = quad.p
        if p == '=':
            p = '=='
        elif p == '<>':
            p = '!='
        temp = 'if (' + str(quad.x) + ' ' + p + ' ' + str(quad.y) + ') jump to' + str(quad.z) + ';'
    elif quad.p == ':=':
        temp = quad.z + ' = ' + str(quad.x) + ';'
    elif quad.p in ('+', '-', '*', '/'):
        temp = quad.z + ' = ' + str(quad.x) + ' ' + str(quad.p) + ' ' + str(quad.y) + ';'
    elif quad.p == 'out':
        temp = 'printf("%d\\n", ' + str(quad.x) + ');'
    elif quad.p == 'retv':
        temp = 'return (' + str(quad.x) + ');'
    elif quad.p == 'begin_block':
        mode = False
        if quad.x == tokens[1][1]:
            temp = 'int main(void)\n{'
        else: 
            temp = 'int ' + quad.x + '()\n{'
        var = vardeclare(quad)
        temp += changedeclare(var)
        temp += '\n\tL_' + str(quad.quad) + ':'
    elif quad.p == 'call':
        temp = quad.x + '();'
    elif quad.p == 'end_block':
        mode = False
        temp = '\tL_' + str(quad.quad) + ': {}\n'
        temp += '}\n'
    elif quad.p == 'halt':
        temp = 'return 0;' 
    else:
        return None
    if mode == True:
        temp = '\tL_' + str(quad.quad) + ': ' + temp
    return temp
        

def make_c():
    c.write('#include <stdio.h>\n\n\n')
    for quad in InterCarray:
        i = convert_c(quad)
        if i != None:
            c.write(i + '  //' + str(quad) + '\n')
    c.close()



def gnlvcode(x):
    temp = search_entity_by_name(name)
    entlvl = search_entity_by_name(name)
    curr_scope = scope_array[-1].nestlvl
    c = curr_scope - entlvl - 1
    while c > 0:
        assembly_file.write('    lw      $t0, -4($t0)\n')
        c -= 1
    assembly_file.write('    addi    $t0, $t0, -%d\n' % temp.offset)


def loadvr(v, r):
    if str(v).numbers():
        assembly_file.write('    li      $t%s, %d\n' % (r, v))
    else:
        temp, entlvl = search_entity_by_name(name)
        curr_scope  = scope_array[-1].nestlvl
        if temp.elemtype == 'VARIABLE' and entlvl == 0:
            assembly_file.write('    lw      $t%s, -%d($s0)\n' % (r, temp.offset))
        elif (temp.elemtype == 'VARIABLE' and entlvl == curr_scope) or \
             (temp.elemtype == 'PARAMETER' and temp.partype == 'in' and entlvl == curr_scope) or \
             (temp.elemtype == 'TMPVAR'):
            assembly_file.write('    lw      $t%s, -%d($sp)\n' % (r, temp.offset))
        elif temp.elemtype == 'PARAMETER' and temp.partype == 'inout' and entlvl == curr_scope:
            assembly_file.write('    lw      $t0, -%d($sp)\n' % temp.offset)
            assembly_file.write('    lw      $t%s, ($t0)\n' % r)
        elif (temp.elemtype == 'VARIABLE' and entlvl < curr_scope) or \
             (temp.elemtype == 'PARAMETER' and temp.partype == 'in' and entlvl < curr_scope):
            gnvlcode(x)
            assembly_file.write('    lw      $t%s, ($t0)\n' % r)
        elif temp.elemtype == 'PARAMETER' and temp.partype == 'inout' and entlvl < curr_scope:
            gnvlcode(x)
            assembly_file.write('    lw      $t0, ($t0)\n')
            assembly_file.write('    lw      $t%s, ($t0)\n' % r)
        else:
            print("Error: Unreachable load argument from quad to register")
            quit()


        
def storerv(r, v):
    temp, entlvl = search_entity_by_name(name)
    curr_scope = scope_array[-1].nestlvl
    if (temp.elemtype == 'VARIABLE' and entlvl == 0):
      assembly_file.write('    sw      $t%s, -%d($s0)\n' %  (r, temp.offset))
      
    elif (temp.elemtype == 'VARIABLE' and entlvl == curr_scope) or \
         (temp.elemtype == 'PARAMETER' and temp.partype == 'in' and entlvl == curr_scope) or \
         (temp.elemtype == 'TMPVAR'):
        assembly_file.write('    sw      $t%s, -%d($sp)\n' % (r, temp.offset))
      
    elif (temp.elemtype == 'PARAMETER' and temp.partype == 'inout' and entlvl == curr_scope):
        assembly_file.write('    lw      $t0, -%d($sp)\n' % temp.offset)
        assembly_file.write('    sw      $t%s, ($t0)\n' % r)

    elif (temp.elemtype == 'VARIABLE' and entlvl < curr_scope) or \
         (temp.elemtype == 'PARAMETER' and temp.partype == 'in' and entlvl < curr_scope):
        gnvlcode(x)
        assembly_file.write('    sw      $t%s, ($t0)\n' % r)

    elif (temp.elemtype == 'PARAMETER' and temp.partype == 'inout' and entlvl < curr_scope):
        gnvlcode(x)
        assembly_file.write('    lw      $t0, ($t0)\n')
        assembly_file.write('    sw      $t%s, ($t0)\n' % r) 
    else:
        print("Error: Unreachable store argument from quad to register")
        quit()


def transform_to_assembly(quad, element):
    global math_symbols, relations, math_operations, branches

    relations=['<','>','=','<=','>=','<>']
    branches = ('beq', 'bne', 'blt', 'ble', 'bgt', 'bge')
    math_symbols=['+','-','*','/']
    math_operations = ('add', 'sub', 'mul', 'div')

    global assembly_file,number_of_functions_mips,L_counter

    if quad.p == 'jump':
        assembly_file.write('L_%d:\n'%(quad.quad))
        assembly_file.write('    j       L_%s\n' % quad.z)
    elif quad.p in relations:
        relop = branches[relations.array(quad.p)]
        assembly_file.write('L_%d:\n'%(quad.quad))
        loadvr(quad.x, '1')
        loadvr(quad.y, '2')
        assembly_file.write('    %s     $t1, $t2, L_%d\n' % (relop, quad.z))
    elif quad.p in math_symbols:
        op = branches[math_symbols.array(quad.p)]
        assembly_file.write('L_%d:\n'%(quad.quad))
        loadvr(quad.x, '1')
        loadvr(quad.y, '2')
        assembly_file.write('    %s     $t1, $t2, $t2%d\n' % (op, quad.z))
    elif quad.p == ':=':  
        assembly_file.write('L_%d:\n' % (quad.quad))
        loadvr(quad.x, '1')
        storerv('1', quad.z)
    elif quad.p == 'out':
        assembly_file.write('L_%d:\n'%(quad.quad))
        loadvr(quad.x,'9')
        assembly_file.write('    li      $v0, 1\n')
        assembly_file.write('    add      $a0,$zero,$t9 \n')
        assembly_file.write('    syscall       \n')
    elif quad.p == 'in':
        assembly_file.write('    li      $v0, 5\n')
        assembly_file.write('    syscall       \n')
    elif quad.op == 'retv':
        loadvr(quad.x, '1')
        assembly_file.write('    lw      $t0, -8($sp)\n')
        assembly_file.write('    sw      $t1, -8($t0)\n')
        assembly_file.write('    jr      $ra\n\n')
    elif quad.p == 'par':
        if element == tokens[1][1]:
            function_c = 0
            framelength = mainframelength
        else:
            entity = search_entity(element, 'FUNCTION')
            function_c= search_entity(element, 'FUNCTION')
            framelength = entity.framelength
        if quads == []:
            assembly_file.write('    addi    $fp, $sp, -%d\n' % framelength)
        quads.append(quad)
        temp_offset = 12 + 4 * quads.array(quad)
        if quad.y == 'CV':
            loadvr(quad.x, '0')
            assembly_file.write('    sw      $t0, -%d($fp)\n' % temp_offset)
        elif quad.y == 'REF':
            varent = search_entity_by_name(quad.x)
            var_c = search_entity_by_name(quad.x)
            if function_c == var_c:
                if varent.elemtype == 'VARIABLE':
                    assembly_file.write('    addi    $t0, $sp, -%s\n' % varent.offset)
                    assembly_file.write('    sw      $t0, -%d($fp)\n' % temp_offset) 
                elif varent.elemtype == 'PARAMETER' and varent.partype == 'in':
                    assembly_file.write('    addi    $t0, $sp, -%s\n' % varent.offset)
                    assembly_file.write('    sw      $t0, -%d($fp)\n' % temp_offset)
                elif varent.elemtype == 'PARAMETER' and varnt.partype == 'inout':
                    assembly_file.write('    lw      $t0, -%d($sp)\n' % varent.offset)
                    assembly_file.write('    sw      $t0, -%d($fp)\n' % temp_offset)
            else:
                if varent.elemtype == 'VARIABLE':
                    gnvlcode(quad.x)
                    assembly_file.write('    sw      $t0, -%d($fp)\n' % temp_offset)    
                elif varent.elemtype == 'PARAMETER' and varent.partype == 'in':
                    gnvlcode(quad.x)
                    assembly_file.write('    sw      $t0, -%d($fp)\n' % temp_offset)
                elif varient.elemtype == 'PARAMETER' and varent.partype == 'inout':
                    gnvlcode(quad.x)
                    assembly_file.write('    lw      $t0, 0($t0)\n')
                    assembly_file.write('    sw      $t0, -%d($fp)\n' % temp_offset)
        elif quad.y == 'RET':
            varent = search_entity_by_name(quad.x)
            var_c = search_entity_by_name(quad.x)
            assembly_file.write('    addi    $t0, $sp, -%d\n' % varent.offset) 
            assembly_file.write('    sw      $t0, -8($fp)\n')
    elif quad.p == 'call':
        if element == tokens[1][1]:
            function_c = 0
            framelength = mainframelength 
        else:
            par_function = search_entity(element, 'FUNCTION')
            function_c = search_entity(element, 'FUNCTION')
            framelength = entity.framelength
            child_function, child_function_c = search_entity(quad.x, 'FUNCTION')     
        if function_c == child_function_c:
            assembly_file.write('    lw      $t0, -4($sp)\n')
            assembly_file.write('    sw      $t0, -4($fp)\n')
        else:
            assembly_file.write('    sb      $sp, -4($fp)\n')
            assembly_file.write('    addi    $sp, $sp, %d\n' % framelength)
            assembly_file.write('    jal     L_%s\n' % str(child_function.startquad))
            assembly_file.write('    addi    $sp, $sp, -%d\n' % framelength)
    elif quad.p == 'begin_block':
        if element == tokens[1][1]:
            assembly_file.write('    j       L_0\n')
            assembly_file.write('L_0:\n')
            assembly_file.seek(0,2)   
            assembly_file.write('    addi    $sp, $sp, %d\n' % mainframelength)
            assembly_file.write('    move    $s0, $sp\n')  
        else: 
            assembly_file.write('    j      L_t%d\n'%(L_counter))
            function_c += 1
            assembly_file.write('L_d%d:\n' % (function_c))
            assembly_file.write('    sw      $ra, 0($sp)\n')
    elif quad.p == 'end_block':
        assembly_file.write('    lw      $ra, 0($sp)\n')
        assembly_file.write('    jr      $ra\n\n')
    elif quad.p == 'halt':
        assembly_file.write('L_d%d:\n' % (quad.quad))
        assembly_file.write('    li      $v0, 10\n')
        assembly_file.write('    syscall       \n')
    



class Lexer(object):
  
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
      
        global tokens  #krataw ta tokens poy ftiaxnei o lexer
        new_lines = [] # exw tis 8eseis twn \n
                        
        # briskw se poio string ginetai allagh grammhs kai ta krtaw se enan pinaka new_lines
        change_line_counter=0
        test=self.source_code
        temp_counter=0
        while temp_counter != len(test)-1:
            if test[temp_counter]== ' ' or test[temp_counter]== '\t' and test[temp_counter-1]!= '\n':
                change_line_counter+=1
            while test[temp_counter] == ' ' or test[temp_counter]== '\t':
                temp_counter+=1
            if test[temp_counter]== '\n' and test[temp_counter-1]!= '\n' :
                new_lines.append(space_counter+1)
                change_line_counter+=1
            temp_counter+=1
      

        # to string periexei ka8e grammh toy source kwdika gia ton elegxo twn tokens ston parser
        counter_t=-1
        global string
        help=""
        for i in self.source_code:
            counter_t+=1
            if i != '\n' and i!='\t':  # thelw na krataw mono to string xwris kena tabs ktlp
                help+=i
            elif i == '\n':        # bazw (and help!= "") an xreiastei na mhn metraw tis kenes grammes
                string.append(help)
                help=""
            if counter_t == len(self.source_code)-1:
                string.append(help)

    #print(new_lines)  

        source_code= self.source_code.split() #lista apo tis le3eis toy kwdika moy

        global counter  #metrhths gia thn lista mas
 
        reminder = 0 # flag gia elgxo eidikhs le3hs
        reminder2 = 0 # flag gia elegxo eidikhs le3hs (se periptwsh string)
        reminder3 = 0 # flag gia elegxo eidikhs le3hs meta apo grouping sumbolo ( se periptwsh string)

        while counter < len(source_code):
            word = source_code[counter]
            word = word[0: 30] #diabazw ta prwta 30 grammata apo ka8e leksh
       
        #elegxos gia akeraious
        if re.match('[0-9]',word):
                word2=word
                counter2=0 # metrhths gia ka8e mia le3h tou word
                flag = 0 # elegxos gia gramma
                while counter2 != len(word2):
                    if word2[counter2].isalpha():
                        flag+=1
                        counter2+=1
                if flag != 0:
                    print('invalid string:' + word)
                    quit()
                else:
                    if word[len(word)-1] == ';': 
                        int_word=int(word[0:len(word) - 1])
                        if int_word < 32767: # elegxos gia ta oria twn integer
                            tokens.append(['INTEGER',word[0:len(word) - 1]])
                        else:
                            print('error integers must be under 32767')
                            quit()
                    else:
                        int_word=int(word)
                        if int_word < 32767: # elegxos gia ta oria twn integer
                            tokens.append(['INTEGER',word])
                        else:
                            print('error integers must be under 32767')
                            quit()
        #elegxos gia operations
        if word[0] in " + - * / " :
            if len(word) >= 2:
                if(word[1].isalnum()):
                  #print(word[1])
                  pr = 0
                  error_line = 0
                  for i in string:
                    pr+=1
                    if word in i:
                      error_line=str(pr)
                      break
                  print('error: syntax error in line: ' + error_line)
                  quit()
                else:
                    tokens.append(['OPERATOR',word[0]])
        #elegxos gia sugriseis
        elif word[0] in relations:
            if word[0] == ">":
                if word[1]== "=":
                  if len(word)>=3:
                    print('error: word starting with "match" operator')
                    quit()
                  else:
                    tokens.append('MATCH',">=")
                elif len(word) == 1:
                    tokens.append('MATCH',">")
                else:
                    print('error: word starting with "match" operator')
                    quit()
            elif word[0] == "<":
                if word[1]== "=":
                  if len(word)>=3:
                    print('error: word starting with "match" operator')
                    quit()
                  else:
                    tokens.append('MATCH',"<=")
                elif word[1]== ">":
                  if len(word)>=3:
                    print('error: word starting with "match" operator')
                    quit()
                  else:
                    tokens.append('MATCH',"<>")
                elif len(word) == 1:
                    tokens.append('MATCH',"<")
                else:
                    print('error: word starting with "match" operator')
                    quit()
            elif word[0] == "=":
                if len(word)>=2:
                  print('error: word starting with "match" operator')
                  quit()
                else:
                  tokens.append('MATCH',"=")
        #elegxos gia anathesh
        elif word in ":=":
              pr = 0
              error_line = 0
              for i in string:
                pr+=1
                if word in i:
                  error_line=str(pr)
                  break
              print('error: can not have := alone in line: ' + error_line)
              quit()
          #elegxos gia diaxwristes
        elif word[0] in "; , :":
              print('error: seperators can not stand alone') 
              quit()    
        #elegxos gia omadopoihsh
        elif word[0] in "( ) [ ] ":
            if word[0] == ")" or word[0] == "]":
              if len(word) > 1:
                print('error: expresion can not start with ) or ]')
                quit()
            if len(word)>1:
              if word[0] == "(" or word[0] == "[":
                tokens.append(['GROUPING_SEP',word[0]])
                if word[1].isalpha() or (word[1].isalpha())==False :
                  word_s=word[1:len(word)]
                  #print(word_s)
                  ##################################################################
                  w=""  # kratame thn le3h poy einai prin apo eidiko xarakthra
                  flag = 0 # elexgoume an meta to string exoyme eidiko xarakthra (!= tou string)
                  pol = 0 # metrhths gia thn 8esh sto word poy koitame
                  flager = 0 # elegxoume thn periptwsh poy exoyme := ,<=, >=
                  flager2 = 0 # elegxoume thn periptwsh poy exoyme <>
                  flager3 = 0 # elegxoyme to string sthn periptwsh poy einai eidikos xarakrhras
                  integer="" # krataei ari8mous poy briskontai mesa se string
                  for i in word_s:
                    pol+=1
                    flag = 0 
                    #elegxos gia operations
                    if i in " + - * / " :
                      if flager3 == 1:
                        flager3 = 0
                      else:
                        if w != "":
                          tokens.append(['IDENTIFIER',w])
                      tokens.append(['OPERATOR',i])
                      flag=1
                      w=""
                    #elegxos gia sugriseis
                    elif i in "< > <= >= = <>":
                      if i == "=":
                        if flager == 1:
                          flager = 0
                          continue
                        else:
                          if flager3 == 1:
                            flager3 = 0
                          else:
                            if w != "":
                              tokens.append(['IDENTIFIER',w])
                          tokens.append(['MATCH',i])
                          flag=1
                          w=""
                      elif i == "<":
                        flager = 1
                        if pol!=len(word_s) and word_s[pol] == "=":   # gia to <=
                          if flager3 == 1:
                            flager3 = 0
                          else:
                            if w != "":
                              tokens.append(['IDENTIFIER',w])
                          tokens.append(['MATCH',"<="])
                          flag=1
                          w=""
                        elif pol!=len(word_s) and word_s[pol] == ">": # gia to <>
                          flager2 = 1
                          if flager3 == 1:
                            flager3 = 0
                          else:
                            if w != "":
                              tokens.append(['IDENTIFIER',w])
                          tokens.append(['MATCH',"<>"])
                          flag=1
                          w=""
                        else:
                          if flager3 == 1:
                            flager3 = 0
                          else:
                            if w != "":
                              tokens.append(['IDENTIFIER',w])
                          tokens.append(['MATCH',i])
                          flag=1
                          w=""
                      elif i == ">":
                        if flager2 == 1:
                          flager2 = 0
                          continue
                        flager = 1
                        if pol!=len(word_s) and word_s[pol] == "=":   # gia to >=
                          if flager3 == 1:
                            flager3 = 0
                          else:
                            if w != "":
                              tokens.append(['IDENTIFIER',w])
                          tokens.append(['MATCH',">="])
                          flag=1
                          w=""
                        else:
                          if flager3 == 1:
                            flager3 = 0
                          else:
                            if w != "":
                              tokens.append(['IDENTIFIER',w])
                          tokens.append(['MATCH',i])
                          flag=1
                          w=""
                    #elegxos gia diaxwristes
                    elif i in "; , :":
                      if i == ":":
                        flager=1
                        if pol!=len(word_s) and word_s[pol] == "=":   # gia thn ana8esh :=
                          if flager3 == 1:
                            flager3 = 0
                          else:
                            if w != "":
                              tokens.append(['IDENTIFIER',w])
                          tokens.append(['SETTING',":="])
                          flag=1
                          w=""
                        else:
                          if flager3 == 1:
                            flager3 = 0
                          else:
                            if w != "":
                              tokens.append(['IDENTIFIER',w])
                          tokens.append(['SEPERATORS',i])
                          flag=1
                          w=""
                      else:
                        if flager3 == 1:
                          flager3 = 0
                        else:
                          if w != "":
                            tokens.append(['IDENTIFIER',w])
                        tokens.append(['SEPERATORS',i])
                        flag=1
                        w=""
                    #elegxos gia omadopoihsh
                    elif i in "( ) [ ] ":
                      if flager3 == 1:
                        flager3 = 0
                      else:
                        if w != "":
                          tokens.append(['IDENTIFIER',w])
                      tokens.append(['GROUPING',i])
                      flag=1
                      w=""
                    elif i.isalpha() and flag == 0:
                      w+=i
                      if(pol == len(word_s)):
                      #elegxos gia eidikh leksh
                        for i in special:
                          if w == i[1]:
                            tokens.append(i)
                            reminder2 = 1
                            break
                          else:
                            reminder2 = 0
                        if reminder2 == 0:
                          if w != "":
                            tokens.append(['IDENTIFIER',w])
                        if w[len(w)-1] == ';':
                          tokens.append(['IDENTIFIER',w])  
                      elif word_s[pol] in "( ) [ ] ":          # elegxo to epomeno gramma an einai sumbolo omadopoihshs
                      #elegxos gia eidikh le3h
                        for i in special:
                          if w == i[1]:
                            flager3=1
                            tokens.append(i)
                            reminder3 = 1
                            break
                          else:
                            reminder3 = 0
                      elif word_s[pol] in "+ - * / ":          # elegxo to epomeno gramma an einai operation symbol
                      #elegxos gia eidikh le3h
                        for i in special:
                          if w == i[1]:
                            flager3=1
                            tokens.append(i)
                            reminder3 = 1
                            break
                          else:
                            reminder3 = 0
                      elif word_s[pol] in "< > >= <= = <> ":          # elegxo to epomeno gramma an einai match symbol
                      #elegxos gia eidikh le3h
                        for i in special:
                          if w == i[1]:
                            flager3=1
                            tokens.append(i)
                            reminder3 = 1
                            break
                          else:
                            reminder3 = 0
                      elif word_s[pol] in "; , :":          # elegxo to epomeno gramma an einai seperators
                      #elegxos gia eidikh le3h
                        for i in special:
                          if w == i[1]:
                            flager3=1
                            tokens.append(i)
                            reminder3 = 1
                            break
                          else:
                            reminder3 = 0  
                    elif i.isnumeric() and flag == 0: 
                      if pol != len(word_s):
                        if word_s[pol-2].isalpha():
                          for x in range((pol-1),len(word_s)):
                            if word_s[x].isalnum():
                              w+=word[x]
                            else:
                              break
                        elif (word_s[pol-2].isnumeric()==False):
                          for x in range((pol-1),len(word_s)):
                            if word_s[x].isnumeric():
                              integer+=word_s[x]
                            elif word_s[x].isalpha():
                              print('invalid string:' + word_s)
                              quit()
                            else:
                              break
                          if int(integer)>32767:
                            print('error:integer bigger than 32767')
                            quit()
                          tokens.append(['INTEGER',integer])
                          integer="" 
                      if pol == len(word_s):
                        if word_s[pol-2].isalpha():
                          w+=i
                          tokens.append(['IDENTIFIER',w])
                        elif (word_s[pol-2].isnumeric()==False):
                          integer+=word_s[pol-1]
                          if int(integer)>32767:
                            print('error:integer bigger than 32767')
                            quit()
                          tokens.append(['INTEGER',integer])
            elif len(word) == 1:
              tokens.append(['GROUPING_SEP',word[0]])
                  ################################################################# 
        #elegxos gia diaxwristes sxoliwn
        if word in "/* */ // ":
              #tokens.append(['COMMENT_SEP',word])
              word2=word
              counter2=counter
              word3=word
              if word2 == "/*":
                while word2 != "*/": 
                  counter2+=1
                  if source_code[counter2] == "/*": # elegxos gia synexomena sxolia 
                     pr = 0
                     error_line = 0
                     for i in string:
                       pr+=1
                       if word in i:
                         error_line=str(pr)
                         break
                     print('error: consecutive /* in line: '+ error_line)
                     quit()
                  elif source_code[counter2] == "*/": # elegxos gia termatismo sxoliwn 
                     #tokens.append(['COMMENT_SEP',source_code[counter2]]) 
                     counter=counter2
                     break
                  elif source_code[counter2] == "//":
                    pr = 0
                    error_line = 0
                    for i in string:
                      pr+=1
                      if word in i:
                        error_line=str(pr)
                        break
                    print('error: nested commmets in line: ' + error_line)
                    quit()
                  if counter2 == len(source_code)-1:
                    pr = 0
                    error_line = 0
                    for i in string:
                      pr+=1
                      if word in i:
                        error_line=str(pr)
                        break
                    print('error: unclosed comments in line: ' + error_line)
                    quit()
                  word2=source_code[counter2]
              elif word2 == "*/":
                pr = 0
                error_line = 0
                for i in string:
                  pr+=1
                  if word in i:
                    error_line=str(pr)
                    break
                print('error: starting with */ in line: ' + error_line)
                quit()
              if word3 == "//":
                for i in new_lines:
                  if counter < i:
                    counter = i -1
                    break
        #elegxos gia grammata kefalaia kai mh
        if reminder!=1 and (re.match('[a-z]',word) or re.match('[A-Z]',word)):
            #print(word)
            w=""  # kratame thn le3h poy einai prin apo eidiko xarakthra
            flag = 0 # elexgoume an meta to string exoyme eidiko xarakthra (!= tou string)
            pol = 0 # metrhths gia thn 8esh sto word poy koitame
            flager = 0 # elegxoume thn periptwsh poy exoyme := ,<=, >=
            flager2 = 0 # elegxoume thn periptwsh poy exoyme <>
            flager3 = 0 # elegxoyme to string sthn periptwsh poy einai eidikos xarakrhras
            integer="" # krataei ari8mous poy briskontai mesa se string
            for i in word:
              pol+=1
              flag = 0 
              #elegxos gia operations
              if i in " + - * / " :
                if flager3 == 1:
                  flager3 = 0
                else:
                  if w != "":
                    tokens.append(['IDENTIFIER',w])
                    tokens.append(['OPERATOR',i])
                flag=1
                w=""
              #elegxos gia sugriseis
              elif i in relations:
                if i == "=":
                  if flager == 1:
                    flager = 0
                    continue
                  else:
                    if flager3 == 1:
                      flager3 = 0
                    else:
                      if w != "":
                        tokens.append(['IDENTIFIER',w])
                    tokens.append(['MATCH',i])
                    flag=1
                    w=""
                elif i == "<":
                  flager = 1
                  if pol!=len(word) and word[pol] == "=":   # gia to <=
                    if flager3 == 1:
                      flager3 = 0
                    else:
                      if w != "":
                        tokens.append(['IDENTIFIER',w])
                    tokens.append(['MATCH',"<="])
                    flag=1
                    w=""
                  elif pol!=len(word) and word[pol] == ">": # gia to <>
                    flager2 = 1
                    if flager3 == 1:
                      flager3 = 0
                    else:
                      if w != "":
                        tokens.append(['IDENTIFIER',w])
                    tokens.append(['MATCH',"<>"])
                    flag=1
                    w=""
                  else:
                    if flager3 == 1:
                      flager3 = 0
                    else:
                      if w != "":
                        tokens.append(['IDENTIFIER',w])
                    tokens.append(['MATCH',i])
                    flag=1
                    w=""
                elif i == ">":
                  if flager2 == 1:
                    flager2 = 0
                    continue
                  flager = 1
                  if pol!=len(word) and word[pol] == "=":   # gia to >=
                    if flager3 == 1:
                      flager3 = 0
                    else:
                      if w != "":
                        tokens.append(['IDENTIFIER',w])
                    tokens.append(['MATCH',">="])
                    flag=1
                    w=""
                  else:
                    if flager3 == 1:
                      flager3 = 0
                    else:
                      if w != "":
                        tokens.append(['IDENTIFIER',w])
                    tokens.append(['MATCH',i])
                    flag=1
                    w=""
              #elegxos gia diaxwristes
              elif i in "; , :":
                if i == ":":
                  flager=1
                  if pol!=len(word) and word[pol] == "=":   # gia thn ana8esh :=
                    if flager3 == 1:
                      flager3 = 0
                    else:
                      if w != "":
                        tokens.append(['IDENTIFIER',w])
                    tokens.append(['SETTING',":="])
                    flag=1
                    w=""
                  else:
                    if flager3 == 1:
                     flager3 = 0
                    else:
                      if w != "":
                        tokens.append(['IDENTIFIER',w])
                    tokens.append(['SEPERATORS',i])
                    flag=1
                    w=""
                else:
                   if flager3 == 1:
                     flager3 = 0
                   else:
                     if w != "":
                       tokens.append(['IDENTIFIER',w])
                   tokens.append(['SEPERATORS',i])
                   flag=1
                   w=""
              #elegxos gia omadopoihsh
              elif i in "( ) [ ] ":
                if flager3 == 1:
                  flager3 = 0
                else:
                  if w != "":
                    tokens.append(['IDENTIFIER',w])
                tokens.append(['GROUPING',i])
                flag=1
                w=""
              elif i.isalpha() and flag == 0:
                w+=i
                if(pol == len(word)):
                  #elegxos gia eidikh leksh
                  for i in special:
                    if w == i[1]:
                      tokens.append(i)
                      reminder2 = 1
                      break
                    else:
                      reminder2 = 0
                  if reminder2 == 0:
                    if w != "":
                      tokens.append(['IDENTIFIER',w])
                  if w[len(w)-1] == ';':
                    tokens.append(['IDENTIFIER',w])  
                elif word[pol] in "( ) [ ] ":          # elegxo to epomeno gramma an einai sumbolo omadopoihshs
                  #elegxos gia eidikh le3h
                  for i in special:
                    if w == i[1]:
                      flager3=1
                      tokens.append(i)
                      reminder3 = 1
                      break
                    else:
                      reminder3 = 0
                elif word[pol] in "+ - * / ":    # elegxo to epomeno gramma an einai operation symbol
                  #elegxos gia eidikh le3h
                  for i in special:
                    if w == i[1]:
                      flager3=1
                      tokens.append(i)
                      reminder3 = 1
                      break
                    else:
                      reminder3 = 0
                elif word[pol] in "< > <= >= = <> ":    # elegxo to epomeno gramma an einai match symbol
                  #elegxos gia eidikh le3h
                  for i in special:
                    if w == i[1]:
                      flager3=1
                      tokens.append(i)
                      reminder3 = 1
                      break
                    else:
                      reminder3 = 0
                elif word[pol] in "; , : ":    # elegxo to epomeno gramma an einai diaxwrisths
                  #elegxos gia eidikh le3h
                  for i in special:
                    if w == i[1]:
                      flager3=1
                      tokens.append(i)
                      reminder3 = 1
                      break
                    else:
                      reminder3 = 0
              elif i.isnumeric() and flag == 0: 
                if pol != len(word):
                  if word[pol-2].isalpha():
                    for x in range((pol-1),len(word)):
                      if word[x].isalnum():
                        w+=word[x]
                      else:
                        break
                  elif (word[pol-2].isnumeric()==False):
                    for x in range((pol-1),len(word)):
                      if word[x].isnumeric():
                        integer+=word[x]
                      elif word[x].isalpha():
                        print('invalid string:' + word)
                        quit()
                      else:
                        break
                    if int(integer) > 32767:
                            print('error:integer bigger than 32767')
                            quit()
                    tokens.append(['INTEGER',integer])
                    integer="" 
                if pol == len(word):
                  if word[pol-2].isalpha():
                    w+=i
                    tokens.append(['IDENTIFIER',w])
                  elif (word[pol-2].isnumeric()==False):
                    integer+=word[pol-1]
                    if int(integer)>32767:
                            print('error:integer bigger than 32767')
                            quit()
                    tokens.append(['INTEGER',integer])
 
               
        counter += 1
      
        #print(string)
        #print('---------------------------------------------------------------------------------------')
        #print (tokens)
        #print('number of tokens: ' + str(len(tokens)))
    
        return tokens





def syntax(self):

  
    global token_index # metraei se poio token briskomaste
    global last_token 
    genquad('begin_block',tokens[1][1])
    from_quad_to_assembly(quad_List[0],tokens[1][1])
    scopes_array.append(Scope())
    while token_index < len(tokens):
    
        token_type = tokens[token_index][0] # krataei ton typo tou token
        token_value = tokens[token_index][1] # krataei thn timh tou token
  
        if tokens[0][1] != 'program' or tokens[len(tokens)-1][1] != 'endprogram': # periptwsh poy den 3ekinaei me program h den teleiwnei me endprogram 
            print('error: program needs to start with "program <identifier>" and end with "endprogram" in line:' + lines())
            quit()
        else:
            if token_index == 0:
                token_index+=1
                if tokens[token_index][0] != 'IDENTIFIER': # periptwsh poy meta apo to program den erxetai identifier
                    print('error: after "program" expect identifier in line:' + lines())
                    quit()
            else:
                if len(tokens) == 3: # periptwsh poy dex exoyme block meta3y twn program kai endprogram
                    print('error: there is no code between program and endprogram in line:' + lines())
                    quit()
        
        block(tokens[1][1])
        
    token_index+=1
    genquad('halt')
    genquad('end_block',tokens[1][1])
    from_quad_to_assembly(quad_List[-2],tokens[1][1])
    from_quad_to_assembly(quad_List[-1],tokens[1][1])

    global counter


    E_place =''
    F_place = ''
    T_place = ''
    ID_place = ''
    B_true = []
    B_false = []
    Q_true = []
    Q_false = []
    R_true = []
    R_false = []
    COND_true = []
    COND_false = []


    def program():
        token=connectSyntaxLex()
        if (token == progtk):
            token = connectSyntaxLex()
            if (token == idtk):
                token = connectSyntaxLex()
                if (token == leftCurlyBrackettk):
                    genquad('begin_block',token,'_','_')
                    block()
                    genquad('halt','_','_','_')
                    genquad('end_block',token,'_','_')
                    token = connectSyntaxLex()
                    if (token == rightCurlyBrackettk):
                        pass
                    else:
                        print("Error: The '}' expected")
                else:
                    print("Error: The '{' expected")
            else:
                print("Error: The Program id expected")
        else:
            print("Error: The keyword 'program' expected")
        
    def block():
        declarations()
        subprograms()
        statements()

    def declarations():
        connectSyntaxLex()
        if (token == leftRoundBrackettk):
            declare()
            token = connectSyntaxLex()
            if (token == declaretk):
                varlist()
                token = connectSyntaxLex()
                if (token == greekqmtk):
                    token = connectSyntaxLex()
                    if (token == rightRoundBrackettk):
                        pass
                    else:
                        print("Error: The ')' expected")
                else:
                    print("Error: The ';' expected")
            else:
                print("Error: The declaration expected")
        else:
             print("Error: The '(' expected")
             
    
                      
    def varlist():
        token = connectSyntaxLex()
        if (token == idtk):
            token = connectSyntaxLex()
            if (token == leftRoundBrackettk):
                token = connectSyntaxLex()
                while token == idtk: 
                    if (token == idtk):
                        token = connectSyntaxLex()
                        if (token == rightRoundBrackettk):
                            pass
                        else:
                            print ("Error: The ')' expected")
                    else:
                        print("Error: The Varlist name expected")
            else:
                print("Error: The '(' expected")
        else:
            print("Error: The Program id expected")

    def subprograms():
        connectSyntaxLex()
        while token == subprogram:
            token = connectSyntaxLex()
            if (token == leftRoundBrackettk):
                subprogram()
                token = connectSyntaxLex()
                if (token == rightRoundBrackettk):
                    pass
                else:
                    print("Error: The ')' expected")
            else:
                print("Error: The '(' expected")
        return
                
    def subprogram():
        token = connectSyntaxLex()
        if (token == functiontk):
            token = connectSyntaxLex()
            if (token == idtk):
                funcbody()
            else:
                print("Error: The function name expected")
        elif (token == proceduretk):
            token = connectSyntaxLex()
            if (token == idtk):
                genquad('begin_block',token,'_','_')
                funcbody()
                genquad('halt','_','_','_')
                genquad('end_block',fname,'_','_')
            else:
                print("Error: The Procedure name expected")
        elif (token != proceduretk):
            print("Error: The keyword 'procedure' expected")
        elif (token != functiontk):
            print("Error: The keyword 'function' expected")

    def funcbody():
        formalpars()
        token = connectSyntaxLex()
        if (token == leftCurlyBrackettk):
            block()
            token = connectSyntaxLex()
            if (token == rightCurlyBrackettk):
                pass
            else:
                print("Error: The '}' expected")
        else:
            print("Error: The '{' expected")
      
    def formalpars():
        token = connectSyntaxLex()
        if (token == leftRoundBrackettk):
            token = connectSyntaxLex()
            formalparlist()
            if (token == rightRoundBrackettk):
                pass
            else:
                print("Error: The ')' expected")
        else:
            print("Error: The '(' expected")

    def formalparlist():
        formalparitem()
        token = connectSyntaxLex()
        while (token == formalparitemtk):
            if (token == leftRoundBrackettk):
                if (token == komatk):
                    formalparitem()
                    token = connectSyntaxLex()
                    if (token == rightRoundBrackettk):
                        pass
                    else:
                        print("Error: The ',' expected")
                else:
                    print("Error: The ')' expected")
            else:
                print("Error: The '(' expected")
        return
    

    def formalparitem():
        token = connectSyntaxLex()
        if (token == intk):
            token = connectSyntaxLex()
            if ((token not in relations) and (token not in delimeters) and (token not in operators)):
                a = token
                genquad('par', a, 'CV','_')
            else:
                print("Error: The in name expected")
        elif (token == inouttk):
            token = connectSyntaxLex()
            if ((token not in relations) and (token not in delimeters) and (token not in operators)):
                b = token
                genquad('par',b,'CV','_')
            else:
                 print("Error: The inout name expected")
        else:
            return
                
    def statements():
        statement()
        token = connectSyntaxLex()
        if (token == leftCurlyBrackettk):
            statement()
            token = connectSyntaxLex()
            while (token == greekqmtk):
                token = connectSyntaxLex()
                if(token == leftRoundBrackettk):
                    token = connectSyntaxLex()
                    if(token == greekqmtk):
                        statement()
                        token = connectSyntaxLex()
                        if(token == rightRoundBrackettk):
                            pass
                        else:
                            print("Error: The ')' expected")
                    else:
                        print("Error: The ';' expected")
                else:
                    print("Error: The '(' expected")
            return
            if (token == rightCurlyBrackettk):
                pass
            else:
                print("Error: The '}' expected") 
        else:
            print("Error: The '{' expected")

    def statement():
        token = connectSyntaxLex()
        if(token == iftk):   
            ifstat()
        elif(token == whiletk):
            whilestat()
        elif(token == doublewhile):
            doublewhilestat()
        elif(token == looptk):
            loopstat()
        elif(token == exittk):
            exitstat()
        elif(token == inputtk):
            inputstat()
        elif(token == forcasetk):
            forcasestat()
        elif(token == incasetk):
            incasestat()
        elif(token == calltk):
            callstat()
        elif(token == returntk):
            returnstat()
        elif(token == printtk):
            printstat()
        elif(token == assignmenttk):
            assigmentstat()
        return


    def assignmentstat():
        token = connectSyntaxLex()
        if(token == idtk):
            token = connectSyntaxLex()
            if(token == definetk):
                a = expression()
                genquad(':=',a,'_',token)
            else:
                print("Error: The ':=' expected") 
        else:
            print("Error: The assignment name expected") 


    def ifstat():
        token = connectSyntaxLex()
        global B_true, B_false
        if(token == leftRoundBrackettk):
            condition()
            token = connectSyntaxLex()
            if(token == rightRoundBrackettk):
                token = connectSyntaxLex()
                if(token == thentk):
                    statements()
                    backpatch(B_true,nextquad())
                    L = makelist(nextquad())
                    a = genquad('jump','_','_','_')
                    B_false.append(a)
                    elsepart(L)
                else:
                    print("Error: The keyword 'then' expected")
            else:
                print("Error: The ')' expected")
        else:
            print("Error: The '(' expected") 


    def elsepart(x):
        global B_true, B_false
        token = connectSyntaxLex()
        if(token == elsetk):
            statements()
            backpatch(B_false,nextquad())
            backpatch(x,nextquad())
        else:
            pass



    def whilestat():
        global B_true, B_false
        token = connectSyntaxLex()
        if(token == leftRoundBrackettk):
            B_quad=nextquad()
            condition()
            token = connectSyntaxLex()
            if(token == rightRoundBrackettk):
                backpatch(B_true,nextquad())
                statements()
                genquad('jump','_','_',B_quad)
                backpatch(B_false,nextquad())
            else:
                print("Error: The ')' expected") 
        else:
            print("Error: The '(' expected")



    def forcase():
        global B_true, B_false
        token = connectSyntaxLex()
        while token == whentk:
            token = connectSyntaxLex()
            if(token == leftRoundBrackettk):
                B_quad=nextquad()
                condition()
                token = connectSyntaxLex()
                if(token == rightRoundBrackettk):
                    backpatch(B_true,nextquad())
                    token = connectSyntaxLex()
                    if(token == updowntk):
                        statements()
                        genquad('jump','_','_',B_quad)
                        backpatch(B_false,nextquad())
                    else:
                        print("Error: The  ':' expected")
                else:
                    print("Error: The ')' expected")
            else:
                print("Error: The '(' expected")
        if(token == defaulttk):
            token = connectSyntaxLex()
            if(token == updowntk):
                statements()
            else:
                print("Error: The ':' expected")
        else:
            print("Error: The keyword 'default' expected")   



    def returnstat():
        global E_place
        expression()
        genquad('retv',E_place, '_','_')
        


    def callstat():
        token = connectSyntaxLex()
        if ((token not in relations) and (token not in delimeters) and (token not in operators)):
            actualpars()
        else:
            print("Error: the name expected")



    def printstat():
        global E_place
        token = connectSyntaxLex()
        if(token == leftRoundBrackettk):
            expression()
            token = connectSyntaxLex()
            genquad('out', E_place, "_" , "_")
            if (token == rightRoundBrackettk):
                pass
            else:
                print("Error: The ')' expected")
        else:
            print("Error: The '(' expected")



    def inputstat():
        token = connectSyntaxLex()
        if (token == leftRoundBrackettk):
            token = connectSyntaxLex()
            if ((token not in relations) and (token not in delimeters) and (token not in operators)):
                token = connectSyntaxLex()
                if (token == rightRoundBrackettk):
                    genquad('inp',token,'_','_')
                else:
                    print("Error: The ')' expected")
            else:
                print("Error: The input id expected")
        else:
            print("Error: The '(' expected")



    def actualpars():
        token = connectSyntaxLex()
        if (token == leftRoundBrackettk):
            actualparlist()
            token = connectSyntaxLex()
            if (token == rightRoundBrackettk):
                pass
            else:
                print("Error: The ')' epxected")
        else:
            print("Error: The '(' expected")



    def actualparlist():
        actualparitem()
        while(token == connectSyntaxLex()):
            actualparitem()
            token = connectSyntaxLex()
            break
        return



    def actualparitem():
        global E_place
        token = connectSyntaxLex()
        if (token == intk):
            expression()
            token = connectSyntaxLex()
            genquad('par',E_place,'CV','_')
        elif (token == inouttk):
            if ((token not in relations) and (token not in delimeters) and (token not in operators)):
                genquad('par',token,'REF','_')
            else:
                print("Error: The inout name expected")
        elif (token != inouttk):
            print("ERROR!!!The keyword 'inout' expected")
        elif (token != intk):
            print("Error: The keyword 'in' expected")



    def condition():
        global B_true, B_false, Q_true, Q_false
        boolterm()
        B_true  = Q_true
        B_false = Q_false
        while(token == connectSyntaxLex()):
            backpatch(B_false,nextquad())
            boolterm()
            B_true = merge(B_true,Q_true)
            B_false = Q_false
            token = connectSyntaxLex()
            break

        return



    def boolterm():
        global Q_true, Q_false, R_true, R_false
        boolfactor()
        Q_true = R_true
        Q_false = R_false
        while (token == connectSyntaxLex()):
            backpatch(Q_true,nextquad())
            boolfactor()
            Q_false = merge(Q_false,R_false)
            Q_true = R_true
            token = connectSyntaxLex()
            break
        return



    def boolfactor():
        global E_place, B_true, B_false, R_true, R_false
        token = connectSyntaxLex()
        if (token == nottk):
            token = connectSyntaxLex()
            if (token == leftBoxBrackettk):
                condition()
                R_true = B_false
                R_false = B_true
                token = connectSyntaxLex()
                if (token == rightBoxBrackettk):
                    return
                else:
                    print("Error: The ']' expected")
            else:
                print("Error: The '[' expected")
        elif (token == leftBoxBrackettk):
            condition()
            R_true= B_true
            R_false = B_false
            token = connectSyntaxLex()
            if (token == rightBoxBrackettk):
                return
            else:
                print("Error: The ']' expected")
        elif (token != leftBoxBrackettk):
            print("Error: The '[' expected")
        elif (token != nottk):
            print("Error: The keyword 'not' exptected")                    
        else:
            expression()
            p1 = E_place
            relop = relationaloper()
            expression()
            p2 = E_place
            R_true = makelist(nextwuad())
            genquad(relop,p1,p2,'_')
            R_false = makelist(nextquad())
            genquad('jump','_','_','_')
            
            return
        


    def expression():
        global E_place, T_place
        term()
        p1
        p = addopper()
        while op in ['+','-']:
            w = newtemp()
            p = addoper()
            term()
            p2 = T_place
            genquad(p,p1,p2,w)
            p1 = w
            break
        E_place = p1
        return



    def term():
        global T_place
        p1 = factor()
        p = muloper()
        while p in ['*','/']:
            w = newtemp()
            p22 = factor()
            genquad(p,p1,p2,w)
            p1 = w
            break
                
        T_place = p1
        return    



    def factor():
        global E_place
        h = ''
        token = connectSyntaxLex()
        if ((token != leftRoundBrackettk)and (token not in relations) and (token not in delimeters) and (token not in operators)):
            h = token
        elif (token == leftRoundBrackettk):
            expression()
            h = E_place
            token = connectSyntaxLex()
            if (token == rightRoundBrackettk):
                pass
            else:
                print("Error: The ')' expected")
        elif(   token != leftRoundBrackettk):
            print("Error: The '(' expected")
        elif ((token not in relations) and (token not in delimeters) and (token not in operators)):
            genquad(':=','_','_',token)
            idtail()

        return



    def idtail():
        actualpars()
        token = connectSyntaxLex()
        return
    

    def relationaloper():
        token = connectSyntaxLex()
        if (token == equalstk):
            return token
        elif(token == minequaltk):
            return token
        elif(token == maxequualqtk):
            return token
        elif(token == maxtk):
            return token
        elif(token == mintk):
            return token
        elif(token == minmaxtk):
            return token
        else:
            return



    def addoper():
        token = connectSyntaxLex()
        if(token == plustk):
            return token
        elif(token == minustk):
            return token
        else:
            return

    def muloper():
        token = connectSyntaxLex()
        if (token == multtk):
            return token
        elif (token == devidetk):
            return token
        else:
            return

    def optionalsign():
        addoper()
        token = connectSyntaxLex()
        return

syntax(tokens)

