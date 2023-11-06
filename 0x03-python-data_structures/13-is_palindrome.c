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
	listint_t *prevn, *currn, *nextn;

    	prevn = NULL;
    	currn = *head;

    	while (currn != NULL)
    	{
        	nextn = currn->next;
        	currn->next = prevn;
        	prevn = currn;
        	currn = nextn;
    	}

    	*head = prevn;
    	return *head;
}


/**
 *is_palindrome - Function to check if linked list is palindrome
 *@head: pointer to pointer to the list
 *
 *Return: 1 if palindrome, 0 if not
 */

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
