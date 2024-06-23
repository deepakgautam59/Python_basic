#File Writing
deepak="""What is Python?
Python is a high-level, general-purpose, and very popular programming language. Python programming language (latest Python 3) is being used in web development, Machine Learning applications, along with all cutting-edge technology in Software Industry."""
with open("file.txt",'w+') as my_file:
    my_file.writelines(deepak)
    