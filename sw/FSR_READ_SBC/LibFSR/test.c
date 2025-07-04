#include <stdio.h>

int main()
{
	init();
	on();

	int a[8][8]={1,};

	while(1)
	{
		getData(0,a);
		for(int y=0;y<8;y++)
		{
			for(int x=0;x<8;x++)
			{
				printf("%04d ", a[x][y]);
			}
			printf("\n");
		}
		printf("\n");
	}

}
