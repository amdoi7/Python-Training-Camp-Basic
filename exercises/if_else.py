"""
练习: if-elif-else 条件语句

描述：
根据学生的成绩判断其等级。
- 成绩 >= 90: 优秀
- 成绩 >= 80: 良好
- 成绩 >= 70: 中等
- 成绩 >= 60: 及格
- 成绩 < 60: 不及格

请补全下面的函数，实现成绩等级判断。
"""

import bisect


def check_grade(score):
    """
    根据分数返回等级

    参数:
    - score: 学生分数，0-100的整数

    返回:
    - 对应的等级：优秀、良好、中等、及格、不及格
    """
    # 法一
    # grade_ranges = {
    #     (90, 100): "优秀",
    #     (80, 89): "良好",
    #     (70, 79): "中等",
    #     (60, 69): "及格",
    #     (0, 59): "不及格",
    # }

    # for (low, high), grade in grade_ranges.items():
    #     if low <= score <= high:
    #         return grade
    # 法二
    breakpoints = [60, 70, 80, 90]
    grades = ["不及格", "及格", "中等", "良好", "优秀"]
    return grades[bisect.bisect_right(breakpoints, score)]
