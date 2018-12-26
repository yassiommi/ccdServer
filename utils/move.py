import time, requests
from file import locked_read, remove_first, locked_write

while True:
    data = locked_read('./queue/move.json', './queue/.lock2')
    if data == []:
        time.sleep(1.01)
    else:
        data = data[0]
        print('data came:', time.time()
        print(data))
        requests.post('http://172.18.1.47:5000/get_image_back', headers={'host': 'a'}, files={'file': open(data, 'rb')})
        time.sleep(10)
        print('sent data', time.time())
        remove_first('./queue/move.json', './queue/.lock2')
        print('removed data', time.time())
