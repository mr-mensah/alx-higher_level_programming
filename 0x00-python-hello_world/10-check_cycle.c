#include "lists.h"
/**
 * check_cycle - Function that looks at everything
 * @list: lists
 * Return: 0
 */
int check_cycle(listint_t *list)
{
listint_t *snail = list;
listint_t *speed = list;
if (!list)
return (0);
while (snail && speed && speed->next)
{
snail = snail->next;
speed = speed->next->next;
if (snail == speed)
return (1);
}
return (0);
}
