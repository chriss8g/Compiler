#define PI  3.141592
#define E 2.71828
#include <stdio.h>

float next(float x);
int main();

float next(float x){ 
float local__internal_0;
float local__internal_1;
local__internal_0 = 1;
local__internal_1 = x + local__internal_0;
return local__internal_1;
}
int main(){ 
float local__internal_0;
float local__internal_1;
int local__internal_2;
local__internal_0 = 8;
local__internal_1 = next(local__internal_0);
local__internal_2 = printf("%f\n", local__internal_1);

return 0;
}