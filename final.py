#GIATSOS GEORGIOS 3202 

import sys
import os

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
returntk = 'return'
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
statementslst=['if','else','while','doublewhile','loop','exit','forcase','incase','call','return','input','print']

math_operations = ('add', 'sub', 'mul', 'div')
branches = ('beq', 'bne', 'blt', 'ble', 'bgt', 'bge')


#useful globals
count=0 
varforc=[]
lextotokens = []
InterCarray = []
scope_count = 0
scope_array = [] 
mainframelength=-1
nq = 0  
vartemp = dict() 
nextvartemp = 1
R_true = 0
R_false= 0

quads = []
counterformips = 0
"""Read File"""
piece = ''
f=input("Enter the file name:")
file=open(f,"r")


""" IC defs"""
def mintointname(x):
    p=[]
    k=x.split()
    for i,j in enumerate( k):
        if j==".":
            p=k[0:i-1]
            
    
    return ''.join(p)
intfilename=mintointname(f)    

def intfile(ic):
    global intfilename
    name= intfilename+'.int'
    intCode=open(name,"w")
    for i in range(len(ic)):
        k=ic[i]
        x=k[1]
        intCode.write(','.join(x)+'\n' or 'null')
    intCode.close()

def cfile(ic):
    global intfilename
    name=intfilename+'.c'
    cCode=open(name,"w")
    cCode.write('#include <stdio.h>'+'\n')
    
    for i in range(len(ic)):
        k=ic[i]
        x=k[1]
        if x[0] in arithmsymbol:
            cCode.write(x[3]+'='+x[1]+x[0]+x[2]+';'+'\n')
        elif x[0]=='jump':
            cCode.write('goto'+' '+x[3]+';'+'\n')
        elif x[0] in  correlationopers:
            cCode.write('if'+'('+x[1]+x[0]+x[2]+')'+' '+'goto'+' '+x[3]+';'+'\n')
        elif x[0]==':=':
            cCode.write(x[3]+'='+x[1]+';'+'\n')
        elif x[0]=='out':
            cCode.write('printf('+x[1]+')'+';'+'\n')
        elif x[0]=='inp':
            cCode.write('scanf('+x[1]+')'+';'+'\n')
        elif x[0]=='ret':
            cCode.write('return'+x[1]+';'+'\n')
       
        
    cCode.close()


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


class Quad():

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
    global nq
    nq=+1
    return nq


def genquad(p, x, y, z):
    genquads=[]
    tempq = nextquad()-1
    quads = [tempq, [p,x,y,z]]
    InterCarray.append(genquads)
    return tempq


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
    global quad_code
    for quad in quads:
        if quad.label in l1:
          quad.res = z



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
            assembly_file.write('    j 		L_t%d\n'%(L_counter))
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
    



def lex():
    
    print('mpike lex')
    #global tokens
    
    
     
    def readInpiecies(file):#"""Read file after opening line by line"""   
            ret=[]
            print('reading file')
          
            while True:
                data=file.readlines()
                
                if not data:
                    break
                yield data
                
                
    
   



    
    
   
#"""helping fucntion"""               
    def splithlp(word): 
        return [char for char in word]
        
    def remove_comm(l):
        for i in  range(len(l)):
            if(l[i]=='/'):
                print('anagnorizei//')
                k=1
                s=1
                prev=''
            elif l[i]=='\n' :
                print('anagnorizei n')
                k=0
                s=0
                prev=''
            elif(prev=='/' and l[i]=='*'and s==0):
                k=1
                s=1
                prev=''
            elif(prev=='*' and l[i]=='/')and s==1:
                 k=0
                 s=0
#"""helping function. Removes Excess stuff because of a bug at stateEngine"""
    def removeExcess(array):
        tokens=[]
        tokens=array
        print(array)
        print('in remove excess')
        for i in range(0,len(tokens)-1):
            print('in remove excess '+tokens[i]+' '+tokens[i+1])
            if tokens[i]==':=' and tokens[i+1]=='=':
                tokens[i+1]=''
            elif tokens[i]=='<>' and tokens[i+1]=='>':
                tokens[i+1]=''
            elif tokens[i]=='<=' and tokens[i+1]=='=':
                tokens[i+1]=''
            elif tokens[i]=='>=' and tokens[i+1]=='=':
                print('remove =')
                tokens[i+1]=''
            else:
                pass
                
        return removeSpace(tokens)    
