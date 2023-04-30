Basically from the name and by looking and seeing how it was stripped we can see that this is basically a Python Executable, Extract the elf and then get the .pyc
the .pyc after decompiled using Decompile++ will let us get the .py file that we can reverse

Coming to the .py file we can see that it is just comparing the variable c after all of its function to the values in source , basically it is just a linear equation of the form c\*(input) = source[i], using a brute force method would've been easier but since i wanted to practice with z3 i just used that.
