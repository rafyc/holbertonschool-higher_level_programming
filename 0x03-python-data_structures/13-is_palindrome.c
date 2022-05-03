#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a linked list is a palindrom
 * @head: the head of the linked list
 * Return: 1 if is a palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int count = 0;
	int idx = 0, i = 0, j, check = 0;
	int array[2048];

	while (tmp)
	{
		tmp = tmp->next;
		count++;
	}
	tmp = *head;
	while (tmp)
	{
		array[idx] = tmp->n;
		tmp = tmp->next;
		idx++;
	}
	idx = idx - 1;
	j = count - 1;
	while (i <= (count / 2) && j >= (count / 2))
	{
		if (array[i] != array[j])
		{
			check = 1;
			break;
		}
		i++;
		j--;
	}
	if (check == 1)
		return (0);
	else
		return (1);
}
