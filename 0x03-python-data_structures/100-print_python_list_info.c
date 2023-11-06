#include <Python.h>

/**
 * print_python_list_info - print Pyobject info
 * @p: Pylist Object
 */
void print_python_list_info(PyObject *p)
{
	int size, obj_allocated, n;
	PyObject *object;

	size = PyList_Size(p);
	obj_allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", obj_allocated);

	for (n = 0; n < size; n++)
	{
		object = PyList_GetItem(p, n);
		printf("Element %d: %s\n", n, Py_TYPE(object)->tp_name);
	}
}

