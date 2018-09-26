def is_prime(data):
    data = int(data)
    import math
    # data = int(input())
    prime = 0
    if data == 1 or data == 0:
        prime = 1
    else:
        for x in range(2, int(math.sqrt(data)+1)):
            if (data % x == 0):
                prime = 1
                break
    if prime == 1:
        # print ("NO")    
        return 0
    else:
        # print ("YES")
        return 1

# def beauti_chk(data):
#     ListData = [int(x) for x in str(data)]
#     position = 0
#     beauti = 0
#     stop = 0
#     while stop == 0:
#         data_to_chk =''
#         for k in range(position,len(ListData)):
#             data_to_chk += str(ListData[k])
#             #print("str",data_to_chk)
#             chk = is_prime(int(data_to_chk))
#             #print(chk)
#             if chk ==1 and k == len(ListData)-1:
#                 stop = 1
#                 beauti = 1
#             elif chk ==0 and k == len(ListData)-1:
#                 print(data_to_chk)
#                 stop = 1
#                 beauti = 0
#             if chk ==1:
#                 position = k+1
                
#                 break
#     #if beauti == 1:
#         #print(data)
#     return beauti
            
def beauti_chk_two(data):
    
    sum = 0
    for i in range(len(data)):
        chk_first_start = data[i]
        #print(chek_first_start)
        if chk_first_start[0] == "0":
            #print("x")
            return 0
        sum += is_prime(int(data[i]))
    if sum == len(data):
        return 1
    else:
        return 0

def permutation(pre,data):
    global beauti
    data = [int(x) for x in str(data)]
    for i in range(len(data)):
        now = ''
        for k in range(0,i+1):
            now += str(data[k])
        
        next = ''
        for j in range(i+1,len(data)):
            next += str(data[j])

        list=[]
        if next != '' and now != '': 
            set = str(pre) + ' ' + str(now) + ' ' + str(next)
            
            #list = []
            data_in = ''
            for l in range(0,len(set)):
                if set[l] != ' ':
                    data_in = str(data_in) + str(set[l])
                elif set[l] == ' ' and data_in !='':
                    list.append(data_in)
                    data_in = ''
            list.append(data_in)
            #print(list)
            test_beauti = beauti_chk_two(list)
            if test_beauti == 1:
                beauti +=1
            else:
                now = str(pre) + ' ' + str(now)
                permutation(now,next)

if __name__ == "__main__":
    count = 0
    num = int(input())
    
    for i in range(0,num+1):
        beauti = 0
        beauti += is_prime(i)
        permutation('',i)
        if beauti>0:
            count +=1
            with open("dataMos.txt", "a") as f:
                f.write(str(i) +"\n")
    print(count)
    #permutation('',302)
 