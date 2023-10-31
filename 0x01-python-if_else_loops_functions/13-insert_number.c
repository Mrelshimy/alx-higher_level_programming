#include "lists.h"

/**
 *insert_node - Function to insert node in a sorted list
 *@head: pointer to pointer to list
 *@number: inserted integer
 *
 *Discription: Function to insert node to a sorted list
 *
 *Return: address to new node , NULL if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = (*head), *hold = (*head);
	listint_t *nnode;

	while (hold != NULL)
	{
		if (hold->n < number)
		{
			prev->next = hold;
			hold = hold->next;
		}
		else
		{
			nnode->n = number;
			nnode->next = hold;
			prev->next = nnode;
		}
	}
	return (nnode)
}
