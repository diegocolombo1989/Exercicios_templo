
def elevador(left,right,call) -> int:
           
    call_1 = 'Elevador da esquerda esta vindo'
    call_2 = 'Elevador da direita esta vindo'
    
    if left == call: return print(call_1)
    elif right == call: return print(call_2)
    elif left == right: return print(call_2)
    elif left > right: return print(call_2)
    elif right > left: return print(call_2)



elevador(2,1,2)
elevador(1,2,2)
elevador(1,1,2)
elevador(2,1,0)
elevador(2,0,0)
elevador(1,1,0)
elevador(1,0,1)
elevador(2,0,1)
elevador(1,2,2)
elevador(1,0,0)





