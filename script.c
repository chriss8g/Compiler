#define PI  3.141592
#define E 2.71828
#include <stdio.h>

float function_fib_0(float param_n_0);
int main();

float function_fib_0(float param_n_0){ 
float local_fib_0_internal_0;
float local_fib_0_internal_1;
float local_fib_0_internal_2;
int local_fib_0_internal_3;
float local_fib_0_internal_4;
int local_fib_0_internal_5;
int local_fib_0_internal_6;
float local_fib_0_internal_7;
float local_fib_0_internal_8;
float local_fib_0_internal_9;
float local_fib_0_internal_10;
float local_fib_0_internal_11;
float local_fib_0_internal_12;
float local_fib_0_internal_13;
float local_fib_0_internal_14;
local_fib_0_internal_0 = param_n_0;
local_fib_0_internal_2 = 0;
local_fib_0_internal_3 = local_fib_0_internal_0 == local_fib_0_internal_2;
local_fib_0_internal_4 = 1;
local_fib_0_internal_5 = local_fib_0_internal_0 == local_fib_0_internal_4;
local_fib_0_internal_6 = local_fib_0_internal_3 | local_fib_0_internal_5;
goto my_begin;
my_if:
local_fib_0_internal_7 = 1;
local_fib_0_internal_1 = local_fib_0_internal_7;
goto my_end;
my_else:
local_fib_0_internal_8 = 1;
local_fib_0_internal_9 = local_fib_0_internal_0 - local_fib_0_internal_8;
local_fib_0_internal_10 = function_fib_0(local_fib_0_internal_9);
local_fib_0_internal_11 = 2;
local_fib_0_internal_12 = local_fib_0_internal_0 - local_fib_0_internal_11;
local_fib_0_internal_13 = function_fib_0(local_fib_0_internal_12);
local_fib_0_internal_14 = local_fib_0_internal_10 + local_fib_0_internal_13;
local_fib_0_internal_1 = local_fib_0_internal_14;
goto my_end;
my_begin:
if (local_fib_0_internal_6) 
	goto my_if;
else 
	goto my_else;

my_end:
return local_fib_0_internal_1;
}
int main(){ 
float local__internal_0;
float local__internal_1;
int local__internal_2;
local__internal_0 = 5;
local__internal_1 = function_fib_0(local__internal_0);
local__internal_2 = printf("%.6g\n", local__internal_1);

return 0;
}