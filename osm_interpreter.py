import sys

# reads the file name 
file_path = sys.argv[1]

# making sure that the file name ends with the correct extension
if (file_path.endswith(".osm")!=True):
    sys.exit()

###########################
# Tokenizing the program  #
###########################

# reading lines from the program file
program_lines = []
with open(file_path, "r") as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]

# parsing 
program = []
token_counter = 0   # token_counter will be used as a indicator which will indicate where we are at the program in terms of parsing
label_tracker = {}  # label_tracker will be used to track which index in our program list a label is pointing to.

for line in program_lines:
    parts = line.split(" ")
    instruction = parts[0]

    # checks for empty line
    if (instruction == ""):
        continue

    # checks for label
    if (instruction.endswith(":")):
        label_tracker[instruction[:-1]] = token_counter
        continue

    # stores instruction token 
    program.append(instruction)
    token_counter += 1

    # handling the instructions
    if (instruction == "PUSH"):
        # expecting an integer 
        program.append(int(parts[1]))
        token_counter += 1
    elif (instruction == "PRINT"):
        # parse string literal
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
        token_counter += 1
    elif (instruction == "JUMP_IF_ZERO"):
        # reads the label
        label = parts[1]
        program.append(label)
        token_counter += 1
    elif (instruction == "JUMP_GT_ZERO"):
        label = parts[1]
        program.append(label)
        token_counter += 1
    
# print(program)
    

#########
# STACK #
#########

class Stack:
    
    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1
    
    def push(self, number):
        self.sp += 1
        self.buf[self.sp] = number
    
    def pop(self):
        number = self.buf[self.sp]
        self.sp -= 1
        return number

    def top(self):
        return self.buf[self.sp]
    
pc = 0
stack = Stack(256)

while (program[pc]!="END"):
    instruction = program[pc]
    pc += 1

    if (instruction == "PUSH"):
        number = program[pc]
        pc += 1
        stack.push(number)
    
    elif (instruction == "POP"):
        stack.pop()
    
    elif (instruction == "ADD"):
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)
    
    elif (instruction == "SUBTRACT"):
        a = stack.pop()
        b = stack.pop()
        stack.push(b-a)

    elif (instruction == "PRODUCT"):
        a = stack.pop()
        b = stack.pop()
        stack.push(a*b)
    
    elif (instruction == "PRINT"):
        string_literal = program[pc]
        pc += 1
        print(string_literal)

    elif (instruction == "GET_INPUT"):
        a = int(input())
        stack.push(a)
    
    elif (instruction == "JUMP_IF_ZERO"):
        number = stack.top()
        if (number==0):
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    
    elif (instruction == "JUMP_GT_ZERO"):
        number = stack.top()
        if (number>0):
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    

