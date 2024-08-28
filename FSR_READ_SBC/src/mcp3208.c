
#include "../header/mcp3208.h"

int read_mcp3208_adc(unsigned char adcChannel)
{
        unsigned char buff[3];
        int adcValue = 0;

        // buff[0] = 0x06 | ((adcChannel & 0x07) >> 2);
        buff[0] = 0x06 | ((adcChannel & 0x07) >> 7);
        buff[1] = ((adcChannel & 0x07) << 6);
        buff[2] = 0x00;

        digitalWrite(CS_MCP3208, 0);

        wiringPiSPIDataRW(SPI_CHANNEL, buff, 3);

        buff[1] = 0x0F & buff[1];
        adcValue = (buff[1] << 8) | buff[2];

        digitalWrite(CS_MCP3208, 1);
        return adcValue;

}

