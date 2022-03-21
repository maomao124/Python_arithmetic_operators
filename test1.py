"""
 * Project name(项目名称)：Python算术运算符 
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 19:33
 * Version(版本): 1.0
 * Description(描述)： Python算术运算符
 """

# 运算符	说明	实例	结果
# +	加	12.45 + 15	27.45
# -	减	4.56 - 0.26	4.3
# *	乘	5 * 3.6	18.0
# /	除法（和数学中的规则一样）	7 / 2	3.5
# //	整除（只保留商的整数部分）	7 // 2	3
# %	取余，即返回除法的余数	7 % 2	1
# **	幂运算/次方运算，即返回 x 的 y 次方	2 ** 4	16，即 2的4次方

if __name__ == '__main__':
    m = 10
    n = 97
    sum1 = m + n
    x = 7.2
    y = 15.3
    sum2 = x + y
    print("sum1=%d, sum2=%.2f" % (sum1, sum2))

    n = 45
    m = -n
    x = -83.5
    y = -x
    print(m, ",", y)

    n = 45
    n_neg = -n
    f = -83.5
    f_neg = -f
    print(n_neg, ",", f_neg)

    n = 45
    m = +n
    x = -83.5
    y = +x
    print(m, ",", y)

    n = 4 * 25
    f = 34.5 * 2
    print(n, ",", f)

    str1 = "hello "
    print(str1 * 8)
    # /表示普通除法，使用它计算出来的结果和数学中的计算结果相同。
    # //表示整除，只保留结果的整数部分，舍弃小数部分；注意是直接丢掉小数部分，而不是四舍五入。
    # 整数不能除尽
    print("23/5 =", 23 / 5)
    print("23//5 =", 23 // 5)
    print("23.0//5 =", 23.0 // 5)
    print("-------------------")
    # 整数能除尽
    print("25/5 =", 25 / 5)
    print("25//5 =", 25 // 5)
    print("25.0//5 =", 25.0 // 5)
    print("-------------------")
    # 小数除法
    print("12.4/3.5 =", 12.4 / 3.5)
    print("12.4//3.5 =", 12.4 // 3.5)

    print("-----整数求余-----")
    print("15%6 =", 15 % 6)
    print("-15%6 =", -15 % 6)
    print("15%-6 =", 15 % -6)
    print("-15%-6 =", -15 % -6)
    print("-----小数求余-----")
    print("7.7%2.2 =", 7.7 % 2.2)
    print("-7.7%2.2 =", -7.7 % 2.2)
    print("7.7%-2.2 =", 7.7 % -2.2)
    print("-7.7%-2.2 =", -7.7 % -2.2)
    print("---整数和小数运算---")
    print("23.5%6 =", 23.5 % 6)
    print("23%6.5 =", 23 % 6.5)
    print("23.5%-6 =", 23.5 % -6)
    print("-23%6.5 =", -23 % 6.5)
    print("-23%-6.5 =", -23 % -6.5)

    print('----次方运算----')
    print('3**4 =', 3**4)
    print('2**5 =', 2**5)
    print('----开方运算----')
    print('81**(1/4) =', 81**(1/4))
    print('32**(1/5) =', 32**(1/5))

    input()
