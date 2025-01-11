#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define MAX_LOAN 0x1000000
#define MAX_BUF 0x200
#define NAME_COST 1337

__asm__("pop %rdi; ret;");

int has_name_rights = 0;

struct MinerAccount {
    float cash;
    float debt_balance;
    int mining_attempts;
    char name[0x20];
};

void initialize() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

void loan(struct MinerAccount *account) {
    uint32_t amount = 0;
    
    printf("How much loan would you like to request?\n");
    if(scanf("%d", &amount) != 1) {
        printf("Invalid input\n");
        return;
    }
    
    if(account->debt_balance + amount > MAX_LOAN) {
        printf("Loan limit exceeded\n");
        return;
    }

    account->cash += amount;
    account->debt_balance += amount;

    printf("Current cash: $%.2f\n", account->cash);
    printf("Debt balance: $%.2f\n", account->debt_balance);
}

void repayment(struct MinerAccount *account) {
    uint32_t amount = 0;

    printf("How much would you like to repay?\n");
    if(scanf("%d", &amount) != 1) {
        printf("Invalid input\n");
        return;
    }

    if(amount > account->cash || amount > account->debt_balance) {
        printf("Insufficient cash or debt balance\n");
        return;
    }

    account->cash -= amount;
    account->debt_balance -= amount;
}

void mining(struct MinerAccount *account) {
    char buffer[MAX_BUF];
    printf("Enter mining work :\n");
    scanf("%5s", buffer);

    printf("Working...\n");
    size_t length = strlen(buffer);
    account->mining_attempts += length;
    sleep(account->mining_attempts);

    account->cash += length * 0.01;
    printf("You mined and earned: $%.2f\n", length * 0.01);

    if (length >= MAX_BUF) {
        printf("Died due to toxic gas\n");
        exit(1);
    }
    printf("Current cash: $%.2f\n", account->cash);
}

void change_name(struct MinerAccount *account) {
    if (has_name_rights != 1) {
        printf("You do not have the right to change your name.\n");
        printf("Please purchase a name to gain the rights to rename your no-name.\n");
        return;
    }
    if(account->debt_balance != 0) {
        printf("You still have debts to repay.\n");
        printf("Pay off your debts to rename your no-name.\n");
        return;
    }
    printf("Enter new name.\n");
    read(0, account->name, MAX_BUF);

    printf("Name updated successfully.\n");
}

void buy_name(struct MinerAccount *account) {
    if(has_name_rights == 1) {
        change_name(account);
    }
    if(account->cash < NAME_COST) {
        printf("Not enough cash to buy a name. You need at least $%d.\n", NAME_COST);
        return;
    }

    account->cash -= NAME_COST;
    has_name_rights = 1;

    printf("Congratulations! You have purchased a name. \n");
    change_name(account);
}



int main() {
    initialize();
    srand(time(NULL));
    struct MinerAccount account = {0, 0, 0, "no-name"};
    while(1) {
        int choice;
        printf("===========================\n");
        printf("Welcome to %s\n", account.name);
        printf("Current cash: $%.2f\n", account.cash);
        printf("Debt balance: $%.2f\n", account.debt_balance);
        printf("===========================\n");

        printf("1. Loan\n2. Repayment\n3. Mining\n4. Buy Name\n5. Change Name\n6. Exit\nChoose an action.\n");
        scanf("%d", &choice);
        switch(choice) {
            case 1:
                loan(&account);
                break;
            case 2:
                repayment(&account);
                break;
            case 3:
                mining(&account);
                break;
            case 4:
                buy_name(&account);
                break;
            case 5:
                change_name(&account);
                break;
            case 6:
                return 0;
            default:
                printf("Invalid choice\n");
                break;
        }
    }
    return 0;
}
