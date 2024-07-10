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
float local__internal_5;
int local__internal_6;
float local__internal_7;
float local__internal_8;
float local__internal_9;
float local__internal_10;
float local__internal_11;
int local__internal_12;
float local__internal_13;
float local__internal_14;
float local__internal_15;
float local__internal_16;
float local__internal_17;
int local__internal_18;
int local__internal_19;
int local__internal_20;
int local__internal_21;
int local__internal_22;
int local__internal_23;
int local__internal_24;
float local__internal_25;
float local__internal_26;
int local__internal_27;
int local__internal_28;
char * local__internal_29;
char * local__internal_30;
char * local__internal_31;
char * local__internal_32;
int local__internal_33;
float local__internal_34;
float local__internal_35;
float local__internal_36;
int local__internal_37;
float local__internal_38;
float local__internal_39;
float local__internal_40;
int local__internal_41;
float local__internal_42;
float local__internal_43;
int local__internal_44;
int local__internal_45;
int local__internal_46;
float local__internal_47;
float local__internal_48;
int local__internal_49;
int local__internal_50;
float local__internal_51;
float local__internal_52;
int local__internal_53;
float local__internal_54;
float local__internal_55;
int local__internal_56;
float local__internal_57;
float local__internal_58;
float local__internal_59;
int local__internal_60;
float local__internal_61;
float local__internal_62;
float local__internal_63;
int local__internal_64;
int local__internal_65;
int local__internal_66;
int local__internal_67;
int local__internal_68;
float local__internal_69;
float local__internal_70;
float local__internal_71;
float local__internal_72;
float local__internal_73;
int local__internal_74;
local__internal_0 = 5;
local__internal_1 = printf("%f\n", local__internal_0);

local__internal_2 = PI;
local__internal_3 = 2;
local__internal_4 = local__internal_2 / local__internal_3;
local__internal_5 = sin(local__internal_4);

local__internal_6 = printf("%f\n", local__internal_5);

local__internal_7 = 3;
local__internal_8 = 4.5;
local__internal_9 = 10;
local__internal_10 = local__internal_8 * local__internal_9;
local__internal_11 = local__internal_7 + local__internal_10;
local__internal_12 = printf("%f\n", local__internal_11);

local__internal_13 = 3;
local__internal_14 = 4;
local__internal_15 = local__internal_13 + local__internal_14;
local__internal_16 = 10.5;
local__internal_17 = local__internal_15 * local__internal_16;
local__internal_18 = printf("%f\n", local__internal_17);

local__internal_19 = 1;
local__internal_20 = 0;
local__internal_21 = local__internal_19 & local__internal_20;
local__internal_22 = 1;
local__internal_23 = local__internal_21 | local__internal_22;
local__internal_24 = printf("%d\n", local__internal_23);

local__internal_25 = 3.0;
local__internal_26 = 2;
local__internal_27 = local__internal_25 >= local__internal_26;
local__internal_28 = printf("%d\n", local__internal_27);

local__internal_29 = data_0;
local__internal_30 = data_1;
local__internal_32 = concatenateStrings((char*)local__internal_29, (char*)local__internal_30);

local__internal_31 = local__internal_32;
local__internal_33 = printf("%s\n", local__internal_31);

local__internal_34 = 100;
local__internal_35 = 10;
local__internal_36 = log(local__internal_34)/log(local__internal_35);

local__internal_37 = printf("%f\n", local__internal_36);

local__internal_38 = 3.14;
local__internal_39 = 2.71;
local__internal_40 = local__internal_38 + local__internal_39;
local__internal_41 = printf("%f\n", local__internal_40);

local__internal_42 = 5;
local__internal_43 = 5;
local__internal_44 = local__internal_42 == local__internal_43;
local__internal_45 = !local__internal_44;
local__internal_46 = printf("%d\n", local__internal_45);

local__internal_47 = 10;
local__internal_48 = 20;
local__internal_49 = local__internal_47 != local__internal_48;
local__internal_50 = printf("%d\n", local__internal_49);

local__internal_51 = 4;
local__internal_52 = sqrt(local__internal_51);

local__internal_53 = printf("%f\n", local__internal_52);

local__internal_54 = 1;
local__internal_55 = exp(local__internal_54);

local__internal_56 = printf("%f\n", local__internal_55);

local__internal_57 = 4;
local__internal_58 = 2.0;
local__internal_59 = local__internal_57 / local__internal_58;
local__internal_60 = printf("%f\n", local__internal_59);

local__internal_61 = 10;
local__internal_62 = 5;
local__internal_63 = local__internal_61 - local__internal_62;
local__internal_64 = printf("%f\n", local__internal_63);

local__internal_65 = 1;
local__internal_66 = printf("%d\n", local__internal_65);

local__internal_67 = 0;
local__internal_68 = printf("%d\n", local__internal_67);

local__internal_69 = PI;
local__internal_70 = sin(local__internal_69);

local__internal_71 = E;
local__internal_72 = cos(local__internal_71);

local__internal_73 = local__internal_70 + local__internal_72;
local__internal_74 = printf("%f\n", local__internal_73);

return 0;
}