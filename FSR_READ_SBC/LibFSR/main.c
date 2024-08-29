#include <stdio.h>
//#include <stdlib.h>
//#include <errno.h>
//#include <string.h>

#include "./header/main.h"
#include "./header/mcp3208.h"

int main()
{
	int adcChannel = 0;
	init();
	//off();
	on();

	while(1)
	{
		for(int y=0; y<SENSOR_SIZE_Y; y++)
		{
			muxOutSet(y);
			for(int x=0; x<SENSOR_SIZE_X; x++)
			{
				muxInSet(x);
				printf("%04d ", read_mcp3208_adc(adcChannel));
			}
			printf("\n");
		}
		printf("\n");
		delay(1000);
	}

	return 0;
}

