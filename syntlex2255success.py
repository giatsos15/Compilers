#Vampiris Dimitrios 3186
#Zioudas Konstantinos 3225
#[1.2.0] - 2020-03-03
#based on Η γραμματική της minimal++.v1.2
##Changed
#-<call-stat> as asked
#_<factor>
##Added
#-<idtail>
#[1.1.0] - 2020-02-26
#based on Η γραμματική της minimal++.v1.1
##Changed
#-<call-stat> as asked
#-<factor>  as asked
##Removed
#-<idtail> as asked
##debugging
#[1.0.0] - 2020-02-20
##all arrays are lists array names given for our own convenience


programtk = 'program'

LeftBratk = '{'
RightBratk = '}'
LeftPartk = '('
RightPartk = ')'
declaretk = 'declare'
notdeclaretk = 'notdeclare'
char1 = ';'
functiontk = 'function'
proceduretk = 'procedure'
formalparstk = 'formalist'
assigmenttk = ':='
formalparitemtk = 'formalparitem'
intk = 'in'
inouttk = 'inout'
calltk = 'call'
printtk = 'print'
inputtk = 'input'
thentk = 'then'
iftk = 'if'
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
char2tk = ':'
defaulttk = 'default'
incasetk = 'incase'
boolfactortk = 'boolfactor'
whentk = 'when'
nottk = 'not'
returntk = 'return'
LeftBrackettk = '['
RightBrackettk = ']'
addopertk = 'addo-oper'
termtk = 'term'
mulopertk = 'mul-oper'
factortk = 'factor'
equalstk = '='
mineqtk = '<='
maxeqtk = '>='
mintk = '<'
maxtk = '>'
minmaxtk = '<>'
plustk = '+'
minustk = '-'
multitk = '*'
dividetk = '/'

alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=['0','1','2','3','4','5','6','7','8','9']
arithmsymbol=['+','-','*','/']
correlationopers=['<','>','=','<=','>=','<>']
assignmentSymbol=":="
seperators=[';',',',':']
groupingopers=['(',')','{','}','[',']']
commseps=['/*','*/','//']
keywords=['program','declare','function','procedure','in','inout','if','else','while','doublewhile','loop','exit','forcase','incase','when','default','not','and','or','call','return','input','print']
statementslst=['if','else','while','doublewhile','loop','exit','forcase','incase','call','return','input','print']
linenum=0
 
nq=0
count=0#for syntax
varforc=[]
helpIC = []
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

def nextquad():
    global nq
    nq+=1
    return nq

def genquad(op,x,y,z):
    
    global helpIC
    
    lstForGenquad=[]#dimiourgi lista 5don tin etiketa kai ta op x y z
    t=nextquad()-1
    lstForGenquad=[t,[op,x,y,z]] #pinakas [etiketa,[tetrada]]
    helpIC.append(lstForGenquad) 
    
    return t 

def newtemp():
    t=''
    return t
    

def emptylist():
    emptylist = []

    return emptylist

def makelist(x):
    t=[x]
    return t

def merge(l1,l2):
    retlist=[]
    retlist = l1+l2
    
    return retlist

def backpatch(l1,z):
    #l1 lista me deiktes se tetrades xoris z simpliromeno
    # episkepsi mia mia tis tetrades kai simplirosi tou z se autes
    for i in l1:
        for j in range(len(helpIC)):
            if i==helpIC[j]:
                helpIC[j+1][3]=z

    return
"""start of lex"""

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
                
                #print ( data )
    
   



    
    
   
