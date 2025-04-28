"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""


def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作

    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数

    返回:
    - 操作后的学生列表
    """
    # ops = {
    #     "add": lambda s, a: s.append(a[0]),
    #     "remove": lambda s, a: s.remove(a[0]),
    #     "update": lambda s, a: s.__setitem__(s.index(a[0]), a[1]),
    # }

    # ops[operation](students, args)
    # return students
    if operation == "add":
        students.append(args[0])
    elif operation == "remove":
        students.remove(args[0])
    elif operation == "update":
        index = students.index(args[0])
        students[index] = args[1]
    return students
