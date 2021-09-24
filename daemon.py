import json
import psutil,os,time

def is_exist(p_name):
    flag = False
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == p_name:
            flag = True
            break
    return flag

if __name__ == '__main__':
    with open(r'conf.json',encoding='utf8') as f:
        json_data = json.loads(f.read())
    while True:
        time.sleep(5)
        if not is_exist(json_data['pid_name']):
            os.system(json_data['open_path'])

