from collections import deque

image = [[0, 1, 3], [1, 1, 1], [1, 5, 4]]

pixel_row = 0
pixel_col = 1
new_color = 2


def overall(row,col):

    visited = []
    given = image[row][col]

    def getNbr(row, col):
        result = []

        if row-1 >=0:
            result.append((row,col))
        
        if col-1 >=0:
            result.append((row,col-1))

        if row+1 < len(image):
            result.append((row+1,col))
        
        if col+1 <len(image[0]):
            result.append((row, col+1))
        
        return result
    
    def helper(row, col):

        image[row][col] = new_color
        visited.append((row,col))
        q  = deque()
        q.append((row,col))
        


        while q:
            new_row, new_col = q.popleft()

            for i,j in getNbr(new_row, new_col):
                
                if (i,j) not in visited:
                    if image[i][j] == given:
                        image[i][j] = new_color
                        visited.append((i,j))
                        q.append((i,j))

        # for i,j in getNbr(row, col):

        #     if (i,j) not in visited:
        #         if image[i][j] == given:
        #             image[i][j] = new_color
        #             visited.append((i,j))
        #             helper(i,j)
            
    helper(row,col)

overall(pixel_row, pixel_col)
print(image)








































# row = 0
# column = 1
# new_color = 2




# def flood_fill(row, column, new_color, image):

#     if not image or image[row][column] == new_color: 
#         return image
#     value = image[row][column]


#     def bfs(row, column, new_color, image, value):

#         if row < 0 or row >= len(image) or column < 0 or column>=len(image[0]) or image[row][column] != value :
#             return
#         image[row][column] = new_color
#         bfs(row+1,column, new_color, image, value)
#         bfs(row-1,column, new_color, image, value)
#         bfs(row,column+1, new_color, image, value)
#         bfs(row,column-1, new_color, image, value)


#     bfs(row, column, new_color, image, value)
    


# flood_fill(0,1,2,image)

# for item in image:
#     print(item)