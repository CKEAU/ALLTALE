#现在我们解读一下这些代码,他们都是由Python构建的,可以理解为一个Python拓展或者也可以当作一个编程语言的雏形。
import os#os库大家肯定不陌生不多做讲解
from Neutron import *
def read_file(file_path):#这个函数用来读取文件
    with open(file_path, 'r') as file:#打开文件
        contents = file.read()#读取文件(使用read()函数)contents
    return contents#返回值

def execute_files():#为了更加直观的让你们理解所以此处用翻译,OK啊知道现在这个函数的用途就是执行我们的.lt文件里面的代码,并且让main.py主要(我的意思是包含)函数的文件
    num = int(input("PRESS QUANTITY:"))#打开的.lt文件数量
    for i in range(num):#循环的次数为上面的输入(整数类型)
        path = input("PRESS FILE PATH:")#文件路径
        if not os.path.exists(path):#不多做讲解很简单
            print(f"File '{path}' does not exist.")
            continue

        if not path.endswith(".lt"):#检测到不是.lt文件,那就没必要运行了毕竟不是别的语言就是(不支持我们)好吧
            print(f"File '{path}' is not a .lt file")#告诉你这个文件的后缀名并不是.lt
            continue#继续

        contents = read_file(path)
        exec(contents)#这个喜人的充电器不太好用大家见谅[抱拳]
if __name__ == "__main__":
    execute_files()#这行代码很简单,不多做讲解
#谢谢大家的观看,还有别的函数,我们现在讲解一下