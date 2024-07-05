#include <stdio.h>

int main(){ 
int local__internal_0;
int local__internal_1;
int local__internal_2;

local__internal_0 = 5;
local__internal_1 = 0;
local__internal_2 = local__internal_0 == local__internal_1;
if( local__internal_2) 
	function_block_1();
 else 
	function_block_2();
;
return 0;;
 }
    int function_block_1(){ 
int local_block_1_internal_0;

local_block_1_internal_0 = 2;
printf("%d\n", local_block_1_internal_0);
;
return 0;;
 }
    int function_block_2(){ 
int local_block_2_internal_0;

local_block_2_internal_0 = 5;
printf("%d\n", local_block_2_internal_0);
;
return 0;;
 }