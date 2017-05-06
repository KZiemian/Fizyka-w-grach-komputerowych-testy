CC=g++
CFLAGS=-std=gnu++11
PROGNAME1=fizyka-cpp-s01
PROGNUM1=-05
PROGEXT1=.cpp
PROGNAME2=Rysuj-Python
PROGNUM2=-02
PROGEXT2=.py
PROG=prog



all:
	$(CC) $(CFLAGS) $(PROGNAME1)$(PROGNUM1)$(PROGEXT1) -o $(PROG)
	./$(PROG)

run:
	./$(PROG)

rysuj:
	./$(PROGNAME2)$(PROGNUM2)$(PROGEXT2)

wszystko:
	$(CC) $(CFLAGS) $(PROGNAME1)$(PROGNUM1)$(PROGEXT1) -o $(PROG)
	./$(PROG)
	./$(PROGNAME2)$(PROGNUM2)$(PROGEXT2)

preprocesor:
	$(CC) $(CFLAGS) -E $(PROGNAME1)$(PROGNUM1)$(PROGEXT1) \
	-o $(PROG)$(PROGEXT1)

changemode:
	chmod u+x $(PROGNAME2)$(PROGNUM2)$(PROGEXT2)


clean:
	rm $(PROG)
