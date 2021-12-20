from math import log2

DATA = 'input_data.txt'
SCALE = 16 # hex


class Bit:
    def __init__(self, version, literal_value=0):
        self.version = version
        self.literal_value = 0
        if literal_value:
            self.literal_value = int(literal_value, 2)


def decode_packet(binary_string, existing_packets=[]):
    packet_version = int(binary_string[:3], 2)
    packet_id = int(binary_string[3:6], 2)
    if packet_id == 4:
        binary_encoded_string = binary_string[6:]
        binary_literal = ''
        while True:
            value = binary_encoded_string[:5]
            binary_literal = binary_literal + value[1:]
            binary_encoded_string = binary_encoded_string[5:]
            if not int(value[:1]):
                break
        existing_packets.append(Bit(packet_version, binary_literal))
        return existing_packets, binary_encoded_string
    else:
        existing_packets.append(Bit(packet_version))
        length_type_id = int(binary_string[6:7])
        if length_type_id:
            number_sub_packets = int(binary_string[7:18], 2)
            sub_packets = binary_string[18:]
            for i in range(number_sub_packets):
                existing_packets, sub_packets = decode_packet(sub_packets, existing_packets)
        else:
            total_sub_packet_length = int(binary_string[7:22], 2)
            sub_packets = binary_string[22:]
            sub_packet_start_length = len(sub_packets)
            while len(sub_packets) > sub_packet_start_length - total_sub_packet_length:
                existing_packets, sub_packets = decode_packet(sub_packets, existing_packets)
        return existing_packets, sub_packets

with open(DATA) as data:
    hex_data = data.readline().strip()
    binary_input = bin(int(hex_data, SCALE))[2:].zfill(int(len(hex_data) * log2(SCALE)))

packets, remaining = decode_packet(binary_input)

sum_versions = 0

for packet in packets:
    sum_versions += packet.version

print('Sum of versions: ' + str(sum_versions))
