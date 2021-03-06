#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - tells if pal
 * @head: ptr to ptr to ll
 * Return: 1 for pal 0 if not
 */
int is_palindrome(listint_t **head)
{
	int arr[5000], j, i, count = 1;
	listint_t *end, *store;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	end = store = *head;
	for (; end->next != NULL; count++)
		end = end->next;
	for (i = 0; store != NULL; i++)
	{
		arr[i] = store->n;
		store = store->next;
	}
	for (i = 0, j = count - 1; i < j; i++, j--)
		if (arr[i] != arr[j])
			return (0);
	return (1);
}
