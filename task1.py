def group_by_owners(files):
    files_name= list(files.values())
    # print(files_name)
    files_name = set(files_name)
    # print(files_name)
    files_name = list(files_name)
    # print(files_name)
    owners = list(files.keys())
    
    dict_con = {}
    number_files = len(files_name)
    number_owners = len(owners)
    for i in range(number_files):
        for j in range(number_owners):
            if files_name[i] ==list(files.values())[j]:
                files_list = [owners[j]]
                # print(files_list)
                if files_name[i] in dict_con:
                    dict_con[files_name[i]].append(owners[j])
                else:
                    dict_con[files_name[i]] = files_list
    return dict_con





files = {
"Input.txt": 'Randy',
'Code.py': 'Stan',
'Output.txt': 'Randy'
}
print(group_by_owners(files))