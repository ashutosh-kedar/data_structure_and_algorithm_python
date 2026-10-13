import time

def get_response(fun,max_attempt=2,base_wait=1.0):

    for attempt in range(max_attempt):
        try:
            return fun()
        except:
            if attempt < max_attempt-1:
                time.sleep(base_wait*(2**attempt))
            else:
                return 'Failure'
        







call_track = {'n':0}

def fun_call():
    call_track['n'] = call_track.get('n',0) + 1

    if call_track['n'] < 3:
        raise Exception('Connectio')

    return "Success"


    
print(get_response(fun_call,max_attempt=3, base_wait=0.1))
