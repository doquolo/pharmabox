import serial.tools.list_ports

# trinh chon cong com
def listPort():
    # hien thi tat ca cong serial dang mo tren may tinh
    ports = serial.tools.list_ports.comports()
    ports = sorted(ports)

    portlist = []
    for i in range(len(ports)):
        port = ports[i].name
        desc = ports[i].description
        hwid = ports[i].hwid
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

# try init and send test sequence
print("Setting up slots")
ser.flush()
ser.write(b'S\n')
# while (True):
#     while (ser.in_waiting):
#         data = ser.readline()
#         if (data.strip() == "R"):
#             break


slot = [19, 18, 17, 16]
command = ""
for i in slot:
    command += f'O{i};'
command += '\n'
print(command)
ser.write(bytes(command, encoding='utf-8')) # sending 19;
print("done")

# test sequence
print("testing..")
ser.write(b'D\n')
test = [16, 18, 17, 19, 16, 18]
command = ""
for i in test:
    command += f'{i};'
command += '\n'
print(command)
ser.write(bytes(command, 'utf-8'))

# print("Verifying...")
# temp = slot
# # verify if all port is setup
# while (len(temp) != 0):
#     data = ser.readline()
#     for i in temp:
#         if i in data.strip():
#             print(f"slot {i} done!")
#             temp.remove(temp.index(i))
