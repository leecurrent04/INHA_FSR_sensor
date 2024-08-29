#ifndef MAIN_H
#define MAIN_H

#include <wiringPi.h>
#include <wiringPiSPI.h>

#define SENSOR_SIZE_X 8
#define SENSOR_SIZE_Y 8

int init();
int on();
int off();

void muxReset();
void muxOutSet(int num);
void muxInSet(int num);

#endif
