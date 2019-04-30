#include "lists.h"

/**
 * check_cycle - check for a loop/cycle in a singly linked list
 * @list: singly linked list
 *
 * Return: 0 if no cyle found, 1 if a cycle is found
 */
int check_cycle(listint_t *list)
{
	while (list)
	{
		if (list < list->next)
			return (1);

		list = list->next;
	}

	return (0);
}
