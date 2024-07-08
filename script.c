#define PI  3.141592
#define E 2.71828
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

                            char* concatenateStrings(const char* str1, const char* str2) {
                                // Calculamos la longitud total de la cadena resultante
                                size_t length1 = strlen(str1);
                                size_t length2 = strlen(str2);
                                size_t totalLength = length1 + length2 + 1; // +1 para el carácter nulo

                                // Reservamos memoria para la cadena resultante
                                char* result = (char*)malloc(totalLength * sizeof(char));
                                if (result == NULL) {
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
                        

#define data_0 "The meaning of life is "
#define data_1 "42"
int main(){ 
char* local__internal_0;
char* local__internal_1;
char* local__internal_2;
char* local__internal_3;
char* local__internal_4;
local__internal_0 = data_0;
local__internal_1 = data_1;
local__internal_3 = concatenateStrings(local__internal_0, local__internal_1);

local__internal_2 = local__internal_3;
local__internal_4 = printf("%s\n", local__internal_2);

return 0;
}