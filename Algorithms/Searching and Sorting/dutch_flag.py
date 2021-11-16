given_liset =  ["B", "R"]

def swap(a,b,array):
    array[a], array[b] = array[b], array[a]

def dutch_sort(balls):

    i = 0
    g = -1
    r = -1

    while i < len(balls):
        if balls[i] == "G":
            g += 1 #0
            swap(i,g,balls)
        
        if balls[i] == "R":
            g += 1
            swap(i,g,balls)

            r += 1
            swap(r,g,balls)
        i += 1
dutch_sort(given_liset)
print(given_liset)
            




