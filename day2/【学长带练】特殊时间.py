def answer(november_condition):
    return 4 * ((2 + 1 + 4 + 2) * 4 + november_condition)


def get_h_m(code):
    h1, h2, m1, m2 = code

    return h1 * 10 + h2, m1 * 10 + m2


def judge_time(k, x):
    time_code = [1] * 4
    time_code[k] = x
    
    h, m = get_h_m(time_code)

    return h < 24 and m < 60


if __name__ == '__main__':
    cnt = 0
    for x in range(3, 10):
        for k in range(4):
            if judge_time(k, x):
                cnt += 1
    
    print(answer(cnt))
