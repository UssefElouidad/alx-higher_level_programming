#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - a function that inserts a number into
 * a sorted singly linked list.
 * @head: is the pointer to the head node.
 * @number: the number to be inserted.
 * Return: the addresse of te new node or NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	current = *head;
	prev = NULL;
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}
