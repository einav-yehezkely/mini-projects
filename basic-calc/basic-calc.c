#include <stdio.h>

int main(void) {
    char operation;
    double a, b;
    printf("Enter operation: ");
    scanf("%c", &operation);
    printf("Enter a: ");
    scanf("%lf", &a);
    printf("Enter b: ");
    scanf("%lf", &b);

    switch (operation) {
        case '+':
            printf("%.2lf + %.2lf = %.2lf\n", a, b, a + b);
            break;
        case '*':
            printf("%.2lf * %.2lf = %.2lf\n", a, b, a * b);
            break;
        case '-':
            printf("%.2lf - %.2lf = %.2lf\n", a, b, a - b);
        case '/':
            if (b == 0) {
                printf("Error: devision by zero");
                break;
            }
            else {
                printf("%.2lf / %.2lf = %.2lf\n", a, b, a/b);
                break;
            }
        default:
            printf("Invalid operation\n");
    }
}