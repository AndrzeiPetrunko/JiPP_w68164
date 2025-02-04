import numpy as np
import re

def validate_matrices(operation, *matrices):
    if operation == "add" or operation == "subtract":
        if not all(m.shape == matrices[0].shape for m in matrices):
            raise ValueError("All matrices must have the same dimensions for addition/subtraction.")
    elif operation == "multiply":
        for i in range(len(matrices) - 1):
            if matrices[i].shape[1] != matrices[i + 1].shape[0]:
                raise ValueError("Matrix dimensions are not compatible for multiplication.")
    elif operation == "transpose":
        if len(matrices) != 1:
            raise ValueError("Only one matrix can be transposed at a time.")

def execute_operation(operation, *matrices):
    validate_matrices(operation, *matrices)
    if operation == "add":
        return sum(matrices)
    elif operation == "subtract":
        result = matrices[0]
        for m in matrices[1:]:
            result -= m
        return result
    elif operation == "multiply":
        result = matrices[0]
        for m in matrices[1:]:
            result = np.dot(result, m)
        return result
    elif operation == "transpose":
        return np.transpose(matrices[0])

def parse_and_execute(command):
    commands = {
        "add": "add",
        "subtract": "subtract",
        "multiply": "multiply",
        "transpose": "transpose"
    }
    parts = command.split(maxsplit=1)
    if len(parts) < 2:
        raise ValueError("Invalid command format. Example: 'add [[1, 2], [3, 4]] [[5, 6], [7, 8]]'")

    operation = commands.get(parts[0].lower())
    if not operation:
        raise ValueError("Unsupported operation. Supported operations: add, subtract, multiply, transpose.")

    try:
        matrices = [np.array(eval(mat.strip())) for mat in re.findall(r'\[.*?\]', parts[1])]
    except Exception as e:
        raise ValueError(f"Error parsing matrices: {e}")

    return execute_operation(operation, *matrices)

# Example usage
try:
    command = "add [[1, 2], [3, 4]] [[5, 6], [7, 8]]"
    result = parse_and_execute(command)
    print("Result:", result)

    command = "multiply [[1, 2], [3, 4]] [[5, 6], [7, 8]]"
    result = parse_and_execute(command)
    print("Result:", result)

    command = "transpose [[1, 2, 3], [4, 5, 6]]"
    result = parse_and_execute(command)
    print("Result:", result)

except Exception as e:
    print("Error:", e)
