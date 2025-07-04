#ifndef FSR_H
#define FSR_H

#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <stdint.h>

const uint8_t MUX_OUT_SEL[3] = {25, 26, 27};
const uint8_t MUX_IN_SEL[3] = {22, 23, 24};
const uint8_t MUX_EN = 16;
const uint16_t MUX_DELAY = 10;

int init();
int on();
int off();

void muxReset();
void muxOutSet(uint8_t num);
void muxInSet(uint8_t num);
uint8_t getData(uint8_t adc_channel, uint16_t value[SENSOR_SIZE_X][SENSOR_SIZE_Y]);
#endif
