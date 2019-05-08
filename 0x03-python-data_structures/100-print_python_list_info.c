#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - C function that prints some basic info about
 * Python lists.
 * @p: PyObject List
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int size = PyList_Size(p);
	int i = 0;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", size);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: int\n", i);
	}
}
