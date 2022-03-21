"""
 * Project name(项目名称)：Python算术运算符
 * Package(包名): 
 * File(文件名): test6
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 20:00
 * Version(版本): 1.0
 * Description(描述)： 三目运算符

 exp1 if contion else exp2
condition 是判断条件，exp1 和 exp2 是两个表达式。如果 condition 成立（结果为真），
就执行 exp1，并把 exp1 的结果作为整个表达式的结果；如果 condition 不成立（结果为假），就执行 exp2，并把 exp2 的结果作为整个表达式的结果。
 """

if __name__ == '__main__':
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    print("a大于b") if a > b else (print("a小于b") if a < b else print("a等于b"))

    input()
