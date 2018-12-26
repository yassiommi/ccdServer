import time, requests
from file import locked_read, remove_first, locked_write
from pywindi.winclient import Winclient

while True:
    data = locked_read('./queue/queue.json', './queue/.lock1')
    if data == []:
        time.sleep(1.01)
    else:
        data = data[0]
        client = Winclient('localhost', 7624)
        ccd = client.get_device('SBIG CCD')
        ccd.configure(image_directory='./images/')
        ccd.set_binning(eval(data['binning'])[0], eval(data['binning'])[1])
        ccd.set_temperature(float(data['temperature']))
        ccd.set_frame_type(data['type'])
        filename = ccd.take_image(float(data['exposure_time']))
        client.disconnectServer()
        remove_first('./queue/queue.json', './queue/.lock1')
        locked_write(filename, './queue/move.json', './queue/.lock2')
        if int(data['chiz']) != 1:
            time.sleep(float(data['interval']))
