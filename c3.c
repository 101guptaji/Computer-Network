/* WAp to read a file , convert in binary and display it , and again convert in text file and store in output file.*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <stdio.h>

int main() {
        int num;
        FILE *fp1, *fp2;
        char ch;

        
        /* open the source file in read mode */
        fp1 = fopen("file1.txt", "r");

        /* error handling */
        if (!fp1) {
                printf("Unable to open the input file!!\n");
                return 0;
        }

        /* open the target file in binary write mode */
        fp2 = fopen("tg.bin", "wb");

        /* error handling */
        if (!fp2) {
                printf("Unable to open the output file!!\n");
                return 0;
        }

        /*
         * read data from input file and write
         * the binary form of it in output file
         */
        while (!feof(fp1)) {
                /* reading one byte of data */
                fread(&ch, sizeof(char), 1, fp1);
                /* converting the character to ascii integer value */
                num = ch;
                /* writing 4 byte of data to the output file */
                fwrite(&num, sizeof(int), 1, fp2);
        }

        /* close all opened files */
        fclose(fp1);
        fclose(fp2);
        return 0;
  }

