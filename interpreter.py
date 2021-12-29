instructions = ">++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+."

cells = {}
programPointer = 0
instructionPointer = 0
depth = 0
enterPoint = {}

while instructionPointer < len(instructions):
  c = instructions[instructionPointer]

  if c == '>':
    programPointer += 1
    if not programPointer in cells:
      cells[programPointer] = 0
  if c == '<':
    programPointer -= 1
    if not programPointer in cells:
      cells[programPointer] = 0

  if c == '+':
    cells[programPointer] += 1

  if c == '-':
    cells[programPointer] -= 1

  if c == '.':
    print(chr(cells[programPointer]))
    
  if c == ',':
    cells[programPointer] = ord(input())

  if c == '[':
    if cells[programPointer]:
      depth += 1
      enterPoint[depth] = instructionPointer - 1
    else:
      while instructions[instructionPointer] != ']':
        instructionPointer += 1

  if c == ']':
    if cells[programPointer]:
      instructionPointer = enterPoint[depth]
      depth -= 1

  instructionPointer += 1