# OSM-language
A programming language and an interpreter for it created out of boredom.
OSM is a stack-based language. A stack is a type of storage system which follows LIFO [Last In First Out], OSM uses array to replicate such stack-based storage system.

OSM's language instruction:

- PUSH **number**  
Takes a number and pushes it to the top of the stack.

- POP  
Removes a number from the top of the stack and return it.

- GET_INPUT  
Gets an integer as an input from the user and pushes it onto the stack.

- ADD  
Remove two numbers from the top of the stack, then adds them and pushes the sum.

- SUBTRACT  
Remove two numbers from the top of the stack, then subtracts them and pushes the difference.

- PRODUCT  
Remove two numbers from the top of the stack, then multiply them and pushes the product. 

- PRINT  **string_literal**    
Takes a string_literal and prints it out on the terminal screen.

- READ  
Reads a number from the I/O input and pushes it to the top of the stack.

- JUMP_IF_ZERO **label**  
Jumps to the label if the top of the stack is 0.

- JUMP_GT_ZERO **label**  
Jumps to the label if the top of the stack is greater than 0.

- END  
Ends/Exits/Stops the program.


## program1.osm
Let's see line by line of how the instructions are executing in **program1.osm** file.

**program1.osm** is created in order to check if two integers are equal or not

```bash
GET_INPUT
GET_INPUT
SUBTRACT
JUMP_IF_ZERO L1
PRINT "Not Equal"
END

L1:
    PRINT "Equal"
    END
```

As you can see, I have ran `GET_INPUT` instruction two times in order to get two integrals input from the user and then push it to the top of the stack.  
`SUBTRACT` instruction pops the two values from the top of the stack(*which in this case are the input values by the user*) and subtracts them, and pushes the difference to the top of the stack.  
`JUMP_IF_ZERO` checks if the value at the top of the stack is 0, the value at the top of the stack will be 0 if the difference is 0 (*i.e. the numbers are equal*), If the difference is 0, then the program will jump to label **L1**. 

**If the difference is not equal to 0, the next instructions will execute without jumping to another label, so `PRINT "Not Equal"` will be executed and the user will see "Not Equal" printed on his/her console screen. Afterwards the `END` stops/exits the program**

**If the difference is equal to 0, the instructions below the label *L1* will start executing, so `PRINT "Equal"` will print "Equal" onto the user's console screen, and the next statement `END` will stop/exit the program**


## program2.osm

Here is one more sample program for better visualization.  
This program takes two integral inputs from the user and checks their sign.

```bash
GET_INPUT
GET_INPUT
PRODUCT
JUMP_GT_ZERO L1
JUMP_IF_ZERO L2
PRINT "Both integers have different sign"
END

L1:
    PRINT "Both integers have same sign"
    END

L2:
    PRINT "Either both integers are 0, or one of them is 0 and another number can be any integer"
    END
```

The logic this snippet of code uses is very simple, the `PRODUCT` instruction multiplies the two numbers and stores their product on the top of the stack.
If the product is positive (i.e. greater than 0), i.e. *both numbers have the same sign*.  
If the product is negative, i.e. *both numbers have different sign*.  
If the product is 0, i.e. well *Either both integers are 0, or one of them is 0 and another number can be any integer*.
