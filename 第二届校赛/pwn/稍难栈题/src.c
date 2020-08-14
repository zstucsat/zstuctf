//gcc src.c -o main -z noexecstack -fstack-protector-all -pie -z now -s
#include<stdio.h>
#include<string.h>
#include<stdlib.h>



void get_input(size_t *p,size_t size)
{
	char c;
	int n = 0;
	while(n<=size)
	{
		int ret = read(0,&c,1);
		if(!ret || c == '\n'){
			*((char*)p + n) = 0;
			break;
		}
		*((char*)p + n) = c;
		n++;
		
	}
}


long long my_read()
{
	char str[10];
	size_t ret;
	read(0,str,10);
	ret = atol(str);
	return ret;
}

void my_init()
{
	setvbuf(stdin,0LL,2,0LL);
	setvbuf(stdout,0LL,2,0LL);
	setvbuf(stderr,0LL,2,0LL);
	return alarm(0xF);
}
int check(size_t size)
{
	if(size <0 || size > 0x70)
		return 1;
	return 0;
}
void message()
{
	char buf[0x60];
	size_t size;
	puts("You Can Leave Your Message");
	puts("Can tell me the len of message?");
	size = my_read();
	if(check(size))
		exit(0);
	puts("OK,you can leave the message to me");
	get_input(buf,size);
}
int main()
{
	char p[0x28];
	memset(p,0,0x28);
	my_init();
	puts("Welcome Here");
	puts("tell me your name,please!");
	get_input(p,0x28);
	printf("Hey,%s\n",p);
	puts("So,What do U want to do");
	get_input(p,0x10);
	if(!strcmp(p,"PlaytheCTF"))
		message();
	else
		puts("U should learn more about CTF");
}
