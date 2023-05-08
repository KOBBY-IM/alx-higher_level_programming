#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle in it.
 * @list: Pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list, *fast_ptr = list;

	/* Traverse the list using two pointers at different speeds */
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		/* If both pointers meet at some node, there is a cycle */
		if (slow_ptr == fast_ptr)
		{
			return (1);
		}
	}

	/* If one of the pointers reaches the end of the list, there is no cycle */
	return (0);
}
