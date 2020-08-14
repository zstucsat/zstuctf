#include <stdio.h>
int main()
{
	
	int flag[31]={122,114,118,118,103,113,96,124,92,97,
	59,120,83,60,125,80,113,78,39,34,121,101,122,114,
	71,126,91,118,121,96,30};
	char buffer[31];
	printf("«Î ‰»Îflag\n");
	scanf("%s",buffer);
	int i=0;
	for(i=0;i<31;i++)
	{


		if(flag[i]!=(buffer[i]^i)){


			printf("wrong flag!\n");
			return -1;
		}
	}
	printf("congratulations!");
	return 0;
 }
