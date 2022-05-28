for num in range(1, 101):
    string = ''

    # ここから記述

    # 条件に応じてstringに値を追加する
    if num % 15 == 0:
        string += 'Fizzbuss'
    elif num % 3 == 0:
        string += 'Fizz'
    elif num % 5 == 0:
        string += 'Buzz'
    else:
        string += str(num)

    # ここまで記述

    print(string)
