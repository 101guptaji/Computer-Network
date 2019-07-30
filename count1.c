#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
	FILE *fp;
        char filename[]="file2.txt",w[20],sea1[]="IIIT",sea2[]="Nagpur";
	char w1[20];
        fp=fopen(filename,"r");
        if(!fp)
	{
                printf("could not find the file");
                exit(0);
	}
	int a=0,i=0;
        while ( fscanf ( fp,"%s", w ) != EOF ) 
	{
	w1[i]=w;
	i++;
        }
for(int j=0;j<i;j++)
{
 if(strcmp(w1[j],sea1))
	{
		//printf("%s", w);
		if(strcmp(w1[j+1],sea2))
			{
				//printf("%s", w);
				a++;
			}
	}
}
	if (a)
	printf("%d", a);
	else
	printf("not present");


        fclose ( fp );


        return 0;
}
