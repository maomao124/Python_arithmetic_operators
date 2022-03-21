"""
 * Project name(项目名称)：Python算术运算符
 * Package(包名): 
 * File(文件名): test4
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 19:54
 * Version(版本): 1.0
 * Description(描述)： 比较运算符
 """

# 比较运算符	说明
# >	大于，如果>前面的值大于后面的值，则返回 True，否则返回 False。
# <	小于，如果<前面的值小于后面的值，则返回 True，否则返回 False。
# ==	等于，如果==两边的值相等，则返回 True，否则返回 False。
# >=	大于等于（等价于数学中的 ≥），如果>=前面的值大于或者等于后面的值，则返回 True，否则返回 False。
# <=	小于等于（等价于数学中的 ≤），如果<=前面的值小于或者等于后面的值，则返回 True，否则返回 False。
# !=	不等于（等价于数学中的 ≠），如果!=两边的值不相等，则返回 True，否则返回 False。
# is	判断两个变量所引用的对象是否相同，如果相同则返回 True，否则返回 False。
# is not	判断两个变量所引用的对象是否不相同，如果不相同则返回 True，否则返回 False。


if __name__ == '__main__':
    print("89是否大于100：", 89 > 100)
    print("24*5是否大于等于76：", 24 * 5 >= 76)
    print("86.5是否等于86.5：", 86.5 == 86.5)
    print("34是否等于34.0：", 34 == 34.0)
    print("False是否小于True：", False < True)
    print("True是否等于True：", True < True)

    import time  # 引入time模块

    t1 = time.gmtime()
    t2 = time.gmtime()
    print(t1 == t2)  # 输出True
    print(t1 is t2)  # 输出False

    input()
