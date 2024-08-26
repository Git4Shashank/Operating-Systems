#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

struct PCB{
    int id;
    char state[20];
    int time;
    struct PCB *next;
};


struct PCB *head , *newnode = NULL, *temp = NULL;


void enquepcb(){
    newnode = (struct PCB*) malloc(sizeof(struct PCB));
    printf("Enter id, state and time ");
    scanf("%d%s%d ", &newnode->id, &newnode->state, newnode->time);
    if(head == NULL){
        head = newnode;
    }
    else{
        temp = head;
        while(temp->next != NULL){
            temp = temp->next;
        }
        temp->next = newnode;
    }
}

void dequepcb(){
    if(head == NULL){
        printf("PCB Already empty");
    }
    else{
        head = head->next;
    }
}


int main(){
    int ch, cont=0;
    do{
        printf("1. Load the new PCB\n");
        printf("2. Remove the PCB completed\n");
        printf("Enter your choice ");
        scanf("%d", &ch);
        if(ch==1){
            enquepcb();
        }
        else if(ch == 2){
            dequepcb();
        }
        else{
            printf("Inavlid Choice ");
        }
        printf("Do you want to continue 1 for Yes, 0 for NO ");
        scanf("%d", &cont);
    }
    while(cont==1);
    getche();


    return 0;
}

