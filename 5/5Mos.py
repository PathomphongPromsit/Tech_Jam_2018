def solution(A,S):
        LEN = len(A)
        max = 0
        for i in range(0,LEN):
            sum = 0
            for j in range(i,LEN):
                sum = sum+ int(A[j])
                if sum ==S:
                    length = (j+1)-i
                    if length >max:
                        max = length
        print(max)

if __name__ == '__main__':
    A = [1, 0, -1, 1, 1, -1, -1]
    S = int(input())
    solution(A,S)
   