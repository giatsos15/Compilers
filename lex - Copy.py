import gramm.py

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
        
def checkSeparator( a):
    i=0
    keepsep=0
    for i in seperators:
        if(a==i):
            keepsep=a
            return True
        else:
            return False

def checkArithSymbol(a):
    i=0
    keepArithSymbol=0
    for i in arithmsymb:
        if(a==i):
            keepArithSymbol=a
            return True
        else:
            return False

def checkCorrelatiOper(a):
    i=0
    keepCorrelatiOper=0
    for i in keywords:
        if(a==i):
            keepCorrelatiOper=a
            return True
        else:
            return False

def checkAssignmentSymbol(a):
    
    
    if(a==assignmentSymbol):
        
        return True
    else:
        return False




def checkGroupingOpers(a):
    i=0
    keepGroupingOpers=0
    for i in groupingopers:
        if(a==i):
            keepGroupingOpers=a
            return True
        else:
            return False    

  
def checkCommSeps(a):
    i=0
    keepCommSeps=0
    for i in commseps:
        if(a==i):
            keepCommSeps=a
            return True
        else:
            return False    

def checkalphabet(a):
    i=0
    keepalphabet=0
    for i in alphabet:
        if(a==i):
            keepalphabet=a
            return True
        else:
            return False

def checknum(a):
    i=0
    keepnum=0
    for i in alphabet:
        if(a==i):
            keepnum=a
            return True
        else:
            return False



def stateEngine(array):
    state = ' '
    for i in range(0, len(array)):
        while (state!=OK and state!=error and state!=eof):
            if (state==state_0 and checkalphabet(array[i]) == True):
                state=state_1
                s +=array[i]
            elif (state == state_0 and checknum(array[i])==True):
                state=state_2
                s +=array[i]
            elif (state == state_0 and checkArithSymbol(array[i])==True):
                s +=array[i]
                state = OK
            elif ( state == state_0 and checkCorrelatiOper(array[i])==True):
                s +=array[i]
                if ( s == '<'):
                    state = state_3
                    if(array[i+1] == '='):
                        s +=array[i]
                        state = OK
                    elif (array[i+1] == '>'):
                        s +=array[i]
                        state = OK
                    else:
                        state = OK
                elif ( s== '>'):
                    state = state_4
                    if ( array[i+1] == '='):
                        s +=array[i]
                        state = OK
                    else:
                        state = OK
            elif(state == state_0 and checkCommSeps(array[i])==True):
                s +=array[i]
                if (s == ':'):
                    state = state_5
                    if(arra[i+1] == '=' ):
                        s +=array[i]
                        state = Ok
                    else:
                        state = error
                else:
                    state = OK
            elif ( state == state_0 and checkGroupingOpers(array[i])==True):
                s +=array[i]
                if (s == '{'):
                    state = state_6
                    if (s == '}'):
                        state = state_0
                    elif ( s == eof):
                        state = error
                    else:
                        state = state_6
            elif ( state == state_0 and eof):
                state = eof
            elif ( state == state_0):
                state = error
            elif ( state == state_1 and checkalphabet(array[i])==True):
                s +=array[i]
                state = state_1
            elif (state == state_1 and checknum(array[i])==True):
                  s +=array[i]
                  state = state_1
            elif (state == state_1 and eof):
                state = eof
            elif (state == state_1):
                i-=1
                state = OK
            elif ( state == state_2 and ckecknum(array[i])==True):
                s +=array[i]
                state = state_2
            elif (state == state_2 and eof):
                state = eof
            elif (state == state_2):
                i-=1
                state = OK
            elif (state==state_3 and eof):
                state = eof
            elif (state==state_4 and eof):
                state = eof
            elif (state==state_5):
                state=error
                
                    
        
  

def state_1(c):
    while (c in alphabet or c in num):
        token.append(c)
    return token
    state_0(c1)

def state_2(c):
    while (c in num and token.length() < 5):
        token.append(c)
        break
        if ( c <= 32767 and c >= (-32767)):
            return token 
        else:
            print("OUT OF BOUNDS")


                        
            
            
        
                                
            
                

    

    
