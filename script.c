#define PI  3.141592
#define E 2.71828
#include <stdio.h>

float function_next_0(float param_x_0);
int main();

float function_next_0(float param_x_0){ 
float local_next_0_internal_0;
float local_next_0_internal_1;
float local_next_0_internal_2;
local_next_0_internal_0 = param_x_0;
local_next_0_internal_1 = 1;
local_next_0_internal_2 = local_next_0_internal_0 + local_next_0_internal_1;
return local_next_0_internal_2;
}
int main(){ 
float local__internal_0;
float local__internal_1;
int local__internal_2;
local__internal_0 = 8;
local__internal_1 = function_next_0(local__internal_0);
local__internal_2 = printf("%.6g\n", local__internal_1);

return 0;
}