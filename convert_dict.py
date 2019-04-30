def convert_dict(prop_idents):
    identifier_nodes_dict = {}
    count = 0
    keys = set()
    for P_number,p_entity in prop_idents.items():
        count += 1
        print(P_number)
        print(count)
        for identi,Q_number in p_entity.items():
            #if identi in identifier_nodes_dict.keys():
            if identi in keys:
                identifier_nodes_dict[identi].append(P_number + '/' + Q_number)
            else:
                keys.add(identi)
                identifier_nodes_dict[identi] = [P_number + '/' + Q_number]
    return identifier_nodes_dict

def dict_slice(adict, start, end):
    keys = adict.keys()
    dict_slice = {}
    for k in keys[start:end]:
        dict_slice[k] = adict[k]
    return dict_slice
