#include "stdio.h"
#include "stdlib.h"
typedef struct Node{
    int data;
    struct Node*next;
}line;
line*createnode(int data){
    line*node=(line*) malloc(sizeof (line));
    if (!node){
        printf("%s","失败");
        exit(1);
    }
    node->data=data;
    node->next=NULL;
    return node;
}
line*inserthead(line**head,int data){
    line*node= createnode(data);
    node->next=*head;
    *head=node;
}
line*inserttail(line**head,int data){
    line*node= createnode(data);
    if (*head == NULL) {
        *head = node;
        return 0;
    }
    line*p=*head;
    while (p->next!=NULL){
        p=p->next;
    }
    p->next=node;
}
line*insertbody(line**head,int data,int object){
    line*node= createnode(data);
    line*p=*head;
    line*prev=NULL;
    while(p!=NULL&&p->next!=object){
        prev=p;
        p=p->next;
    }
    prev->next=node;
    node->next=p;
}
line*release(int k,line**head){
    line*p=*head;
    line*prev=NULL;
    if (head->data==k){
        line*head=head->next;
    }
    while(p!=NULL&&p->data!=k){
        prev->next=p->next;

    }
}
