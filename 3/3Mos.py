def solution(A, K, L):
    if K+L > len(A):
        return -1
    else:
        if K>L:
            LEN_st = K
            LEN_nd = L
        else:
            LEN_st = L
            LEN_nd = K
        #############ST###################
        max_st = 0
        index_start = 0
        index_stop = 0
        stop = (len(A)-LEN_st)+1
        for i in range(0,stop):
            sum = 0
            for j in range(i,i+LEN_st):
                sum = sum+int(A[j])
            if sum > max_st:
                max_st = sum
                index_start = i
                index_stop = (i+LEN_st)-1
        del A[index_start:index_stop+1]

        #################ND################
        max_nd = 0
        index_start = 0
        index_stop = 0
        stop = (len(A)-LEN_nd)+1
        for i in range(0,stop):
            sum = 0
            for j in range(i,i+LEN_nd):
                sum = sum+int(A[j])
            if sum > max_nd:
                max_nd = sum
                index_start = i
                index_stop = (i+LEN_nd)-1
        MAX = max_st+max_nd
        return MAX

            
        
if __name__ == '__main__':
    A = list(input())
    K = int(input())
    L = int(input())
    max = solution(A,K,L)
    print(max)
    

