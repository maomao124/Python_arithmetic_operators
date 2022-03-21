"""
 * Project name(项目名称)：Python算术运算符
 * Package(包名): 
 * File(文件名): test5
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 19:57
 * Version(版本): 1.0
 * Description(描述)： 逻辑运算符
 """

# 逻辑运算符	含义	基本格式	说明
# and	逻辑与运算，等价于数学中的“且”	a and b	当 a 和 b 两个表达式都为真时，a and b 的结果才为真，否则为假。
# or	逻辑或运算，等价于数学中的“或”	a or b	当 a 和 b 两个表达式都为假时，a or b 的结果才是假，否则为真。
# not	逻辑非运算，等价于数学中的“非”	not a	如果 a 为真，那么 not a 的结果为假；如果 a 为假，那么 not a 的结果为真。相当于对 a 取反。

if __name__ == '__main__':
    age = int(input("请输入年龄："))
    height = int(input("请输入身高："))
    if age >= 18 and age <= 30 and height >= 170 and height <= 185:
        print("恭喜，你符合报考飞行员的条件")
    else:
        print("抱歉，你不符合报考飞行员的条件")

    num = 2
    print("----False and xxx-----")
    print(False and print(num))
    print("----True and xxx-----")
    print(True and print(num))
    print("----False or xxx-----")
    print(False or print(num))
    print("----True or xxx-----")
    print(True or print(num))

    input()
