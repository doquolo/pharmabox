import serial.tools.list_ports
import serial

# trinh chon cong com
def listPort():
    # hien thi tat ca cong serial dang mo tren may tinh
    ports = serial.tools.list_ports.comports()
    ports = sorted(ports)

    portlist = []
    for i in range(len(ports)):
        portlist.append({
            'name': ports[i].name,
            'desc': ports[i].description,
            'hwid': ports[i].hwid
        })

    return portlist

portlist = listPort()
for i in portlist:
    if 'CP2102' in i['desc']:
        ser = serial.Serial(f"/dev/{i['name']}", 115200, timeout=0)
        break

print("Setting up slots")
ser.flush()
ser.write(b'S\n')

slot = [19, 18, 17, 16]
command = ""
for i in slot:
    command += f'O{i};'
command += '\n'
print(command)
ser.write(bytes(command, encoding='utf-8')) # sending 19;
print("done")


def dropMedicine(test):
    # test = [16, 18, 17, 19, 16, 18]
    ser.write(b'D\n')
    command = ""
    for i in test:
        command += f'{i};'
    command += '\n'
    print(command)
    ser.write(bytes(command, 'utf-8'))
