#include <conio.h>
#include "stdio.h"
#include "time.h"
#include "stdlib.h"
#define row 10
#define line 10
char maze[row][line];
void initialize(){
    for(int i=0;i<10;i++){
        for(int j=0;j<10;j++){
            maze[i][j]='#';
        }}
}
void set_maze(int* a,int*b){
    srand(time(NULL));
    *b=rand()%row;
    * a=rand()%line;
}
void design(int a,int b){
    int direction[4][2]={{0.1},{0,-1},{1,0},{-1,0}};
    int dir=rand()%4;
    int x=a;
    int y=b;
    x=x+direction[dir][0];
    y=y+direction[dir][1];
    while (x>0 && x<=line &&y>=0 &&y<=10 && maze[x][y]!='e'){
        maze[x][y]=' ';
        design(x,y);
    }
}
void create(){
    initialize();
    int start_x;
    int start_y;
    set_maze( &start_x, &start_y);
    maze[start_x][start_y]='.';
    design(start_x,start_y);
}
void maze_show(){
    for(int i=0;i<10;i++){
        for(int j=0;j<10;j++){
            printf("%s\n",maze[i][j]);
        }}
}
void add_box(){

}
int main(){
    maze[line][row]='e';
    create();
    maze_show();
    return 0;
}
