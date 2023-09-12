# Задание 1. Написать функцию на Python, которой
# передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда
# успешно выполнена и текст найден в ее выводе
# и False в противном случае. Передаваться
# должна только одна строка, разбиение вывода
# использовать не нужно.


import subprocess


def script_1(command_in: str, text_in: str):
    result = subprocess.run(command_in, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0:
        res = result.stdout.split("\n")
        if text_in in res:
            return True
        else:
            return False


if __name__ == "__main__":
    res = script_1("cat /etc/os-release", "VERSION_CODENAME=jammy")
    # res = script_1("cat /home/user/text.txt", "test")
    if res:
        print("SECCUESS")
    else:
        print("FAIL")