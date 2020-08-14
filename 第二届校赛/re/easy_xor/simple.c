#include <stdio.h>
int main()
{
	
	char ts[100] = "plz input your flag\n";
	int flag[31]={39, 41, 22, 67, 38, 3, 21, 42, 32, 72, 28, 48, 47, 33, 84, 51, 51, 34, 51, 76, 0};
	char buffer[31];
	printf("%s", ts);
	scanf("%s",buffer);
	int i=0;
	for(i=0;i<21;i++)
	{
		if(flag[i]!=(buffer[i]^ts[i])){
			printf("wrong flag!\n");
			return -1;
		}
	}
	printf("congratulations!");
	return 0;
 }
