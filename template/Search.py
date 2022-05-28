from operator import le


def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    # 左端と右端のインデックス番号をセット
    left_index = 0
    right_index = len(sorted_array) - 1

    # 右端よりも左端のインデックス番号のほうが大きくなった場合は処理を終了
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        
        # 配列の中央に正解があった場合その値を返す
        if sorted_array[mid_index] == target_number:
            return mid_index
        # 配列の中央の値が正解よりも小さかった場合は配列の左側を探索する
        elif sorted_array[mid_index] < target_number:
            left_index = mid_index + 1
        # 配列の中央の値が正解よりも大きかった場合は配列の右側を探索する
        elif sorted_array[mid_index] > target_number:
            right_index = mid_index - 1
    
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
