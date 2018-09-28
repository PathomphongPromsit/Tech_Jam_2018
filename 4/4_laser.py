import math
def laser(data):
    
    degree_set =[]
    for i in data:
        pair = i.split(',')
        x = int(pair[0])
        y = int(pair[1])
        #print("x,y",x,y)
        
        if x == 0 and y > 0:   
            degree = 90    
        elif x == 0 and y < 0:
            degree = 270
        elif x > 0 and y == 0: 
            degree = 0
        elif x < 0 and y== 0: 
            degree = 180
        else:
            degree = math.atan2(y, x)
            
        # elif x > 0 and y > 0: #Q1
        #     print("Q1")
        #     degree = math.atan2(y, x)
        # elif x < 0 and y > 0: #Q2
        #     print("Q2")
        #     degree = math.atan2(y, x)
        # elif x < 0 and y < 0: #Q3
        #     print("Q3")
        #     degree = math.atan2(y, x)
        # elif x > 0 and y < 0: #Q4
        #    degree = math.atan2(y, x)
        #print(degree)
        if degree not in degree_set:
            degree_set.append(degree)
    return len(degree_set)

if __name__ == "__main__":
    raw_data = input().split()
    shot = laser(raw_data)
    print(shot)