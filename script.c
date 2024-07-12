#define PI 3.141592
#define E 2.71828
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

typedef struct
{
    char *firstname;
    char *lastname;
} Person;

void *init_firstname_of_Person(char *firstname, char *lastname, Person *self);
void *init_lastname_of_Person(char *firstname, char *lastname, Person *self);
char *function_name_at_Person(Person *self);

char *concatenateStrings(const char *str1, const char *str2)
{
    // Calculamos la longitud total de la cadena resultante
    size_t length1 = strlen(str1);
    size_t length2 = strlen(str2);
    size_t totalLength = length1 + length2 + 1; // +1 para el carácter nulo

    // Reservamos memoria para la cadena resultante
    char *result = (char *)malloc(totalLength * sizeof(char));
    if (result == NULL)
    {
        // Si no se pudo asignar memoria, devolvemos NULL
        printf("Error: No se pudo asignar memoria.\n");
        return NULL;
    }

    // Copiamos la primera cadena en el resultado
    strcpy(result, str1);
    // Concatenamos la segunda cadena al resultado
    strcat(result, str2);

    return result;
}

char *floatToString(float num, int precision)
{
    static char buffer[20]; // Buffer para almacenar el string
    snprintf(buffer, 20, "%.*g", precision, num);
    return buffer;
}

float function_hash_at_Person(Person *self);
int main();
#define data_0 " "
void *init_firstname_of_Person(char *firstname, char *lastname, Person *self)
{
    char *local_tname_of_Person_internal_0;
    char *local_tname_of_Person_internal_1;
    Person *local_tname_of_Person_internal_2;
    local_tname_of_Person_internal_0 = firstname;
    local_tname_of_Person_internal_1 = lastname;
    local_tname_of_Person_internal_2 = self;
    self->firstname = local_tname_of_Person_internal_0;
    return local_tname_of_Person_internal_0;
}
void *init_lastname_of_Person(char *firstname, char *lastname, Person *self)
{
    char *local_name_of_Person_internal_0;
    char *local_name_of_Person_internal_1;
    Person *local_name_of_Person_internal_2;
    local_name_of_Person_internal_0 = firstname;
    local_name_of_Person_internal_1 = lastname;
    local_name_of_Person_internal_2 = self;
    self->lastname = local_name_of_Person_internal_1;
    return local_name_of_Person_internal_1;
}
char *function_name_at_Person(Person *self)
{
    Person *local_name_at_Person_internal_0;
    char *local_name_at_Person_internal_1;
    char *local_name_at_Person_internal_2;
    char *local_name_at_Person_internal_3;
    char *local_name_at_Person_internal_4;
    local_name_at_Person_internal_0 = self;
    local_name_at_Person_internal_1 = data_0;
    local_name_at_Person_internal_3 = concatenateStrings(self->firstname, local_name_at_Person_internal_1);

    local_name_at_Person_internal_4 = concatenateStrings(local_name_at_Person_internal_3, self->lastname);

    local_name_at_Person_internal_2 = local_name_at_Person_internal_4;
    return local_name_at_Person_internal_2;
}
float function_hash_at_Person(Person *self)
{
    Person *local_hash_at_Person_internal_0;
    float local_hash_at_Person_internal_1;
    local_hash_at_Person_internal_0 = self;
    local_hash_at_Person_internal_1 = 5;
    return local_hash_at_Person_internal_1;
}
int main()
{
    Person *local__internal_0;
    int local__internal_1;
    {

        local__internal_0 = malloc(sizeof(Person));

        init_firstname_of_Person("Phil", "Collins", local__internal_0);
        init_lastname_of_Person("Phil", "Collins", local__internal_0);

        local__internal_1 = printf("%s\n", function_name_at_Person(local__internal_0));
    }

    return 0;
}