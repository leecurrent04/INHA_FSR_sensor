#ifndef MCP3208_H
#define MCP3208_H

#include <wiringPi.h>
#include <wiringPiSPI.h>

#define CS_MCP3208 8

#define SPI_CHANNEL 0
#define SPI_SPEED 1000000

int read_mcp3208_adc(unsigned char adcChannel);

#endif
