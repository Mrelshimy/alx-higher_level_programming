#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *is_palindrome - Function to check if linked list is palindrome
 *@head: pointer to pointer to the list
 *
 *Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *hold = *head;
	int i = 0, j, l = 0;

	if (!(*head))
		return (1);

	while (hold != NULL)
	{
		hold = hold->next;
		l++;
	}
	int *elements = malloc(sizeof(int) * (l));

	if (!elements)
		return (0);

	hold = *head;
	while (hold != NULL)
	{
		elements[i] = hold->n;
		hold = hold->next;
		i++;
	}
	for (j = 0; j < i; j++)
	{
		if (elements[i - 1] == elements[j])
			i--;
		else
		{
			free(elements);
			return (0);
		}
	}
	free(elements);
	return (1);
}
