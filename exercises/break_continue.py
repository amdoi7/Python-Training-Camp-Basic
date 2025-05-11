"""
练习: break和continue语句

描述：
返回从1到n的所有非3的倍数的整数列表。

请补全下面的函数，使用continue语句跳过3的倍数。
"""


def skip_multiples_of_three(n):
    """
    返回从1到n的所有非3的倍数的整数列表

    参数:
    - n: 正整数上限

    返回:
    - 从1到n中所有不是3的倍数的整数列表
    """
    return [x for x in range(1, n + 1) if x % 3 != 0]

    # result = []
    # for num in range(1, n + 1):
    #     if num % 3 == 0:
    #         continue  # 跳过3的倍数
    #     result.append(num)
    # return result
