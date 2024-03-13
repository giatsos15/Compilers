import gramm.py

alphabet=['A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=[0,1,2,3,4,5,6,7,8,9]
arithmsymbol=['+','-','*','/']
correlationopers=['<','>','=','<=','>=','<>']
assignmentSymbol=":="
seperators=[';',',',':']
groupingopers=['(',')','{','}','[',']']
commseps=['/','*/','//']
keywords=['program','declare','function','procedure','in','inout','if','else','while','doublewhile','loop','exit','forcase','incase','when','default','not','and','or','call','return','input','print']
linenum=0

piece = ''
f=raw_input("Enter the file name:")
file=open(f,"r")
for piece in readInpiecies(file):
    shapedata(piece)
file.close()    



array = [] #gia tis metavlites
token = 0
def shapedata(piece):#


    archar=split(piece)
    counterspace=0
    for c in archar:
        if(c==' ' or c=='    '):
            counterspace=counterspace+1
            while counterspace==1:
                array.append('^')
                continue
        else:
            array.append(c1)
            counterspace=0
    processdata(array)            
    
def readInpiecies(file):#diavazo to arxio se komatia ton 30 xaraktiron
    
    
       
        while True:
            
            data=file.read(30)
            if not data:
                break
            yield data
            
def split(word): 
    return [char for char in word] 
def processdata(array):
    laststate= state_0
    for i in range(0,len(array)):
        while array[i] in alphabet or :
         laststate= state_1   
        elif array[i] in num:
          laststate= state_2
          return number 
        elif array[i] in arithmsymbol:
            laststate= state_0
            return arithmetic_symbol
        elif array[i] in correlationopers:
            
        elif array[i] in assignmentSymbol:

        elif array[i] in seperators:

        elif array[i] in groupingopers:

        elif array[i] in commseps:

        elif array[i] in keywords:


        
        
def state_0(c):
    if c in alphabet:
        state_1(c1)
    elif  c in num:
        state_2(c1)
    elif    

def state_1(c):
    while (c in alphabet or c in num)
        token.append(c)
    return token
    state_0(c1)

def state_2(c):
    while (c in num and token.length() < 5)
        token.append(c)
        break
        if ( c <= 32767 and c >= (-32767)):
            return token 
        else:
            print("OUT OF BOUNDS")

def state_3(c,c1):
    while (c == '<'):
        if (c == '='):
            return
        elif ( c == '>'):
            return
        else:
            return

def state_4(c):
    if ( c == '>'):
        if ( c == '='):
            return token
        else:
            return
    return

def state_5(c):
    if ( c == ':'):
        if ( c == '='):
            return token
        else:
            print("ERROR")
    return

def state_6(c):
    if ( c == '{'):
        if ( c == '}'):
            return token
        else:
            
        
            
            
            
        
    

file.close() #sto telos

def checkKeyword(a):
    
i=0
keepword=0
for i in keywords:
    if(a == i):
        keepword=a
        
        return True
    else:
        return False
        
def checkSeparator(char a):
    i=0
    keepsep=0
    for i in seperators:
        if(a==i):
            keepsep=a
            return True
        else:
            return False

def checkArithSymbol(char a):
    i=0
    keepArithSymbol=0
    for i in arithmsymb:
       if(a==i):
            keepArithSymbol=a
            return True
        else:
           return False

def checkCorrelatiOper(char a):
    i=0
    keepCorrelatiOper=0
    for i in keywords:
        if(a==i):
            keepCorrelatiOper=a
            return True
        else:
            return False

def checkAssignmentSymbol(char a):
    
    
    if(a==assignmentSymbol):
        
        return True
    else:
        return False




def checkGroupingOpers(char a):
    i=0
    keepGroupingOpers=0
    for i in groupingopers:
       if(a==i):
            keepGroupingOpers=a
            return True
        else:
           return False    

  
def checkCommSeps(char a):
    i=0
    keepCommSeps=0
    for i in commseps:
       if(a==i):
            keepCommSeps=a
            return True
        else:
           return False    

def checkalphabet(char a):
    i=0
    keepalphabet=0
    for i in alphabet:
        if(a==i):
            keepalphabet=a
            return True
        else:
           return False

def checknum(char a):
    i=0
    keepnum=0
    for i in alphabet:
        if(a==i):
            keepnum=a
            return True
        else:
           return False

def tokenManager():
    tsekarei token ena ena

def stateEngine(array):
    state = ' '
    for i in range(0, len(array))
        while (state!=OK and state!=error)
    
            if (state==state0 and checkalphabet(array[i])):
                state=state1
                s +=array[i]
            elif (state==state0):
                state=error;
            elif (state==state1 and input==x):
                state=state1
            elif (state==state1 and input==y):
                state=state2;
            elif (state==state1):
                state=error;
            elif (state==state2 and input==x):
                state=state2
            elif (state==state2 and input==y):
                state=error
            elif (state==state2):
                state=OK

    

    
