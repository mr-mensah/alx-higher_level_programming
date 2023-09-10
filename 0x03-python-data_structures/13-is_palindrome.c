#include "lists.h"
#include <stddef.h>
/**
 * reverse_listint - function that switches everything up
 * @head: Argument
 * Return: head
 */
listint_t *reverse_listint(listint_t **head)
{
        listint_t *node = *head, *next, *end = NULL;
        while (node)
        {
                next = node->next;
                node->next = end;
                end = node;
                node = next;
        }
        *head = end;
        return (*head);
}
/**
 * is_palindrome - Function that checks all functions
 * @head: argument
 *
 * Return: 1
 */
int is_palindrome(listint_t **head)
{
        listint_t *tmp, *rev, *mid;
        size_t size = 0, i;
        if (*head == NULL || (*head)->next == NULL)
                return (1);
        tmp = *head;
        while (tmp)
        {
                size++;
                tmp = tmp->next;
        }
        tmp = *head;
        for (i = 0; i < (size / 2) - 1; i++)
                tmp = tmp->next;
        if ((size % 2) == 0 && tmp->n != tmp->next->n)
                return (0);
        tmp = tmp->next->next;
        rev = reverse_listint(&tmp);
        mid = rev;
        tmp = *head;
        while (rev)
        {
                if (tmp->n != rev->n)
                        return (0);
                tmp = tmp->next;
                rev = rev->next;
        }
        reverse_listint(&mid);
        return (1);
}

