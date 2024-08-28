#include <stdio.h>
//#include <stdlib.h>
#include <errno.h>
#include <string.h>

#include "./header/main.h"
#include "./header/mcp3208.h"

int main(void)
{
        int adcChannel = 0;
        int adcValue = 0;

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

        pinMode(CS_MCP3208, OUTPUT);

	pinMode(MUX_EN, OUTPUT);
	for(int n=0; n<3; n++)
	{
		pinMode(MUX_IN_SEL[n], OUTPUT);
		pinMode(MUX_OUT_SEL[n], OUTPUT);
	}

	digitalWrite(MUX_EN, 0);
	digitalWrite(MUX_IN_SEL[0], LOW);
	digitalWrite(MUX_IN_SEL[1], LOW);
	digitalWrite(MUX_IN_SEL[2], LOW);
	digitalWrite(MUX_OUT_SEL[0], LOW);
	digitalWrite(MUX_OUT_SEL[1], LOW);
	digitalWrite(MUX_OUT_SEL[2], LOW);


        while(1){
                adcValue = read_mcp3208_adc(adcChannel);
                printf("adc0 Value = %u\n", adcValue);
        }
        return 0;
}
