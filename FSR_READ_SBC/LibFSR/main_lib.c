#include <stdio.h>
//#include <stdlib.h>
//#include <errno.h>
//#include <string.h>

#include "./header/main.h"
#include "./header/mcp3208.h"

int getData(int adcChannel, unsigned int value[SENSOR_SIZE_X][SENSOR_SIZE_Y])
{
	for(int y=0; y<SENSOR_SIZE_Y; y++)
	{
		muxOutSet(y);
		for(int x=0; x<SENSOR_SIZE_X; x++)
		{
			muxInSet(x);
			value[x][y] = read_mcp3208_adc(adcChannel);
		}
	}

	return 0;
}
