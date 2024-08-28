compile :
	gcc -c -o ./out/main.o main.c -lwiringPi

adc :
	gcc -c -o ./out/object/mcp3208.o ./src/mcp3208.c -lwiringPi


link :
	gcc -g ./out/object/* ./out/main.o -lwiringPi -o ./out/main.out

run :
	./out/main.out
