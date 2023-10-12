#include <Python.h>

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: The Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	printf("  size: %ld\n", size);

	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first 10 bytes:");

	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf(" %02x", PyBytes_AsString(p)[i]);
	}

	printf("\n");
}

/**
 * print_python_list - Print information about a Python list object.
 * @p: The Python list object.
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("[!] Invalid Python List\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);

	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: ", i);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyLong_Check(item))
			printf("int\n");
		else if (PyFloat_Check(item))
			printf("float\n");
		else if (PyTuple_Check(item))
			printf("tuple\n");
		else if (PyList_Check(item))
			printf("list\n");
		else if (PyUnicode_Check(item))
			printf("str\n");
		else
			printf("Unknown\n");
	}
}
