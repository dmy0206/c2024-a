#include <stdio.h>
#include <stdlib.h>

void print(){
    FILE*fp;
    fp= fopen("C:\\Users\\33014\\CLionProjects\\c2024-a\\level1\\p10_warehouse\\warehouse.txt","r");
    if (fp==NULL){
        perror("error");
        printf("cannot open");
        return;
    }
    char current[20]={};
    while(fgets(current,sizeof (current),fp)!=NULL){
        printf("%s\n",current);
    }
    fclose(fp);
}
void menu(){
    printf("check:0,input:1,output:2,close:3\n");
    int choose=scanf_s("%d",&choose);
    if (choose==0){
        print();
    }
    if(choose==1){
        print();
        int input= scanf_s("%d",&input);
        FILE *fp;
        fp= fopen("C:\\Users\\33014\\CLionProjects\\c2024-a\\level1\\p10_warehouse\\warehouse.txt","a");
        int number;
        while(fscanf_s(fp,"%d",&number)==1){
            printf("%d",number);
            number=number+input;
            fprintf(fp,"Ʒ�ƣ�legion");
            fprintf(fp,"ʣ�ࣺ%d",number);
            fclose(fp);
            print();
            }
        }
    if(choose==2){
        print();
        int input= scanf_s("%d",&input);
        FILE *fp;
        fp= fopen("C:\\Users\\33014\\CLionProjects\\c2024-a\\level1\\p10_warehouse\\warehouse.txt","a");
        int number;
        while(fscanf_s(fp,"%d",&number)==1){
            printf("%d",number);
            number=number-input;
            fprintf(fp,"Ʒ�ƣ�legion");
            fprintf(fp,"ʣ�ࣺ%d",number);
            fclose(fp);
            print();
        }
    }
    if(choose==3){
        exit(1);
    }
}
int main() {
    menu();
    return 0;
}