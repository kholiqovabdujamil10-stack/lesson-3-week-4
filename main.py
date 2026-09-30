# 1
# with open("hello.txt", "w") as file:
#     file.write("Salom, jahon!")

# 2
# with open("hello.txt", "r") as file:
#     f = file.read()
# print(f)

# 3
# with open("hello.txt") as file:
#     for i in file:
#         print(i, end="")

# 4
# with open("hello.txt", "r") as file:
#     f = file.readlines()
#     print(len(f))

# 5
# with open("hello.txt", "a") as file:
#     f = file.write("\norange")

# 6
# names = ["Ali", "Vali", "Guli"]
# with open("hello.txt","w") as file:
#     for i in names:
#         file.writelines(i + "\n")

# 7
# with open("hello.txt","r") as file:
#     f = file.read()
# a = f.split()
# print(len(a))

# 8
# with open("hello.txt") as file:
#     f = file.read()
# a = f.replace(" ", "")
# print(len(a))

# 9
# with open("hello.txt", "r") as file:
#     total = 0
#     for line in file:
#         total += int(line)
# print(total)

# 10
# with open("hello.txt", "r") as file:
#     numbers = []
#     for i in file:
#         numbers.append(i.strip())
# print(max(numbers))

# 11
# with open("hello.txt", "r") as file1:
#     content = file1.read()

# with open("copy.txt", "w") as file2:
#     file2.write(content)

# 12
# with open("hello.txt", "r") as file:
#     n = 1
#     for i in file:
#         print(n,":", i.strip())
#         n += 1

# 13
# with open("hello.txt", "r") as file:
#     text = file.read()
# words = text.split()
# count = words.count("python")
# print(count)

# 14
# with open("hello.txt", "r") as file:
#     lines = file.readlines()
# longest = max(lines, key=len)
# print(longest.strip())

# 15
# with open("hello.txt", "r") as file:
#     text = file.read()
# text = text.upper()
# with open("copy.txt", "w") as file:
#     file.write(text)

# 16
# with open("hello.txt", "r") as file:
#     lines = file.readlines()
# with open("copy.txt", "w") as file:
#     for line in lines:
#         if line.strip() != "":
#             file.write(line)

# 17
# with open("hello.txt", "r") as file1:
#     lines1 = file1.readlines()
# with open("copy.txt", "r") as file2:
#     lines2 = file2.readlines()
# with open("merged.txt", "w") as merged:
#     for line in lines1:
#         merged.write(line)
#     for line in lines2:
#         merged.write(line)

# 18
# with open("hello.txt", "r") as file:
#     names = []
#     scores = []
#     for i in file:
#         name, score = i.split()
#         names.append(name)
#         scores.append(int(score))
# average = sum(scores) / len(scores)
# top = names[scores.index(max(scores))]
# print(f"Average: {average}")
# print(f"Top: {top}")
