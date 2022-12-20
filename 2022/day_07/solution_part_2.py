DATA = 'input_data.txt'

total: int = 0
directories = []

current_directory = None
path = []

with open(DATA) as data:
    for line in data:
        if line.startswith('$'):
            cmd_parts = line.split(' ')
            if cmd_parts[1] == 'cd':
                dir = cmd_parts[2].strip()
                if dir == '..':
                    path.pop()
                else:
                    path.append(dir)
                    directories.append({'name': dir, 'path': path.copy(), 'filesize': 0})
        elif line.startswith('dir'):
            obj_type, name = line.split(' ')
        else:
            # must be a file
            size = int(line.split(' ')[0])
            total += size
            directories[-1]['filesize'] += size
            parent_path = []
            for dir in directories[-1]['path'][:-1]:
                parent_path.append(dir)
                for d in directories:
                    if d['path'] == parent_path:
                        d['filesize'] += size

smallest_file = None
for dir in directories:
    if (70000000-total) + dir['filesize'] >= 30000000:
        if not smallest_file:
            smallest_file = dir['filesize']
        else:
            if dir['filesize'] < smallest_file:
                smallest_file = dir['filesize']

print(smallest_file)            
