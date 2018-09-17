import os

path = 'd:\\Tomi\\python_projects\\text_files\\'
file_name = 'TCs'
file_ext = '.txt'
full_path = os.path.join(path + file_name + file_ext)

print('\neleresi utvonal: ' + full_path)
with open(full_path, 'r') as f:
    text = f.read()
    print('\na teljes file tartalma:\n' + text)
    f.close()
tc_list = []
with open(full_path, 'r') as f:
    i = 1
    print('a file tartalma soronkent:')
    while True:
        line = f.readline()
        if not line:
            break
        print('%s.sor: ' % i, line.strip())
        tc_list.append(line.strip())

        i = i + 1
    f.close()
print('\na lista tartalma:')
print(tc_list)
print('\na lista emelkedo sorrendben:')
sorted_tc_list = sorted(tc_list)
print(sorted(sorted_tc_list))

with open(path + file_name + '_sorted' + file_ext, 'w') as f:
    for tc_id in sorted_tc_list:
        f.writelines(tc_id + '\n')
    f.close()

with open(path + file_name + '_sorted' + file_ext) as f:
    sorted_file_content = f.read()
    print('\na teljes rendezett file tartalma visszaolvasva:\n' + sorted_file_content)
    f.close()




