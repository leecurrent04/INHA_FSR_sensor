#include <stdio.h>
//#include <stdlib.h>
#include <errno.h>
//#include <string.h>

#include "../header/fsr.h"
#include "../header/mcp3208.h"

int init()
{
	if(wiringPiSetupGpio() == -1)
	{
		fprintf(stdout, "Unable to start wiringPi: %s\n", strerror(errno));
		return 1;
	}

	if(wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1)
	{
		fprintf(stdout, "wiringPiSPISetup Failed: %s\n", strerror(errno));
		return 1;

	}

	// pinMode Setting
	pinMode(CS_MCP3208, OUTPUT);
	pinMode(MUX_EN, OUTPUT);
	for(int n=0; n<3; n++)
	{
		pinMode(MUX_IN_SEL[n], OUTPUT);
		pinMode(MUX_OUT_SEL[n], OUTPUT);
	}

	return 0;
}

int on()
{
	digitalWrite(MUX_EN, 0);
	return 0;
}

int off()
{
	digitalWrite(MUX_EN, 1);
	return 0;
}

void muxReset()
{
	for(int n=0; n<8; n++)
	{
		digitalWrite(MUX_OUT_SEL[n],0);
	}
	return;
}

void muxOutSet(int num)
{
	digitalWrite(MUX_OUT_SEL[0], (num>>0)&0x1);
	digitalWrite(MUX_OUT_SEL[1], (num>>1)&0x1);
	digitalWrite(MUX_OUT_SEL[2], (num>>2)&0x1);
	printf("%d:%d] ", num, (num>>2)&0x1);
	delay(MUX_DELAY);
}

void muxInSet(int num)
{
	digitalWrite(MUX_IN_SEL[0], (num>>0)&0x1);
	digitalWrite(MUX_IN_SEL[1], (num>>1)&0x1);
	digitalWrite(MUX_IN_SEL[2], (num>>2)&0x1);
	delay(MUX_DELAY);
}
