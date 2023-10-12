#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    if (size < 10)
        printf("  first %ld bytes: ", size + 1);
    else
        printf("  first 10 bytes: ");

    for (i = 0; i < size && i < 10; i++)
        printf("%02x%s", (unsigned char)str[i], i == size - 1 ? "\n" : " ");
}

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *element;

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
        if (PyBytes_Check(element))
            print_python_bytes(element);
    }
}
