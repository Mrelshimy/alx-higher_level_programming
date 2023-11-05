#include "lists.h"                                              
                                                                 
/**                                                             
 *is_palindrome - Function to check if linked list is palindrome
 *@head: pointer to pointer to the list                         
 *                                                              
 *Return: 1 if palindrome, 0 if not                             
 */                                                             
                                                                 
int is_palindrome(listint_t **head)
{
	if(head == NULL || *head == NULL)
		return (1);
	return (palind_ext(head, *head));
}

int palind_ext(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);
	if(palind_ext(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
