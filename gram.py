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
import lex
import yacc

def syntaxanalysis():
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
    
    def program():
        if (token == programtk):
            token = lex()
            if (token == idtk):
                token = lex()
                if (token == LeftBratk):
                    token = lex()
                    if (token == RightBratk):
                        token = lex()
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

    def declariations():
        while (token == declaretk or token == notdeclaretk):
          if (token == LeftPartk):
                token = lex()
                declare()
                if (token == declaretk):
                    token = lex()
                    varlist()
                    if (token == char1):
                        token = lex()
                        varlist()
                        if (token == RightPartk):
                            token = lex()
                        else:
                            print("ERROR!!!The ')' expected")
                    else:
                        print("ERROR!!!The ';' expected")
                else:
                    print("ERROR!!!The declariation expected")
          else:
                print("ERROR!!!The '(' expected")

    #<varlist> ::= ε | id ( , id )*            
    def varlist():
        
        if (token == idtk):
            token = lex()
            if (token == LeftPartk):
                token = lex()
                while token == idtk: 
                    if (token == idtk):
                        token = lex()
                        if (token == RightPartk):
                            token = lex()
                        else:
                            print ("ERROR!!!The ')' expected")
                    else:
                        print("ERROR!!!Varlist name expected")
            else:
                print("ERROR!!!The '(' expected")
        else:
            print("ERROR!!!Program name expected")

    #<subprograms> ::= (<subprogram>)*

    def subprograms():
        while token == subprogram:
            if (token == LeftPartk):
                token = lex()
                subprogram()
                if (token == RightPartk):
                    token = lex()
                else:
                    print("ERROR!!!The ')' expected")
            else:
                print ("ERROR!!!The '(' expected")
        return        
    #<subprogram> ::= function id <funcbody> | procedure id <funcbody>            
    def subprogram():
        if (token == functiontk):
            token = lex()
            if (token == idtk):
                token = lex()
                funcbody()
            else:
                print("ERROR!!!The function name expected")
           
        elif (token == proceduretk):
            token = lex()
            if (token == idtk):
                token = lex()
                funcbody()
            else:
                print ("ERROR!!!Procedure name expecte")
        elif (token != proceduretk):
            print("ERROR!!!The keyword 'procedure' expected")        
        elif (token != functiontk):
            print("ERROR!!!The keyword 'function' expected")         
        
           
    #<funcbody> ::= <formalpars> { <block> }
    def funcbody():
            formalpars()
            if (token == LeftBratk):
                token == lex()
                block()
                if (token == RightBratk):
                    token = lex()
                else:
                    print ("ERROR!!!The '}' expected")
            else:
                print("ERROR!!!The '{' expected")
      
    #<formalpars> ::= ( <formalparlist> )

    def formalpars():
        if (token == LeftPartk):
            token = lex()
            formalparlist()
            if (token == RightPartk):
                token = lex()
            else:
                print ("ERROR!!!The ')' expected")
        else:
            print("ERROR!!!The '(' expected")
            
    #<formalparlist> ::= <formalparitem> ( , <formalparitem> )* | ε 
    def formalparlist():
        formalparitem()
        while token == formalparitemtk :
            if (token == LeftPartk):
                token = lex()
                formalparitem()
                if (token == RightPartk):
                    token = lex()
                else:
                    print("ERROR!!!The ')' expected")
            else:
                print("ERROR!!!The '(' expected")
        return
                
    #<formalparitem> ::= in id | inout id 
    def formalparitem():
        if (token == intk):
            token = lex()
            if (token == idtk):
                token = lex()
            else:
                print("ERROR!!!The in name expected")
        elif (token != intk):
            print("ERROR!!!The keyword 'in' expected")
        elif (token == inouttk):
            token = lex()
            if(token == idtk):
                token = lex()
            else:
                 print("ERROR!!!The inout name expected")
        elif (token != intk):
            print("ERROR!!!The keywortd 'inout' expected")
            

    #<statements> ::= <statement> | { <statement> ( ; <statement> )* }
    def statements():
        statement()
        if(token == LeftBra):
            token=lex()
            statement()
            while(token==char1):
                token=lex()
                return
             
                if(token==LeftPartk):
                    token=lex()
                    if(token==char1):
                        token==lex()
                        statement()
                        if(token==RightPartk):
                            token==lex()
                        
                        else:
                            print("ERROR!!!The ')' expected")
                    else:
                        print("ERROR!!!The ';' expected")
                else:
                     print("ERROR!!!The '(' expected")             
                if(token==RightBra):
                    token=lex()
                else:
                     print("ERROR!!!The '}' expected")
            return
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

    def assignment_stat():
        if(token==idtk):
            token=lex();
            if(token==definetk):
                token=lex()
                expression()
            else:
                print("ERROR!!!The ':=' expected") 
        else:
            print("ERROR!!!The assigment name expected") 

    #<if-stat> ::= if (<condition>) then <statements> <elsepart>

    def if_stat():
        token=lex()
        if(token==LeftPartk):
            token=lex()
            condition()
            if(token==RightPartk):
                token=lex()
                if(token==thentk):
                    token=lex()
                    statements()
                    elsepart()
                else:
                    print("ERROR!!!The keyword 'then' expected")
            else:
                print("ERROR!!!The ')' expected")
        else:
            print("ERROR!!!The '(' expected") 

    #<elsepart> ::= ε | else <statements>
    def elsepart():

        if(token==elsetk):
            token=lex()
            statements()

        else:
            print("ERROR!!!The keyword 'else' expected")


    #<while-stat> ::= while (<condition>) <statements>
    def while_stat():

        if(token==whiletk):
            token=lex()
            if(token==LeftPartk):
                token=lex()
                condition()
                if(token==RightPartk):
                    token=lex()
                    statements()
                else:
                    print("ERROR!!!The ')' expected") 
            else:
                print("ERROR!!!The '(' expected")
        else:
            print("ERROR!!!The keyword 'while' expected")
            
    #<doublewhile-stat> ::= doublewhile (<condition>) <statements>
    # else <statements>

    def doublewhile_stat():

        if(token==whiletk):
            token=lex()
            if(token==LeftPartk):
                token=lex()
                condition()
                if(token==RightPartk):
                    token=lex()
                    statements()
                    if(token==elsetk):
                        token=lex()
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
    def loop_stat():
        if(token==looptk):
            token=lex()
            statements()
        else:
             print("ERROR!!!The keyword 'loop' expected")

    #<exit-stat> ::= exit
    def exit():
        if(token==exittk):
            token=lex()
        else:
             print("ERROR!!!The keyword 'exit' expected")
             
    #<forcase-stat> ::= forcase
    # ( when (<condition>) : <statements> )*
    # default: <statements> 
    def for_case():

        if(token==forcasetk):
            token=lex()
            while(token==forcasetk):
                if(token==LeftPartk):
                    token=lex()
                    if(token==whentk):
                        token=lex()
                        if(token==LeftPartk):
                            token=lex()
                            condition()
                            if(token==RightPartk):
                                token=lex()
                                if(token==char2):
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
                
        else:
            print("ERROR!!!The keyword 'forcase' expected")
        if(token==defaulttk):
            token=lex()
            if(token==char2):
                token=lex()
                statements()
            else:
                print("ERROR!!!The ':' expected")
        else:
            print("ERROR!!!The keyword 'default' expected")

        return    
    #<incase-stat> ::= incase
    #( when (<condition>) : <statements> )*
    def incase_stat():
        if(token==incasetk):
            token=lex()
            while(token==incasetk):
                if(token==LeftPartk):
                    token=lex()
                    if(token==whentk):
                        token=lex()
                        if(token==LeftPartk):
                            token=lex()
                            condition()
                            if(token==RightPartk):
                                token=lex()
                                if(token==char2):
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
                
        else:
            print("ERROR!!!The keyword 'incase' expected")
        return

    
    #<return-stat> ::= return <expression>
    def return_stat():
        if(token==returntk):
            token=lex()
            expression()
        else:
            print("ERROR!!!The keyword 'return' expected")
            
    #<call-stat> ::= call id <actualpars>

    def callstat():
        if (token == calltk):
            token = lex()
            if (token == idtk):
                token = lex()
                
                actualpars()
            else:        
                print("ERROR!!!The call name expected")
        else:
            print("ERROR!!!The keyword 'call' expected")
            
    #<print-stat> ::= print (<expression>)
    def printstat():
        if (token == printtk):
            token = lex()
            if(token == LeftPartk):
                token = lex()
                expression()
                if (token == RightPartk):
                    token = lex()
                else:
                    print("ERROR!!!The ')' expected")
            else:
                print("ERROR!!!The '(' expected")
        else:
            print("ERROR!!!The keyword 'print' expected")
            
    #<input-stat> ::= input (id)
    def inputstat():
        if (token == inputtk):
            token = lex()
            if (token == LeftPartk):
                token = lex()
                if (token == idtk):
                    token = lex()
                    if (token == RightPartk):
                        token = lex()
                    else:
                        print("ERROR!!!The ')' expected")
                else:
                    print("ERROR!!!The input name expected")
            else:
                print("ERROR!!!The '(' expected")
        else:
            print("ERROR!!!The keyword 'input' expected")
            
    #<actualpars> ::= ( <actualparlist> ) 
    def actualpars():
        if (token == LeftPartk):
            token = lex()
            actualparlist()
            if (token == RightPartk):
                token = lex()
            else:
                print("ERROR!!!The ')' epxected")
            
        else:
            print("ERROR!!!The '(' expected")
        return
            
    #<actualparlist> ::= <actualparitem> ( , <actualparitem> )* | ε
    def actualparlist():
        actualparitem()
        while token == actualparitem :
            if (token == LeftPartk):
                token = lex()
                actualparitem()
                if (token == RightPartk):
                    token = lex()
                else:
                    print("ERROR!!!The ')' expected")
            else:
                print("ERROR!!!The '(' expected")
                
    #<actualparitem> ::= in <expression> | inout id
    def actualparitem():
        if (token == intk):
             token = lex()
             expression()
        elif (token != intk):
            print("ERROR!!!The keyword 'in' expected")
        elif (token == inouttk):
            token = lex()
            if (token == idtk):
                    token = lex()
            else:
                print("ERROR!!!The inout name expected")
        elif (token != inout):
            print("ERROR!!!The keyword 'inout' expected")
        
        

    #<condition> ::= <boolterm> (or <boolterm>)*

    def condition():
        boolterm()
        while token == booltermtk:
            if (token == LeftPartk):
                token = lex()
                boolterm()
                if (token == ortk):
                    token = lex()
                    if (token == RightPartk):
                        token = lex()
                    else:
                        print("ERROR!!!The ')' expected")
                else:
                    print("ERROR!!!The keyword 'or' expected")
            else:
                print("ERROR!!!The '(' expected")
                
    #<boolterm> ::= <boolfactor> (and <boolfactor>)*

    def boolterm():
        boolfactor()
        while token == boolfactortk :
            if (token == LeftPartk):
                token = lex()
                if (tolem == andtk):
                    token = lex()
                    boolfactor()
                    if (token == RightPartk):
                        token = lex()
                    else:
                        print("ERROR!!!The ')' expected")
                else:
                    print("ERROR!!!The keyword 'and' expected")
            else:
                print("ERROR!!!The '(' expected")
                
    #<boolfactor> ::= not [<condition>] | [<condition>] |<expression> <relational-oper> <expression> 
    def boolfactor():
        if (token == nottk):
            token = lex()
            if (token == LeftBrackettk):
                token = lex()
                condition()
                if (token == RightBrackettk):
                    token = lex()
                else:
                    print("ERROR!!!The '[' expected")
            else:
                print("ERROR!!!The ']' exptected")
        elif (token == LeftBrackettk):
                    token = lex()
                    condition()
                    
                    if (token == RightBrackettk):
                         token = lex()
                    else:
                        print("ERROR!!!The ']' exptected")
        elif (token != LeftBrackettk):
            print("ERROR!!!The '[' expected")
        elif ( token != nottk):
            print("ERROR!!!The keyword 'not' exptected")
                    
        else:
            expression()
            relationaloper()
            expression()
                            
                
            
       
    #<expression> ::= <optional-sign> <term> ( <add-oper> <term>)* 
    def expression():
        optionalsign()
        term()
        while token == addopertk or token == termtk :
            if (token == LeftPartk):
                token = lex()
                addoper()
                term()
                if (token == RightPartk):
                    token = lex()
                else:
                    print("ERROR!!!The ')' expected")
            else:
                print("ERROR!!!The '(' expected")
                
    #<term> ::= <factor> (<mul-oper> <factor>)*
    def term():
        factor()
        while token == mulopertk or token == factortk :
            if (token == LeftPartk):
                token = lex()
                muloper()
                factor()
                if (token == RightPartk):
                    token = lex()
                
                else:
                    print("ERROR!!!The ')' expected")
            else:
                print("ERRor!!!The '(' exptected")
        return    
    #<factor> ::= constant | (<expression>) | id <actualpars>
    def factor():
        constant()
        if (token == LeftPartk):
            token = lex()
            expression()
            if (token == RightPartk):
                token = lex()
            else:
                print("ERROR!!!The ')' expected")
        elif(token != LeftPartk):
            print("ERROR!!!The '(' expected")
                
        elif (token == idtk):
            token = lex()
            idtail()
        elif (token != idtk):
            print("ERROR!!!The factor name expected")
           
    #<idtail> ::= ε | <actualpars>

    def idtail():
        actualpars()


    #<relational-oper> ::= = | <= | >= | > | < | <>
    def relationaloper():
        if (token == equalstk):
            token = lex()
        elif (token == mineqtk):
            token = lex()
        elif (token == maxeqtk):
                oken = lex()
        elif (token == maxtk):
                token = lex()
        elif (token == mintk):
                token = lex()
        elif (token == minmaxtk):
                token = lex()
        elif (token != minmaxtk):
            print("ERROR!!!The '<>' expected")
        elif (token != mintk):
            print("ERROR!!!The '<' expected")
        elif (token != maxtk):
            print("ERROR!!!The '>' expected")
        elif (token != maxeqtk):
            print("ERROR!!!The '>=' expected")
        elif (token != mineqtk):
            print("ERROR!!!The '<=' expected")
        elif (token != equalstk):
            print("ERROR!!!The '=' expected")

    #<add-oper> ::= + | -

    def addoper():
        if (token == plustk):
            token=lex()
        elif (token==minustk):
            token = lex()
        elif (token!=minustk):
            print("ERROR!!!The '-' expected")
        elif (token != plustk):
            print("ERROR!!!The '+' expected")
        
    #<mul-oper> ::= * | /

    def muloper():
        if (token == multitk):
            token = lex()
        elif (token == dividetk):
                token = lex()
        elif (token != dividetk):
                print("ERROR!!!The '/' expected")
        elif (token != multitk):
            print("ERROR!!!The '*' expected")
    #<optional-sign> ::= ε | <add-oper> 
    def optionalsign():
        global token
        add-oper()
        
syntaxanalysis()        
                
                
            
        
            
            
        
                    
                
            
        
                    
