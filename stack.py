

"""
	
 
 
            ██████▀╩█▀█████ⁿ╤▄;
            ▐████▄╙╗       └╙▀▀██Φ▄▄
              ▀▀    `x           "▀███▄▄                        ░
                       V             ▀▀███▄
                         *              "▀███▄,
                           '.             ▀█████▌
                             "~             ▀ⁿ▀███▄
                    ;          `═               └▀██▄
                     █W,          *               '███▄
                      ▀██           *,              ▌███▄
    ░                   "█N           "v   ░        ╙▀████╕
                          '▀æ           "v            ▀▀██▄
                             ▀g           `w             ▀██
                               ╙φ,           w            ▀██
                                 ╙Φ╖           \           █Ç▌
                                   "Ñw           \          █▓▄
                                     └ÑW           *,       ▐██
                                       `▀M           ",      █▓█
                                          ▀▄           "∞    -██
                                            ▀▌µ           ═   ██▌
                                              ████▄         \ç▐█▌
                                              ╙▓"█▄▓▄        └██▌
                                                ╙█▐██▓█▄       █▌
                                                  ▀╫█▌ ¬▀+     ██▄,
                                                    └▀         ▐███▄
                                                                ▀▀▀
 
 
"""






















stack=[]

top=None


def push(stack,plate):
    stack.append(plate)
    top=len(stack)-1


def pop(stack):
    
    if stack==[]:
        return 'underflow'
    plate=stack.pop()
    
    if stack==[]:
        top=None
    else:
        top=len(stack)-1
    return plate

def peak(stack):
    if stack==[]:
            return "stack is underflow"
    else:
        top=len(stack)-1
        return stack[top]

def display(stack):
    if stack==[]:
        return "underflow"
    top=len(stack)-1        
    print(stack[top],"<<top")
    for i in range(len(stack)-2,-1,-1): 
        print(stack[i])

while True:
    print("Welcome")
    print("1. push the plates")
    print("2. pop the plates")
    print("3. peak of the stack")
    print("4. display the menue")
    print("5. exit the menue")

    choice=int(input("What option do you wish to run"))

    if choice==1:
        plate=input("enter the clor of plate you wanna push")
        push(stack,plate)
    elif choice==2:
        output=pop(stack)
        if output=="underflow":
            print("stack is empty")
        else:
            print("poped plate is",output)
    elif choice==3:
        output=peak(stack)
        if output=="stack is undeflow":
            print("stack is underflow")
        else:
            print("peak is", output)
    elif choice==4:
        display(stack)

    elif choice==5:
        print("thank you")
        break
    else: 
        print("please give a valid input, try again")
  
