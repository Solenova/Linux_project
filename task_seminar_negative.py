from sem import checkout_negative

folderin = "/home/user/tst"
folderout = "/home/user/out"
folderext = "/home/user/folder1"
folderbad = "/home/user/folder2"


def test_step1():
    # test1
    assert checkout_negative(f"cd {folderbad}; 7z e arx2.7z -o{folderext} -y", "ERRORS"), "test1 FAIL"


def test_step2():
    # test2
    assert checkout_negative(f"cd {folderbad}; 7z t arx2.7z", "ERRORS"), "test2 FAIL"