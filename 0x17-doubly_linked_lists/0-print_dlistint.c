#include "lists.h"
#include <stdio.h>
#include <stddef.h>
/**
 * print_dlistint - a function that prints all the elemets of a list
 * @h: a pointer
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t node = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		node++;
	}
	return (node);
}
