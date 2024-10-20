struct Node {
    char data;
    struct Node* next;
};

struct Stack {
    struct Node* top;
};

struct Stack* createStack() {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->top = NULL;
    return stack;
}

bool isEmpty(struct Stack* stack) { return stack->top == NULL; }

void push(struct Stack* stack, char value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = stack->top;
    stack->top = newNode;
}

char pop(struct Stack* stack) {
    if (isEmpty(stack)) {
        return '\0';
    }
    struct Node* temp = stack->top;
    char value = temp->data;
    stack->top = stack->top->next;
    free(temp);
    return value;
}

char peek(struct Stack* stack) {
    if (isEmpty(stack)) {
        return '\0';
    }
    return stack->top->data;
}

void freeStack(struct Stack* stack) {
    while (!isEmpty(stack)) {
        pop(stack);
    }
    free(stack);
}

bool parseBoolExpr(char* expression) {
    struct Stack* stack = createStack();
    int i = 0;

    for (i = 0; i < strlen(expression); i++) {
        char c = expression[i];

        if (c == ',' || c == '(') {
            continue;
        } else if (c != ')') {
            push(stack, c);
        } else {
            bool has_true = false;
            bool has_false = false;

            while (peek(stack) != '!' && peek(stack) != '&' &&
                   peek(stack) != '|') {
                char top_value = pop(stack);
                if (top_value == 't') {
                    has_true = true;
                } else if (top_value == 'f') {
                    has_false = true;
                }
            }

            char op = pop(stack);

            if (op == '!') {
                if (!has_true) {
                    push(stack, 't');
                } else {
                    push(stack, 'f');
                }
            } else if (op == '&') {
                if (has_false) {
                    push(stack, 'f');
                } else {
                    push(stack, 't');
                }
            } else if (op == '|') {
                if (has_true) {
                    push(stack, 't');
                } else {
                    push(stack, 'f');
                }
            }
        }
    }

    char result = peek(stack);
    freeStack(stack);
    return result == 't';
}
