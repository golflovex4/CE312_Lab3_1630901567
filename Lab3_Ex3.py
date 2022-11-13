Equ = "(A+B)*C-D*F+C"
Equa = list(Equ)
Sym = ["+","-","*","/"]
Out = []
Opr = []

Current = ""
Result = ""

def postfix(input):
    
    if input in Sym:
        if(((input=="/") or (input == "*")) and (Opr != [])):
            if((Opr[-1] == "*") or (Opr[-1] == "/")):
                Out.append(Opr.pop())
                Opr.append(Equa.pop())
            else:
                Opr.append(Equa.pop(0))
        else:
            if(Opr != []):
                if(((input =="+") or (input == "-")) and ((Opr[-1]=="*") or (Opr[-1] == "/"))):
                    Out.append(Opr.pop())
                    while len(Opr) > 0:
                        Out.append(Opr.pop())
                else:
                    Opr.append(Equa.pop())
            else:
                Opr.append(Equa.pop(0))
    else:
        Out.append(Equa.pop(0))
        
while len(Equa) > 0:
    Current = Equa[0]
  %