#"""helping fucntion"""               
    def splithlp(word): 
        return [char for char in word]
        
    def remove_comm(l):
        for i in  range(len(l)):
            if(l[i]=='/'):
                print('anagnorise//')
                k=1
                s=1
                prev=''
            elif l[i]=='\n' :
                print('anagnorise n')
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
        for i in range(0,len(tokens)-1):
            if tokens[i]==':=' and tokens[i+1]=='=':
                tokens[i+1]=''
            elif tokens[i]=='<>' and tokens[i+1]=='>':
                tokens[i+1]=''
            elif tokens[i]=='<=' and tokens[i+1]=='=':
                tokens[i+1]=''
            elif tokens[i]=='>=' and tokens[i+1]=='=':
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
            
                         
                if array[i]  in alphabet :
                    s=s+array[i]
                    #print('mpike'+' '+array[i])
                elif array[i] in num:
                    if array[i-1] in alphabet:
                        
                        s=s+array[i]
                    else:
                        n=n+array[i]
                        if int(n)>32767 or int(n)<-32767:

                            numb=n
                            print('Error int {numb} out of bounds')
                
                else:
                   
                    tokenshlp.append(s)
                    tokenshlp.append(n)
                    
                    if ((array[i] in arithmsymbol) or  (array[i] in  correlationopers) or  (array[i] in  seperators) or  (array[i] in  groupingopers) ):
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
        tokens=removeExcess(tokenshlp)
                 





    
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
                print('anagnorise//')
                k=1
                s=1
                prev=''
            elif archar[i]=='\n' :
                print('anagnorise n')
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
        #count+=1
        print(token)
        if ( token== programtk):
                print('mpike IF PROGRAM TK')
                
                #continue
                #counter = counter + 1
                #tokens[0] = lex()
                count+=1
                token=tokenlst[count]
                
                if (isinstance(token,str)==True):
                    #continue
                    name=token
                    print('mpike program if idtk'+" "+token)
                    count+=1
                    token=tokenlst[count]
                    
                    print(token)
                    if (token == LeftBratk):
                        genquad('begin_block',name,'_','_')
                        block()
                        genquad('halt','_','_','_')
                        genquad('end_block',name,'_','_')
                        token=tokenlst[count]
                        count+=1
                        #block(tokens[i:len(tokens)-1])
                        if (token == RightBratk):
                            """tokens[len(tokens)-1] = lex()
                            print('t pou tha parei i block')
                            print(tokens[3:len(tokens)-1])
                            block(tokens[3:len(tokens)-1])"""
                            return
                        else:
                             print("ERROR!!!The '}' expected)"+' '+token)
                    else:
                        print("ERROR!!!The '{' expected")
                else:
                    print("ERROR!!!Program name expected")
        else:
                print("ERROR!!!The keyword 'program' expected")
    
    #<block> ::= <declarations> <subprograms> <statements>
    def block():
        print('mpike block')
        declariations()
        subprograms()
        statements()
        
            
    #<declarations> ::= (declare <varlist>;)*

    def declariations():
        print('mpike declarations')
        global count
        token=tokenlst[count]
        count+=1
          
        if (token == declaretk):
                    print('(token == declaretk)')
                    varlist()
                    token=tokenlst[count]
                    count+=1
                    if (token == char1):
                       
                        return    
                        
                        
                    else:
                        print("ERROR!!!The ';' expected")
                        return
        else:
                print("ERROR!!!The declariation expected")
                return

    #<varlist> ::= | id ( , id )*            
    def varlist():
        print('varlist')
        global count
        global varforc
        token1=tokenlst[count]
        count+=1
        if (isinstance(token1,str)== True and token1 in correlationopers or  token1  in  seperators or token1  in  groupingopers or token1 in keywords):#prepei na einai str alla oxi symbol
            count-=1
            return ""
            print('not var')
        
        elif (isinstance(token1,str)==True and token1 not in correlationopers and  token1 not in  seperators and token1 not in  groupingopers and token1 not in keywords):#prepei na einai str alla oxi symbol
            print(token1)
            token2=tokenlst[count]
            count+=1
            
            print('var ok'+' '+token2)    
            while token2==',':
                    print('var while bef'+' '+token2)
                    token3=tokenlst[count]
                    count+=1
                    print('var while after'+' '+token3)
                    if ((isinstance(token3,str)==True) and (token3 not in correlationopers) and  (token3 not in  seperators) and (token3 not in  groupingopers)and (token3 not in  keywords)):
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

    #<subprograms> ::= (<subprogram>)*

    def subprograms():
        global count
        global token1
        print('sub/ms')
        token1=tokenlst[count]
        count+=1
        print('token subms bef while'+' '+token1)
        while token1 == functiontk or token1==proceduretk:
            print('subms while')
            subprogram(token1)
            break        
        count-=1     
              
    #<subprogram> ::= function id <funcbody> | procedure id <funcbody>            
    def subprogram(t):
        global count
        print('sub/m')
        if (t == functiontk):
            token=tokenlst[count]
            count+=1
            if ((isinstance(token,str)==True) and (token not in correlationopers) and  (token not in  seperators) and (token not in  groupingopers)):
                fname= token
                genquad('begin_block',fname,'_','_')
                funcbody()
               
                genquad('end_block',fname,'_','_')
            else:
                print("ERROR!!!The function name expected")
           
        elif (t == proceduretk):
            token=tokenlst[count]
            count+=1
            if ((isinstance(token,str)==True) and (token not in correlationopers) and  (token not in  seperators) and (token not in  groupingopers)):
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
        
           
    #<funcbody> ::= <formalpars> { <block> }
    def funcbody():
            global count
            formalpars()
            token=tokenlst[count]
            count+=1
            if (token == LeftBratk):
                block()
                token=tokenlst[count]
                count+=1
                if (token == RightBratk):
                    pass
                else:
                    print ("ERROR!!!The '}' expected")
            else:
                print("ERROR!!!The '{' expected")
      
    #<formalpars> ::= ( <formalparlist> )

    def formalpars():
        global count
        token=tokenlst[count]
        count+=1
        if (token == LeftPartk):
            
            formalparlist()
            token=tokenlst[count]
            count+=1
            if (token == RightPartk):
                pass 
            else:
                print ("ERROR!!!The ')' expected formalpars")
        else:
            print("ERROR!!!The '(' expectedformalpars")
            
    #<formalparlist> ::= <formalparitem> ( , <formalparitem> )* | 
    def formalparlist():
        global count
        
        formalparitem()
        token1=tokenlst[count]
        count+=1
        while token1 == ',' :
            
                
            
            formalparitem()
            token1=tokenlst[count]
            count+=1
            break
            count-=1
           
           
        
                
    #<formalparitem> ::= in id | inout id 
    def formalparitem():
        global count
        token1=tokenlst[count]
        count+=1
        if (token1 == intk):
            token=tokenlst[count]
            count+=1
            if ((isinstance(token,str)==True) and (token not in correlationopers) and  (token not in  seperators) and (token not in  groupingopers)):
                idn=token
                genquad('par',idn,'CV','_')
                
            else:
                print("ERROR!!!The in name expected")
        
        elif (token1 == inouttk):
            token=tokenlst[count]
            count+=1
            if((isinstance(token,str)==True) and (token not in correlationopers) and  (token not in  seperators) and (token not in  groupingopers)):
                idn2=token
                genquad('par',idn2,'REF','_')
            else:
                 print("ERROR!!!The inout name expected")
        elif (token1 != intk):
            print("ERROR!!!The keyword 'in' expected")         
        elif (token1 != inout):
            print("ERROR!!!The keywortd 'inout' expected")
            

    #<statements> ::= <statement> | { <statement> ( ; <statement> )* }
    def statements():#edo prepei na vroume tropo na diaxiristoume tin pithanotita or | 
        global count
        print('statements')
        token=tokenlst[count]
        count+=1
        print('statements token bef if'+' '+token)
        if token not in statementslst and token != LeftBratk:
            print('statements not ok')
            pass

        elif token in statementslst:
            print('statement ok')
            statement()
            
            
        elif(token == LeftBratk):
            print('statement ok')
            statement()
            token2=tokenlst[count]
            count+=1
            while(token2==char1):
                
                statement()
                token2=tokenlst[count]
                count+=1
                        
                 
                break    
                count-=1    
            
            if(token2==RightBra):
                pass
            else:
                print("ERROR!!!The '}' expected")
        else:
            print("ERROR!!!The '{' expected")



    #<statement> ::= <assignment-stat> |<if-stat> |<while-stat> |<doublewhile-stat> |<loop-stat> |<exit-stat> |<forcase-stat> |<incase-stat> |<call-stat> |<return-stat> |<input-stat> |<print-stat>         
    def statement():
        print('in statement')
        global count
        count-=1
        token=tokenlst[count]
        print('in statement token'+' '+token)
        #count+=1
        if(token==assigmenttk):#themataki me :=
            
            assigment_stat()
        elif(token==iftk):
                
            if_stat()
        elif(token==whiletk):
            
            while_stat()
        elif(token==doublewhiletk):
            
            doublewhile_stat()
        elif(token==looptk):
            
            loop_stat()
        elif(token==exittk):
            
            exit_stat()
        elif(token==forcasetk):
            
            forcase_stat()
        elif(token==incasetk):
            
            incase_stat()
        elif(token==calltk):
            
            call_stat()
        elif(token==returntk):
            
            return_stat()
        elif(token==inputtk):
            
            input_stat()
        elif(token==printtk):
            
            print_stat()
        return

    #<assignment-stat> ::= id := <expression>

    def assignment_stat(): #otan lisoume to thema me to := tha einai komple
        global count
        token=tokenlst[count]
        count+=1
        if((isinstance(t1,str)==True) and (t1 not in correlationopers) and  (t1 not in  seperators) and (t1 not in  groupingopers)):
            
            if(t2==assigmenttk):
                
                t=expression()
                genquad(':=',t,'_',t1)
            else:
                print("ERROR!!!The ':=' expected") 
        else:
            print("ERROR!!!The assigment name expected") 

    #<if-stat> ::= if (<condition>) then <statements> <elsepart>

    def if_stat():
        global count
        nonlocal Btrue
        print('in if')
        token=tokenlst[count+1]
        count+=1
        print('in if tokenbef'+' '+token)
        if(token==LeftPartk):
            
            count+=1
            token=tokenlst[count]
            print('in if tokenbef cond'+' '+token)
            condition()
            if(token==RightPartk):
                token=tokenlst[count]
                count+=1
                if(token==thentk):
                    statements()
                    backpatch(Btrue,nextquad())#c theortika oti einai true
                    iflist=makelist(nextquad())
                    
                    k=genquad('jump','_','_','_')
                    Bfalse.append(k)
                    
                    elsepart(iflist)
                else:
                    print("ERROR!!!The keyword 'then' expected")
            else:
                print("ERROR!!!The ')' expected ifstat"+' '+token)
        else:
            print("ERROR!!!The '(' expectedifstat") 

    #<elsepart> ::=  | else <statements>
            # ti tha kanoume me to e to keno xoris else diladi 
    def elsepart(iflist):
        global count
        nonlocal Bfalse
        token=tokenlst[count]
        count+=1
        iflist= iflist
        
        if(token==elsetk):
            statements()
            backpatch(Bfalse,nextquad())
            
            backpatch(iflist,nextquad())

        else:
            
            pass     

    #<while-stat> ::= while (<condition>) <statements>
    def while_stat():
        global count
        nonlocal Btrue, Bfalse
        token=tokenlst[count]
        count+=1
        if(token==LeftPartk):
            Bquad=nextquad()
            condition()
            
            token=tokenlst[count]
            count+=1
            if(token==RightPartk):
                backpatch(Btrue,nextquad())
                statements()#tetrada se periptosi true
               
                genquad('jump','_','_',Bquad)
                backpatch(Bfalse,nextquad())
                
            else:
                print("ERROR!!!The ')' expected while") 
        else:
            print("ERROR!!!The '(' expected while")
        
    """
    This is a multiline
comment.
    #<doublewhile-stat> ::= doublewhile (<condition>) <statements>
    # else <statements>

    def doublewhile_stat():

        
        t1=lex()
        if(t1==LeftPartk):
            Bquad=nextquad()
            condition()
            t1=lex()
            backpatch(t,nextquad())
            genquad('jump','_','_',Bquad)
            if(t3==RightPartk):
                
                t=statements()
                backpatch(t,nextquad())
                genquad('jump','_','_',Bquad)
                
                t1=lex()
                if(t1==elsetk):
                    
                    f=statements()
                    backpatch(f,nextquad())
                else:
                    print("ERROR!!!The keyword 'else' expected") 
                        
                        
            else:
                print("ERROR!!!The ')' expected") 
        else:
            print("ERROR!!!The '(' expected")
        
            

    #<loop-stat> ::= loop <statements>
    def loop_stat():
        
        
        statements()
        
    #<exit-stat> ::= exit
    def exit_stat():#mexri stigmis den xreiazete na kanei kati
        #if(t1==exittk):
         #   t1=lex()
        #else:
         #    print("ERROR!!!The keyword 'exit' expected")
        pass
        """
    #<forcase-stat> ::= forcase
    # ( when (<condition>) : <statements> )*
    # default: <statements> 
    def for_case():
        global count
        nonlocal Btrue,Bfalse                                       
        
            
            
        t3=tokenlst[count]
        count+=1     
        
        while t3==whentk:
            t4=tokenlst[count]
            count+=1
            if(t4==LeftPartk):
                sQuad=nextquad()
                condition()
                t5=tokenlst[count]
                count+=1
                            
                if(t5==RightPartk):
                    t6=tokenlst[count]
                    count+=1
                    if(t6==char2):
                        statements()
                        backpatch(Btrue,sQuad)                            
                    else:
                        print("ERROR!!!The  ':' expected")
                else:
                    print("ERROR!!!The ')' expected for")
            else:
                print("ERROR!!!The '(' expected for")
        
                
        
        if(t3==defaulttk):
            token=tokenlst[count]
            count+=1 
            if(token==char2):
                statements()
                backpatch(Bfalse,nextquad())
            else:
                print("ERROR!!!The ':' expected")
        else:
            print("ERROR!!!The keyword 'default' expected")

        


    '''
    #<incase-stat> ::= incase
    #( when (<condition>) : <statements> )*
    def incase_stat():
                                      #kai auti diorthosi prosoxi me tis parentheseis kai ta when 
        t1=lex()
        while(t1==incasetk):
            if(t2==LeftPartk):
                t2=lex()
                if(t3==whentk):
                    t3=lex()
                    if(t4==lex()):
                        condition()
                        if(t4==RightPartk):
                            token=lex()
                            if(t5==char2):
                                token=lex()
                                statements()
                            else:
                                print("ERROR!!!The  ':' expected")
                        else:
                            print("ERROR!!!The ')' expected")
                    else:
                        print("ERROR!!!The '(' expected")
                else:
                    print("ERROR!!!The keyword 'when' expected")
            else:
                print("ERROR!!!The '(' expected")
         
                
    
        

    '''
    #<return-stat> ::= return <expression>
    def return_stat():
            global count
            nonlocal Eplace
            expression()
            t=Eplace
            genquad('retv',t,'_','_')
            
    #<call-stat> ::= call id <actualpars>

    def call_stat():
        global count
       
        t1=tokenlst[count]
        count+=1
        if((isinstance(t1,str)==True) and (t1 not in correlationopers) and  (t1 not in  seperators) and (t1 not in  groupingopers)):
            
            
            actualpars()
            """for i in range(len(t)):
                if t[i][1]==intk:
                    genquad('par',t[i][2],'CV','_')
                elif t[i][1]==inouttk:
                    genquad('par',t[i][2],'REF','_')
            genquad('call',t1,'_','_')"""    
                
                
        else:        
                print("ERROR!!!The call name expected")
        
            
    #<print-stat> ::= print (<expression>)
    def print_stat():
        global count
        nonlocal Eplace
        print('in print')
        count+=1
        t=tokenlst[count]
        print('in print token '+t)
        if(t == LeftPartk):
            
            expression()
            e=Eplace
            count+=1
            t=tokens[count]
            
            if (t == RightPartk):
                genquad('out',e,'_','_')
            else:
                print("ERROR!!!The ')' expected print")
        else:
            print("ERROR!!!The '(' expected print")
       
            
    #<input-stat> ::= input (id)
    def input_stat():
        global count
        
        t1=tokenlst[count]
        count+=1
        if (t1 == LeftPartk):
            t1=tokenlst[count]
            count+=1
            if((isinstance(t1,str)==True) and (t1 not in correlationopers) and  (t1 not in  seperators) and (t1 not in  groupingopers)):
                idn=t1
                t1=tokenlst[count]
                count+=1
                if (t1== RightPartk):
                    genquad('inp',idn,'_','_')
                else:
                    print("ERROR!!!The ')' expected input")
            else:
                print("ERROR!!!The input name expected")
        else:
            print("ERROR!!!The '(' expected input")
    
            
    #<actualpars> ::= ( <actualparlist> ) 
    def actualpars():
        global count
        
        t1=tokenlst[count]
        count+=1
        if (t1 == LeftPartk):
            
            actualparlist()
            t1=tokenlst[count]
            count+=1
            if (t1 == RightPartk):
                pass
            else:
                print("ERROR!!!The ')' epxected actualpars")
            
        else:
            print("ERROR!!!The '(' expected actualpars")
        return  
            
    #<actualparlist> ::= <actualparitem> ( , <actualparitem> )* | 
    def actualparlist():
        global count
        
        actualparitem()
        t1=tokenlst[count]
        count+=1
        while t1 == Comatk :
            
               
            actualparitem()
            t1=tokenlst[count]
            count+=1
            
            break
        count-=1
        return    
    #<actualparitem> ::= in <expression> | inout id
    def actualparitem():
        global count
        nonlocal Eplace
        t1=tokenlst[count]
        count+=1
        if (t1 == intk):
             
             expression()
             e=Eplace
             genquad('par',e,'CV','_')
        
        elif (t1 == inouttk):
                
                t1=tokenlst[count]
                count+=1
                if((isinstance(t1,str)==True) and (t1 not in correlationopers) and  (t1 not in  seperators) and (t1 not in  groupingopers)):
                    genquad('par',t1,'REF','_')
                else:
                    print("ERROR!!!The inout name expected")
        elif (t1 != inout):
            print("ERROR!!!The keyword 'inout' expected")
        elif (t1 != intk):
            print("ERROR!!!The keyword 'in' expected")
        
        return 
    #<condition> ::= <boolterm> (or <boolterm>)*

    def condition():
        global count
        nonlocal Btrue, Bfalse,Qtrue,Qfalse
        print('in condition')
        
        boolterm()
        Btrue=Qtrue
        Bfalse=Qfalse
        #count+=1
        t1=tokenlst[count]
        
        print('in condition token bef while'+' '+t1)
        #count+=1
        while t1 == ortk:
            backpatch(Bfalse,nextquad())
            boolterm()
            Btrue=merge(Btrue,Qtrue)
            Bfalse=Qfalse
            
            t1=tokenlst[count]
            count+=1
            break 
            
        
           
        return 
                
    #<boolterm> ::= <boolfactor> (and <boolfactor>)*

    def boolterm():
        global count
        nonlocal Qtrue,Qfalse,Rtrue,Rfalse
        boolfactor()
        Qtrue=Rtrue
        Qfalse=Rfalse
        t1=tokenlst[count]
        #count+=1
        while t1== andtk :
            backpatch(Qtrue,nextquad())
            boolfactor()
            Qfalse=merge(Qfalse,Rfalse)
            Qtrue=Rtrue
            t1=tokenlst[count]
            count+=1
            break
            count-=1
        return       
    #<boolfactor> ::= not [<condition>] | [<condition>] |<expression> <relational-oper> <expression> 
    def boolfactor():
        global count
        nonlocal Rtrue,Rfalse,Btrue,Bfalse,Eplace
        print('in boolfactor')
        count+=1
        t1=tokenlst[count]
        print('in boolfactor token bef if'+' '+t1)
        #count+=1
        if (t1 == nottk):
            count+=1
            t2=tokenlst[count]
            
            if (t2 == LeftBrackettk):
                
                condition()
                Rtrue=Bfalse
                Rfalse=Btrue
                count+=1
                t2=tokenlst[count]
                
                if (t2 == RightBrackettk):
                    return
                else:
                    print("ERROR!!!The ']' expected")
            else:
                print("ERROR!!!The '[' exptected")
        elif (t1 == LeftBrackettk):
            
            condition()
            Rtrue=Btrue
            Rfalse=Bfalse
            count+=1
            t1=tokenlst[count]
            
                    
            if (t1 == RightBrackettk):
                return
            else:
                print("ERROR!!!The ']' exptected")
        
        
                    
        else:
            count-=1
            expression()
            e1=Eplace
            print('in boolfactor e1')
            relop=relationaloper()
            print('in boolfactor relop')
            
            expression()
            e2=Eplace
            print('in boolfactor e2')
            Rtrue=makelist(nextquad())
            genquad(relop,e1,e2,'_')
            Rfalse=makelist(nextquad())
            genquad('jump','_','_','_')
            
         
            return                
                
            
       
    #<expression> ::= <optional-sign> <term> ( <add-oper> <term>)* 
    def expression():
        global count
        nonlocal Tplace,Eplace
        print('in expr')
        #optionalsign()
        term()
        t1=Tplace
        print('in expr t1'+' '+Tplace)
        op=addoper()
        while op in ['+','-']:
                w=newtemp()
                op=addoper()
                term()
                print('while exp')
                t2=Tplace
                genquad(op,t1,t2,w)
                t1=w
                break
        #count-=1    
        Eplace=t1
        print('in expr Eplace'+' '+Eplace)
        return 
                
    #<term> ::= <factor> (<mul-oper> <factor>)*
    def term():
        global count
        nonlocal Tplace
        print('in term')
        f1=factor()
        print('in term f1'+' '+f1)
        op=muloper()
        while op in ['*','/']:
                w=newtemp()
                print('in term w'+' '+w)
                
                print('in term op'+' '+op)
                f2=factor()
                print('in term f1'+' '+f2)
                genquad(op,f1,f2,w)
                f1=w
                break
                
        Tplace = f1
        print('in term Tplace'+' '+Tplace)
        return    
    #<factor> ::= constant | (<expression>) | id <idtail>
    def factor():
        nonlocal Eplace
        print('in factor')
        global count
        ret=''
        p=0
        t1=tokenlst[count]
        count+=1
        print('in factor token bef if'+' '+t1)
        if t1!= LeftPartk and  (isinstance(t1,str)==True) and (t1 not in correlationopers) and  (t1 not in  seperators) and (t1 not in  groupingopers):
            ret= t1
            p=1
            print('constant'+' '+t1)
            
        elif (t1 == LeftPartk and p==0):
            
            expression()
            ret=Eplace
            
            t2=tokenlst[count]
            count+=1
            print('in factor token after if'+' '+t2)
            if (t2 == RightPartk):
                pass
            else:
                print("ERROR!!!The ')' expected factor"+' '+t2)
        elif(t1 != LeftPartk and p==0):
            print("ERROR!!!The '(' expected factor"+' '+t1)
                
        elif (isinstance(t1,str)==True) and (t1 not in correlationopers) and  (t1 not in  seperators) and (t1 not in  groupingopers):
            thlp=genquad(':=','_','_',t1)
            idtail()
            
        return ret
           
    #<idtail> ::= | <actualpars>

    def idtail(): #kati prepei na kanoume edo
        global count
        t=tokenlst[count]
        count+=1
        if t=='(':
            for i in range(len(helpIC)):
                if thlp == i:
                    actualpars()
                    helpIc[i][1]='??'


    #<relational-oper> ::= = | <= | >= | > | < | <>
    def relationaloper():
        global count
        print('in relop')
        t1=tokenlst[count]
        count+=1
        print('in relop bef if token'+' '+t1)
        if (t1 == equalstk):
            #t1 = lex()
            return t1
        elif (t1 == mineqtk):
            
            #t1 = lex()
            return t1
        elif (t1 == maxeqtk):
            
                #t1 = lex()
            return t1
        elif (t1 == maxtk):
                #t1 = lex()
            return t1
        elif (t1 == mintk):
                #t1 = lex()
            return t1
        elif (t1 == minmaxtk):
                #t1 = lex()
            return t1
        else:
            return
        #elif (t1 != minmaxtk):
         #   print("ERROR!!!The '<>' expected")
        #elif (t1 != mintk):
         #   print("ERROR!!!The '<' expected")
        #elif (t1 != maxtk):
         #   print("ERROR!!!The '>' expected")
        #elif (t1 != maxeqtk):
         #   print("ERROR!!!The '>=' expected")
        #elif (t1 != mineqtk):
         #   print("ERROR!!!The '<=' expected")
        #elif (t1 != equalstk):
           # print("ERROR!!!The '=' expected")

    #<add-oper> ::= + | -

    def addoper():
        global count
        count+=1
        token=tokenlst[count]
        
        if (token == plustk):
            return token
        elif (token==minustk):
            return token
        else:
            count-=1
            
        
            
      
        
    #<mul-oper> ::= * | /

    def muloper():
        global count
        count+=1
        token=tokenlst[count]
        #count+=1
        if (token == multitk):
            return
        elif (token == dividetk):
            return
        else:
            
            count-=1
            
        
    #<optional-sign> ::= | <add-oper>
    #TODO: FIX NOTHING CASE
    def optionalsign():
        
        addoper()
        return 
    program()          
syntax()    
file.close()

intfile(helpIC)
cfile(helpIC)

print(helpIC)  
