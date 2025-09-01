def oprate(custom_num,drink_lst, custom_lst):
    tmp_len=0
    index_lst=[]
    for i in range(custom_num):
        tmp_lst=[]
        index_lst.append(i)
        tmp_lst.append(custom_lst[i][0])
        tmp_lst.append(custom_lst[i][1])
        for indx,cus in enumerate(custom_lst):
            if indx in index_lst:
                continue
            if cus[0] in tmp_lst or cus[1] in tmp_lst:
                continue
            tmp_lst.append(cus[0])
            tmp_lst.append(cus[1])
        if len(tmp_lst)>tmp_len:
            tmp_len=len(tmp_lst)
    return tmp_len/2

line = input()
ln = line.split(" ")
custom_num = int(ln[0])
drink_num = int(ln[1])
drink_lst = [i for i in range(drink_num)]
custom_lst=[]

while True:
    line=input()
    if line=="":
        break
    lns = line.split(" ")
    custom_lst.append([int(lns[0]),int(lns[1])])


num_len = oprate(custom_num=custom_num,
                 drink_lst=drink_lst,
                 custom_lst=custom_lst)
print(int(num_len))


