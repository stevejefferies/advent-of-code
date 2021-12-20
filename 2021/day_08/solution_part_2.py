DATA = 'input_data.txt'

total = 0

with open(DATA) as data:
    for line in data:
        in_value, out_value = line.split('|', 1)
        input_values = in_value.split()
        output_values = out_value.split()
        output_codes = {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None,
        }
        not_matched_values = []
        for val in output_values + input_values:
            val = ''.join(sorted(val))
            match len(val):
                case 2:
                    output_codes[1] = val
                case 3:
                    output_codes[7] = val
                case 4:
                    output_codes[4] = val
                case 7:
                    output_codes[8] = val
                case _:
                    not_matched_values.append(val)
        while len(not_matched_values):
            for val in not_matched_values:
                val = ''.join(sorted(val))
                if len(val) == 6:
                    match = True
                    for char in output_codes[4]:
                        if not char in val:
                            match = False
                    if match:
                        output_codes[9] = val
                    else:
                        match = True
                        for char in output_codes[7]:
                            if not char in val:
                                match = False
                        if match:
                            output_codes[0] = val
                        else:
                            output_codes[6] = val
                    not_matched_values.remove(val)
                if len(val) == 5:
                    match = True
                    for char in output_codes[7]:
                        if not char in val:
                            match = False
                    if match:
                        output_codes[3] = val
                    else:
                        match = True
                        match_string = output_codes[4]
                        for char in output_codes[1]:
                            match_string = match_string.replace(char, '')
                        for char in match_string:
                            if not char in val:
                                match = False
                        if match:
                            output_codes[5] = val
                        else:
                            output_codes[2] = val
                    not_matched_values.remove(val)

        display_value = []
        for val in output_values:
            val = ''.join(sorted(val))
            keys = list(output_codes.keys())
            values = list(output_codes.values())
            display_value.append(str(keys[values.index(val)]))
        total += int(''.join(display_value))

print("Total: " + str(total))