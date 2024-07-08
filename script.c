#define PI 3.141592
#define E 2.71828
#include <stdio.h>

#define data_0 "The meaning of life is "
#define data_1 "aaaa"
int main()
{
    char *local__internal_0;
    char *local__internal_1;
    char *local__internal_2;
    char *local__internal_3;
    local__internal_0 = data_0;
    local__internal_1 = data_1;
    local__internal_2 = local__internal_0 + local__internal_1;
    local__internal_3 = printf("%s\n", local__internal_2);

    return 0;
}