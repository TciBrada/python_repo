import os


def filelines_to_list(full_path):
    """ Returns the lines of the given file in a lst in alphabetical order """
    lst = []
    with open(full_path) as f:
        for tc_id in f:
            lst.append(tc_id.strip())
    f.close()
    return sorted(lst)


def list_compare(ls_1, ls_2):
    """ Based on 2 lists as input parameters it returns 3 lists:
            1st with common elements,
            2nd with only list A elements and
            3rd with only list B elements """
    ls_common = list(set(ls_1) & set(ls_2))
    ls_a = list((set(ls_1) | set(ls_2)) - set(ls_2))
    ls_b = list((set(ls_1) | set(ls_2)) - set(ls_1))
    return sorted(ls_common), sorted(ls_a), sorted(ls_b)


def write_list_to_file(lst_to_be_written, file_name):
    """ Function writes the items of the given list to text file defined by parameter """
    with open(file_name, "w") as f:
        for item in lst_to_be_written:
            f.writelines(item + '\n')
    f.close()


path: str = r'd:\SVN\mss_python\My_Shit\my_python_scripts\tc_set_compare_files\\'
file_name_set_a = 'tc_set_A'
file_name_set_b = 'tc_set_B'
file_ext = '.txt'

full_path_file_a = os.path.join(path + file_name_set_a + file_ext)
full_path_file_b = os.path.join(path + file_name_set_b + file_ext)

full_path_file_a_sorted = os.path.join(path + '_' + file_name_set_a + '_sorted' + file_ext)
full_path_file_b_sorted = os.path.join(path + '_' + file_name_set_b + '_sorted' + file_ext)

full_path_file_a_b_common = os.path.join(path + '_tc_set_A_B_common' + file_ext)
full_path_file_only_a = os.path.join(path + '_tc_set__only_in_set_A' + file_ext)
full_path_file_only_b = os.path.join(path + '_tc_set__only_in_set_B' + file_ext)

lst_common = []
lst_a = []
lst_b = []

tc_list_sorted_a = filelines_to_list(full_path_file_a)
tc_list_sorted_b = filelines_to_list(full_path_file_b)


lst_common, lst_a, lst_b = list_compare(tc_list_sorted_a, tc_list_sorted_b)

print('"' + file_name_set_a + file_ext + '" contains ' + str(len(tc_list_sorted_a)) + ' items')
print(tc_list_sorted_a)
write_list_to_file(tc_list_sorted_a, full_path_file_a_sorted)

print('"' + file_name_set_b + file_ext + '" contains ' + str(len(tc_list_sorted_b)) + ' items')
print(tc_list_sorted_b)
write_list_to_file(tc_list_sorted_b, full_path_file_b_sorted)

print('Common items of A and B sets: ' + str(len(lst_common)) + ' piece(s)')
print(lst_common)
write_list_to_file(lst_common, full_path_file_a_b_common)

print('Items only of set A: ' + str(len(lst_a)) + ' piece(s)')
print(lst_a)
write_list_to_file(lst_a, full_path_file_only_a)

print('Items only of set B: ' + str(len(lst_a)) + ' piece(s)')
print(lst_b)
write_list_to_file(lst_b, full_path_file_only_b)

