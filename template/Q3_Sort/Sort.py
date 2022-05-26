from re import S
from openpyxl import NUMPY


def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
    #    print(array)
    #    print("array")
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述


    pivot_count = 0
    left = []
    right = []
    pivot_index = 0
    array_index = list(range(len(array)))[::-1]
    flag=0
    for i,j in enumerate(array):
        for index,num in enumerate(reversed(array)):
            if i+1 == array_index[index]:
                flag = 1
                break

            elif j >= pivot:
                pivot2 = j
                pivot2_index = i
                if num < pivot:
                    array[pivot2_index], array[array_index[index]], = array[array_index[index]], array[pivot2_index]
                    break
            
            elif num < pivot:
                array[pivot2_index], array[array_index[index]], = array[array_index[index]], array[pivot2_index]
                break
        else:
            continue
        left = array[:i+1]
        right = array[i+1:] 
        pivot_count += 1
        if flag:
            break
    #print("left")
    #print(left, right)

    left = sort(left)
    right = sort(right)

    return left  + right
       


#    for i,j in enumerate(array):
#        if j >= pivot:
#            pivot2 = j
#            pivot2_index = i
#            for index,num in enumerate(reversed(array)):
#                if i+1 == array_index[index]:
#                    break
#
#                elif num < pivot2:
#                    array[pivot2_index], array[array_index[index]], = array[array_index[index]], array[pivot_index]
#                    break
#        else:
#            left = array[:i]
#            right = array[array_index[index]:]
#            pivot_count += 1
#            continue

#    left = sort(left)
#    right = sort(right)
#
#    return left + right
#
#    for index,num in enumerate(reversed(array)):
#        if num < pivot:
#            array[pivot_index], array[-index], = array[-index], array[pivot_index]
#            for i,j in enumerate(array):
#                if j >= pivot:
#                    pivot = i
#                    pivot_index = i
#                    break
            


#    for num in array:
#        if num < pivot:
#            left.append(num)
#        elif num > pivot:
#            right.append(num)
#        else:
#            pivot_count += 1
#    left = sort(left)
#    right = sort(right)
#
#    return left + [pivot] * pivot_count + right

    # ここまで記述

if __name__ == '__main__':
    main()
