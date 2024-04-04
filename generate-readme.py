import csv
from pytablewriter import MarkdownTableWriter
from pytablewriter.style import Style

engines = [ 'Base', 'DelphiDoom', 'DSDA-Doom', 'Eternity', 'GZDoom' ]
map_elements = [ 'linedef', 'sidedef', 'sector', 'vertex', 'thing' ]
data_types = [ 'int', 'float', 'bool', 'string', '-' ]
file_name_template = 'csv/{0}-{1}.csv'
output_file_name = 'README.md'
output_template = 'readme_template.txt'
all_fields = {}

data = {}

for map_element in map_elements:
    data[map_element] = {}
    all_fields[map_element] = set()
    for engine in engines:
        data[map_element][engine] = {}
        file_name = file_name_template.format(engine.lower(), map_element)
        with open(file_name, 'r', newline='') as file:
            csv_reader = csv.reader(file, delimiter=';', quotechar='"')
            for line in csv_reader:
                data_type = None
                if len(line) == 0:
                    continue
                if len(line) == 1:
                    print(f'{file_name}: {line[0]} has no data type')
                if len(line) >= 1:
                    field = line[0]
                    if line[1] not in data_types:
                        print(f'{file_name}: unsupported data type {line[1]} for field {field}')
                    data_type = line[1]
                data[map_element][engine][field] = {
                    'type': data_type
                }
                all_fields[map_element].add(field)

with open(output_file_name, 'w', encoding='utf-8') as output_file:
    with open(output_template, 'r') as template_file:
        output_file.write(template_file.read() + '\n')

    for map_element in data:
        value_matrix = []
        for field in sorted(all_fields[map_element]):
            values = [ field ]
            types = set()
            for engine in engines:
                if field in data[map_element][engine]:
                    types.add(data[map_element][engine][field]['type'])
                    values.append('✔️')
                else:
                    #values.append('❌')
                    values.append('-')
            if len(types) == 1:
                values.insert(1, list(types)[0])
            else:
                values.insert(1, '*mixed*')
                for i, engine in enumerate(engines):
                    if field in data[map_element][engine]:
                        values[2 + i] = f'{values[2 + i]} ({data[map_element][engine][field]["type"]})'
            value_matrix.append(values)

        writer = MarkdownTableWriter(
            #table_name = map_element.capitalize(),
            headers = [ 'Field', 'Type' ] + engines,
            value_matrix = value_matrix,
            column_styles = [ Style(), Style() ] + [ Style(align='center') for e in engines ]
        )
        output_file.write(f'## { map_element.capitalize()}\n')
        output_file.write(writer.dumps())
        output_file.write('\n')


