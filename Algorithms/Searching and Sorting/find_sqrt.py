num = 9
start = 0
end = 8.0



while start <= end:
    print(start, end)
    mid = (start+end)/2
    mid_square = mid**2
    print(mid_square)

    if abs(mid**2-num) <= 0.001:
        print("hello")
        break 
    elif mid_square < num:
        print("small")
        start = mid+ 0.001
    else:
        print("big")
        end = mid-0.001
    print(start, end)



# def square_root(n, epsilon=1e-10):
#     x = n / 2  # start with an initial guess for the square root
#     while abs(x**2 - n) > epsilon:
#         x = (x + n/x) / 2
#     return x
# print(square_root(0.25))
