#define PI  3.141592
#define E 2.71828
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

                        typedef struct {
                            char * firstname;
    char * lastname;
                        } Person;
                        

                        typedef struct {
                            float x;
    float y;
                        } Point;
                        
float function_tan_0(float param_x_0);
float function_cot_1(float param_x_0);
float function_fib_2(float param_n_0);
float function_fact_3(float param_x_0);
float function_next_4(float param_x_0);
char * init_firstname_of_Person(char * firstname, char * lastname, Person* self);
char * init_lastname_of_Person(char * firstname, char * lastname, Person* self);
char * function_name_at_Person(Person* self);

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
                        

                        char *floatToString(float num, int precision) {
                            static char buffer[20]; // Buffer para almacenar el string
                            snprintf(buffer, 20, "%.*g", precision, num); 
                            return buffer;
                        }
                        
float function_hash_at_Person(Person* self);
float init_x_of_Point(float x, float y, Point* self);
float init_y_of_Point(float x, float y, Point* self);
float function_getX_at_Point(Point* self);
float function_getY_at_Point(Point* self);
float function_setX_at_Point(float x, Point* self);
float function_setY_at_Point(float y, Point* self);
int main();
#define data_0 " "
#define data_1 "Hello World"
#define data_2 "The message is \"Hello World\""
#define data_3 "The meaning of life is "
#define data_4 "Hello World"
#define data_5 "Hello World"
#define data_6 "The meaning of life is"
#define data_7 " "
#define data_8 "The meaning of life is"
#define data_9 "The meaning of life is"
#define data_10 "Even"
#define data_11 "odd"
#define data_12 "even"
#define data_13 "odd"
#define data_14 "Even"
#define data_15 "Odd"
#define data_16 "Magic"
#define data_17 "Dumb"
#define data_18 "x: "
#define data_19 "; y: "
#define data_20 "x: "
#define data_21 "; y: "
float function_tan_0(float param_x_0){ 
float local_tan_0_internal_0;
float local_tan_0_internal_1;
float local_tan_0_internal_2;
float local_tan_0_internal_3;
local_tan_0_internal_0 = param_x_0;
local_tan_0_internal_1 = (float)sin(local_tan_0_internal_0);

local_tan_0_internal_2 = (float)cos(local_tan_0_internal_0);

local_tan_0_internal_3 = local_tan_0_internal_1 / local_tan_0_internal_2;
return local_tan_0_internal_3;
}
float function_cot_1(float param_x_0){ 
float local_cot_1_internal_0;
float local_cot_1_internal_1;
float local_cot_1_internal_2;
float local_cot_1_internal_3;
local_cot_1_internal_0 = param_x_0;
local_cot_1_internal_1 = 1;
local_cot_1_internal_2 = function_tan_0(local_cot_1_internal_0);
local_cot_1_internal_3 = local_cot_1_internal_1 / local_cot_1_internal_2;
return local_cot_1_internal_3;
}
float function_fib_2(float param_n_0){ 
float local_fib_2_internal_0;
float local_fib_2_internal_1;
float local_fib_2_internal_2;
int local_fib_2_internal_3;
float local_fib_2_internal_4;
int local_fib_2_internal_5;
int local_fib_2_internal_6;
float local_fib_2_internal_7;
float local_fib_2_internal_8;
float local_fib_2_internal_9;
float local_fib_2_internal_10;
float local_fib_2_internal_11;
float local_fib_2_internal_12;
float local_fib_2_internal_13;
float local_fib_2_internal_14;
local_fib_2_internal_0 = param_n_0;
local_fib_2_internal_2 = 0;
local_fib_2_internal_3 = local_fib_2_internal_0 == local_fib_2_internal_2;
local_fib_2_internal_4 = 1;
local_fib_2_internal_5 = local_fib_2_internal_0 == local_fib_2_internal_4;
local_fib_2_internal_6 = local_fib_2_internal_3 | local_fib_2_internal_5;
goto my_begin_function_fib_2_6;
my_if_function_fib_2_6:
local_fib_2_internal_7 = 1;
local_fib_2_internal_1 = local_fib_2_internal_7;
goto my_end_function_fib_2_6;
my_else_function_fib_2_6:
local_fib_2_internal_8 = 1;
local_fib_2_internal_9 = local_fib_2_internal_0 - local_fib_2_internal_8;
local_fib_2_internal_10 = function_fib_2(local_fib_2_internal_9);
local_fib_2_internal_11 = 2;
local_fib_2_internal_12 = local_fib_2_internal_0 - local_fib_2_internal_11;
local_fib_2_internal_13 = function_fib_2(local_fib_2_internal_12);
local_fib_2_internal_14 = local_fib_2_internal_10 + local_fib_2_internal_13;
local_fib_2_internal_1 = local_fib_2_internal_14;
goto my_end_function_fib_2_6;
my_begin_function_fib_2_6:
if (local_fib_2_internal_6) 
	goto my_if_function_fib_2_6;
else 
	goto my_else_function_fib_2_6;

my_end_function_fib_2_6:
return local_fib_2_internal_1;
}
float function_fact_3(float param_x_0){ 
float local_fact_3_internal_0;
float local_fact_3_internal_1;
float local_fact_3_internal_2;
float local_fact_3_internal_3;
float local_fact_3_internal_4;
float local_fact_3_internal_5;
float local_fact_3_internal_6;
float local_fact_3_internal_7;
float local_fact_3_internal_8;
float local_fact_3_internal_9;
float local_fact_3_internal_10;
float local_fact_3_internal_11;
float local_fact_3_internal_12;
int local_fact_3_internal_13;
local_fact_3_internal_0 = param_x_0;
{

local_fact_3_internal_1 = param_x_0;
local_fact_3_internal_2 = local_fact_3_internal_0;
local_fact_3_internal_3 = 1;
{

local_fact_3_internal_4 = 1;
local_fact_3_internal_5 = 1;
local_fact_3_internal_6 = local_fact_3_internal_4 - local_fact_3_internal_5;
local_fact_3_internal_4 = local_fact_3_internal_6;
goto while_label_function_fact_3_10;
body_function_fact_3_10:
local_fact_3_internal_8 = local_fact_3_internal_3 * local_fact_3_internal_4;
local_fact_3_internal_3 = local_fact_3_internal_8;
local_fact_3_internal_3 = local_fact_3_internal_8;
local_fact_3_internal_7 = local_fact_3_internal_8;
while_label_function_fact_3_10:
local_fact_3_internal_9 = 1;
local_fact_3_internal_10 = local_fact_3_internal_4 + local_fact_3_internal_9;
local_fact_3_internal_4 = local_fact_3_internal_10;
local_fact_3_internal_4 = local_fact_3_internal_10;
local_fact_3_internal_11 = 1;
local_fact_3_internal_12 = local_fact_3_internal_1 + local_fact_3_internal_11;
local_fact_3_internal_13 = local_fact_3_internal_10 < local_fact_3_internal_12;
if (local_fact_3_internal_13) 
	goto body_function_fact_3_10;
else 
	goto endwhile_label_function_fact_3_10;

endwhile_label_function_fact_3_10:
}

}

return local_fact_3_internal_7;
}
float function_next_4(float param_x_0){ 
float local_next_4_internal_0;
float local_next_4_internal_1;
float local_next_4_internal_2;
local_next_4_internal_0 = param_x_0;
local_next_4_internal_1 = 1;
local_next_4_internal_2 = local_next_4_internal_0 + local_next_4_internal_1;
return local_next_4_internal_2;
}
char * init_firstname_of_Person(char * firstname, char * lastname, Person* self){ 
char * local_tname_of_Person_internal_0;
char * local_tname_of_Person_internal_1;
Person* local_tname_of_Person_internal_2;
local_tname_of_Person_internal_0 = firstname;
local_tname_of_Person_internal_1 = lastname;
local_tname_of_Person_internal_2 = self;
self->firstname = local_tname_of_Person_internal_0;
return local_tname_of_Person_internal_0;
}
char * init_lastname_of_Person(char * firstname, char * lastname, Person* self){ 
char * local_name_of_Person_internal_0;
char * local_name_of_Person_internal_1;
Person* local_name_of_Person_internal_2;
local_name_of_Person_internal_0 = firstname;
local_name_of_Person_internal_1 = lastname;
local_name_of_Person_internal_2 = self;
self->lastname = local_name_of_Person_internal_1;
return local_name_of_Person_internal_1;
}
char * function_name_at_Person(Person* self){ 
Person* local_name_at_Person_internal_0;
char * local_name_at_Person_internal_1;
char * local_name_at_Person_internal_2;
char * local_name_at_Person_internal_3;
char * local_name_at_Person_internal_4;
local_name_at_Person_internal_0 = self;
local_name_at_Person_internal_1 = data_0;
local_name_at_Person_internal_3 = concatenateStrings(self->firstname, local_name_at_Person_internal_1);

local__internal_102 = 3.0;
local__internal_103 = 2;
local__internal_104 = local__internal_102 >= local__internal_103;
local__internal_105 = printf("%d\n", local__internal_104);

local__internal_106 = data_2;
local__internal_107 = data_3;
local__internal_109 = concatenateStrings(local__internal_106, local__internal_107);

local__internal_108 = local__internal_109;
local__internal_110 = printf("%s\n", local__internal_108);

local__internal_111 = 10;
local__internal_112 = 100;
local__internal_113 = (float)(log(local__internal_112)/log(local__internal_111));

local_name_at_Person_internal_2 = local_name_at_Person_internal_4;
return local_name_at_Person_internal_2;
}
float function_hash_at_Person(Person* self){ 
Person* local_hash_at_Person_internal_0;
float local_hash_at_Person_internal_1;
local_hash_at_Person_internal_0 = self;
local_hash_at_Person_internal_1 = 5;
return local_hash_at_Person_internal_1;
}
float init_x_of_Point(float x, float y, Point* self){ 
float local__Point_internal_0;
float local__Point_internal_1;
Point* local__Point_internal_2;
local__Point_internal_0 = x;
local__Point_internal_1 = y;
local__Point_internal_2 = self;
self->x = local__Point_internal_0;
return local__Point_internal_0;
}
float init_y_of_Point(float x, float y, Point* self){ 
float local__Point_internal_0;
float local__Point_internal_1;
Point* local__Point_internal_2;
local__Point_internal_0 = x;
local__Point_internal_1 = y;
local__Point_internal_2 = self;
self->y = local__Point_internal_1;
return local__Point_internal_1;
}
float function_getX_at_Point(Point* self){ 
Point* local_getX_at_Point_internal_0;
local_getX_at_Point_internal_0 = self;
return self->x;
}
float function_getY_at_Point(Point* self){ 
Point* local_getY_at_Point_internal_0;
local_getY_at_Point_internal_0 = self;
return self->y;
}
float function_setX_at_Point(float x, Point* self){ 
float local_setX_at_Point_internal_0;
Point* local_setX_at_Point_internal_1;
local_setX_at_Point_internal_0 = x;
local_setX_at_Point_internal_1 = self;
self->x = local_setX_at_Point_internal_0;
return local_setX_at_Point_internal_0;
}
float function_setY_at_Point(float y, Point* self){ 
float local_setY_at_Point_internal_0;
Point* local_setY_at_Point_internal_1;
local_setY_at_Point_internal_0 = y;
local_setY_at_Point_internal_1 = self;
self->y = local_setY_at_Point_internal_0;
return local_setY_at_Point_internal_0;
}
int main(){ 
float local__internal_0;
float local__internal_1;
int local__internal_2;
float local__internal_3;
float local__internal_4;
float local__internal_5;
float local__internal_6;
float local__internal_7;
float local__internal_8;
float local__internal_9;
float local__internal_10;
float local__internal_11;
int local__internal_12;
char * local__internal_13;
int local__internal_14;
char * local__internal_15;
int local__internal_16;
char * local__internal_17;
float local__internal_18;
char * local__internal_19;
char * local__internal_20;
int local__internal_21;
float local__internal_22;
float local__internal_23;
float local__internal_24;
float local__internal_25;
float local__internal_26;
float local__internal_27;
float local__internal_28;
float local__internal_29;
float local__internal_30;
float local__internal_31;
float local__internal_32;
float local__internal_33;
float local__internal_34;
float local__internal_35;
float local__internal_36;
int local__internal_37;
float local__internal_38;
int local__internal_39;
float local__internal_40;
float local__internal_41;
float local__internal_42;
float local__internal_43;
int local__internal_44;
char * local__internal_45;
int local__internal_46;
float local__internal_47;
float local__internal_48;
float local__internal_49;
float local__internal_50;
float local__internal_51;
float local__internal_52;
float local__internal_53;
float local__internal_54;
float local__internal_55;
int local__internal_56;
char * local__internal_57;
int local__internal_58;
float local__internal_59;
char * local__internal_60;
char * local__internal_61;
char * local__internal_62;
char * local__internal_63;
char * local__internal_64;
int local__internal_65;
float local__internal_66;
char * local__internal_67;
char * local__internal_68;
char * local__internal_69;
int local__internal_70;
float local__internal_71;
char * local__internal_72;
char * local__internal_73;
char * local__internal_74;
int local__internal_75;
float local__internal_76;
float local__internal_77;
float local__internal_78;
int local__internal_79;
float local__internal_80;
float local__internal_81;
float local__internal_82;
int local__internal_83;
float local__internal_84;
float local__internal_85;
float local__internal_86;
float local__internal_87;
int local__internal_88;
float local__internal_89;
int local__internal_90;
float local__internal_91;
int local__internal_92;
float local__internal_93;
float local__internal_94;
float local__internal_95;
int local__internal_96;
float local__internal_97;
float local__internal_98;
float local__internal_99;
int local__internal_100;
float local__internal_101;
float local__internal_102;
int local__internal_103;
int local__internal_104;
float local__internal_105;
float local__internal_106;
float local__internal_107;
float local__internal_108;
int local__internal_109;
float local__internal_110;
float local__internal_111;
float local__internal_112;
float local__internal_113;
int local__internal_114;
float local__internal_115;
int local__internal_116;
float local__internal_117;
int local__internal_118;
float local__internal_119;
float local__internal_120;
int local__internal_121;
int local__internal_122;
float local__internal_123;
char * local__internal_124;
float local__internal_125;
float local__internal_126;
float local__internal_127;
int local__internal_128;
char * local__internal_129;
int local__internal_130;
char * local__internal_131;
int local__internal_132;
float local__internal_133;
char * local__internal_134;
float local__internal_135;
float local__internal_136;
float local__internal_137;
int local__internal_138;
char * local__internal_139;
char * local__internal_140;
int local__internal_141;
float local__internal_142;
char * local__internal_143;
float local__internal_144;
float local__internal_145;
float local__internal_146;
int local__internal_147;
int local__internal_148;
char * local__internal_149;
int local__internal_150;
char * local__internal_151;
int local__internal_152;
float local__internal_153;
float local__internal_154;
float local__internal_155;
char * local__internal_156;
float local__internal_157;
int local__internal_158;
char * local__internal_159;
char * local__internal_160;
int local__internal_161;
float local__internal_162;
float local__internal_163;
int local__internal_164;
float local__internal_165;
float local__internal_166;
float local__internal_167;
int local__internal_168;
float local__internal_169;
float local__internal_170;
int local__internal_171;
float local__internal_172;
float local__internal_173;
int local__internal_174;
float local__internal_175;
float local__internal_176;
int local__internal_177;
Person* local__internal_178;
int local__internal_179;
Point* local__internal_180;
char * local__internal_181;
char * local__internal_182;
char * local__internal_183;
char * local__internal_184;
char * local__internal_185;
char * local__internal_186;
char * local__internal_187;
char * local__internal_188;
int local__internal_189;
Point* local__internal_190;
char * local__internal_191;
char * local__internal_192;
char * local__internal_193;
char * local__internal_194;
char * local__internal_195;
char * local__internal_196;
char * local__internal_197;
char * local__internal_198;
int local__internal_199;
local__internal_0 = 42;
local__internal_1 = 42;
local__internal_2 = printf("%.6g\n", local__internal_1);

local__internal_3 = 1;
local__internal_4 = 2;
local__internal_5 = local__internal_3 + local__internal_4;
local__internal_6 = 3;
local__internal_7 = local__internal_5 * local__internal_6;
local__internal_8 = 4;
local__internal_9 = local__internal_7 * local__internal_8;
local__internal_10 = 5;
local__internal_11 = local__internal_9 / local__internal_10;
local__internal_12 = printf("%.6g\n", local__internal_11);

local__internal_13 = data_1;
local__internal_14 = printf("%s\n", local__internal_13);

local__internal_15 = data_2;
local__internal_16 = printf("%s\n", local__internal_15);

local__internal_17 = data_3;
local__internal_18 = 42;
local__internal_20 = concatenateStrings(local__internal_17, floatToString(local__internal_18,6));

local__internal_19 = local__internal_20;
local__internal_21 = printf("%s\n", local__internal_19);

local__internal_22 = 2;
local__internal_23 = PI;
local__internal_24 = local__internal_22 * local__internal_23;
local__internal_25 = (float)sin(local__internal_24);

local__internal_26 = 2;
local__internal_27 = local__internal_25 * local__internal_26;
local__internal_28 = 3;
local__internal_29 = PI;
local__internal_30 = local__internal_28 * local__internal_29;
local__internal_31 = 4;
local__internal_32 = 64;
local__internal_33 = (float)(log(local__internal_32)/log(local__internal_31));

local__internal_34 = local__internal_30 / local__internal_33;
local__internal_35 = (float)cos(local__internal_34);

local__internal_36 = local__internal_27 + local__internal_35;
local__internal_37 = printf("%.6g\n", local__internal_36);

local__internal_38 = 42;
local__internal_39 = printf("%.6g\n", local__internal_38);

local__internal_40 = PI;
local__internal_41 = 2;
local__internal_42 = local__internal_40 / local__internal_41;
local__internal_43 = (float)sin(local__internal_42);

local__internal_44 = printf("%.6g\n", local__internal_43);

local__internal_45 = data_4;
local__internal_46 = printf("%s\n", local__internal_45);

local__internal_47 = PI;
local__internal_48 = function_tan_0(local__internal_47);
local__internal_49 = 2;
local__internal_50 = local__internal_48 * local__internal_49;
local__internal_51 = PI;
local__internal_52 = function_cot_1(local__internal_51);
local__internal_53 = 2;
local__internal_54 = local__internal_52 * local__internal_53;
local__internal_55 = local__internal_50 + local__internal_54;
local__internal_56 = printf("%.6g\n", local__internal_55);

{

local__internal_57 = data_5;
local__internal_58 = printf("%s\n", local__internal_57);

}

{

local__internal_59 = 42;
{

local__internal_60 = data_6;
local__internal_61 = data_7;
local__internal_63 = concatenateStrings(local__internal_60, local__internal_61);

local__internal_64 = concatenateStrings(local__internal_63, floatToString(local__internal_59,6));

local__internal_62 = local__internal_64;
local__internal_65 = printf("%s\n", local__internal_62);

}

}

{

local__internal_66 = 42;
{

local__internal_67 = data_8;
local__internal_69 = concatenateStrings(local__internal_67, floatToString(local__internal_66,6));

local__internal_68 = local__internal_69;
local__internal_70 = printf("%s\n", local__internal_68);

}

}

{

local__internal_71 = 42;
{

local__internal_72 = data_9;
local__internal_74 = concatenateStrings(local__internal_72, floatToString(local__internal_71,6));

local__internal_73 = local__internal_74;
local__internal_75 = printf("%s\n", local__internal_73);

}

}

{

local__internal_76 = 6;
{

local__internal_77 = 7;
local__internal_78 = local__internal_76 * local__internal_77;
local__internal_79 = printf("%.6g\n", local__internal_78);

}

}

{

local__internal_80 = 6;
{

local__internal_81 = 7;
local__internal_82 = local__internal_80 * local__internal_81;
local__internal_83 = printf("%.6g\n", local__internal_82);

}

}

{

local__internal_84 = 5;
{

local__internal_85 = 10;
{

local__internal_86 = 20;
local__internal_87 = local__internal_84 + local__internal_85;
local__internal_88 = printf("%.6g\n", local__internal_87);

local__internal_89 = local__internal_85 * local__internal_86;
local__internal_90 = printf("%.6g\n", local__internal_89);

local__internal_91 = local__internal_86 / local__internal_84;
local__internal_92 = printf("%.6g\n", local__internal_91);

}

}

}

{

{

local__internal_93 = 6;
local__internal_94 = 7;
local__internal_95 = local__internal_93 * local__internal_94;
}

local__internal_96 = printf("%.6g\n", local__internal_95);

}

{

local__internal_97 = 6;
local__internal_98 = 7;
local__internal_99 = local__internal_97 * local__internal_98;
}

local__internal_100 = printf("%.6g\n", local__internal_99);

{

local__internal_101 = 20;
{

local__internal_102 = 42;
local__internal_103 = printf("%.6g\n", local__internal_102);

}

local__internal_104 = printf("%.6g\n", local__internal_101);

}

{

local__internal_105 = 7;
{

local__internal_106 = 7;
local__internal_107 = 6;
local__internal_108 = local__internal_106 * local__internal_107;
local__internal_109 = printf("%.6g\n", local__internal_108);

}

}

{

local__internal_110 = 7;
{

local__internal_111 = 7;
local__internal_112 = 6;
local__internal_113 = local__internal_111 * local__internal_112;
local__internal_114 = printf("%.6g\n", local__internal_113);

}

}

{

local__internal_115 = 0;
local__internal_116 = printf("%.6g\n", local__internal_115);

local__internal_117 = 1;
local__internal_115 = local__internal_117;
local__internal_115 = local__internal_117;
local__internal_118 = printf("%.6g\n", local__internal_115);

}

{

local__internal_119 = 0;
{

local__internal_120 = 1;
local__internal_119 = local__internal_120;
local__internal_119 = local__internal_120;
local__internal_121 = printf("%.6g\n", local__internal_119);

local__internal_122 = printf("%.6g\n", local__internal_120);

}

}

{

local__internal_123 = 42;
local__internal_125 = 2;
local__internal_126 = (int)local__internal_123 % (int)local__internal_125;

local__internal_127 = 0;
local__internal_128 = local__internal_126 == local__internal_127;
goto my_begin_main_185;
my_if_main_185:
local__internal_129 = data_10;
local__internal_130 = printf("%s\n", local__internal_129);

local__internal_124 = local__internal_129;
goto my_end_main_185;
my_else_main_185:
local__internal_131 = data_11;
local__internal_132 = printf("%s\n", local__internal_131);

local__internal_124 = local__internal_131;
goto my_end_main_185;
my_begin_main_185:
if (local__internal_128) 
	goto my_if_main_185;
else 
	goto my_else_main_185;

my_end_main_185:
}

{

local__internal_133 = 42;
local__internal_135 = 2;
local__internal_136 = (int)local__internal_133 % (int)local__internal_135;

local__internal_137 = 0;
local__internal_138 = local__internal_136 == local__internal_137;
goto my_begin_main_206;
my_if_main_206:
local__internal_139 = data_12;
local__internal_134 = local__internal_139;
goto my_end_main_206;
my_else_main_206:
local__internal_140 = data_13;
local__internal_134 = local__internal_140;
goto my_end_main_206;
my_begin_main_206:
if (local__internal_138) 
	goto my_if_main_206;
else 
	goto my_else_main_206;

my_end_main_206:
local__internal_141 = printf("%s\n", local__internal_134);

}

{

local__internal_142 = 42;
local__internal_144 = 2;
local__internal_145 = (int)local__internal_142 % (int)local__internal_144;

local__internal_146 = 0;
local__internal_147 = local__internal_145 == local__internal_146;
goto my_begin_main_226;
my_if_main_226:
local__internal_148 = printf("%.6g\n", local__internal_142);

local__internal_149 = data_14;
local__internal_150 = printf("%s\n", local__internal_149);

local__internal_143 = local__internal_149;
goto my_end_main_226;
my_else_main_226:
local__internal_151 = data_15;
local__internal_152 = printf("%s\n", local__internal_151);

local__internal_143 = local__internal_151;
goto my_end_main_226;
my_begin_main_226:
if (local__internal_147) 
	goto my_if_main_226;
else 
	goto my_else_main_226;

my_end_main_226:
}

{

local__internal_153 = 42;
{

local__internal_154 = 3;
local__internal_155 = (int)local__internal_153 % (int)local__internal_154;

local__internal_157 = 0;
local__internal_158 = local__internal_155 == local__internal_157;
goto my_begin_main_249;
my_if_main_249:
local__internal_159 = data_16;
local__internal_156 = local__internal_159;
goto my_end_main_249;
my_else_main_249:
local__internal_160 = data_17;
local__internal_156 = local__internal_160;
goto my_end_main_249;
my_begin_main_249:
if (local__internal_158) 
	goto my_if_main_249;
else 
	goto my_else_main_249;

my_end_main_249:
local__internal_161 = printf("%s\n", local__internal_156);

}

}

{

local__internal_162 = 10;
goto while_label_main_266;
body_main_266:
local__internal_164 = printf("%.6g\n", local__internal_162);

local__internal_165 = 1;
local__internal_166 = local__internal_162 - local__internal_165;
local__internal_162 = local__internal_166;
local__internal_162 = local__internal_166;
local__internal_163 = local__internal_166;
while_label_main_266:
local__internal_167 = 0;
local__internal_168 = local__internal_162 >= local__internal_167;
if (local__internal_168) 
	goto body_main_266;
else 
	goto endwhile_label_main_266;

endwhile_label_main_266:
}

local__internal_169 = 5;
local__internal_170 = function_fact_3(local__internal_169);
local__internal_171 = printf("%.6g\n", local__internal_170);

local__internal_172 = 5;
local__internal_173 = function_fib_2(local__internal_172);
local__internal_174 = printf("%.6g\n", local__internal_173);

local__internal_175 = 8;
local__internal_176 = function_next_4(local__internal_175);
local__internal_177 = printf("%.6g\n", local__internal_176);

{

local__internal_178 = malloc(sizeof(Person));

init_firstname_of_Person("Phil", "Collins", local__internal_178);
init_lastname_of_Person("Phil", "Collins", local__internal_178);

local__internal_179 = printf("%s\n", function_name_at_Person(local__internal_178));

}

{

local__internal_180 = malloc(sizeof(Point));

init_x_of_Point(4, 5, local__internal_180);
init_y_of_Point(4, 5, local__internal_180);

local__internal_181 = data_18;
local__internal_183 = concatenateStrings(local__internal_181, floatToString(function_getX_at_Point(local__internal_180),6));

local__internal_182 = local__internal_183;
local__internal_184 = data_19;
local__internal_186 = concatenateStrings(local__internal_182, local__internal_184);

local__internal_185 = local__internal_186;
local__internal_188 = concatenateStrings(local__internal_185, floatToString(function_getY_at_Point(local__internal_180),6));

local__internal_187 = local__internal_188;
local__internal_189 = printf("%s\n", local__internal_187);

}

{

local__internal_190 = malloc(sizeof(Point));

init_x_of_Point(3, 4, local__internal_190);
init_y_of_Point(3, 4, local__internal_190);

local__internal_191 = data_20;
local__internal_193 = concatenateStrings(local__internal_191, floatToString(function_getX_at_Point(local__internal_190),6));

local__internal_192 = local__internal_193;
local__internal_194 = data_21;
local__internal_196 = concatenateStrings(local__internal_192, local__internal_194);

local__internal_195 = local__internal_196;
local__internal_198 = concatenateStrings(local__internal_195, floatToString(function_getY_at_Point(local__internal_190),6));

local__internal_197 = local__internal_198;
local__internal_199 = printf("%s\n", local__internal_197);

}

return 0;
}