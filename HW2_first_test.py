# Задание 1.
# # Условие:
# Дополнить проект тестами,
# проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).

from sem import checkout

folder_in = "/home/user/tst"
folder_out = "/home/user/out"
folder_ext = "/home/user/folder1"


def test_step8():
    assert checkout(f"cd {folder_out}; 7z l arx2.7z", "2 files")


def test_step9():
    assert checkout(f"cd {folder_out}; 7z x arx2.7z {folder_ext}", "Everything is Ok")