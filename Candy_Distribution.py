def candy_distribution(ratings):
    n = len(ratings)
    output = 0
    candies_distributed=[]
    #each child gets one candy atleast
    for i in range(n):
        candies_distributed.append(1)
    print(candies_distributed)
    for i in range(n):
        if i+1<n:
            if ratings[i]>ratings[i+1]:
                candies_distributed[i] = candies_distributed[i] + 1
                print(candies_distributed)
            elif ratings[i+1]>ratings[i]:
                candies_distributed[i+1] =candies_distributed[i+1] + 1
        if i==n-1:
            if ratings[i]<ratings[i-1]:
                candies_distributed[i] = candies_distributed[i] - 1
                
                
                
    for candy in candies_distributed:
        output += candy
    return output

ratings = [1,0,2]
result = candy_distribution(ratings)
print(result)
