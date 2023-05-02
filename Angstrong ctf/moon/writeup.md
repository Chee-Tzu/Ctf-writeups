# This is my solution and understanding for what i understood from doing the moon challenge:


using pwntools I extracted the array needed from the elf 

after that to extract the assembly code of each of the function 
I used pwntools:

then i made a loop to pick out the commands that had "add    rax" , "sub     rax" then the last peice of "mov" statement and put it in a list for later use.

Then i used sagemath to put the check in a matrix then took its transpose and then takes needed and creates a vector object, which is the solution of out equation with that we can get our oputput araray after converting this to ascii we get our flag

i couldnt use z3 becuase it was slower compared to this and killed itself after running for some time

actf{3verything_is_just_linear_algebr4_33e431e52e896c92}