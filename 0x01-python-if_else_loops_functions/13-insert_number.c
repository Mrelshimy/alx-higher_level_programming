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
	listint_t *hold = (*head);
	listint_t *nnode;

	nnode = malloc(sizeof(listint_t));
	if (nnode == NULL)
		return (NULL);
	nnode->n = number;
	nnode->next = NULL;

	if (hold == NULL || nnode->n < hold->n)
	{
		*head = nnode;
		return (nnode);
	}

	while (hold != NULL)
	{
		if (nnode->n < hold->next->n)
		{
			nnode->next = hold->next;
			hold->next = nnode;
			return (nnode);
		}
		hold = hold->next;
	}
	return (NULL);
}
