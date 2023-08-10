#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - a function that checks if a singly linked liste has a cycle in it or not.
 * @list: a pointer to the head of the list.
 * Return: 0 if no cycle 1 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list->next;
	listint_t *slow = list;
	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}

	fast = fast->next->next;
        slow = slow->next;
	}
	return (0);
}
