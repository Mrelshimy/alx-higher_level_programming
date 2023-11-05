#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *hold = *head;
	int i = 0, j, l = 0;

	if (!(*head))
		return(1);

	while (hold != NULL)
	{
		hold = hold->next;
		l++;
	}
	int *elements = malloc(sizeof(int) * (l));

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
			return(0);
		}
	}
	free(elements);
	return(1);
}
