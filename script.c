#define PI  3.141592
#define E 2.71828
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

float function_operate_0(float param_x_0, float param_y_1);
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
                        

                        char *floatToString(float num, int precision) {
                            static char buffer[20]; // Buffer para almacenar el string
                            snprintf(buffer, 20, "%.*g", precision, num); 
                            return buffer;
                        }
                        
#define data_0 "The message is \"Hello World\""
#define data_1 "Hello World"
#define data_2 "Hello"
#define data_3 " World!"
#define data_4 "Magic"
#define data_5 "Woke"
#define data_6 "Dumb"
float function_operate_0(float param_x_0, float param_y_1){ 
float local_operate_0_internal_0;
float local_operate_0_internal_1;
float local_operate_0_internal_2;
int local_operate_0_internal_3;
float local_operate_0_internal_4;
int local_operate_0_internal_5;
float local_operate_0_internal_6;
int local_operate_0_internal_7;
float local_operate_0_internal_8;
int local_operate_0_internal_9;
local_operate_0_internal_0 = param_x_0;
local_operate_0_internal_1 = param_y_1;
local_operate_0_internal_2 = local_operate_0_internal_0 + local_operate_0_internal_1;
local_operate_0_internal_3 = printf("%.6g\n", local_operate_0_internal_2);

local_operate_0_internal_4 = local_operate_0_internal_0 - local_operate_0_internal_1;
local_operate_0_internal_5 = printf("%.6g\n", local_operate_0_internal_4);

local_operate_0_internal_6 = local_operate_0_internal_0 * local_operate_0_internal_1;
local_operate_0_internal_7 = printf("%.6g\n", local_operate_0_internal_6);

local_operate_0_internal_8 = local_operate_0_internal_0 / local_operate_0_internal_1;
local_operate_0_internal_9 = printf("%.6g\n", local_operate_0_internal_8);

return local_operate_0_internal_8;
}
int main(){ 
float local__internal_0;
float local__internal_1;
float local__internal_2;
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
float local__internal_13;
float local__internal_14;
float local__internal_15;
int local__internal_16;
float local__internal_17;
float local__internal_18;
float local__internal_19;
float local__internal_20;
int local__internal_21;
float local__internal_22;
int local__internal_23;
float local__internal_24;
int local__internal_25;
float local__internal_26;
int local__internal_27;
float local__internal_28;
int local__internal_29;
float local__internal_30;
int local__internal_31;
float local__internal_32;
int local__internal_33;
float local__internal_34;
float local__internal_35;
float local__internal_36;
int local__internal_37;
float local__internal_38;
float local__internal_39;
int local__internal_40;
int local__internal_41;
float local__internal_42;
float local__internal_43;
float local__internal_44;
int local__internal_45;
float local__internal_46;
float local__internal_47;
int local__internal_48;
int local__internal_49;
float local__internal_50;
float local__internal_51;
float local__internal_52;
int local__internal_53;
float local__internal_54;
float local__internal_55;
int local__internal_56;
int local__internal_57;
float local__internal_58;
float local__internal_59;
float local__internal_60;
int local__internal_61;
float local__internal_62;
float local__internal_63;
int local__internal_64;
int local__internal_65;
char * local__internal_66;
int local__internal_67;
float local__internal_68;
int local__internal_69;
float local__internal_70;
float local__internal_71;
float local__internal_72;
float local__internal_73;
int local__internal_74;
char * local__internal_75;
int local__internal_76;
float local__internal_77;
int local__internal_78;
float local__internal_79;
float local__internal_80;
float local__internal_81;
float local__internal_82;
int local__internal_83;
float local__internal_84;
float local__internal_85;
float local__internal_86;
float local__internal_87;
float local__internal_88;
int local__internal_89;
float local__internal_90;
float local__internal_91;
float local__internal_92;
float local__internal_93;
float local__internal_94;
int local__internal_95;
int local__internal_96;
int local__internal_97;
int local__internal_98;
int local__internal_99;
int local__internal_100;
int local__internal_101;
float local__internal_102;
float local__internal_103;
int local__internal_104;
int local__internal_105;
char * local__internal_106;
char * local__internal_107;
char * local__internal_108;
char * local__internal_109;
int local__internal_110;
float local__internal_111;
float local__internal_112;
float local__internal_113;
int local__internal_114;
float local__internal_115;
float local__internal_116;
float local__internal_117;
int local__internal_118;
float local__internal_119;
float local__internal_120;
int local__internal_121;
int local__internal_122;
int local__internal_123;
float local__internal_124;
float local__internal_125;
int local__internal_126;
int local__internal_127;
float local__internal_128;
float local__internal_129;
int local__internal_130;
float local__internal_131;
float local__internal_132;
int local__internal_133;
float local__internal_134;
float local__internal_135;
float local__internal_136;
int local__internal_137;
float local__internal_138;
float local__internal_139;
float local__internal_140;
int local__internal_141;
int local__internal_142;
int local__internal_143;
int local__internal_144;
int local__internal_145;
float local__internal_146;
float local__internal_147;
float local__internal_148;
float local__internal_149;
float local__internal_150;
int local__internal_151;
float local__internal_152;
float local__internal_153;
float local__internal_154;
float local__internal_155;
float local__internal_156;
float local__internal_157;
float local__internal_158;
float local__internal_159;
float local__internal_160;
float local__internal_161;
float local__internal_162;
int local__internal_163;
float local__internal_164;
float local__internal_165;
float local__internal_166;
float local__internal_167;
int local__internal_168;
float local__internal_169;
float local__internal_170;
float local__internal_171;
int local__internal_172;
float local__internal_173;
float local__internal_174;
float local__internal_175;
char * local__internal_176;
float local__internal_177;
float local__internal_178;
char * local__internal_179;
float local__internal_180;
int local__internal_181;
float local__internal_182;
float local__internal_183;
float local__internal_184;
int local__internal_185;
char * local__internal_186;
char * local__internal_187;
char * local__internal_188;
int local__internal_189;
float local__internal_190;
float local__internal_191;
float local__internal_192;
int local__internal_193;
float local__internal_194;
float local__internal_195;
int local__internal_196;
float local__internal_197;
float local__internal_198;
float local__internal_199;
int local__internal_200;
local__internal_0 = 6;
local__internal_1 = 3;
local__internal_2 = function_operate_0(local__internal_0, local__internal_1);
local__internal_3 = 1;
local__internal_4 = 2;
local__internal_5 = local__internal_3 + local__internal_4;
local__internal_6 = 3;
local__internal_7 = 4;
local__internal_8 = local__internal_6 * local__internal_7;
local__internal_9 = 5;
local__internal_10 = local__internal_8 * local__internal_9;
local__internal_11 = local__internal_5 - local__internal_10;
local__internal_12 = printf("%.6g\n", local__internal_11);

{

local__internal_13 = 6;
{

local__internal_14 = 7;
local__internal_15 = local__internal_13 * local__internal_14;
local__internal_16 = printf("%.6g\n", local__internal_15);

}

}

{

local__internal_17 = 5;
{

local__internal_18 = 10;
{

local__internal_19 = 20;
local__internal_20 = local__internal_17 + local__internal_18;
local__internal_21 = printf("%.6g\n", local__internal_20);

local__internal_22 = local__internal_18 * local__internal_19;
local__internal_23 = printf("%.6g\n", local__internal_22);

local__internal_24 = local__internal_19 / local__internal_17;
local__internal_25 = printf("%.6g\n", local__internal_24);

}

}

}

{

local__internal_26 = 7;
local__internal_27 = printf("%.6g\n", local__internal_26);

}

{

local__internal_28 = 20;
local__internal_29 = printf("%.6g\n", local__internal_28);

}

{

local__internal_30 = 0;
local__internal_31 = printf("%.6g\n", local__internal_30);

local__internal_32 = 1;
local__internal_30 = local__internal_32;
local__internal_30 = local__internal_32;
local__internal_33 = printf("%.6g\n", local__internal_30);

}

{

local__internal_34 = 10;
local__internal_36 = 10;
local__internal_37 = local__internal_34 == local__internal_36;
goto my_begin_main_56;
my_if_main_56:
local__internal_38 = 3;
local__internal_39 = local__internal_34 + local__internal_38;
local__internal_40 = printf("%.6g\n", local__internal_39);

local__internal_35 = local__internal_39;
goto my_end_main_56;
my_else_main_56:
local__internal_41 = printf("%.6g\n", local__internal_34);

local__internal_35 = local__internal_34;
goto my_end_main_56;
my_begin_main_56:
if (local__internal_37) 
	goto my_if_main_56;
else 
	goto my_else_main_56;

my_end_main_56:
}

{

local__internal_42 = 5;
local__internal_44 = 10;
local__internal_45 = local__internal_42 == local__internal_44;
goto my_begin_main_75;
my_if_main_75:
local__internal_46 = 3;
local__internal_47 = local__internal_42 + local__internal_46;
local__internal_48 = printf("%.6g\n", local__internal_47);

local__internal_43 = local__internal_47;
goto my_end_main_75;
my_else_main_75:
local__internal_49 = printf("%.6g\n", local__internal_42);

local__internal_43 = local__internal_42;
goto my_end_main_75;
my_begin_main_75:
if (local__internal_45) 
	goto my_if_main_75;
else 
	goto my_else_main_75;

my_end_main_75:
}

{

local__internal_50 = 5;
local__internal_52 = 10;
local__internal_53 = local__internal_50 == local__internal_52;
goto my_begin_main_94;
my_if_main_94:
local__internal_54 = 3;
local__internal_55 = local__internal_50 + local__internal_54;
local__internal_56 = printf("%.6g\n", local__internal_55);

local__internal_51 = local__internal_55;
goto my_end_main_94;
my_else_main_94:
local__internal_57 = printf("%.6g\n", local__internal_50);

local__internal_51 = local__internal_50;
goto my_end_main_94;
my_begin_main_94:
if (local__internal_53) 
	goto my_if_main_94;
else 
	goto my_else_main_94;

my_end_main_94:
}

{

local__internal_58 = 5;
local__internal_60 = 10;
local__internal_61 = local__internal_58 == local__internal_60;
goto my_begin_main_113;
my_if_main_113:
local__internal_62 = 3;
local__internal_63 = local__internal_58 + local__internal_62;
local__internal_64 = printf("%.6g\n", local__internal_63);

local__internal_59 = local__internal_63;
goto my_end_main_113;
my_else_main_113:
local__internal_65 = printf("%.6g\n", local__internal_58);

local__internal_59 = local__internal_58;
goto my_end_main_113;
my_begin_main_113:
if (local__internal_61) 
	goto my_if_main_113;
else 
	goto my_else_main_113;

my_end_main_113:
}

local__internal_66 = data_0;
local__internal_67 = printf("%s\n", local__internal_66);

local__internal_68 = 42;
local__internal_69 = printf("%.6g\n", local__internal_68);

local__internal_70 = PI;
local__internal_71 = 2;
local__internal_72 = local__internal_70 / local__internal_71;
local__internal_73 = (float)sin(local__internal_72);

local__internal_74 = printf("%.6g\n", local__internal_73);

local__internal_75 = data_1;
local__internal_76 = printf("%s\n", local__internal_75);

local__internal_77 = 5;
local__internal_78 = printf("%.6g\n", local__internal_77);

local__internal_79 = PI;
local__internal_80 = 2;
local__internal_81 = local__internal_79 / local__internal_80;
local__internal_82 = (float)sin(local__internal_81);

local__internal_83 = printf("%.6g\n", local__internal_82);

local__internal_84 = 3;
local__internal_85 = 4.5;
local__internal_86 = 10;
local__internal_87 = local__internal_85 * local__internal_86;
local__internal_88 = local__internal_84 + local__internal_87;
local__internal_89 = printf("%.6g\n", local__internal_88);

local__internal_90 = 3;
local__internal_91 = 4;
local__internal_92 = local__internal_90 + local__internal_91;
local__internal_93 = 10.5;
local__internal_94 = local__internal_92 * local__internal_93;
local__internal_95 = printf("%.6g\n", local__internal_94);

local__internal_96 = 1;
local__internal_97 = 0;
local__internal_98 = local__internal_96 & local__internal_97;
local__internal_99 = 1;
local__internal_100 = local__internal_98 | local__internal_99;
local__internal_101 = printf("%d\n", local__internal_100);

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

local__internal_114 = printf("%.6g\n", local__internal_113);

local__internal_115 = 3.14;
local__internal_116 = 2.71;
local__internal_117 = local__internal_115 + local__internal_116;
local__internal_118 = printf("%.6g\n", local__internal_117);

local__internal_119 = 5;
local__internal_120 = 5;
local__internal_121 = local__internal_119 == local__internal_120;
local__internal_122 = !local__internal_121;
local__internal_123 = printf("%d\n", local__internal_122);

local__internal_124 = 10;
local__internal_125 = 20;
local__internal_126 = local__internal_124 != local__internal_125;
local__internal_127 = printf("%d\n", local__internal_126);

local__internal_128 = 4;
local__internal_129 = (float)sqrt(local__internal_128);

local__internal_130 = printf("%.6g\n", local__internal_129);

local__internal_131 = 1;
local__internal_132 = (float)exp(local__internal_131);

local__internal_133 = printf("%.6g\n", local__internal_132);

local__internal_134 = 4;
local__internal_135 = 2.0;
local__internal_136 = local__internal_134 / local__internal_135;
local__internal_137 = printf("%.6g\n", local__internal_136);

local__internal_138 = 10;
local__internal_139 = 5;
local__internal_140 = local__internal_138 - local__internal_139;
local__internal_141 = printf("%.6g\n", local__internal_140);

local__internal_142 = 1;
local__internal_143 = printf("%d\n", local__internal_142);

local__internal_144 = 0;
local__internal_145 = printf("%d\n", local__internal_144);

local__internal_146 = PI;
local__internal_147 = (float)sin(local__internal_146);

local__internal_148 = E;
local__internal_149 = (float)cos(local__internal_148);

local__internal_150 = local__internal_147 + local__internal_149;
local__internal_151 = printf("%.6g\n", local__internal_150);

local__internal_152 = 2;
local__internal_153 = PI;
local__internal_154 = local__internal_152 * local__internal_153;
local__internal_155 = (float)sin(local__internal_154);

local__internal_156 = 3;
local__internal_157 = PI;
local__internal_158 = local__internal_156 * local__internal_157;
local__internal_159 = 2;
local__internal_160 = local__internal_158 / local__internal_159;
local__internal_161 = (float)cos(local__internal_160);

local__internal_162 = local__internal_155 + local__internal_161;
local__internal_163 = printf("%.6g\n", local__internal_162);

{

local__internal_164 = 5;
local__internal_165 = 1;
local__internal_166 = local__internal_164 - local__internal_165;
local__internal_164 = local__internal_166;
goto while_label_main_231;
body_main_231:
local__internal_168 = printf("%.6g\n", local__internal_164);

local__internal_167 = local__internal_164;
while_label_main_231:
local__internal_169 = 1;
local__internal_170 = local__internal_164 + local__internal_169;
local__internal_164 = local__internal_170;
local__internal_164 = local__internal_170;
local__internal_171 = 10;
local__internal_172 = local__internal_170 < local__internal_171;
if (local__internal_172) 
	goto body_main_231;
else 
	goto endwhile_label_main_231;

endwhile_label_main_231:
}

{

local__internal_173 = 0;
local__internal_174 = 1;
local__internal_175 = local__internal_173 - local__internal_174;
local__internal_173 = local__internal_175;
goto while_label_main_250;
body_main_250:
{

local__internal_177 = 3;
local__internal_178 = (int)local__internal_173 % (int)local__internal_177;

local__internal_180 = 0;
local__internal_181 = local__internal_178 == local__internal_180;
local__internal_182 = 3;
local__internal_183 = (int)local__internal_178 % (int)local__internal_182;

local__internal_184 = 1;
local__internal_185 = local__internal_183 == local__internal_184;
goto my_begin_main_261;
my_if_main_261:
local__internal_186 = data_4;
local__internal_179 = local__internal_186;
goto my_end_main_261;
my_elif_0_main_261:
local__internal_187 = data_5;
local__internal_179 = local__internal_187;
goto my_end_main_261;
my_else_main_261:
local__internal_188 = data_6;
local__internal_179 = local__internal_188;
goto my_end_main_261;
my_begin_main_261:
if (local__internal_181) 
	goto my_if_main_261;
else if(local__internal_185)
	goto my_elif_0_main_261 ;
else 
	goto my_else_main_261;

my_end_main_261:
local__internal_189 = printf("%s\n", local__internal_179);

}

local__internal_176 = local__internal_179;
while_label_main_250:
local__internal_190 = 1;
local__internal_191 = local__internal_173 + local__internal_190;
local__internal_173 = local__internal_191;
local__internal_173 = local__internal_191;
local__internal_192 = 10;
local__internal_193 = local__internal_191 < local__internal_192;
if (local__internal_193) 
	goto body_main_250;
else 
	goto endwhile_label_main_250;

endwhile_label_main_250:
}

{

local__internal_194 = 10;
goto while_label_main_292;
body_main_292:
local__internal_196 = printf("%.6g\n", local__internal_194);

local__internal_197 = 1;
local__internal_198 = local__internal_194 - local__internal_197;
local__internal_194 = local__internal_198;
local__internal_194 = local__internal_198;
local__internal_195 = local__internal_198;
while_label_main_292:
local__internal_199 = 0;
local__internal_200 = local__internal_194 >= local__internal_199;
if (local__internal_200) 
	goto body_main_292;
else 
	goto endwhile_label_main_292;

endwhile_label_main_292:
}

return 0;
}