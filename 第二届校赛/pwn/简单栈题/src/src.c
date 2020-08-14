//gcc src.c -o main -z noexecstack -fstack-protector-explicit -no-pie -z now
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int mprotect(void *addr, size_t len, int prot);
void input()
{
	char buf[0x20];
	memset(buf,0,0x20);
	read(0,buf,0x50);
	
}
void my_init()
{
	int buf;
	int fd = open("/dev/urandom",0);
	read(fd,&buf,4);
	close(fd);
	buf = buf&0xFFFFF000;
	int ret = mmap(buf, 0x1000, 3 , 34, 0xFFFFFFFF, 0LL);
	if(!ret)
	{
		puts("[~] MMAP Error");
		exit(0);
	}
	mprotect(buf,0x1000,7);
}
int main()
{
	my_init();
	input();
}
