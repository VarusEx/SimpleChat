import socket, struct


def ping(serverid):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
        s.bind((serverid, 0))
        while 1:
            recpacket, addr = s.recvfrom(1024)
            icmp_header = recpacket[20:28]
            ty, code, checksum, p_id, sequence = struct.unpack('bbHHh', icmp_header)
            print("type: [" + str(ty) + "] code: [" + str(code) + "] checksum: [" + str(checksum) + "] p_id: [" + str(
                p_id) + "] sequence: [" + str(sequence) + "]")
    except OSError as error:
        print(error)
        print("Error with os")
