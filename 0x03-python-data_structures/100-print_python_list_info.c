#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	PyObject *item;

	/* Get the size of the list.*/
	size = PyList_Size(p);

	/* Iterate over the list and print each item.*/
	for (Py_ssize_t i = 0; i < size; i++) {
		item = PyList_GetItem(p, i);
		printf("Item %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
