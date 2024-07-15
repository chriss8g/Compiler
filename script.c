#define PI  3.141592
#define E 2.71828
#include <math.h>
#include <stdio.h>

int main();

int main(){ 
float local__internal_0;
float local__internal_1;
float local__internal_2;
int local__internal_3;
local__internal_0 = 2;
local__internal_1 = 4;
local__internal_2 = (float)(pow(local__internal_0, local__internal_1));

local__internal_3 = printf("%.6g\n", local__internal_2);

return 0;
}