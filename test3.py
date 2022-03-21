"""
 * Project name(项目名称)：Python算术运算符
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 19:51
 * Version(版本): 1.0
 * Description(描述)： 位运算符
 """

# 位运算符	说明	使用形式	举 例
# &	按位与	a & b	4 & 5
# |	按位或	a | b	4 | 5
# ^	按位异或	a ^ b	4 ^ 5
# ~	按位取反	~a	~4
# <<	按位左移	a << b	4 << 2，表示整数 4 按位左移 2 位
# >>	按位右移	a >> b	4 >> 2，表示整数 4 按位右移 2 位


if __name__ == '__main__':
    n = 0X8FA6002D
    print("%X" % (9 & 5))
    print("%X" % (-9 & 5))
    print("%X" % (n & 0XFFFF))

    n = 0X2D
    print("%X" % (9 | 5))
    print("%X" % (-9 | 5))
    print("%X" % (n | 0XFFFF0000))

    n = 0X0A07002D
    print("%X" % (9 ^ 5))
    print("%X" % (-9 ^ 5))
    print("%X" % (n ^ 0XFFFF0000))

    print("%X" % (~9))
    print("%X" % (~-9))

    print("%X" % (9 << 3))
    print("%X" % ((-9) << 3))

    print("%X" % (9 >> 3))
    print("%X" % ((-9) >> 3))

    input()
