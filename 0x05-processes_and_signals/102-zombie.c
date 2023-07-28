#include <stdio.h>

/**
 * infinite_while - ...
 *
 * Return: int
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - program entry point
 *
 * Return: int
 */
int main(void)
{
	infinite_while();
	return (0);
}
