#define PI  3.141592
#define E 2.71828
#include <stdio.h>

float function_operate_0(float param_x_0, float param_y_1);
int main();

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
local__internal_0 = 6;
local__internal_1 = 3;
local__internal_2 = function_operate_0(local__internal_0, local__internal_1);
return 0;
}