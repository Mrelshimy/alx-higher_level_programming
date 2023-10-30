#include "lists.h"

/**
 * check_cycle - Function to check if linked list contains cycle
 *@list: pointer to list
 *
 *Return: 1 if cycle, 0 if no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}

