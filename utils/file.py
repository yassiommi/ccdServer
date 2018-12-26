import os, json, time

def locked_write(content, path, lock):
    try:
        while os.path.exists(lock):
            time.sleep(1)
        os.system('touch ' + lock)
        if not os.path.exists(path):
            os.system('touch ' + path)
        if os.stat(path).st_size == 0:
            with open(path, 'w') as f:
                json.dump({'data': [content]}, f)
        else:
            json_file = None
            with open(path, 'r') as f:
                json_file = json.load(f)
            data = json_file['data']
            data.append(content)
            with open(path, 'w') as f:
                json.dump({'data': data}, f)
    except Exception as e:
        print(e)
    finally:
        os.remove(lock)

def locked_read(path, lock):
    try:
        while os.path.exists(lock):
            time.sleep(1)
        if os.stat(path).st_size == 0:
            return []
        else:
            with open(path, 'r') as f:
                json_file = json.load(f)
                return json_file['data']
    except Exception as e:
        print(e)
        return 'error'

def remove_first(path, lock):
    try:
        while os.path.exists(lock):
            time.sleep(1)
        os.system('touch ' + lock)
        json_file = None
        with open(path, 'r') as f:
            json_file = json.load(f)
        data = json_file['data']
        data.pop(0)
        with open(path, 'w') as f:
            json.dump({'data': data}, f)
    except Exception as e:
        print(e)
    finally:
        os.remove(lock)
