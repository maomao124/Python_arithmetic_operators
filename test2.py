"""
 * Project name(项目名称)：Python算术运算符
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 19:47
 * Version(版本): 1.0
 * Description(描述)： 赋值运算符
 """

# 运算符	说 明	用法举例	等价形式
# =	最基本的赋值运算	x = y	x = y
# +=	加赋值	x += y	x = x + y
# -=	减赋值	x -= y	x = x - y
# *=	乘赋值	x *= y	x = x * y
# /=	除赋值	x /= y	x = x / y
# %=	取余数赋值	x %= y	x = x % y
# **=	幂赋值	x **= y	x = x ** y
# //=	取整数赋值	x //= y	x = x // y
# &=	按位与赋值	x &= y	x = x & y
# |=	按位或赋值	x |= y	x = x | y
# ^=	按位异或赋值	x ^= y	x = x ^ y
# <<=	左移赋值	x <<= y	x = x << y，这里的 y 指的是左移的位数
# >>=	右移赋值	x >>= y	x = x >> y，这里的 y 指的是右移的位数


if __name__ == '__main__':
    sum1 = 25 + 46
    s2 = str(1234)  # 将数字转换成字符串
    s3 = str(100) + "abc"
    print(sum1)
    print(s2)
    print(s3)

    a = b = c = 100
    print(a)
    print(b)
    print(c)

    n1 = 100
    f1 = 25.5
    n1 -= 80  # 等价于 n1=n1-80
    f1 *= n1 - 10  # 等价于 f1=f1*( n1 - 10 )
    print("n1=%d" % n1)
    print("f1=%.2f" % f1)

    input()
