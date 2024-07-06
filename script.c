#define PI  3.141592
#define E 2.71828
#include <stdio.h>

int next(int x){ 
double local__internal_0;
double local__internal_1;

local__internal_0 = 1 * 1.0;
local__internal_1 = x + local__internal_0 * 1.0;
return local__internal_1;
 }
    int main(){ 
double local__internal_0;
double local__internal_1;

local__internal_0 = 8 * 1.0;
local__internal_1 = printf("%d\n", next(local__internal_0));

return 0;
 }