#define PI  3.141592
#define E 2.71828
#include <stdio.h>
#include <stdlib.h>


                        typedef struct {
                            float a;
                        } MyClass;
                        

int function_method_at_MyClass(){ 
int local_method_at_MyClass_internal_0;
int local_method_at_MyClass_internal_1;
local_method_at_MyClass_internal_0 = 2;
local_method_at_MyClass_internal_1 = printf("%d\n", local_method_at_MyClass_internal_0);

return local_method_at_MyClass_internal_1;
}
int main(){ 
MyClass* local__internal_0;
MyClass* local__internal_1;
local__internal_0 = malloc(sizeof(MyClass));

local__internal_1 = function_block_2(local__internal_0);
return 0;
}
int function_block_2(MyClass* a){ 
MyClass* local_block_2_internal_0;
local_block_2_internal_0 = a;
return function_method_at_MyClass();
}