#"""stateEngine function. Produces tokens. """
    #TODO: Fix issue with wrong order of tokens.
    def stateEngine(array):
        s=""
        n=''
        st=''
        tokenshlp=[]
        global tokens
        tokens=[] 
        for i in range(0,len(array)):
            
                         
                if array[i]  in letters :
                    s=s+array[i]
                    #print('mpike'+' '+array[i])
                elif array[i] in numbers:
                    if array[i-1] in letters:
                        
                        s=s+array[i]
                    else:
                        n=n+array[i]
                        if int(n)>32767 or int(n)<-32767:

                            numb=n
                            print('Error int {numb} out of bounds')
                
                else:
                   
                    tokenshlp.append(s)
                    tokenshlp.append(n)
                    
                    if ((array[i] in math_symbols) or  (array[i] in  relations) or  (array[i] in  delimeters) or  (array[i] in  operators) ):
                        print('in se ')
                        #print( array[i] +' '+ array[i+1])
                        if array[i]==':' and array[i+1]=='=':
                            st=':='
                            print('in se :=')
                            #i=i+2
                        elif  array[i]=='<' and array[i+1]=='>':
                            st='<>'
                            print('in se <>')
                            #i=i+2
                        elif array[i]=='<' and array[i+1]=='=':
                            st='<='
                            print('in se <=')
                            #i=i+2
                        elif  array[i]=='>' and array[i+1]=='=':
                            st='>='
                            print('in se >=')
                            #i=i+2
                        else:
                            st=array[i]
                            print('in se '+array[i])
                        tokenshlp.append(st)
                        print('appended'+st)
                    n=''
                    s=""
                    st=''
                    continue
        tokens=removeExcess(removeSpace(tokenshlp))
                 





    
#"""Helping Function: Removes white char"""      
    def removeSpace(array):
        tokens=[]
        for i in range(0,len(array)):
            if array[i]==' ' or array[i]=='':
                pass
            else:
                tokens.append(array[i])
        #print(tokens)
        return tokens        
        
#"""shapedata function: Shapes data so they can be easily used by stateEngine"""
#TODO: FIX ignore comment issue
    def shapedata(piece):#
        #print('mpike spacedata')
        array=[]
        changeline='\n'
        archar=splithlp(piece)
        #print(archar)
        counterspace=0
        counter=0
        Flagst1=''
        end1=''
        st2=''
        end2=''
        k=0
        s=0
        f=''
        prev=''
        
        for i in range(0, len(archar)):
            
            

           
                        
            if(archar[i]=='/'):
                print('anagnorizei//')
                k=1
                s=1
                prev=''
            elif archar[i]=='\n' :
                print('anagnorizei n')
                k=0
                s=0
                prev=''
            elif(prev=='/' and archar[i]=='*'and s==0):
                k=1
                s=1
                prev=''
            elif(prev=='*' and archar[i]=='/')and s==1:
                 k=0
                 s=0
                 
                        
                
            while k==0:
                    array.append(archar[i])
                    prev=archar[i]
                    break 
            
            
            
                    
                    
                    
            
        final='\n'.join(map(str, ''.join(array).replace('\t','').replace(' ','^').replace('\n','').strip().split('\n')))#anorthodox way but it works
        stateEngine(splithlp(final))            
        
        #print('\n'.join(map(str, ''.join(array).replace('\t','').replace(' ','^').replace('\n','').strip().split('\n')))+' '+'ayto [airnei i state apo shape') 
        #print(final)
        
   
    
     
    for piece in readInpiecies(file):
        shapedata(piece)
        
    
    print(tokens)
    return tokens


    
#finaltoken = [lex()]
#counter = 0                               
#"""Start of Syntax"""            
              
