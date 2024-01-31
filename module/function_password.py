# 密码数据库的相关方法

import configparser
import pickle

from constant import _CONFIG_FILE, _PASSWORD_FILE, _PASSWORD_EXPORT
from module import function_normal


def create_empty_keywords():
    """创建初始空密码数据库"""
    function_normal.print_function_info()
    with open(_PASSWORD_FILE, 'wb') as f:
        pickle.dump({}, f)


def read_passwords() -> list:
    """读取密码，按使用次数排序后返回"""
    function_normal.print_function_info()
    with open(_PASSWORD_FILE, 'rb') as f:
        password_dict = pickle.load(f)

    # 排序
    sorted_keys = sorted(password_dict, key=password_dict.get, reverse=True)
    sorted_passwords = list(sorted_keys)

    return sorted_passwords


def export_password():
    """导出明文密码"""
    function_normal.print_function_info()
    passwords = read_passwords()

    with open(_PASSWORD_EXPORT, 'w', encoding='utf-8') as pw:
        pw.write("\n".join(passwords))


def update_password(passwords: list):
    """更新密码"""
    function_normal.print_function_info()
    # 密码数据库格式说明：存储一个dict，键为密码str，值为对应的使用次数int
    # 读取
    with open(_PASSWORD_FILE, 'rb') as f:
        password_dict = pickle.load(f)

    # 添加
    for pw in passwords:
        if pw not in password_dict:
            password_dict[pw] = 0

    # 保存
    with open(_PASSWORD_FILE, 'wb') as f:
        pickle.dump(password_dict, f)


def add_pw_count(pw: str):
    """在配置文件中将对应的解压密码使用次数+1"""
    function_normal.print_function_info()
    config = configparser.ConfigParser()
    config.read(_CONFIG_FILE, encoding='utf-8')

    old_count = int(config.get(pw, 'use_count'))
    config.set(pw, 'use_count', str(old_count + 1))
    config.write(open(_CONFIG_FILE, 'w', encoding='utf-8'))