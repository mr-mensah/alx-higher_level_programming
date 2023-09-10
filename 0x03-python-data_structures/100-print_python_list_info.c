#include <Python.h>
/**
 * print_python_list_info - function that prints the python links
 * @p: argument
 */
void print_python_list_info(PyObject *p)
{
int hows, place, i;
PyObject *obj;
hows = Py_SIZE(p);
place = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %d\n", hows);
printf("[*] Allocated = %d\n", place);
for (i = 0; i < hows; i++)
{
printf("Element %d: ", i);
obj = PyList_GetItem(p, i);
printf("%s\n", Py_TYPE(obj)->tp_name);
}
}

