#ifndef MAIN_H
#define MAIN_H

#include <wiringPi.h>
#include <wiringPiSPI.h>

#define SENSOR_SIZE_X 8
#define SENSOR_SIZE_Y 8

const int MUX_OUT_SEL[3] = {25, 26, 27};
const int MUX_IN_SEL[3] = {22, 23, 24};
const int MUX_EN = 16;
const int MUX_DELAY = 10;

int init();
int on();
int off();

void muxReset();
void muxOutSet(int num);
void muxInSet(int num);

#endif
