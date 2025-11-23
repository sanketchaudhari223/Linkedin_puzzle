import cv2 as cv
import numpy as np
import pandas as pd

# Reading an image
img = "test1.png"
original = cv.imread(img)
#new_dimensions = (10, 10)
#gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
#resized_image = cv.resize(original, new_dimensions, interpolation=cv.INTER_AREA)
#original.shape[0]
#original[0][0]
#print(int(original.size()))
#np.where(original[0] == [0,0,0])
#original[100,159:169]


img_width = original.shape[1] 
img_height = original.shape[0]
m_row = 7
m_col = 7
new_dimensions = (10, 10)
print(img_height,img_width)


step_row = img_height // m_col
step_col = img_width // m_row
it_row = step_row // 2
it_col = step_col // 2
start_row = it_row
start_col = it_col
#print(it_row,it_col)
#print(step_row,step_col)
#print(it_row,it_col)
color_mat = np.zeros((m_row, m_col), dtype=int) 
paint_color = 1
#color_mat[0][0] = paint_color
#paint_color = paint_color + 1
i = 0 
j = 0
#print(it_row,it_col)
#it_col = it_col + step_col
#print(it_row,img_height)
#print(it_row,it_col)
'''try :
    while i < m_col :
        while j < m_row :
            
            if(((it_row - step_row)>=start_row and (it_col - step_col) >= start_col) and np.array_equal(original[it_row][it_col], original[it_row - step_row][it_col - step_col])):
                color_mat[i][j] = color_mat[i-1][j-1]
                #print("if",i,j,original[it_row][it_col],color_mat[i][j])
            elif((it_row - step_row)>=start_row and np.array_equal(original[it_row][it_col], original[it_row - step_row][it_col])):
                color_mat[i][j] = color_mat[i-1][j]
                #print("else1",i,j,original[it_row][it_col],color_mat[i][j])
            elif(((it_row - step_row)>=start_row and (it_col + step_col) < img_width) and np.array_equal(original[it_row][it_col], original[it_row - step_row][it_col + step_col])):
                color_mat[i][j] = color_mat[i-1][j+1]
                #print("else2",i,j,original[it_row][it_col],color_mat[i][j])
            elif((it_col - step_col) >= start_col and np.array_equal(original[it_row][it_col], original[it_row][it_col - step_col])):
                color_mat[i][j] = color_mat[i][j-1]
                #print("else3",i,j,original[it_row][it_col],color_mat[i][j])
            else:
                color_mat[i][j] = paint_color
                paint_color = paint_color + 1
                #print("else",i,j,original[it_row][it_col],color_mat[i][j])
            it_col = it_col + step_col
            j = j + 1
        it_col = start_col
        j = 0
        it_row = it_row + step_row
        i = i + 1
except IndexError :
    print('error')
#print(original[start_row,start_col + step_col * 7],original[start_row,start_col + step_col * 8],original[start_row,start_col + step_col * 9])
#print(i,j)
print(color_mat)'''

color_dict = {}
print(step_row,step_col)
print(it_row,it_col)
print(start_row,start_col)
print(color_mat)

while i < m_col :
    
    while j < m_row :
        #print(it_row,it_col)
        #print(original[it_row][it_col])
        if tuple(original[it_row][it_col]) not in color_dict:
            color_dict[tuple(original[it_row][it_col])] = paint_color
            paint_color = paint_color + 1
        color_mat[i][j] = color_dict[tuple(original[it_row][it_col])]
        it_col = it_col + step_col
        j = j + 1
    it_col = start_col
    j = 0
    it_row = it_row + step_row
    i = i + 1
        
i,j = 0,0
#paint_color = 10 #paint_color - 1
color_taken = np.zeros(paint_color,dtype=int)
ans_mat = np.zeros((m_row, m_col), dtype=int)
row_pack = np.zeros(m_row,dtype=int)
col_pack = np.zeros(m_col,dtype=int)
print(paint_color)
print(color_taken.shape,row_pack.shape,col_pack.shape)

def check_condition(i,j,ans_mat):
    if i-1 >= 0 and j-1 >= 0 and ans_mat[i-1][j-1] == 1:
        return False
    elif i+1 < m_row and j+1 < m_col and ans_mat[i+1][j+1] == 1:
        return False
    elif i-1 >= 0 and j+1 < m_col and ans_mat[i-1][j+1] == 1:
        return False
    elif i+1 < m_row and j-1 >= 0 and ans_mat[i+1][j-1] == 1:
        return False
    return True

def back_track_queen(i,j,m_row,paint_color,m_col,color_taken,color_mat,row_pack,col_pack,ans_mat):
    if(i == m_row):
        if(paint_color == 1):
            return True
        else:
            return False

    while(j < m_col):
        #print(i,j)
        if color_taken[color_mat[i][j]] == 0 and row_pack[i] == 0 and col_pack[j] == 0 and check_condition(i,j,ans_mat):
            color_taken[color_mat[i][j]] = 1
            row_pack[i] = 1
            col_pack[j] = 1
            ans_mat[i][j] = 1
            i = i + 1
            paint_color = paint_color - 1
            if back_track_queen(i,0,m_row,paint_color,m_col,color_taken,color_mat,row_pack,col_pack,ans_mat) :
                return True
            i = i - 1
            color_taken[color_mat[i][j]] = 0
            row_pack[i] = 0
            col_pack[j] = 0
            ans_mat[i][j] = 0
            paint_color = paint_color + 1
        j = j + 1
    return False

print(back_track_queen(i,j,m_row,paint_color,m_col,color_taken,color_mat,row_pack,col_pack,ans_mat) )
print(ans_mat) 
print()
color_mat