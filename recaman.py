

def recaman(seq_len):
    seq = []
    a = 0
    for i in range(seq_len):
        if a - i > 0 and (a - i) not in seq:
            a -= i
        else:
            a += i
        seq.append(a)
    return seq


seq_len = int(input("How long is the sequence?: "))
print(recaman(seq_len))