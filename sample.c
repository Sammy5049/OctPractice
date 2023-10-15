#include <stdio.h>
#include <stdlib.h>



typedef struct linkedList 
{
    int n;
    struct linkedList *next;
}list;

list **addNode(list **head, int num);

list **addNode(list **head, int num)
{
    list *newNode = NULL;
    list *temp;

    newNode = malloc(sizeof(list));

    if (newNode == NULL)
    {
        return  (NULL);
    }

    newNode->n = num;
    newNode->next = NULL;

    if (*head == NULL)
    {
        *head = newNode;
        return (head);
    }

    temp = *head;

    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = newNode;

    return (head);
}


int main()
{
    list *head = NULL;

    addNode(&head, 7);
    addNode(&head, 9);
    addNode(&head, 10);

    list *current = head;
    printf("%p -> ", current);
    printf("head -> ");
    while (current != NULL)
    {
        printf("%d -> ", current->n);
        current = current->next;
    }
    printf("NULL\n");

    return (0);
}