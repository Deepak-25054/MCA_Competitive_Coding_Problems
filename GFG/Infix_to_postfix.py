''' Write a Python program to convert an infix expression into a postfix expression using a stack.'''

class Solution:

    # Function to return precedence of operators
    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        if op == '^':
            return 3
        return 0

    # Function to convert infix to postfix
    def infixToPostfix(self, expression):

        stack = []
        result = ""

        # Traverse each character
        for ch in expression:

            # If operand, add directly to result
            if ch.isalnum():
                result += ch

            # If opening bracket, push into stack
            elif ch == '(':
                stack.append(ch)

            # If closing bracket, pop until '('
            elif ch == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()

            # If operator
            else:
                while (stack and stack[-1] != '(' and
                       self.precedence(stack[-1]) >= self.precedence(ch)):
                    result += stack.pop()

                stack.append(ch)

        # Pop remaining operators
        while stack:
            result += stack.pop()

        return result


# Take input from user
expression = input("Enter infix expression: ")

# Create object
obj = Solution()

# Convert and print postfix expression
print("Postfix expression:", obj.infixToPostfix(expression))