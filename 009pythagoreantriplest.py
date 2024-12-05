def pythagoreanTriplets() :
    list = []
    sum, m = 0, 2

    while sum < 2000 : 
          
        for n in range(1, m) : 
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n 

            sum = a+b+c
            if sum > 2000 : 
                break
  
            list.append([a, b, c, sum])
  
        m = m + 1
    
    return list
  
for triplets in pythagoreanTriplets():
    if triplets[3] == 1000:
        print(triplets)
        print(triplets[0]*triplets[1]*triplets[2])