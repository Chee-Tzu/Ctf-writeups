We are given with an image and then another .txt file which contains a set of rgb values each of them refferenced with things like "Key1: RGB(...)...." etc

I wasted a lot of time on this but then I Understood that since it ranges from 0 - 127 it must be ascii values,I also extracted the values of the image into a .txt file and i wrote a script that would check if each rgb value of the image is equal to any of the key and store the corresponding index into a list and then print out the rest of the stuff, and viola it resulted in giving me a C program

just by simply reading the code we can see that there is no need to reverse it as just running itself, we do that thus we get the flag
