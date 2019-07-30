#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
	FILE *fp;
        char filename[]="file1.txt",w[200],sea[]="IIIT";
        fp=fopen(filename,"r");
        if(!fp)
	{
                printf("could not find the file");
                exit(0);
	}
	int a=0;
        while ( fscanf ( fp,"%s", w ) != EOF ) 
	{
         if(strstr(w,sea))
			a++;


        }
	if (a)
	printf("%d", a);
	else
	printf("not present");


        fclose ( fp );


        return 0;
}
