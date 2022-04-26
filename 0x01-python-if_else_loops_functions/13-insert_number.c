#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
	{
		return (NULL);
	}

	newnode->n = number;

	if (*head == NULL || number < temp->n)
	{
		newnode->next = *head;
		*head = newnode;
	}

	else
	{
		while (number < temp->next->n && temp)
		{
			temp = temp->next;
		}

		newnode->next = temp->next;
		temp->next = newnode;
	}

	return (newnode);
}
