#include "lists.h"

/**
 * check_cycle - check for a loop/cycle in a singly linked list
 * @list: singly linked list
 *
 * Return: 0 if no cyle found, 1 if a cycle is found
 */
int check_cycle(listint_t *list)
{
	listint_t *next_node = list->next;

	while (next_node)
	{
		if (list->n < next_node->n)
			return (1);

		list = list->next;
		next_node = next_node->next;
	}

	return (0);
}
