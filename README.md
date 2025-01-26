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