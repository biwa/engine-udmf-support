import pathlib
import re
import requests
import time

def get_remote_data(url, as_json=False):
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception(f'Failed getting {url}')
    if as_json:
        return r.json()
    else:
        return r.text
    
def is_source_current(filename):
    file = pathlib.Path(filename)
    max_age = 60*60*24 # 1 day
    
    if not file.exists() or file.stat().st_mtime+max_age < time.time():
        return False
    
    return True

def fill_base_data(data):
    for map_element in data.keys():
        with open(f'../csv/base-{map_element}.csv') as file:
            for line in file:
                prop_name, prop_type = line.strip().split(';')
                data[map_element][prop_name] = prop_type
    
    return data


def generate_eternity():
    filename = 'eternity-udmf.txt'
    url = 'https://eternity.youfailit.net/rest.php/v1/page/UDMF'

    if not is_source_current(filename):
        print(f'Eternity: getting {url}')

        try:
            remote_data = get_remote_data(url, True)
        except Exception as e:
            print(e)
            return
        
        try:
            text_data = remote_data['source']
        except KeyError:
            print("Eternity: 'source' could not be found in JSON data.")
            return
        
        with open(filename, 'w') as file:
            file.write(text_data)
    else:
        print(f'Eternity: {filename} is up-to-date')

    data = {
        'linedef': { },
        'sector': { },
        'sidedef': { },
        'thing': { },
        'vertex': { }
    }

    fill_base_data(data)

    with open(filename) as file:
        lines = list(filter(None, [ line.split('//', 1)[0].strip() for line in file ]))

    i = 0
    current_map_element = None

    while i < len(lines):
        if lines[i] in data.keys() and lines[i+1] == '{':
            current_map_element = lines[i]
            i += 1

        if lines[i] == '}':
            current_map_element = None

        if current_map_element is not None:
            mo = re.search(r'(\w+)\s+=\s+<([-\w]+)>', lines[i])
            
            if mo is not None:
                prop_name = mo.group(1)
                prop_type = mo.group(2)

                if prop_type == 'integer':
                    prop_type = 'int'
                elif prop_type == 'floating-point':
                    prop_type = 'float'
                elif prop_type == 'boolean':
                    prop_type = 'bool'
                
                data[current_map_element][prop_name] = prop_type            

        i += 1

    print('Eternity: writing CSV files...')

    for map_element in data:
        csv_filename = f'../csv/eternity-{map_element}.csv'
        print(f'Eternity: writing {csv_filename}')
        with open(csv_filename, 'w', newline='\n') as outfile:
            for key in sorted(data[map_element].keys()):
                outfile.write(f'{key};{data[map_element][key]}\n')

def generate_dsda_doom():
    filename = 'dsda-doom-udmf.txt'
    url = 'https://raw.githubusercontent.com/kraflab/dsda-doom/master/docs/udmf.md'

    if not is_source_current(filename):
        print(f'DSDA-Doom: getting {url}')

        try:
            text_data = get_remote_data(url)
        except Exception as e:
            print(e)
            return
        
        with open(filename, 'w') as file:
            file.write(text_data)
    else:
        print(f'DSDA-Doom: {filename} is up-to-date')

    data = {
        'linedef': { 'comment': 'string' },
        'sector': { 'comment': 'string' },
        'sidedef': { 'comment': 'string' },
        'thing': { 'comment': 'string' },
        'vertex': { }
    }

    fill_base_data(data)

    current_map_element = None

    with open (filename) as file:
        for line in file:
            if line.startswith('###'):
                if line.startswith('### Linedefs'):
                    current_map_element = 'linedef'
                elif line.startswith('### Sidedefs'):
                    current_map_element = 'sidedef'
                elif line.startswith('### Vertices'):
                    current_map_element = 'vertex'
                elif line.startswith('### Sectors'):
                    current_map_element = 'sector'
                elif line.startswith('### Things'):
                    current_map_element = 'thing'
                else:
                    current_map_element = None
                
                continue

            if current_map_element is not None and line.startswith('|'):
                mo = re.search(r'\*\*(\w+)\*\*\s+_(\w+)_', line)

                if mo is not None:
                    prop_name = mo.group(1)
                    prop_type = mo.group(2)

                    if prop_type == 'integer':
                        prop_type = 'int'
                    
                    data[current_map_element][prop_name] = prop_type

    print('DSDA-Doom: writing CSV files...')

    for map_element in data:
        csv_filename = f'../csv/dsda-doom-{map_element}.csv'
        print(f'DSDA-Doom: writing {csv_filename}')
        with open(csv_filename, 'w', newline='\n') as outfile:
            for key in sorted(data[map_element].keys()):
                outfile.write(f'{key};{data[map_element][key]}\n')

def generate_gzdoom():
    filename = 'gzdoom-udmf.txt'
    url = 'https://raw.githubusercontent.com/ZDoom/gzdoom/master/specs/udmf_zdoom.txt'

    if not is_source_current(filename):
        print(f'GZDoom: getting {url}')

        try:
            text_data = get_remote_data(url)
        except Exception as e:
            print(e)
            return
        
        with open(filename, 'w') as file:
            file.write(text_data)
    else:
        print(f'GZDoom: {filename} is up-to-date')

    data = {
        'linedef': { },
        'sector': { },
        'sidedef': { },
        'thing': { },
        'vertex': { }
    }

    fill_base_data(data)

    with open(filename) as file:
        lines = list(filter(None, [ line.split('//', 1)[0].strip() for line in file ]))

    i = 0
    current_map_element = None

    while i < len(lines):
        if lines[i] in data.keys() and lines[i+1] == '{':
            current_map_element = lines[i]
            i += 1

        if lines[i] == '}':
            current_map_element = None

        if current_map_element is not None:
            mo = re.search(r'(\w+)\s+=\s+<(\w+)>', lines[i])
            
            if mo is not None:
                prop_name = mo.group(1)
                prop_type = mo.group(2)

                if prop_type == 'integer':
                    prop_type = 'int'
                
                data[current_map_element][prop_name] = prop_type            

        i += 1

    # The specs do not list all skill and class variants, so fix that
    for i in range(6, 17):
        data['thing'][f'skill{i}'] = 'bool'

    for i in range(4, 17):
        data['thing'][f'class{i}'] = 'bool'

    print('GZDoom: writing CSV files...')

    for map_element in data:
        csv_filename = f'../csv/gzdoom-{map_element}.csv'
        print(f'GZDoom: writing {csv_filename}')
        with open(csv_filename, 'w', newline='\n') as outfile:
            for key in sorted(data[map_element].keys()):
                outfile.write(f'{key};{data[map_element][key]}\n')

if __name__ == '__main__':
    generate_dsda_doom()
    generate_eternity()
    generate_gzdoom()
