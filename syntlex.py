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
 
def lex():
    

    alphabet=['A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num=[0,1,2,3,4,5,6,7,8,9]
    arithmsymbol=['+','-','*','/']
    correlationopers=['<','>','=','<=','>=','<>']
    assignmentSymbol=":="
    seperators=[';',',',':']
    groupingopers=['(',')','{','}','[',']']
    commseps=['/*','*/','//']
    keywords=['program','declare','function','procedure','in','inout','if','else','while','doublewhile','loop','exit','forcase','incase','when','default','not','and','or','call','return','input','print']
    linenum=0





    def readInpiecies(file):#diavazo to arxio se komatia ton 30 xaraktiron
        
        
           
            while True:
                
                data=file.read(30)
                if not data:
                    break
                yield data
                print ( data )
    
   



    
    array = [] #gia tis metavlites
    token = 0
    
   
                
    def splithlp(word): 
        return [char for char in word] 

     


            

    def checkKeyword(a):
        print('mpike check keyword')
        i=0
        keepword=0
        for i in keywords:
            if(a == i):
                keepword=a
            
                return True
            else:
                return False
            
    def checkSeparator( a):
        print('mpike check sep')
        i=0
        keepsep=0
        for i in seperators:
            if(a==i):
                keepsep=a
                return True
            else:
                return False

    def checkArithSymbol(a):
        print('mpike check arithmsymbol')
        i=0
        keepArithSymbol=0
        for i in arithmsymbol:
            if(a==i):
                keepArithSymbol=a
                return True
            else:
                return False

    def checkCorrelatiOper(a):
        print('mpike check correlation')
        i=0
        keepCorrelatiOper=0
        for i in keywords:
            if(a==i):
                keepCorrelatiOper=a
                return True
            else:
                return False

    def checkAssignmentSymbol(a):
        print('mpike checkassisymbol')
        
        if(a==assignmentSymbol):
            
            return True
        else:
            return False




    def checkGroupingOpers(a):
        print('mpike check group')
        i=0
        keepGroupingOpers=0
        for i in groupingopers:
            if(a==i):
                keepGroupingOpers=a
                return True
            else:
                return False    

      
    def checkCommSeps(a):
        print('mpike check seps')
        i=0
        keepCommSeps=0
        for i in commseps:
            if(a==i):
                keepCommSeps=a
                return True
            else:
                return False    

    def checkalphabet(a):
        print('mpike check alphabet')
        i=0
        keepalphabet=0
        for i in alphabet:
            print('foraplha')
            print(i+'ti pairnei i for')
            
            if(i==a):
                print(a='ti pirnei apo state')
                keepalphabet=a
                return True
            else:
                print('ALPHAFALSE')
                return False
           
                

    def checknum(a):
        print('mpike check num')
        i=0
        keepnum=0
        for i in alphabet:
            if(a==i):
                keepnum=a
                return True
            else:
                return False



    def stateEngine(arr):
        state = ''
        token_hashmap={}
        s=[]
        array=splithlp(arr[0])
        n = 0
        for i in range(0, len(array)):
            print(state)
            print('mpike for state engine')
            print('\n')
            print( array[i]+' '+'print mesa stin state')
            state = 'state_0'
            while (state!='OK'and state!='error' and i!='eof'):
                print("bike while stateengine")
                if (state=='state_0' and checkalphabet(array[i]) == True):
                    state='state_1'
                    s.append(array[i])
                    #print(array[i])
                elif (state == 'state_0' and checknum(array[i])==True):
                    state='state_2'
                    s.append(array[i])
                elif (state == 'state_0' and checkArithSymbol(array[i])==True):
                    s.append(array[i])
                    n = 0 #arithmitiko sumbolo meta apo 0
                    state = 'OK'
                elif ( state == 'state_0' and checkCorrelatiOper(array[i])==True):
                    s.append(array[i])
                    if ( s == '<'):
                        state = 'state_3'
                        if(array[i+1] == '='):
                            s.append(array[i])
                            n = 1 # <= 
                            state = 'OK'
                        elif (array[i+1] == '>'):
                            s.append(array[i])
                            n = 1 # <=
                            state = 'OK'
                        else:
                            n = 1 # <
                            state = 'OK'
                    elif ( s== '>'):
                        state = 'state_4'
                        if ( array[i+1] == '='):
                            s.append(array[i])
                            n = 1 # >=
                            state = 'OK'
                        else:
                            n = 1 # >
                            state = 'OK'
                elif(state == 'state_0' and checkSeparator(array[i])==True):
                    s.append(array[i])
                    if (s == ':'):
                        state = 'state_5'
                        if(array[i+1] == '=' ):
                            s.append(array[i])
                            n = 2 # :=
                            state = 'OK'
                        else:
                            state = 'error'
                            print('error1')
                            
                    else:
                        n = 3 # , / ;  
                        state = 'OK'
                elif ( state == 'state_0' and checkGroupingOpers(array[i])==True):
                    s.append(array[i])
                    if (s == '{'):
                        state = 'state_6'
                        if (s == '}'):
                            state = 'state_0'
                        elif ( s == 'eof'):
                            state = 'error'
                            print('error1')
                        else:
                            state = 'state_6'
                    else:
                        n = 4 # ( / )
                        state = 'OK'
                elif ( state == 'state_0' and i=='eof' ):
                    state = 'eof'
                    print('eof1')
                elif ( state == 'state_0'):
                    state = 'error'
                    print('error2')
                elif ( state == 'state_1' and checkalphabet(array[i])==True):
                    s.append(array[i])
                    state = 'state_1'
                elif (state == 'state_1' and checknum(array[i])==True):
                      s.append(array[i])
                      state = 'state_1'
                elif (state == 'state_1' and i =='eof'):
                   state = 'eof'
                   print('eof2')
                elif (state == 'state_1'):
                    i-=1
                    n = 5 # alphabet with or without numbers
                    state = 'OK'
                elif ( state == 'state_2' and ckecknum(array[i])==True):
                    s.append(array[i])
                    state = 'state_2'
                elif (state == 'state_2' and i=='eof'):
                    state = 'eof'
                    print('eof3')
                elif (state == 'state_2'):
                    i-=1
                    n = 6 # numbers
                    state = 'OK'
                elif (state=='state_3' and i=='eof'):
                    state = 'eof'
                    print('eof4')
                elif (state=='state_4' and i=='eof'):
                    state = 'eof'
                    print('eof5')
                elif (state=='state_5'):
                    state='error'
                    print('error3')
                  
            if state == 'state_1' :        
                token_hashmap.put("1",''.join(s))      
        print(state)            
        print(s)
        #print('bgike apo to foroo')
        print(token_hashmap)
            
      

        #def state_1help(c):
        #   while (c in alphabet or c in num):
        #        token.append(c)
        #    return token
        #    state_0(c1)

        #def state_2help(c):
        #   while (c in num and token.length() < 5):
        #       token.append(c)
        #        break
        #        if ( c <= 32767 and c >= (-32767)):
        #           return token 
        #       else:
         #           print("OUT OF BOUNDS")
    def shapedata(piece):#

        changeline= '\n'
        archar=splithlp(piece)
        counterspace=0
        counter=0
        for i in range(0, len(archar)):
            counter +=1
            if ( i+1 > len(archar)):
                 print("Out of bounts at shapedata, 30 char limit exceded")
                 break

            #if(archar[i]==' ' or ((archar[i]==' ' and archar[i+1]==' '))):
             #       counterspace=counterspace+1
             #       while counterspace!=1:
                        
             #           print('malakia')
             #           array.append('^')
                        
            elif(archar[i]=='/'and archar[i+1]=='/'):
                    while(archar[i]!=changeline[0] and archar[i+1]!=changeline[1]):
                                                    pass
            elif(archar[i]=='/' and archar[i+1]=='*'):
                        while(archar[i]!='*' and archar[i+1]!='/'):
                        
                            pass        
            else:
                        print(archar[i]+' '+'shape')           
                        array.append(archar[i])
                        counterspace=0
                        continue
            print(counter)        
        stateEngine(''.join(array).replace('\t','').replace(' ','^').replace('\n','').strip().split(' '))            
        #print(array+' '+'ayto [airnei i state apo shape')
        print('\n'.join(map(str, ''.join(array).replace('\t','').replace(' ','^').replace('\n','').strip().split('\n')))+' '+'ayto [airnei i state apo shape') 





    piece = ''
    f=input("Enter the file name:")
    file=open(f,"r")
    for piece in readInpiecies(file):
        shapedata(piece)
    file.close()                                   
lex()
                                
            
                
def syntax():
    programtk = 'program'
    idtk = 'id'
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
    definetk = ':='
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

    #<program> ::= program id { <block> }
    
    def program(t1,t2,t3,t4):
        if (t1 == programtk):
            t1 = lex()
            if (t2 == idtk):
                t2 = lex()
                if (t3 == LeftBratk):
                    t3 = lex()
                    if (t4 == RightBratk):
                        t4 = lex()
                        block()
                    else:
                        print("ERROR!!!The '}' expected)")
                else:
                    print("ERROR!!!The '{' expected")
            else:
                print("ERROR!!!Program name expected")
        else:
            print("ERROR!!!The keyword 'program' expected")
    
    #<block> ::= <declarations> <subprograms> <statements>
    def block():
        declariations()
        subprograms()
        statements()
    #<declarations> ::= (declare <varlist>;)*

    def declariations(t1,t2,t3,t4):
        while (t1 == declaretk or t1 == notdeclaretk):
          if (t2 == LeftPartk):
                t2 = lex()
                declare()
                if (t1 == declaretk):
                    t1 = lex()
                    varlist()
                    if (t3 == char1):
                        t3 = lex()
                        varlist()
                        if (t4 == RightPartk):
                            t4 = lex()
                        else:
                            print("ERROR!!!The ')' expected")
                    else:
                        print("ERROR!!!The ';' expected")
                else:
                    print("ERROR!!!The declariation expected")
          else:
                print("ERROR!!!The '(' expected")

    #<varlist> ::= | id ( , id )*            
    def varlist(t1,t2,t3):
        
        if (t1 == idtk):
            t1 = lex()
            if (t2 == LeftPartk):
                t2 = lex()
                while t1 == idtk: 
                    if (t1 == idtk):
                        t1 = lex()
                        if (t3 == RightPartk):
                            t3 = lex()
                        else:
                            print ("ERROR!!!The ')' expected")
                    else:
                        print("ERROR!!!Varlist name expected")
            else:
                print("ERROR!!!The '(' expected")
        else:
            print("ERROR!!!Program name expected")

    #<subprograms> ::= (<subprogram>)*

    def subprograms(t1,t2,t3):
        while t1 == subprogram:
            if (t2 == LeftPartk):
                t2 = lex()
                subprogram()
                if (t3 == RightPartk):
                    t3 = lex()
                else:
                    print("ERROR!!!The ')' expected")
            else:
                print ("ERROR!!!The '(' expected")
        return        
    #<subprogram> ::= function id <funcbody> | procedure id <funcbody>            
    def subprogram(t1,t2):
        if (t1 == functiontk):
            t1 = lex()
            if (t2 == idtk):
                t2 = lex()
                funcbody()
            else:
                print("ERROR!!!The function name expected")
           
        elif (t1 == proceduretk):
            t1 = lex()
            if (t2 == idtk):
                t2 = lex()
                funcbody()
            else:
                print ("ERROR!!!Procedure name expecte")
        elif (t1 != proceduretk):
            print("ERROR!!!The keyword 'procedure' expected")        
        elif (t1 != functiontk):
            print("ERROR!!!The keyword 'function' expected")         
        
           
    #<funcbody> ::= <formalpars> { <block> }
    def funcbody(t1,t2):
            formalpars()
            if (t1 == LeftBratk):
                t1 = lex()
                block()
                if (t2 == RightBratk):
                    t2 = lex()
                else:
                    print ("ERROR!!!The '}' expected")
            else:
                print("ERROR!!!The '{' expected")
      
    #<formalpars> ::= ( <formalparlist> )

    def formalpars(t1,t2):
        if (t1 == LeftPartk):
            t1 = lex()
            formalparlist()
            if (t2 == RightPartk):
                t2 = lex()
            else:
                print ("ERROR!!!The ')' expected")
        else:
            print("ERROR!!!The '(' expected")
            
    #<formalparlist> ::= <formalparitem> ( , <formalparitem> )* | 
    def formalparlist(t1,t2,t3,t4):
        formalparitem()
        while t1 == formalparitemtk :
            if (t2 == LeftPartk):
                t2 = lex()
                if(t3==Comatk):
                    t3=lex()
                    formalparitem()
                else:
                    print("ERROR!!!The ',' expected")
                    if (t4 == RightPartk):
                        t4 = lex()
                    else:
                        print("ERROR!!!The ')' expected")
            else:
                print("ERROR!!!The '(' expected")
        return
                
    #<formalparitem> ::= in id | inout id 
    def formalparitem(t1,t2):
        if (t1 == intk):
            t1 = lex()
            if (t2 == idtk):
                t2 = lex()
            else:
                print("ERROR!!!The in name expected")
        elif (t1 != intk):
            print("ERROR!!!The keyword 'in' expected")
        elif (t1 == inouttk):
            t1 = lex()
            if(t2 == idtk):
                t2 = lex()
            else:
                 print("ERROR!!!The inout name expected")
        elif (t1 != intk):
            print("ERROR!!!The keyword 'in' expected")         
        elif (t1 != inout):
            print("ERROR!!!The keywortd 'inout' expected")
            

    #<statements> ::= <statement> | { <statement> ( ; <statement> )* }
    def statements(t1,t2,t3,t4,t5):
        statement()
        if(t1 == LeftBra):
            t1=lex()
            statement()
            while(t3==char1):
                t3=lex()
                
             
                if(t2==LeftPartk):
                    t2=lex()
                    if(t3==char1):
                        t3=lex()
                        statement()
                        if(t4==RightPartk):
                            t4=lex()
                        
                        else:
                            print("ERROR!!!The ')' expected")
                    else:
                        print("ERROR!!!The ';' expected")
                else:
                     print("ERROR!!!The '(' expected")
            return
            if(t5==RightBra):
                t5=lex()
            else:
                print("ERROR!!!The '}' expected")
        else:
            print("ERROR!!!The '{' expected")



    #<statement> ::= <assignment-stat> |<if-stat> |<while-stat> |<doublewhile-stat> |<loop-stat> |<exit-stat> |<forcase-stat> |<incase-stat> |<call-stat> |<return-stat> |<input-stat> |<print-stat>         
    def statement():
        global token
        if(token==assigmenttk):
            token=lex()
            assigment_stat()
        elif(token==iftk):
            token=lex()    
            if_stat()
        elif(token==whiletk):
            token=lex()
            while_stat()
        elif(token==doublewhiletk):
            token=lex()
            doublewhile_stat()
        elif(token==looptk):
            token=lex()
            loop_stat()
        elif(token==exittk):
            token=lex()
            exit_stat()
        elif(token==forcasetk):
            token=lex()
            forcase_stat()
        elif(token==incasetk):
            token=lex()
            incase_stat()
        elif(token==calltk):
            token=lex()
            call_stat()
        elif(token==returntk):
            token=lex()
            return_stat()
        elif(token==inputtk):
            token=lex()
            input_stat()
        elif(token==printtk):
            token=lex()
            print_stat()
        return

    #<assignment-stat> ::= id := <expression>

    def assignment_stat(t1,t2):
        if(t1==idtk):
            t1=lex()
            if(t2==definetk):
                t2=lex()
                expression()
            else:
                print("ERROR!!!The ':=' expected") 
        else:
            print("ERROR!!!The assigment name expected") 

    #<if-stat> ::= if (<condition>) then <statements> <elsepart>

    def if_stat(t1,t2,t3,t4):
        t1=lex()
        if(t2==LeftPartk):
            t2=lex()
            condition()
            if(t3==RightPartk):
                t3=lex()
                if(t4==thentk):
                    t4=lex()
                    statements()
                    elsepart()
                else:
                    print("ERROR!!!The keyword 'then' expected")
            else:
                print("ERROR!!!The ')' expected")
        else:
            print("ERROR!!!The '(' expected") 

    #<elsepart> ::=  | else <statements>
    def elsepart(t1):

        if(t1==elsetk):
            t1=lex()
            statements()

        else:
            print("ERROR!!!The keyword 'else' expected")


    #<while-stat> ::= while (<condition>) <statements>
    def while_stat(t1,t2,t3):

        if(t1==whiletk):
            t1=lex()
            if(t2==LeftPartk):
                t2=lex()
                condition()
                if(t3==RightPartk):
                    t3=lex()
                    statements()
                else:
                    print("ERROR!!!The ')' expected") 
            else:
                print("ERROR!!!The '(' expected")
        else:
            print("ERROR!!!The keyword 'while' expected")
            
    #<doublewhile-stat> ::= doublewhile (<condition>) <statements>
    # else <statements>

    def doublewhile_stat(t1,t2,t3,t4):

        if(t1==whiletk):
            t1=lex()
            if(t2==LeftPartk):
                t2=lex()
                condition()
                if(t3==RightPartk):
                    t3=lex()
                    statements()
                    if(t4==elsetk):
                        t4=lex()
                        statements()
                    else:
                         print("ERROR!!!The keyword 'else' expected") 
                        
                        
                else:
                    print("ERROR!!!The ')' expected") 
            else:
                print("ERROR!!!The '(' expected")
        else:
            print("ERROR!!!The keyword 'doublewhile' expected")
            

    #<loop-stat> ::= loop <statements>
    def loop_stat(t1):
        if(t1==looptk):
            t1=lex()
            statements()
        else:
             print("ERROR!!!The keyword 'loop' expected")

    #<exit-stat> ::= exit
    def exit_stat(t1):
        if(t1==exittk):
            t1=lex()
        else:
             print("ERROR!!!The keyword 'exit' expected")
             
    #<forcase-stat> ::= forcase
    # ( when (<condition>) : <statements> )*
    # default: <statements> 
    def for_case(t1,t2,t3,t4,t5,t6,t7,t8,t9):

        if(t1==forcasetk):
            t1=lex()
            while(t1==forcasetk):
                if(t2==LeftPartk):
                    t2=lex()
                    if(t3==whentk):
                        t3=lex()
                        if(t4==LeftPartk):
                            t4=lex()
                            condition()
                            if(t5==RightPartk):
                                t5=lex()
                                if(t6==char2):
                                    t6=lex()
                                    statements()
                                    if (t7 == RightPartk):
                                        t7=lex()
                                    else:
                                        print("ERROR!!!The ')' expected")
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
            return  
        else:
            print("ERROR!!!The keyword 'forcase' expected")
        if(t8==defaulttk):
            t8=lex()
            if(t9==char2):
                t9=lex()
                statements()
            else:
                print("ERROR!!!The ':' expected")
        else:
            print("ERROR!!!The keyword 'default' expected")

        return


    
    #<incase-stat> ::= incase
    #( when (<condition>) : <statements> )*
    def incase_stat(t1,t2,t3,t4,t5,t6):
        if(t1==incasetk):
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
            return
                
        else:
            print("ERROR!!!The keyword 'incase' expected")
        

    
    #<return-stat> ::= return <expression>
    def return_stat(t1):
        if(t1==returntk):
            t1=lex()
            expression()
        else:
            print("ERROR!!!The keyword 'return' expected")
            
    #<call-stat> ::= call id <actualpars>

    def call_stat(t1,t2,t3,t4):
        if (t1 == calltk):
            t1 = lex()
            if (t2 == idtk):
                t2 = lex()
                if (t3 == LeftPartk):
                    t3 = lex()
                    actualpars()
                    if (t4 == RightPartk):
                        t4 = lex()
                    else:
                        print("ERROR!!!The ')' expected")
                else:
                    print("ERROR!!!The '(' expected")
                
                
            else:        
                print("ERROR!!!The call name expected")
        else:
            print("ERROR!!!The keyword 'call' expected")
            
    #<print-stat> ::= print (<expression>)
    def print_stat(t1,t2,t3):
        if (t1 == printtk):
            t1 = lex()
            if(t2 == LeftPartk):
                t2 = lex()
                expression()
                if (t3 == RightPartk):
                    t3 = lex()
                else:
                    print("ERROR!!!The ')' expected")
            else:
                print("ERROR!!!The '(' expected")
        else:
            print("ERROR!!!The keyword 'print' expected")
            
    #<input-stat> ::= input (id)
    def input_stat(t1,t2,t3,t4):
        if (t1 == inputtk):
            t1 = lex()
            if (t2 == LeftPartk):
                t2 = lex()
                if (t3 == idtk):
                    t3 = lex()
                    if (t4 == RightPartk):
                        t4 = lex()
                    else:
                        print("ERROR!!!The ')' expected")
                else:
                    print("ERROR!!!The input name expected")
            else:
                print("ERROR!!!The '(' expected")
        else:
            print("ERROR!!!The keyword 'input' expected")
            
    #<actualpars> ::= ( <actualparlist> ) 
    def actualpars(t1,t2):
        if (t1 == LeftPartk):
            t1 = lex()
            actualparlist()
            if (t2 == RightPartk):
                t2 = lex()
            else:
                print("ERROR!!!The ')' epxected")
            
        else:
            print("ERROR!!!The '(' expected")
        return
            
    #<actualparlist> ::= <actualparitem> ( , <actualparitem> )* | 
    def actualparlist(t1,t2,t3):
        actualparitem()
        while t1 == actualparitem :
            if (t2 == LeftPartk):
                t2 = lex()
                actualparitem()
                if (t3 == RightPartk):
                    t3 = lex()
                else:
                    print("ERROR!!!The ')' expected")
            else:
                print("ERROR!!!The '(' expected")
                
    #<actualparitem> ::= in <expression> | inout id
    def actualparitem(t1,t2):
        if (t1 == intk):
             t1 = lex()
             expression()
        
        elif (t1 == inouttk):
            t1 = lex()
            if (t2 == idtk):
                    t2 = lex()
            else:
                print("ERROR!!!The inout name expected")
        elif (t1 != inout):
            print("ERROR!!!The keyword 'inout' expected")
        elif (t1 != intk):
            print("ERROR!!!The keyword 'in' expected")
        

    #<condition> ::= <boolterm> (or <boolterm>)*

    def condition(t1,t2,t3,t4):
        boolterm()
        while t1 == booltermtk:
            if (t2 == LeftPartk):
                t2 = lex()
                boolterm()
                if (t3 == ortk):
                    t3 = lex()
                    if (t4 == RightPartk):
                        t4 = lex()
                    else:
                        print("ERROR!!!The ')' expected")
                else:
                    print("ERROR!!!The keyword 'or' expected")
            else:
                print("ERROR!!!The '(' expected")
        return
                
    #<boolterm> ::= <boolfactor> (and <boolfactor>)*

    def boolterm(t1,t2,t3,t4):
        boolfactor()
        while t1== boolfactortk :
            if (t2 == LeftPartk):
                t2 = lex()
                if (t3 == andtk):
                    t3= lex()
                    boolfactor()
                    if (t4 == RightPartk):
                        t4 = lex()
                    else:
                        print("ERROR!!!The ')' expected")
                else:
                    print("ERROR!!!The keyword 'and' expected")
            else:
                print("ERROR!!!The '(' expected")
        return        
    #<boolfactor> ::= not [<condition>] | [<condition>] |<expression> <relational-oper> <expression> 
    def boolfactor(t1,t2,t3):
        if (t1 == nottk):
            t1 = lex()
            if (t2 == LeftBrackettk):
                t2= lex()
                condition()
                if (t3 == RightBrackettk):
                    t3 = lex()
                else:
                    print("ERROR!!!The ']' expected")
            else:
                print("ERROR!!!The '[' exptected")
        elif (t2 == LeftBrackettk):
            t2 = lex()
            condition()
                    
            if (t3 == RightBrackettk):
                t3 = lex()
            else:
                print("ERROR!!!The ']' exptected")
        elif (t2 != LeftBrackettk):
            print("ERROR!!!The '[' expected")
        elif ( t1 != nottk):
            print("ERROR!!!The keyword 'not' exptected")
                    
        else:
            expression()
            relationaloper()
            expression()
                            
                
            
       
    #<expression> ::= <optional-sign> <term> ( <add-oper> <term>)* 
    def expression(t1,t2,t3):
        optionalsign()
        term()
        while (t1 == addopertk or t1 == termtk):
            if (t2 == LeftPartk):
                t2 = lex()
                addoper()
                term()
                if (t3 == RightPartk):
                    t3 = lex()
                else:
                    print("ERROR!!!The ')' expected")
            else:
                print("ERROR!!!The '(' expected")
        return
                
    #<term> ::= <factor> (<mul-oper> <factor>)*
    def term(t1,t2,t3):
        factor()
        while (t1 == mulopertk or t1 == factortk):
            if (t2 == LeftPartk):
                t2 = lex()
                muloper()
                factor()
                if (t3 == RightPartk):
                    t3 = lex()
                
                else:
                    print("ERROR!!!The ')' expected")
            else:
                print("ERRor!!!The '(' exptected")
        return    
    #<factor> ::= constant | (<expression>) | id <idtail>
    def factor(t1,t2,t3):
        constant()
        if (t1 == LeftPartk):
            t1 = lex()
            expression()
            if (t2 == RightPartk):
                t2 = lex()
            else:
                print("ERROR!!!The ')' expected")
        elif(t1 != LeftPartk):
            print("ERROR!!!The '(' expected")
                
        elif (t1 == idtk):
            t1 = lex()
            idtail()
        elif (t1 != idtk):
            print("ERROR!!!The factor name expected")
           
    #<idtail> ::= | <actualpars>

    def idtail():
        actualpars()


    #<relational-oper> ::= = | <= | >= | > | < | <>
    def relationaloper(t1):
        if (t1 == equalstk):
            t1 = lex()
        elif (t1 == mineqtk):
            t1 = lex()
        elif (t1 == maxeqtk):
                t1 = lex()
        elif (t1 == maxtk):
                t1 = lex()
        elif (t1 == mintk):
                t1 = lex()
        elif (t1 == minmaxtk):
                t1 = lex()
        elif (t1 != minmaxtk):
            print("ERROR!!!The '<>' expected")
        elif (t1 != mintk):
            print("ERROR!!!The '<' expected")
        elif (t1 != maxtk):
            print("ERROR!!!The '>' expected")
        elif (t1 != maxeqtk):
            print("ERROR!!!The '>=' expected")
        elif (t1 != mineqtk):
            print("ERROR!!!The '<=' expected")
        elif (t1 != equalstk):
            print("ERROR!!!The '=' expected")

    #<add-oper> ::= + | -

    def addoper(token):
        if (token == plustk):
            token=lex()
        elif (token==minustk):
            token = lex()
        elif (token!=minustk):
            print("ERROR!!!The '-' expected")
        elif (token != plustk):
            print("ERROR!!!The '+' expected")
        
    #<mul-oper> ::= * | /

    def muloper(token):
        if (token == multitk):
            token = lex()
        elif (token == dividetk):
                token = lex()
        elif (token != dividetk):
                print("ERROR!!!The '/' expected")
        elif (token != multitk):
            print("ERROR!!!The '*' expected")
    #<optional-sign> ::= | <add-oper> 
    def optionalsign():
        global token
        add-oper()
        
syntax()
    

    
