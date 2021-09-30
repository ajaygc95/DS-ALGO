image = [[0, 1, 3], [1, 1, 1], [1, 5, 4]]

row = 0
column = 1
new_color = 2




def flood_fill(row, column, new_color, image):

    if not image or image[row][column] == new_color: 
        return image
    value = image[row][column]


    def bfs(row, column, new_color, image, value):

        if row < 0 or row >= len(image) or column < 0 or column>=len(image[0]) or image[row][column] != value :
            return
        image[row][column] = new_color
        bfs(row+1,column, new_color, image, value)
        bfs(row-1,column, new_color, image, value)
        bfs(row,column+1, new_color, image, value)
        bfs(row,column-1, new_color, image, value)


    bfs(row, column, new_color, image, value)
    


flood_fill(0,1,2,image)

for item in image:
    print(item)