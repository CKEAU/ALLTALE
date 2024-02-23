def keyin(miaoshu):#等于python的input()函数
    opt(miaoshu)
    return input()#前后呼应

def opt(output):#打印这个输入的值,和system.out()或者什么printf()的作用一样
    print(output)

def plus(*nums):#加(数字)
    return sum(nums)

def join(lst, sep):#很简单自己看看就OK谢谢理解
    return sep.join(map(str, lst))
def gui():#这里使用了tkinter的界面把之前很多行的代码简化成了一行,还没有开发完所以不太...好用
    import tkinter as gui
    gui.Tk()


def absl(sth):
    if int(sth) < 0:
        sth = sth * -1
    return sth



def xf(sth, sth2):
    sth2 = int(sth2)
    sth = float(sth)
    flag = sth
    if sth2 > 0:
        for i in range(sth2-1):
            flag*=sth
    elif sth2==0:
        if sth != 0:
            flag = 1
        else:
            flag = 0
    else:
        absl(sth2)
        flag = 10
        for i in range(sth2-1):
            flag *= sth2
        flag = 1/flag*sth
    return flag

def useload(library, *args):#useload函数 的作用非常明显:use的意思是使用,load是载入的意思,比如加载下载英语就是upload和download
    import pkg_resources
    import pip
    import pkgutil
    import importlib.util
    import pip
    import pkgutil
    import importlib.util#这些库有些是用来导入库 的有些是检测到没有这个库所以下载库的,可能需要算了不可能
    from pip._internal.utils.misc import get_installed_distributions#这些是因为Fleet开发环境我没给安装上这些库所以...运行起来没问题(我指的是装上后)
    packages = [dist.project_name for dist in pkg_resources.working_set]
    if library in packages:
        exec(f"import {library}")#特别易读,就是import 库和import是一个作用(我没有敷衍)
        return eval(library)
    else:
        installed_packages = pip._internal.utils.misc.get_installed_distributions()#下载
        for pkg in installed_packages:
            try:
                # 尝试导入包
                mod = importlib.import_module(pkg.key)#看上面的注释
                # 如果导入成功，则将该包添加到useload函数中
                useload_mod = f"useload_{pkg.key}"#不多说了
                setattr(sys.modules[__name__], useload_mod, mod)
                opt(f"Successfully imported library: {pkg.key}")#opt这个函数上面定义过了
            except:#这玩意真好用
                opt(f"Failed to import library: {pkg.key}")
class LtInterpreter:
    def __init__(self):
        self.constants = {}
        self.variables = {}
        self.current_second = 0

    def interpret(self, lt_code):
        lines = lt_code.split("\n")

        for line in lines:
            line = line.strip()

            # 解析常量定义
            if line.startswith("often"):
                key, value = self.parse_constant(line)
                self.constants[key] = value

            # 解析变量定义
            elif line.startswith("var"):
                self.parse_variable(line)

            # 解析循环结构
            elif line.startswith("loop"):
                times, iterable, condition = self.parse_loop(line)
                self.execute_loop(times, iterable, condition)

            # 解析判断结构以及其他结构...

        return self.current_second

    def parse_constant(self, line):
        parts = line.split("=")
        key = parts[0].replace("often ", "").strip()
        value = parts[1].strip().replace('"', '')
        return key, value

    def parse_variable(self, line):
        variable_name = line.replace("var ", "").strip()
        self.variables[variable_name] = None

    def parse_loop(self, line):
        parts = line.replace("loop(", "").replace(");", "").split(",")
        times = int(parts[0].strip()) if parts[0] != "inf" else float("inf")
        iterable = parts[1].strip()
        condition = parts[2].strip()
        return times, iterable, condition

    def execute_loop(self, times, iterable, condition):
        if times == float("inf"):
            while True:
                if self.evaluate_condition(condition):
                    # 执行循环体内的代码
                    pass
                else:
                    break
        else:
            for _ in range(times):
                if self.evaluate_condition(condition):
                    # 执行循环体内的代码
                    pass

    def evaluate_condition(self, condition):
        # 这里需要根据 Lt 语言的条件表达式规则来编写条件求值逻辑
        # 示例：如果 Lt 语言的条件是类似 Python 的布尔表达式，可以尝试解析并计算它
        try:
            # 假设条件是一个简单的比较表达式（例如："current_second < stop_second"）
            python_condition = condition.replace('current_second', str(self.variables['current_second']))
            evaluated_result = eval(python_condition)
            if isinstance(evaluated_result, bool):  # 确保结果是布尔类型
                return evaluated_result
            else:
                raise ValueError("Invalid condition expression.")
        except Exception as e:
            print(f"Error evaluating condition: {condition}. Reason: {str(e)}")
            return False

# 示例用法：
interpreter = LtInterpreter()
lt_code = '''
often inf = "inf";
var current_second;
loop(inf, in_list, current_second < stop_second);
end@;
'''
interpreter.interpret(lt_code)