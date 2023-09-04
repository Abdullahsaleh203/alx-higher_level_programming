#include "lists.h"
#include <string.h>
/**
 * check_cycle - Entry point
 * Desc: check_cycle function
 * @list: pointer to list_t
 * Return: Singly linkes list or cycle.
 **/
int check_cycle(listint_t *list)
{
	listint_t *jar, *bar;

	jar = list;
	bar = list;

	while (jar && bar && bar->next)
	{
		jar = jar->next;
		bar = bar->next->next;
		if (jar == bar)
			return (1);
	}
	return (0);
}

