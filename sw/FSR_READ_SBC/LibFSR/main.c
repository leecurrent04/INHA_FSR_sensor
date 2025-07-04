#include <stdio.h>
//#include <stdlib.h>
//#include <errno.h>
//#include <string.h>

#include "./header/main.h"
#include "./header/mcp3208.h"

int main()
{
	uint8_t adcChannel = 0;
	init();
	//off();
	on();
	uint16_t value[SENSOR_SIZE_X][SENSOR_SIZE_Y];

	while(1)
	{
		getData(adcChannel, value);
		for(uint8_t y=0; y<SENSOR_SIZE_Y; y++)
		{
			for(uint8_t x=0; x<SENSOR_SIZE_X; x++)
			{
				// printf("%04d ", read_mcp3208_adc(adcChannel));
				printf("%04d ", value[x][y]);
			}
			printf("\n");
		}
		printf("\n");
		delay(1000);
	}

	return 0;
}

