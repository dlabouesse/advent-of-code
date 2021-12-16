import tools.readfile as readfile
import uuid

def hex_to_bin(hex_string):
    bin_string = ''
    for hex_digit in hex_string:
        bin_string += format(int(hex_digit, 16), '04b')
    return bin_string

def parse_binary(binary_string, versions_sum, packets, parent_packet, parse_tail = False):
    uid = uuid.uuid4()
    version = int(binary_string[:3], 2)
    versions_sum[0] += version
    type_id = int(binary_string[3:6], 2)
    # print('{} - Version : {}, Type ID: {}'.format(uid, version, type_id))
    current_packet_length = 6
    current_packet = {
        'parent': parent_packet if parent_packet else 'source',
        'type': type_id,
        'children': []
    }
    packets[uid] = current_packet
    if (current_packet['parent'] != 'source'):
        packets[current_packet['parent']]['children'].append(uid)

    if (type_id != 4):
        length_type_id = int(binary_string[6])
        current_packet_length+=1
        if (length_type_id == 0):
            subpackets_length = int(binary_string[7:22], 2)
            current_packet_length += 15

            parse_binary(binary_string[22:22+subpackets_length], versions_sum, packets, uid, True)
            current_packet_length += subpackets_length
        else:
            subpackets_nb = int(binary_string[7:18], 2)
            current_packet_length += 11
            for i in range(subpackets_nb):
                current_packet_length += parse_binary(binary_string[current_packet_length:], versions_sum, packets, uid)

    else:
        literal_value_to_parse = binary_string[6:]
        literal_value_bin = ''
        while(int(literal_value_to_parse[0]) == 1):
            literal_value_bin += str(literal_value_to_parse[1:5])
            literal_value_to_parse = literal_value_to_parse[5:]
            current_packet_length+=5
        literal_value_bin += str(literal_value_to_parse[1:5])
        current_packet['value'] = int(literal_value_bin, 2)
        current_packet_length+=5

    if(parse_tail):
        other_subpackets = binary_string[current_packet_length:]
        if(other_subpackets and int(other_subpackets, 2) != 0):
            parse_binary(other_subpackets, versions_sum, packets, parent_packet, True)

    return current_packet_length

def main():
    lines = readfile.read_lines("input.txt")

    binary_string =  hex_to_bin(lines[0])

    versions_sum = [0]
    packets_list = {}
    parse_binary(binary_string, versions_sum, packets_list, None)

    print("Version sum: {}".format(versions_sum[0]))

if __name__ == "__main__":
    main()
