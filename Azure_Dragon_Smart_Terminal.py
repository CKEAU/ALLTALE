from Neutron import *
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QInputDialog
from PySide6.QtCore import Qt
import os
import pickle
import atexit  # 添加这行导入语句



class AzureDragon:
    def __init__(self):
        self.users = {}
        self.load_users()

    def processCommand(self, command):
        if command.startswith('say'):
            _, rest = command.split(' ', 1)
            return f'>> {rest}'
        elif command.startswith('get'):
            _, type_ = command.split(' ', 1)
            try:
                if type_ == 'int':
                    return str(int(input(f'>>Please enter an integer: ')))
                elif type_ == 'str':
                    return input(f'>>Please enter a string: ')
                else:
                    return '>>[ERROR] Invalid type for get command'
            except ValueError:
                return '>>[ERROR] Invalid input'
        elif command.startswith('UserName:'):
            _, username = command.split(' ', 1)
            if username in self.users:
                if self.users[username] == keyin('>>Please enter your password: '):
                    return f'>>[Done] Welcome back, {username}!'
                else:
                    return '>>[ERROR] Wrong password'
            else:
                self.users[username] = keyin('>>Please enter your password: ')
                self.save_users()
                return f'>>User {username} registered successfully.'
        elif command.startswith('Password:'):
            _, username = command.split(' ', 1)
            if username in self.users:
                return f'>>Your password for {username} is: {self.users[username]}'
            else:
                similar_usernames = [user for user in self.users if user.startswith(username)]
                if similar_usernames:
                    similar_name = similar_usernames[0]
                    return f'>>Are you mean "{similar_name}"?'
                else:
                    return '>>User not found. Would you like to register?'
        elif command.startswith("exit"):
            exit()
        elif command.startswith('help'):
            return '''>>>>>>>Azure Dragon Command Line Interpreter
            say <text> - Say something
            get <type> - Get a value
            UserName: <username> - Get the password of a user
            Password: <username> - Get the password of a user
            exit - Exit the program
            help - Show this help message
            '''


        else:
            try:
                exec(command)
            except NameError:
                return '>>[ERROR] Unknown command'

    def save_users(self, filename='user_data.pkl'):
        with open(filename, 'wb') as file:
            pickle.dump(self.users, file)

    def load_users(self, filename='user_data.pkl'):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                self.users = pickle.load(file)



class CommandLineInterpreter(QMainWindow):
    def __init__(self, azure_dragon):
        super().__init__()

        self.azure_dragon = azure_dragon
        self.initUI()
        self.setStyleSheet("background-color: #D3D3D3;")
        self.command_input.setReadOnly(False)
        self.command_input.setFocus()

    def initUI(self):
        self.setWindowTitle('Azure Dragon Command Line Interpreter')
        self.setGeometry(100, 100, 400, 300)

        # 创建命令输入区域和输出显示区域
        self.command_input = QTextEdit(self)
        self.command_input.setReadOnly(True)
        self.output_display = QTextEdit(self)
        self.output_display.setReadOnly(True)

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.command_input)
        layout.addWidget(self.output_display)

        # 创建中央部件并设置布局
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 创建发送按钮
        send_button = QPushButton('Send', self)
        send_button.setStyleSheet("""
                    QPushButton {
                        background-color: #000000; /* 黑色背景 */
                        color: white;
                        border-radius: 5px;
                    }
                    QPushButton:hover {
                        background-color: #45a049;
                    }
                    """)
        send_button.clicked.connect(self.sendCommand)

        # 将按钮添加到窗口底部
        self.statusBar().addWidget(send_button)
        self.command_input.setStyleSheet('background-color: #000000; color: white')
        self.output_display.setStyleSheet('background-color: #000000; color: white')

    def sendCommand(self):
        # 获取用户输入的命令
        command = self.command_input.toPlainText()
        # 处理命令并显示结果
        result = self.azure_dragon.processCommand(command)
        self.output_display.append(result)
        # 清空输入框以便输入下一条命令
        self.command_input.clear()


def main():
    app = QApplication(sys.argv)

    azure_dragon = AzureDragon()
    cli_interpreter = CommandLineInterpreter(azure_dragon)
    cli_interpreter.show()

    # 在程序结束前保存用户数据
    atexit.register(azure_dragon.save_users)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()