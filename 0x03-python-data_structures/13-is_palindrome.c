#include "lists.h"

/**
 * is_palindrome - checks whether list of integers is palindrome
 * @head: pointer to pointer to head of singly linked list
 *
 * Return: 0 if not Palindrome, 1 if is Palindrome
 */
int is_palindrome(listint_t **head)
{
	int buff[1024];
	listint_t *temp = *head;
	int i, j, k;

	if (temp == NULL)
		return (1);
	i = 0;
	/* populate a list to compare and count number of elements */
	while (temp)
	{
		buff[i] = temp->n;
		temp = temp->next;
		i++;
	}
	/* find middle of list of numbers */
	k = (i + 1) / 2;
	i = i - 1;
	/* compare front to back of list until middle is reached */
	for (j = 0; j < k; j++, i--)
	{
		if (buff[j] != buff[i])
			return (0);
	}
	return (1);
}
