#include "lists.h"

/**
 *reverse_listint - function to reverse a linked list
 *@head: list
 *
 *Discription: Function to reverse a linked list
 *
 *Return: pointer to reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *prevn, *currn;

	prevn = currn = NULL;

	while (*head != 0)
	{
		currn = (*head)->next;
		(*head)->next = prevn;
		prevn = *head;
		*head = currn;
	}
	(*head) = prevn;
	return (*head);
}

int is_palindrome(listint_t **head)
{
	listint_t *original_head = (*head);
	listint_t *reverse_head = reverse_listint(head);

	if (!head || (*head)->next == NULL || *head == NULL)
		return (1);

	while (original_head != NULL && reverse_head != NULL)
	{
		if (original_head->n == reverse_head->n)
		{
			original_head = original_head->next;
			reverse_head = reverse_head->next;
		}
		else
			return (0);
	}
	return (1);
}
