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
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    # 配列の逆向きのインデックス番号を取得
    reverse_array_index = list(range(len(array)))[::-1]
    flag = 0

    # 条件を満たす値を左側と右側から探す
    for left_index, left_num in enumerate(array):
        for right_index, right_num in enumerate(reversed(array)):
    
    # 左側と右側からの探索がぶつかったところで処理を終了するフラグを立てる
            if left_index + 1 == reverse_array_index[right_index]:
                flag = 1
                break

    # 左側からの探索で見つかった値を取得
            elif left_num >= pivot:
                left_pivot = left_num
                left_pivot_index = left_index
    
    # 条件を満たした場合は値を入れ替える
                if right_num < pivot:
                    array[left_pivot_index], array[reverse_array_index[right_index]], = array[reverse_array_index[right_index]], array[left_pivot_index]
                    break

    # 条件を満たした場合は値を入れ替える        
            elif right_num < pivot:
                array[left_pivot_index], array[reverse_array_index[right_index]], = array[reverse_array_index[right_index]], array[left_pivot_index]
                break
        else:
            continue

    # 左側と右側に分割する
        left = array[:left_index+1]
        right = array[left_index+1:] 

    # フラグが立っている場合は処理を終了する
        if flag:
            break

    # 分割した配列について再帰的に処理を行う
    left = sort(left)
    right = sort(right)

    return left  + right
 
    # ここまで記述

if __name__ == '__main__':
    main()
