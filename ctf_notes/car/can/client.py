# import module
import struct
import time

#     Pcap Global Header Format :
#                       ( magic number + 
#                         major version number + 
#                         minor version number + 
#                         GMT to local correction +
#                         accuracy of timestamps + 
#                         max length of captured #packets, in octets +
#                         data link type) 
#
#

PCAP_GLOBAL_HEADER_FMT = '@ I H H i I I I '


# Global Header Values
PCAP_MAGICAL_NUMBER = 2712847316
PCAP_MJ_VERN_NUMBER = 2
PCAP_MI_VERN_NUMBER = 4
PCAP_LOCAL_CORECTIN = 0
PCAP_ACCUR_TIMSTAMP = 0
PCAP_MAX_LENGTH_CAP = 65535
PCAP_DATA_LINK_TYPE = 1



class Pcap:
    
    def __init__(self, filename, link_type=PCAP_DATA_LINK_TYPE):
        self.pcap_file = open(filename, 'wb') 
        self.pcap_file.write(struct.pack('@ I H H i I I I ', PCAP_MAGICAL_NUMBER, PCAP_MJ_VERN_NUMBER, PCAP_MI_VERN_NUMBER, PCAP_LOCAL_CORECTIN, PCAP_ACCUR_TIMSTAMP, PCAP_MAX_LENGTH_CAP, link_type))
        print ("[+] Link Type : {}".format(link_type))

    def writelist(self, data=[]):
        for i in data:
            self.write(i)
        return

    def write(self, data):
        ts_sec, ts_usec = map(int, str(time.time()).split('.'))
      #  import pdb;pdb.set_trace()
        length = len(data)
        self.pcap_file.write(struct.pack('@ I I I I', ts_sec, ts_usec, length, length))
        self.pcap_file.write(data)

    def close(self):
        self.pcap_file.close()
  
  
  
if __name__=='__main__':
    
    # import modules
    import socket
    import struct
    import binascii
    import os

    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
    #    data = s.recv(1024)
    #    print(f"Received {data!r}")


    # Create Socket 
   
    # Create Object
        p = Pcap('temp.pcap')

        while True:
            print('loop')
            # Sniff Packet
            pkt=s.recv(2048)
            print('loop1')
            # Save captured packets into pcap file
            p.write(pkt)

            # flush data
            p.pcap_file.flush()

        # close file
        p.close()
        
    
    