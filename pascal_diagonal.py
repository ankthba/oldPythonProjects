from math import comb

feb_seq_list = [1,1]

def populate_feb_seq(max_val):
    while True:
        seq_len = len(feb_seq_list)
        next_val = feb_seq_list[seq_len - 1] + feb_seq_list[seq_len - 2]
        if(next_val <= max_val):
            feb_seq_list.append(next_val)
        else:
            break


def find_feb_list_idx(feb_num):
    list_idx = -1
    for idx in range(len(feb_seq_list)):
        if feb_seq_list[idx] == feb_num:
            list_idx = idx
            break
    return list_idx


def get_pascal_diag(idx):
    diag = []
    for n in reversed(range(idx+1)):
        for r in range(idx+1):
            if(n >= r and n+r == idx):
                diag.append(comb(n,r))
                
    return " ".join(str(i) for i in diag)

def get_feb_num_pascal_diag(feb_num):
    populate_feb_seq(feb_num)
    idx = find_feb_list_idx(feb_num)
    if (idx > -1):
        diag = get_pascal_diag(idx)
        return diag
    else: 
        return "ERROR"
    
if __name__ == "__main__":
    feb_num = int(input("Enter feb seq number: "))
    print(get_feb_num_pascal_diag(feb_num))