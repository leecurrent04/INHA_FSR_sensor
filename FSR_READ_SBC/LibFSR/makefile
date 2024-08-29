compile :
	gcc -c -o ./out/main.o main.c -lwiringPi
adc :
	gcc -c -o ./out/object/mcp3208.o ./src/mcp3208.c -lwiringPi
fsr :
	gcc -c -o ./out/object/fsr.o ./src/fsr.c -lwiringPi
link :
	gcc -g ./out/object/*.o ./out/main.o -lwiringPi -o ./out/main.out
run :
	./out/main.out
lib:
	gcc -shared out/object/*.o -lwiringPi -o libfsr.so
test:
	gcc test.c -L. -l fsr -o ./out/test.out
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.
	./out/test.out