def syntax():
    
    global  count

    #"""IC helping var"""
    idplace=''
    Eplace=''#addoper
    Tplace=''#muloper
    Fplace=''
    Btrue=[]
    Bfalse=[]
    Qtrue=[]
    Qfalse=[]
    Rtrue=[]
    Rfalse=[]
    condtrue=[]
    condfalse=[]
    
    
    tokenlst=lex()

    def program():
        print('mpike progrAM')
        global count
        token=tokenlst[count]
        count+=1
        print(token)
        
        if (token == progtk):
            print('mpike IF PROGRAM TK')
            token = tokenlst[count]
            count+=1
            if (isinstance(token,str)==True):
                #continue
                name=token
                print('mpike program if idtk'+" "+token)
                token=tokenlst[count]
                count+=1
                print(token)
                if (token == leftCurlyBrackettk):
                    genquad('begin_block',name,'_','_')
                    block()
                    genquad('halt','_','_','_')
                    genquad('end_block',name,'_','_')
                    token = tokenlst[count]
                    count+=1
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
        print('mpike block')
        declarations()
        subprograms()
        statements()


    def declarations():
        print('mpike declarations')
        global count
        token=tokenlst[count]
        count+=1
        if (token == declaretk):
            print('(token == declaretk)')
            varlist()
            token=tokenlst[count]
            count+=1
            if (token == greekqmtk):
                return           
            else:
                print("ERROR!!!The ';' expected")             
        else:
            print("ERROR!!!The declariation expected")
            return
             
    
                      
    def varlist():
        print('varlist')
        global count
        token1=tokenlst[count]
        count+=1
        if (isinstance(token1,str)== True and token1 in relations or  token1  in  delimeters or token1  in  operators or token1 in commited_words):#prepei na einai str alla oxi symbol
            count-=1
            return ""
            print('not var')
        
        elif (isinstance(token1,str)==True and token1 not in relations and  token1 not in  delimeters and token1 not in  operators and token1 not in commited_words):#prepei na einai str alla oxi symbol
            print(token1)
            token2=tokenlst[count]
            count+=1
            
            print('var ok'+' '+token2)    
            while token2==',':
                    print('var while bef'+' '+token2)
                    token3=tokenlst[count]
                    count+=1
                    print('var while after'+' '+token3)
                    if ((isinstance(token3,str)==True) and (token3 not in relations) and  (token3 not in  delimeters) and (token3 not in  operators)and (token3 not in  commited_words)):
                        varforc.append(token3)
                        token2=tokenlst[count]
                        count+=1
                        if token2==';':
                            count-=1
                        print('var if str ok + token after'+'  '+ token2)
                    else:
                        print("ERROR!!! name expected")
                        continue
                
                    break
                    print('break')
                    
        else:
            print("ERROR!!!Program name expected")


    def subprograms():
        global count,token
        token = tokenlst[count]
        while (token == functiontk or token==proceduretk):
            print('subms while')
            subprogram(token)
            count+=1
            break
        count-=1
                
    def subprogram(t):
        global count
        if (t == functiontk):
            count+=1  
            token = tokenlst[count]
            count+=1         
            if ((isinstance(token,str)==True) and (token not in relations) and  (token not in  delimeters) and (token not in  operators)):
                fname= token
                genquad('begin_block',fname,'_','_')
                funcbody()
               
                genquad('end_block',fname,'_','_')
            else:
                print("ERROR!!!The function name expected")
           
        elif (t == proceduretk):
            token=tokenlst[count]
            count+=1
            if ((isinstance(token,str)==True) and (token not in relations) and  (token not in  delimeters) and (token not in  operators)):
                #t2 = lex()
                pname= token
                genquad('begin_block',pname,'_','_')
                funcbody()
                
                genquad('end_block',pname,'_','_')
            else:
                print ("ERROR!!!Procedure name expecte")
        elif (t != proceduretk):
            print("ERROR!!!The keyword 'procedure' expected")        
        elif (t != functiontk):
            print("ERROR!!!The keyword 'function' expected")

    def funcbody():
        global count
        formalpars()
        token = tokenlst[count]
        count+=1
        if (token == leftCurlyBrackettk):
            block()
            token = tokenlst[count]
            count+=1
            if (token == rightCurlyBrackettk):
                pass
            else:
                print("Error: The '}' expected")
        else:
            print("Error: The '{' expected")
      
    def formalpars():
        global count
        token = tokenlst[count]
        count+=1
        if (token == leftRoundBrackettk):
            formalparlist()
            token = tokenlst[count]
            count+=1
            if (token == rightRoundBrackettk):
                pass
            else:
                print("Error: The ')' expected")
        else:
            print("Error: The '(' expected")

    def formalparlist():
        global count
        
        formalparitem()
        token1=tokenlst[count]
        count+=1
        print('in formal par list bef while '+ token1)
        while token1 == ',' :
            
                
            
            formalparitem()
            token1=tokenlst[count]
            count+=1
            #break
        count-=1
    

    def formalparitem():
        global count
        token1=tokenlst[count]
        count+=1
        print('in formalpar item '+token1)
        if (token1 == intk):
            print('in in')
            token=tokenlst[count]
            count+=1
            if ((isinstance(token,str)==True) and (token not in relations) and  (token not in  delimeters) and (token not in  operators)):
                idn=token
                genquad('par',idn,'CV','_')
                print('after in '+token)
            else:
                print("ERROR!!!The in name expected")
        
        elif (token1 == inouttk):
            print('in inout')
            token=tokenlst[count]
            count+=1
            if((isinstance(token,str)==True) and (token not in relations) and  (token not in  delimeters) and (token not in  operators)):
                idn2=token
                genquad('par',idn2,'REF','_')
            else:
                 print("ERROR!!!The inout name expected")
        elif (token1 != intk):
            print("ERROR!!!The keyword 'in' expected")         
        elif (token1 != inout):
            print("ERROR!!!The keywortd 'inout' expected")
                
    def statements():
        global count
        print('statements')
        token=tokenlst[count]
        count+=1
        print('statements token bef if'+' '+token)
        if token not in statementslst and token != leftCurlyBrackettk:
            print('statements not ok')
            pass

        elif token in statementslst:
            print('statement ok')
            statement()
            
            
        elif(token == '{'):
            print('statement ok')
            statement()
            token2=tokenlst[count]
            count+=1
            while(token2==greekqmtk):
                
                statement()
                token2=tokenlst[count]
                count+=1
                        
                 
                   
                #count-=1    
            
            if(token2=='}'):
                pass
            else:
                print("ERROR!!!The '}' expected ")
        else:
            print("ERROR!!!The '{' expected")


    
    def statement():
        global count
        token = tokenlst[count]
        count+=1
        if(token == iftk):   
            ifstat()
        elif(token == whiletk):
            whilestat()
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
        global count
        token = tokenlst[count]
        count+=1
        if(token == idtk):
            token = tokenlst[count]
            count+=1
            if(token == definetk):
                a = expression()
                genquad(':=',a,'_',token)
            else:
                print("Error: The ':=' expected") 
        else:
            print("Error: The assignment name expected") 


    def ifstat():
        global count
        token = tokenlst[count]
        count+=1
        global B_true, B_false
        if(token == leftRoundBrackettk):
            condition()
            token = tokenlst[count]
            count+=1
            if(token == rightRoundBrackettk):
                token = tokenlst[count]
                count+=1
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
        global B_true, B_false, count
        token = tokenlst[count]
        count+=1
        if(token == elsetk):
            statements()
            backpatch(B_false,nextquad())
            backpatch(x,nextquad())
        else:
            pass



    def whilestat():
        global B_true, B_false, count
        token = tokenlst[count]
        count+=1
        if(token == leftRoundBrackettk):
            B_quad=nextquad()
            condition()
            token = tokenlst[count]
            count+=1
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
        global B_true, B_false, count
        token = tokenlst[count]
        count+=1
        while token == whentk:
            token = tokenlst[count]
            count+=1
            if(token == leftRoundBrackettk):
                B_quad=nextquad()
                condition()
                token = tokenlst[count]
                count+=1
                if(token == rightRoundBrackettk):
                    backpatch(B_true,nextquad())
                    token = tokenlst[count]
                    count+=1
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
            token = tokenlst[count]
            count+=1
            if(token == updowntk):
                statements()
            else:
                print("Error: The ':' expected")
        else:
            print("Error: The keyword 'default' expected")   



    def returnstat():
        global E_place, count
        expression()
        t = Eplace
        genquad('retv',t, '_','_')
        


    def callstat():
        global count
        token = tokenlst[count]
        count+=1
        if ((token not in relations) and (token not in delimeters) and (token not in operators)):
            actualpars()
        else:
            print("Error: the name expected")



    def printstat():
        global E_place, count
        token = tokenlst[count]
        count+=1
        if(token == leftRoundBrackettk):
            expression()
            token = tokenlst[count]
            count+=1
            genquad('out', E_place, "_" , "_")
            if (token == rightRoundBrackettk):
                pass
            else:
                print("Error: The ')' expected")
        else:
            print("Error: The '(' expected")



    def inputstat():
        global count
        token = tokenlst[count]
        count+=1
        if (token == leftRoundBrackettk):
            token = tokenlst[count]
            count+=1
            if ((token not in relations) and (token not in delimeters) and (token not in operators)):
                token = tokenlst[count]
                count+=1
                if (token == rightRoundBrackettk):
                    genquad('inp',token,'_','_')
                else:
                    print("Error: The ')' expected")
            else:
                print("Error: The input id expected")
        else:
            print("Error: The '(' expected")



    def actualpars():
        global counnt 
        token = tokenlst[count]
        count+=1
        if (token == leftRoundBrackettk):
            actualparlist()
            token = tokenlst[count]
            count+=1
            if (token == rightRoundBrackettk):
                pass
            else:
                print("Error: The ')' epxected")
        else:
            print("Error: The '(' expected")



    def actualparlist():
        global count
        actualparitem()
        token = tokenlst[count]
        count+=1
        actualparitem()
        while(token == tokenlst[count]):
            actualparitem()
            token = tokenlst[count]
            count+=1
            break
        return



    def actualparitem():
        global E_place, count
        token = tokenlst[count]
        count+=1
        if (token == intk):
            expression()
            token = tokenlst[count]
            count+=1
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
        global B_true, B_false, Q_true, Q_false, count
        boolterm()
        B_true  = Q_true
        B_false = Q_false
        token = tokenlst[count]
        while(token == tokenlst[count]):
            backpatch(B_false,nextquad())
            boolterm()
            B_true = merge(B_true,Q_true)
            B_false = Q_false
            token = tokenlst[count]
            count+=1
            break

        return



    def boolterm():
        global Q_true, Q_false, R_true, R_false
        global count
        boolfactor()
        Q_true = R_true
        Q_false = R_false
        token = tokenlst[count]
        while (token == andtk):
            backpatch(Q_true,nextquad())
            toke = lex()
            boolfactor()
            Q_false = merge(Q_false,R_false)
            Q_true = R_true
            token = tokenlst[count]
            count+=1
            break
        return



    def boolfactor():
        global E_place, B_true, B_false, R_true, R_false
        token = tokenlst[count]
        if (token == nottk):
            token = tokenlst[count]
            if (token == leftBoxBrackettk):
                condition()
                R_true = B_false
                R_false = B_true
                token = tokenlst[count]
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
            token = tokenlst[count]
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
        token = tokenlst[count]
        if ((token != leftRoundBrackettk)and (token not in relations) and (token not in delimeters) and (token not in operators)):
            h = token
        elif (token == leftRoundBrackettk):
            expression()
            h = E_place
            token = tokenlst[count]
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
        token = tokenlst[count]
        if t=='(':
            for i in range(len(InterCarray)):
                if thlp == i:
                    actualpars()
                    InterCarray[i][1]='??'
        return
    

    def relationaloper():
        token = tokenlst[count]
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
        token = tokenlst[count]
        if(token == plustk):
            return token
        elif(token == minustk):
            return token
        else:
            return

    def muloper():
        token = tokenlst[count]
        if (token == multtk):
            return token
        elif (token == devidetk):
            return token
        else:
            return

    def optionalsign():
        addoper()
        token = tokenlst[count]
        return
    program()
syntax()
file.close()

intfile(InterCarray)
cfile(InterCarray)

print(InterCarray) 

