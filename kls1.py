import serial
import time
import Klsinfo

packet1 = bytearray()
packet1.append(0x3A)
packet1.append(0x00)
packet1.append(0x3A)

packet2 = bytearray()
packet2.append(0x3B)
packet2.append(0x00)
packet2.append(0x3B)

i = 0

rec_packet = bytearray

check1 = 0

klsinfo = Klsinfo.KlsInfo()

ser = serial.Serial("COM3", 19200, timeout=1)
time.sleep(1)
read_buffer = [0, 0]
with open("testfile1.csv", "w") as file1:
    print(klsinfo.get_header())
    while True:
        try:
            ser.write(packet1)
            read_buffer[0] = ser.read(19)
            ser.write(packet2)
            read_buffer[1] = ser.read(19)
            klsinfo.new_raw3a(read_buffer[0])
            klsinfo.new_raw3b(read_buffer[1])
            print(klsinfo.get_line())
            file1.writelines(klsinfo.get_line() + "\n")
            time.sleep(0.1)
        except:
            break
