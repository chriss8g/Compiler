#define PI  3.141592
#define E 2.71828
#include <stdio.h>


int main(){ 
int local__internal_0;
int local__internal_1;
int local__internal_2;
int local__internal_3;
local__internal_0 = function_block_1();
local__internal_1 = function_block_2();
local__internal_2 = function_block_3();
local__internal_3 = function_block_4();
return 0;
}
int function_block_1(){ 
int local_block_1_internal_0;
int local_block_1_internal_1;
int local_block_1_internal_2;
int local_block_1_internal_3;
int local_block_1_internal_4;
int local_block_1_internal_5;
int local_block_1_internal_6;
int local_block_1_internal_7;
local_block_1_internal_1 = 10;
local_block_1_internal_0 = local_block_1_internal_1;
local_block_1_internal_2 = 10;
local_block_1_internal_3 = local_block_1_internal_0 == local_block_1_internal_2;
goto my_begin;
my_if:
local_block_1_internal_4 = 3;
local_block_1_internal_5 = local_block_1_internal_0 + local_block_1_internal_4;
local_block_1_internal_6 = printf("%d\n", local_block_1_internal_5);

goto my_end;
my_else:
local_block_1_internal_7 = printf("%d\n", local_block_1_internal_0);

goto my_end;
my_begin:
if (local_block_1_internal_3) 
	goto my_if;
else 
	goto my_else;

my_end:
return ;
}
int function_block_2(){ 
int local_block_2_internal_0;
int local_block_2_internal_1;
int local_block_2_internal_2;
int local_block_2_internal_3;
int local_block_2_internal_4;
int local_block_2_internal_5;
int local_block_2_internal_6;
int local_block_2_internal_7;
local_block_2_internal_1 = 5;
local_block_2_internal_0 = local_block_2_internal_1;
local_block_2_internal_2 = 10;
local_block_2_internal_3 = local_block_2_internal_0 == local_block_2_internal_2;
goto my_begin;
my_if:
local_block_2_internal_4 = 3;
local_block_2_internal_5 = local_block_2_internal_0 + local_block_2_internal_4;
local_block_2_internal_6 = printf("%d\n", local_block_2_internal_5);

goto my_end;
my_else:
local_block_2_internal_7 = printf("%d\n", local_block_2_internal_0);

goto my_end;
my_begin:
if (local_block_2_internal_3) 
	goto my_if;
else 
	goto my_else;

my_end:
return ;
}
int function_block_3(){ 
int local_block_3_internal_0;
int local_block_3_internal_1;
int local_block_3_internal_2;
int local_block_3_internal_3;
int local_block_3_internal_4;
int local_block_3_internal_5;
int local_block_3_internal_6;
int local_block_3_internal_7;
local_block_3_internal_1 = 5;
local_block_3_internal_0 = local_block_3_internal_1;
local_block_3_internal_2 = 10;
local_block_3_internal_3 = local_block_3_internal_0 == local_block_3_internal_2;
goto my_begin;
my_if:
local_block_3_internal_4 = 3;
local_block_3_internal_5 = local_block_3_internal_0 + local_block_3_internal_4;
local_block_3_internal_6 = printf("%d\n", local_block_3_internal_5);

goto my_end;
my_else:
local_block_3_internal_7 = printf("%d\n", local_block_3_internal_0);

goto my_end;
my_begin:
if (local_block_3_internal_3) 
	goto my_if;
else 
	goto my_else;

my_end:
return ;
}
int function_block_4(){ 
int local_block_4_internal_0;
int local_block_4_internal_1;
int local_block_4_internal_2;
int local_block_4_internal_3;
int local_block_4_internal_4;
int local_block_4_internal_5;
int local_block_4_internal_6;
int local_block_4_internal_7;
local_block_4_internal_1 = 5;
local_block_4_internal_0 = local_block_4_internal_1;
local_block_4_internal_2 = 10;
local_block_4_internal_3 = local_block_4_internal_0 == local_block_4_internal_2;
goto my_begin;
my_if:
local_block_4_internal_4 = 3;
local_block_4_internal_5 = local_block_4_internal_0 + local_block_4_internal_4;
local_block_4_internal_6 = printf("%d\n", local_block_4_internal_5);

goto my_end;
my_else:
local_block_4_internal_7 = printf("%d\n", local_block_4_internal_0);

goto my_end;
my_begin:
if (local_block_4_internal_3) 
	goto my_if;
else 
	goto my_else;

my_end:
return ;
}