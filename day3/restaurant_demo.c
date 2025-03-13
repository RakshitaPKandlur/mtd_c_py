#include<stdio.h>
#include "restaurant.c"
int main() 
{
    puts("Welcome to our restaurant The Taste");
    void runMenu();
    puts("Namaste Visit Again");
}


void runMenu()
{
    int foodType = 0, itemNumber = 0;
    puts("Welcome to our restaurant The Taste");
    do 
    {
        puts("What you wish to have Veg:1, Nonveg:2. Your choice please");
        scanf("%d", &foodType);
        switch(foodType) 
        {
            case 1 : puts("1:DB-Dosa 2:ChowChowBath 3:Idly-Vada 4:BB-Bath. Your choice please: ");
            scanf("%d", &itemNumber);
            switch(itemNumber) 
            {
                case 1 : puts("Yummy Davanagere Benne Dosa Ma'am"); break;
                case 2 : puts("Spicy Khara Bath and Tasty Shira Ma'am"); break;
                case 3 : puts("Soft Idli and Hot Vada Ma'am"); break;
                case 4 : puts("Fresh hot Bath with Pure Ghee Sir"); break;
                default : puts("Sorry we don't serve your chaoice of food");
            } break;
            case 2 : puts("1:Fish-Fry 2:Chicken-Biryani 3:Hanumantu-Palav 4:Egg-Masala. Your choice please: ");
            scanf("%d", &itemNumber);
            switch(itemNumber) 
            {
                case 1 : puts("Tasty fish from Manglore Ma'am"); break;
                case 2 : puts("Nati Dum Biryani for you Sir!!!"); break;
                case 3 : puts("Famous Palav for you Ma'am"); break;
                case 4 : puts("Delicious Egg Masala Ma'am!!"); break;
                default : puts("Sorry we don't serve your chaoice of food");
            } break;
            default : puts("This is Restaurant, not Garden. Please Order an item");
        }
        puts("Do you wish to have more? Yes:1, No:Anynumber");
        scanf("%d", &itemNumber);
    }
    while(itemNumber == 1);
}