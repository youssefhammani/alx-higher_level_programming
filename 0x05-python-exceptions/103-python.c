#include <Python.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: ", i);
		print_python_list_element(item, i);
	}
}

void print_python_list_element(PyObject *item, Py_ssize_t index)
{
	if (PyBytes_Check(item))
	{
		printf("bytes\n");
		print_python_bytes(item);
	}
	else if (PyFloat_Check(item))
	{
		printf("float\n");
		print_python_float(item);
	}
	else if (PyList_Check(item))
	{
		printf("list\n");
		print_python_list(item);
	}
	else if (PyTuple_Check(item))
	{
		printf("tuple\n");
		print_python_tuple(item);
	}
	else if (PyLong_Check(item))
	{
		printf("int\n");
		print_python_int(item);
	}
	else if (PyUnicode_Check(item))
	{
		printf("str\n");
		print_python_str(item);
	}
	else
	{
		printf("[ERROR] Unknown Type\n");
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_GET_SIZE(p);
	str = PyBytes_AS_STRING(p);

	printf("[.] bytes object info\n  size: %ld\n", size);
	printf("  trying string: %s\n  first 10 bytes: ", str);

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", str[i] & 0xFF);
	}
	printf("\n");
}

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", PyFloat_AS_DOUBLE(p));
}

void print_python_int(PyObject *p)
{
	if (!PyLong_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Int Object\n");
		return;
	}

	printf("[.] int object info\n");
	printf("  value: %ld\n", PyLong_AsLong(p));
}

void print_python_str(PyObject *p)
{
	if (!PyUnicode_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Str Object\n");
		return;
	}

	printf("[.] str object info\n");
	printf("  trying string: %s\n", PyUnicode_AsUTF8(p));
}

void print_python_tuple(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyTuple_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Tuple Object\n");
		return;
	}

	size = PyTuple_Size(p);

	printf("[*] Python tuple info\n");
	printf("[*] Size of the Python Tuple = %ld\n", size);

	for (i = 0; i < size; i++)
	{
		item = PyTuple_GetItem(p, i);
		printf("Element %ld: ", i);

		if (PyBytes_Check(item))
		{
			printf("bytes\n");
			print_python_bytes(item);
		}
		else if (PyFloat_Check(item))
		{
			printf("float\n");
			print_python_float(item);
		}
		else if (PyList_Check(item))
		{
			printf("list\n");
			print_python_list(item);
		}
		else if (PyTuple_Check(item))
		{
			printf("tuple\n");
			print_python_tuple(item);
		}
		else if (PyLong_Check(item))
		{
			printf("int\n");
			print_python_int(item);
		}
		else if (PyUnicode_Check(item))
		{
			printf("str\n");
			print_python_str(item);
		}
		else
		{
			printf("[ERROR] Unknown Type\n");
		}
	}
}

int main(void)
{
	return (0);
}
