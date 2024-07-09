#define PI  3.141592
#define E 2.71828
#include <stdio.h>
int main();
float function_let_1(float a);
float function_let_2(float a, float b);
float function_let_3(float a);
float function_let_4(float a, float b);
float function_let_5(float a, float b, float c);


int main(){ 
float local__internal_0;
float local__internal_1;
float local__internal_2;
float local__internal_3;
local__internal_0 = 6;
local__internal_1 = function_let_1(local__internal_0);
local__internal_2 = 5;
local__internal_3 = function_let_3(local__internal_2);
return 0;
}
float function_let_1(float a){ 
float local_let_1_internal_0;
float local_let_1_internal_1;
float local_let_1_internal_2;
float local_let_1_internal_3;
local_let_1_internal_0 = a;
local_let_1_internal_1 = 7;
local_let_1_internal_2 = local_let_1_internal_0 * local_let_1_internal_1;
local_let_1_internal_3 = function_let_2(a, local_let_1_internal_2);
return local_let_1_internal_3;
}
float function_let_2(float a, float b){ 
float local_let_2_internal_0;
float local_let_2_internal_1;
int local_let_2_internal_2;
local_let_2_internal_0 = a;
local_let_2_internal_1 = b;
local_let_2_internal_2 = printf("%f\n", local_let_2_internal_1);

return local_let_2_internal_1;
}
float function_let_3(float a){ 
float local_let_3_internal_0;
float local_let_3_internal_1;
float local_let_3_internal_2;
local_let_3_internal_0 = a;
local_let_3_internal_1 = 10;
local_let_3_internal_2 = function_let_4(a, local_let_3_internal_1);
return local_let_3_internal_2;
}
float function_let_4(float a, float b){ 
float local_let_4_internal_0;
float local_let_4_internal_1;
float local_let_4_internal_2;
float local_let_4_internal_3;
local_let_4_internal_0 = a;
local_let_4_internal_1 = b;
local_let_4_internal_2 = 20;
local_let_4_internal_3 = function_let_5(a, b, local_let_4_internal_2);
return local_let_4_internal_3;
}
float function_let_5(float a, float b, float c){ 
float local_let_5_internal_0;
float local_let_5_internal_1;
float local_let_5_internal_2;
float local_let_5_internal_3;
int local_let_5_internal_4;
float local_let_5_internal_5;
int local_let_5_internal_6;
float local_let_5_internal_7;
int local_let_5_internal_8;
local_let_5_internal_0 = a;
local_let_5_internal_1 = b;
local_let_5_internal_2 = c;
local_let_5_internal_3 = local_let_5_internal_0 + local_let_5_internal_1;
local_let_5_internal_4 = printf("%f\n", local_let_5_internal_3);

local_let_5_internal_5 = local_let_5_internal_1 * local_let_5_internal_2;
local_let_5_internal_6 = printf("%f\n", local_let_5_internal_5);

local_let_5_internal_7 = local_let_5_internal_2 / local_let_5_internal_0;
local_let_5_internal_8 = printf("%f\n", local_let_5_internal_7);

return local_let_5_internal_7;
}