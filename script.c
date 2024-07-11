#define PI  3.141592
#define E 2.71828
#include <stdio.h>

int main();
char * function_let_1(float param_mod_0);
#define data_0 "Magic"
#define data_1 "Woke2"
#define data_2 "Woke"
#define data_3 "Dumb"
int main(){ 
float local__internal_0;
char * local__internal_1;
local__internal_0 = 8;
local__internal_1 = function_let_1(local__internal_0);
return 0;
}
char * function_let_1(float param_mod_0){ 
float local_let_1_internal_0;
char * local_let_1_internal_1;
float local_let_1_internal_2;
int local_let_1_internal_3;
float local_let_1_internal_4;
float local_let_1_internal_5;
float local_let_1_internal_6;
int local_let_1_internal_7;
float local_let_1_internal_8;
float local_let_1_internal_9;
float local_let_1_internal_10;
int local_let_1_internal_11;
char * local_let_1_internal_12;
char * local_let_1_internal_13;
char * local_let_1_internal_14;
char * local_let_1_internal_15;
int local_let_1_internal_16;
local_let_1_internal_0 = param_mod_0;
local_let_1_internal_2 = 0;
local_let_1_internal_3 = local_let_1_internal_0 == local_let_1_internal_2;
local_let_1_internal_4 = 2;
local_let_1_internal_5 = (int)local_let_1_internal_0 % (int)local_let_1_internal_4;

local_let_1_internal_6 = 0;
local_let_1_internal_7 = local_let_1_internal_5 == local_let_1_internal_6;
local_let_1_internal_8 = 3;
local_let_1_internal_9 = (int)local_let_1_internal_0 % (int)local_let_1_internal_8;

local_let_1_internal_10 = 0;
local_let_1_internal_11 = local_let_1_internal_9 == local_let_1_internal_10;
goto my_begin;
my_if:
local_let_1_internal_12 = data_0;
local_let_1_internal_1 = local_let_1_internal_12;
goto my_end;
my_elif_0:
local_let_1_internal_13 = data_1;
local_let_1_internal_1 = local_let_1_internal_13;
goto my_end;
my_elif_1:
local_let_1_internal_14 = data_2;
local_let_1_internal_1 = local_let_1_internal_14;
goto my_end;
my_else:
local_let_1_internal_15 = data_3;
local_let_1_internal_1 = local_let_1_internal_15;
goto my_end;
my_begin:
if (local_let_1_internal_3) 
	goto my_if;
else if(local_let_1_internal_7)
	goto my_elif_0 ;
else if(local_let_1_internal_11)
	goto my_elif_1 ;
else 
	goto my_else;

my_end:
local_let_1_internal_16 = printf("%s\n", local_let_1_internal_1);

return local_let_1_internal_1;
}