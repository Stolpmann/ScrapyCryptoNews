r = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test.txt", "r")
#print(r.read())

lines = r.readlines()
second_last_lines = lines[-4:-2]

last_lines = lines[-2:]

print(last_lines)
print(second_last_lines)


def check():
    if last_lines != second_last_lines:
        print("Lines are not equal")

        def pub():
            string=''.join(str(item) for item in last_lines)
            w = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test2.txt", "w")
            w.write(string)
        pub()

    else:
        print("Lines are equal")

check()

