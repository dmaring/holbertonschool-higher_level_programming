#include "lists.h"

/**
 * insert_node - insert node in correctly sorted position in list
 * @head: pointer to pointer of head of linked list
 * @number: node number compare and insert
 *
 * Return: address of new node or NULL if node placement failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL;
	listint_t *current = *head;
	listint_t *newnode = NULL;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;

	while (current->next != NULL)
	{
		if (number < current->next->n)
		{
			temp = current->next;
			current->next = newnode;
			newnode->next = temp;

			return (newnode);
		}
		current = current->next;
	}

	free(newnode);
	return (NULL);
}
