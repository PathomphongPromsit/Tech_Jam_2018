def is_prime(data):
    data = int(data)
    import math
    # data = int(input())
    prime = 0
    if data == 1 or data == 0:
        # prime = 1
        return 0
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

def is_beauty(text, start, end_point, li = []):
    # print (text, start, end_point+1, len(text)-1)
    if end_point == len(text)-1 or start == len(text)-1 :
        # print("end", start, end_point, text[start: end_point+1])
        if is_prime(text[start: end_point+1]):
            return 1
        else :
            return 0
    if is_prime(text[start:end_point+1]):
        # check if text start by 0
        if text[start] == '0' :
            print(text)
            # if already end of range
            if start == len(text)-1 :
                return 0
            else :
                return is_beauty(text, start+1, end_point+1, li)
        else:
            # print ("detected prime", text, start, end_point, text[start:end_point+1])
            return is_beauty(text, end_point+1, end_point+2, li)
    else:
        # print ("not dected", text, start, end_point+1)
        return is_beauty(text, start, end_point+1, li)

def main():
    answer = []
    count = 0
    # for number in range(10000,100000):
    for number in range(10000,100000):
        if is_beauty(str(number),0,0):
            answer.append(number)
            count+=1

    print("count", count)
    """
    write file 
    you can comment it 
    """
    with open("list.txt", 'w') as f:
        for num in answer:
            f.write("%s\n" % num)
    # f.write(answer)
    # print("members", answer)
                    
if __name__ == '__main__':
    main()
    # print (is_beauty('7007', 0, 0))

