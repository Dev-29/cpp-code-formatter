import os

cppExtensions = (".cxx",".cpp",".c", ".hxx", ".hh", ".cc", ".hpp")

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(cppExtensions):
            os.system("clang-format-12 -i -style=file " + root + "/" + file)
