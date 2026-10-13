##You get log lines in the format DATE TIME LEVEL service=NAME message.
##For every service, find the error message that appears most often.
##Only lines with level ERROR count.


logs = [
    "2024-01-01 12:00:01 ERROR service=api timeout",
    "2024-01-01 12:00:02 ERROR service=api timeout",
    "2024-01-01 12:00:03 ERROR service=db disk_full",
    "2024-01-01 12:00:04 INFO service=api ok",
]

##expected -> {'api': 'timeout', 'db': 'disk_full'}

from collections import defaultdict, Counter


def get_service_with_most_error(logs):

    error_logs = defaultdict(Counter)
    
    for log in logs:
        log_data = str(log).split()
        if log_data[2] == 'ERROR':
            service_name = log_data[3].split('=')[1]
            error_msg = log_data[4]

            error_logs[service_name][error_msg] +=  1
            
            
    
##    print(error_logs)

    
    return {srv:value.most_common(1)[0][0] for srv,value in error_logs.items()}


print(get_service_with_most_error(logs))
##    return {service_name: x for service_name,value in error_logs.values}
    
