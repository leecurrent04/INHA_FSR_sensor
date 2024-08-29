#include<stdio.h>
#include<stdlib.h>
#include<wiringPi.h> //wiringPi.h헤더파일을 추가시킵니다.
#include<wiringPiSPI.h>
#include<mcp3004.h>


#define SENSOR_SIZE 8

// PIN
const int row[3]={27, 28 ,29};
const int colum[3]={23, 24, 25};

// matrix of storing FSR data
typedef struct{
	unsigned int matrix[SENSOR_SIZE][SENSOR_SIZE];
} data;

data FSR_data0;
data FSR_data1;
data FSR_data2;
data FSR_data3;

// Mux controll
void muxReset();				// Mux set 0
void muxOutSet(int num);
void muxInSet(int num);

// IDK :(
int SensorValue[20];
#define BASE 100
#define SPI_CHAN 0

// Filter functions
// Modify function name as setMAF (Moving Average Filter)
void setFILTERNAME(data* input_data);

// return sensor data to python
data getData(int sensor_num);


int main(){
	if(wiringPiSetup()==-1) return -1; 
	mcp3004Setup(BASE,SPI_CHAN);


	for(int n=0; n<3; n++) pinMode(row[n], INPUT);
	for(int n=0; n<3; n++) pinMode(colum[n], OUTPUT);

	char matrix[10][10]={0,};

	while(1)
	{
		printf("-----------------------------------------\n");
		for(int out=0; out<8; out++)
		{
			muxReset();
			//MUX OUT SET
			muxOutSet(out);

			for(int in=0; in<8; in++)
			{
				// MUX IN SEt
				muxInSet(in);
				//저주파 통과 필터
				int PredictValue;//추정값
				int FilteredValue;
				if(in==1&&out==1)PredictValue=analogRead(BASE);
				else PredictValue=FilteredValue;

				double alpha=0.6;
				FilteredValue=(1-alpha)*PredictValue+alpha*analogRead(BASE);


				/*for(int t=0;t<19;t++){ //노이즈 필터링-이동평균 필터
				  SensorValue[t]=SensorValue[t+1];
				  }
				  SensorValue[19]=analogRead(BASE);
				  int FilteredValue;//필터링된 값 저장
				  for(int t=0;t<20;t++){
				  FilteredValue+=SensorValue[t];
				  }
				  FilteredValue /=20; //평균필터값*/

				//printf(" %04d",FilteredValue);

				if(FilteredValue>150) 
					//matrix[in][out]=1;
				{matrix[in][out] = FilteredValue;printf(" %04d",matrix[in][out]);}
				else 
					//matrix[in][out]=0;
				{matrix[in][out] = 0; printf(" %04d",matrix[in][out]);}

				/*if(matrix[in-1][out-1]+matrix[in-1][out]+matrix[in-1][out+1]+
				  matrix[in][out-1]+					   matrix[in][out+1]+
				  matrix[in+1][out-1]+matrix[in+1][out]+matrix[in+1][out+1]>=5)	printf(" 1 ");
				  else printf(" 0 ");*/
			}
			printf("\n");

		}
		delay(1000);


	}
}

void muxReset()
{
	for(int n=0; n<8; n++)
	{
		digitalWrite(colum[n],0);
	}
	return;
}

void getData()
{
	return matrix[10][10];
}

void muxOutSet(int num)
{
	pinMode(colum[0], (num&0x111)>>0);
	pinMode(colum[1], (num&0x111)>>1);
	pinMode(colum[2], (num&0x111)>>2);
}

void muxInSet(int num)
{
	pinMode(row[0], (num&0x111)>>0);
	pinMode(row[1], (num&0x111)>>1);
	pinMode(row[2], (num&0x111)>>2);
}
