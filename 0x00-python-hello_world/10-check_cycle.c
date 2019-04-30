#include "lists.h"

/**
 * check_cycle - check for a loop/cycle in a singly linked list
 * @list: singly linked list
 *
 * Return: 0 if no cyle found, 1 if a cycle is found
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
