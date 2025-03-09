from Expression import Expression

def main():
    print("Welcome to the calculator! Enter an expression below.")
    raw_input = input().replace("**","^")
    processed_input = processInput(raw_input)
    exp = Expression(processed_input[0],processed_input[1],processed_input[2])
    print(f"{exp.getOperand1()} {exp.getOperator()} {exp.getOperand2()} = {exp.evaluate()}")

def processInput(expression_input):
    for operand in "+-*/%^":
        if operand in expression_input:
            expression_split = expression_input.split(operand)
            expression_split.append(operand)
    trimmed = [elem.strip() for elem in expression_split]
    trimmed[0] = float(trimmed[0]) 
    trimmed[1] = float(trimmed[1])
    return trimmed

if __name__ == "__main__":
    main()
