{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "73422355-1df5-44f6-a41d-f9e0438c4cd5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "915cf958-432d-491c-bf83-05edc7d250e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "class calculator:\n",
    "    def __init__(self):\n",
    "\n",
    "        \"\"\" initialize the dictionary with basic mathematical operations.\"\"\"\n",
    "        self.operations = {\n",
    "    '+': lambda a, b:  a + b,\n",
    "    '-': lambda a, b:  a - b,\n",
    "    '*': lambda a, b:  a * b,\n",
    "    '/': lambda a, b:  a / b if b != 0 else  \"Division by zero error!\" }\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "479662c4-5d38-4891-9eca-1d43f3466e19",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_operations(self, symbol, function):\n",
    "    \"\"\"Add a new operation to the dictionary.\"\"\"\n",
    "    self.operations[symbol] = function\n",
    "\n",
    "def calculate(self, first_number, operation_symbol, second_number=None):\n",
    "    \"\"\"Perform the calculation based on the operation symbol.\"\"\"\n",
    "    if operation_symbol not in self.operations:\n",
    "        raise ValueError(f\"Invalid operation '{operation_symbol}'! Available operations: {', '.join(self.operations.keys())}\")\n",
    "    if not isinstance(first_number, (int, float)) or (second_number is not None and not isinstance(second_number, (int, float))):\n",
    "        raise ValueError(\"Inputs must be numbers!\")\n",
    "    return self.operations[operation_symbol](first_number, second_number) if second_number is not None else self.operations[operation_symbol](first_number)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "251476cb-340e-425a-8781-d3d3ec7cbe62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "calc = calculator()\n",
    "result = calc.operations['+'](5, 3)  # Adds 5 + 3\n",
    "print(result)  # Output: 8\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "f8f8ff97-73f3-498f-befb-777fed7d79b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.6666666666666667\n"
     ]
    }
   ],
   "source": [
    "calc = calculator()\n",
    "result = calc.operations['/'](5, 3)  # Adds 5 / 3\n",
    "print(result)  # Output: \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "fd3cba42-594f-4933-ad98-a8cea78f06a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "calc = calculator()\n",
    "result = calc.operations['-'](5, 3)  # Adds 5 - 3\n",
    "print(result)  # Output: \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "e625a303-8455-46d9-845b-802eed2d7946",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n"
     ]
    }
   ],
   "source": [
    "calc = calculator()\n",
    "result = calc.operations['*'](5, 3)  # Adds 5 * 3\n",
    "print(result)  # Output: \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "c216f5ca-4b1c-44be-8329-e33fefbe96a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Adavance Operation\n",
    "def exponentiation(base, exp):\n",
    "    return base ** exp\n",
    "    \n",
    "def square_root(number, _):\n",
    "    return math.sqrt(number)\n",
    "\n",
    "def logarithm(number, base):\n",
    "    if number <= 0 or base <= 0:\n",
    "        return \"Logarithm inputs must be positive!\"\n",
    "    return math.log(number,base)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "bfd8de2a-b497-4308-8b8f-af428a487686",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Calculator 2.0\n",
      "Available operations: +, -, *, /, ^, sqrt, log\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Enter operation (or 'exit' to quit):  exit\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting Calculator. Goodbye!\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "class Calculator:\n",
    "    def __init__(self):\n",
    "        self.operations = {}\n",
    "\n",
    "    def add_operation(self, symbol, func):\n",
    "        \"\"\"Add a new operation to the calculator.\"\"\"\n",
    "        self.operations[symbol] = func\n",
    "\n",
    "    def calculate(self, num1, operation, num2=None):\n",
    "        \"\"\"Perform the calculation based on the operation.\"\"\"\n",
    "        if operation not in self.operations:\n",
    "            raise ValueError(f\"Operation '{operation}' is not supported.\")\n",
    "        if num2 is not None:\n",
    "            return self.operations[operation](num1, num2)\n",
    "        return self.operations[operation](num1)\n",
    "        \n",
    "def addition(a, b):\n",
    "    return a + b\n",
    "\n",
    "def subtraction(a, b):\n",
    "    return a - b\n",
    "\n",
    "def multiplication(a, b):\n",
    "    return a * b\n",
    "\n",
    "    \n",
    "def division(a, b):\n",
    "    return a / b\n",
    "    \n",
    "def exponentiation(a, b):\n",
    "    return a ** b\n",
    "\n",
    "def square_root(a):\n",
    "    if a < 0:\n",
    "        raise ValueError(\"Cannot calculate the square root of a negative number.\")\n",
    "    return math.sqrt(a)\n",
    "\n",
    "def logarithm(a, base):\n",
    "    if a <= 0:\n",
    "        raise ValueError(\"Logarithm input must be positive.\")\n",
    "    if base <= 0 or base == 1:\n",
    "        raise ValueError(\"Logarithm base must be positive and not equal to 1.\")\n",
    "    return math.log(a, base)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    calc = Calculator()\n",
    "\n",
    "\n",
    "\n",
    "   # Add Basic operations\n",
    "    calc.add_operation('+', addition)\n",
    "    calc.add_operation('-', subtraction)\n",
    "    calc.add_operation('*', multiplication)\n",
    "    calc.add_operation('/', division)\n",
    "    \n",
    "    # Add advanced operations\n",
    "    \n",
    "    calc.add_operation('^', exponentiation)   # Exponentiation\n",
    "    calc.add_operation('sqrt', square_root)  # Square root\n",
    "    calc.add_operation('log', logarithm)     # Logarithm\n",
    "\n",
    "    print(\"Welcome to Calculator 2.0\")\n",
    "    print(\"Available operations: +, -, *, /, ^, sqrt, log\")\n",
    "\n",
    "    while True:\n",
    "        try:\n",
    "            # Input the operation\n",
    "            operation = input(\"\\nEnter operation (or 'exit' to quit): \").strip().lower()\n",
    "            if operation == 'exit':\n",
    "                print(\"Exiting Calculator. Goodbye!\")\n",
    "                break\n",
    "\n",
    "            # Input numbers based on the operation\n",
    "            if operation in ['sqrt']:\n",
    "                num1 = float(input(\"Enter the number: \"))\n",
    "                result = calc.calculate(num1, operation)\n",
    "            elif operation in ['log']:\n",
    "                num1 = float(input(\"Enter the number: \"))\n",
    "                base = float(input(\"Enter the base: \"))\n",
    "                result = calc.calculate(num1, operation, base)\n",
    "            else:\n",
    "                num1 = float(input(\"Enter the first number: \"))\n",
    "                num2 = float(input(\"Enter the second number: \"))\n",
    "                result = calc.calculate(num1, operation, num2)\n",
    "\n",
    "            print(f\"Result: {result}\")\n",
    "        except ValueError as ve:\n",
    "            print(f\"Error: {ve}\")\n",
    "        except Exception as e:\n",
    "            print(f\"An unexpected error occurred: {e}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
