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




queue=[]

front=None
rear= None
def isempty(queue):
    if queue==[]:
        return False
    else:
        return True

def enque(queue,plate):
    queue.append(plate)
    if len(queue)==1:
        front=rear=0
    else:
        rear=len(queue)-1


def deque(queue):
    
    if out_put=="False":
        return 'queue is underflow'
    if len(queue)==0:
        front=None
        rear=None
    else:
       item_removed= queue.pop(0)
    return item_removed
    


def peek(queue):
    if out_put==False:
            return "queue is underflow"
    else:
        front=0
        return queue[front]

def disp(queue):
    if out_put==False:
        print('queue is underflow')
    elif len(queue)==1:
        print(queue[0],'<<<---- front <<<-----rear')
    else:
        front=0
        rear=len(queue)-1


        print(queue[front],'<<<----front')
        for i in range(front+1,rear):
            print(queue[i])
        print(queue[rear],'<<<---rear')
while True:
    print("Welcome")
    print("1. enque")
    print("2. deque")
    print("3. peek")
    print("4. display the queue")
    print("5. exit the queue")
    out_put=isempty(queue)
    
    
    try: 
        choice=int(input("What option do you wish to run "))
    except:
        print("please only pint an integer listed with the options from the menue above")
        continue



    if choice==1:
        item=input("enter the item you want to enque")
        enque(queue,item)
    elif choice==2:
        output=deque(queue)
        if output=="underflow":
            print("queue is empty")
        else:
            print("remvoed item is",output)
    elif choice==3:
        output=peek(queue)
        if output=="queue is undeflow":
            print("queue is underflow")
        if output==queue[front]:
            print("peak is", output)
    elif choice==4:
        disp(queue)

    elif choice==5:
        print("thank you")
        break
    else: 
        print("please give a valid input, try again")
    
    


