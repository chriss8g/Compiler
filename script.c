#define PI  3.141592
#define E 2.71828
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
int main();

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
                        

#define data_0 "Hello"
#define data_1 " World!"
int main(){ 
float local__internal_0;
int local__internal_1;
float local__internal_2;
float local__internal_3;
float local__internal_4;
int local__internal_5;
float local__internal_6;
float local__internal_7;
float local__internal_8;
float local__internal_9;
int local__internal_10;
float local__internal_11;
float local__internal_12;
float local__internal_13;
float local__internal_14;
float local__internal_15;
int local__internal_16;
float local__internal_17;
float local__internal_18;
float local__internal_19;
float local__internal_20;
float local__internal_21;
int local__internal_22;
float local__internal_23;
float local__internal_24;
int local__internal_25;
int local__internal_26;
char* local__internal_27;
char* local__internal_28;
char * local__internal_29;
char * local__internal_30;
int local__internal_31;
float local__internal_32;
float local__internal_33;
float local__internal_34;
int local__internal_35;
float local__internal_36;
float local__internal_37;
int local__internal_38;
int local__internal_39;
float local__internal_40;
float local__internal_41;
float local__internal_42;
int local__internal_43;
int local__internal_44;
int local__internal_45;
int local__internal_46;
int local__internal_47;
float local__internal_48;
float local__internal_49;
float local__internal_50;
float local__internal_51;
float local__internal_52;
int local__internal_53;
local__internal_0 = 5;
local__internal_1 = printf("%f\n", local__internal_0);

local__internal_2 = PI;
local__internal_3 = E;
local__internal_4 = local__internal_2 + local__internal_3;
local__internal_5 = printf("%f\n", local__internal_4);

local__internal_6 = PI;
local__internal_7 = 2;
local__internal_8 = local__internal_6 / local__internal_7;
local__internal_9 = sin(local__internal_8);

local__internal_10 = printf("%f\n", local__internal_9);

local__internal_11 = 3;
local__internal_12 = 4.5;
local__internal_13 = 10;
local__internal_14 = local__internal_12 * local__internal_13;
local__internal_15 = local__internal_11 + local__internal_14;
local__internal_16 = printf("%f\n", local__internal_15);

local__internal_17 = 3;
local__internal_18 = 4;
local__internal_19 = local__internal_17 + local__internal_18;
local__internal_20 = 10.5;
local__internal_21 = local__internal_19 * local__internal_20;
local__internal_22 = printf("%f\n", local__internal_21);

local__internal_23 = 0;
local__internal_24 = 2;
local__internal_25 = local__internal_23 >= local__internal_24;
local__internal_26 = printf("%d\n", local__internal_25);

local__internal_27 = data_0;
local__internal_28 = data_1;
local__internal_30 = concatenateStrings((char*)local__internal_27, (char*)local__internal_28);

local__internal_29 = local__internal_30;
local__internal_31 = printf("%s\n", local__internal_29);

local__internal_32 = 3.14;
local__internal_33 = 2.71;
local__internal_34 = local__internal_32 + local__internal_33;
local__internal_35 = printf("%f\n", local__internal_34);

local__internal_36 = 10;
local__internal_37 = 20;
local__internal_38 = local__internal_36 != local__internal_37;
local__internal_39 = printf("%d\n", local__internal_38);

local__internal_40 = 10;
local__internal_41 = 5;
local__internal_42 = local__internal_40 - local__internal_41;
local__internal_43 = printf("%f\n", local__internal_42);

local__internal_44 = 1;
local__internal_45 = printf("%d\n", local__internal_44);

local__internal_46 = 0;
local__internal_47 = printf("%d\n", local__internal_46);

local__internal_48 = PI;
local__internal_49 = sin(local__internal_48);

local__internal_50 = E;
local__internal_51 = cos(local__internal_50);

local__internal_52 = local__internal_49 + local__internal_51;
local__internal_53 = printf("%f\n", local__internal_52);

return 0;
}