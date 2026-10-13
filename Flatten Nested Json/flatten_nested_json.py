config = {"db": {"host": "localhost", "port": 5432}, "debug": True}



def get_flattened(config,parent=''):

    flatted_dic = {}


    for key,value in config.items():
        new_key = parent + '.' + key if parent else key
        
        if isinstance(value,dict):
            flatted_dic.update(get_flattened(value,parent=new_key))
        else:
            flatted_dic[new_key] = value

        
    

    return flatted_dic


print(get_flattened(config,parent=''))
