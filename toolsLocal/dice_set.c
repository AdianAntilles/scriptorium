#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int roll_dice(int sides) {
    return (rand() % sides) + 1;
}

int roll_dice_set(int dice[], int num_dice) {
    int result = 0;
    int place_value = 1;  // Start mit der niedrigsten Stelle
    
    for (int i = num_dice - 1; i >= 0; i--) {  // Höchster Würfel zuerst
        int roll = roll_dice(dice[i]);
        result += roll * place_value;
        place_value *= 10;  // Dezimalsystem für Stellwerte
        printf("W%d → %d\n", dice[i], roll);
    }
    
    return result;
}

int main() {
    srand(time(NULL));  // Zufallsgenerator initialisieren
    
    int dice_set[] = {1, 2, 4, 6, 8, 10, 12, 20, 100};  // Würfeldefinition: W6, W8, W10
    int num_dice = sizeof(dice_set) / sizeof(dice_set[0]);

    int result = roll_dice_set(dice_set, num_dice);
    printf("Stellwert-Zahl: %d\n", result);

    return 0;
}
