def countkDist(inputString, num):
    n = len(inputString)
    result = 0
    cnt = [0] * 27
    for i in range(0, n):
        dist_count = 0
        cnt = [0] * 27
        for j in range(i, n):
            if(cnt[ord(inputString[j]) - 97] == 0):
                dist_count += 1
            cnt[ord(inputString[j]) - 97] += 1
            if(dist_count == num):
                result += 1
            if(dist_count > num):
                break
    return result     
 
  
inputString = input()
num = int(input())
print(countkDist(inputString, num))