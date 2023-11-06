#include <Python.h>

/**
 *print_python_list_info - print Pyobject info
 *@p: Pylist Object
 */

void print_python_list_info(PyObject *p)
{
	int obj_allocated, size, n;
	PyObject *object;

	size = Py_SIZE(p);
	obj_allocated = ((PylistObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", obj_allocated);

	for (n = 0; n < size; n++)
	{
		printf("Element %d", n);
		object = PyList_GetItem(p, n);
		printf("%s\n", PyTYPE(object)->tp_name);
	}
}
