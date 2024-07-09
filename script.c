#define PI  3.141592
#define E 2.71828
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
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
int local__internal_23;
int local__internal_24;
int local__internal_25;
int local__internal_26;
int local__internal_27;
int local__internal_28;
float local__internal_29;
float local__internal_30;
int local__internal_31;
int local__internal_32;
char* local__internal_33;
char* local__internal_34;
char * local__internal_35;
char * local__internal_36;
int local__internal_37;
float local__internal_38;
float local__internal_39;
float local__internal_40;
int local__internal_41;
float local__internal_42;
int local__internal_43;
float local__internal_44;
float local__internal_45;
float local__internal_46;
int local__internal_47;
float local__internal_48;
float local__internal_49;
int local__internal_50;
int local__internal_51;
int local__internal_52;
float local__internal_53;
float local__internal_54;
int local__internal_55;
int local__internal_56;
float local__internal_57;
float local__internal_58;
int local__internal_59;
float local__internal_60;
float local__internal_61;
int local__internal_62;
float local__internal_63;
float local__internal_64;
float local__internal_65;
int local__internal_66;
float local__internal_67;
float local__internal_68;
float local__internal_69;
int local__internal_70;
int local__internal_71;
int local__internal_72;
int local__internal_73;
int local__internal_74;
float local__internal_75;
float local__internal_76;
float local__internal_77;
float local__internal_78;
float local__internal_79;
int local__internal_80;
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

local__internal_23 = 1;
local__internal_24 = 0;
local__internal_25 = local__internal_23 & local__internal_24;
local__internal_26 = 1;
local__internal_27 = local__internal_25 | local__internal_26;
local__internal_28 = printf("%d\n", local__internal_27);

local__internal_29 = 3.0;
local__internal_30 = 2;
local__internal_31 = local__internal_29 >= local__internal_30;
local__internal_32 = printf("%d\n", local__internal_31);

local__internal_33 = data_0;
local__internal_34 = data_1;
local__internal_36 = concatenateStrings((char*)local__internal_33, (char*)local__internal_34);

local__internal_35 = local__internal_36;
local__internal_37 = printf("%s\n", local__internal_35);

local__internal_38 = 100;
local__internal_39 = 10;
local__internal_40 = log(local__internal_38)/log(local__internal_39);

local__internal_41 = printf("%f\n", local__internal_40);

srand(time(NULL));
local__internal_42 = (rand()%101)/100.0;

local__internal_43 = printf("%f\n", local__internal_42);

local__internal_44 = 3.14;
local__internal_45 = 2.71;
local__internal_46 = local__internal_44 + local__internal_45;
local__internal_47 = printf("%f\n", local__internal_46);

local__internal_48 = 5;
local__internal_49 = 5;
local__internal_50 = local__internal_48 == local__internal_49;
local__internal_51 = !local__internal_50;
local__internal_52 = printf("%d\n", local__internal_51);

local__internal_53 = 10;
local__internal_54 = 20;
local__internal_55 = local__internal_53 != local__internal_54;
local__internal_56 = printf("%d\n", local__internal_55);

local__internal_57 = 4;
local__internal_58 = sqrt(local__internal_57);

local__internal_59 = printf("%f\n", local__internal_58);

local__internal_60 = 1;
local__internal_61 = exp(local__internal_60);

local__internal_62 = printf("%f\n", local__internal_61);

local__internal_63 = 4;
local__internal_64 = 2.0;
local__internal_65 = local__internal_63 / local__internal_64;
local__internal_66 = printf("%f\n", local__internal_65);

local__internal_67 = 10;
local__internal_68 = 5;
local__internal_69 = local__internal_67 - local__internal_68;
local__internal_70 = printf("%f\n", local__internal_69);

local__internal_71 = 1;
local__internal_72 = printf("%d\n", local__internal_71);

local__internal_73 = 0;
local__internal_74 = printf("%d\n", local__internal_73);

local__internal_75 = PI;
local__internal_76 = sin(local__internal_75);

local__internal_77 = E;
local__internal_78 = cos(local__internal_77);

local__internal_79 = local__internal_76 + local__internal_78;
local__internal_80 = printf("%f\n", local__internal_79);

return 0;
}