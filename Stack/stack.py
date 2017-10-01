# Python3
from Stack.tools import log


class Stack:
    def __init__(self):
        self.content = []

    @log
    def push(self, value):
        self.content.append(value)
        return value

    @log
    def pop(self):
        return self.content.pop()

    def top(self):
        return self.content[-1]

    def size(self) -> int:
        return len(self.content)

    def is_empty(self) -> bool:
        return True if self.size() == 0 else False


# 后缀表达式计算
def postfix_calculate(postfix_expression: str) -> int:
    stack = Stack()
    allowed_operator = ('*', '/', '+', '-')
    allowed_numbers = tuple('%d' % number for number in range(10))
    for one in postfix_expression:
        if one is ' ':
            pass
        elif one in allowed_operator:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.push('%r' % eval('%s%s%s' % (num1, one, num2)))
            # 执行字符串形式的“数字 运算符 数字” 将结果转换为字符串并入栈
        elif one in allowed_numbers:
            stack.push(one)
        else:
            raise ValueError('表达式中包含非法字符，请注意使用半角字符')
    return int(stack.pop())


# 测试
print('测试后缀表达式计算, 6523+8*+3+*, 结果应为288')
print(postfix_calculate('6523 + 8 * + 3 + *'))


# 中缀 -> 后缀
def infix_to_postfix(infix_expression: str) -> str:
    stack = Stack()
    allowed_operator = ('*', '/', '+', '-', '(', ')')

    def get_priority(char: str) -> int:
        operator_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
        return operator_priority.get(char)

    allowed_numbers = list('%d' % number for number in range(10))
    allowed_numbers.extend(('a', 'b', 'c', 'd', 'e', 'f', 'g'))
    postfix_expression = ''
    for one in infix_expression:
        print('-'*10, 'work with ', one)
        if one is ' ':
            pass
        elif one in allowed_operator:
            if one is ')':
                try:
                    while True:
                        last_pop = stack.pop()
                        if last_pop is '(':
                            break
                        postfix_expression += last_pop
                except IndexError:
                    raise ValueError('表达式中括号不匹配')
            elif one is '(':
                stack.push(one)
            else:
                if stack.is_empty() or get_priority(one) >= get_priority(stack.top()):
                    stack.push(one)
                else:
                    while True:
                        last_pop = stack.pop()
                        postfix_expression += last_pop
                        if stack.is_empty() or get_priority(stack.top()) < get_priority(one):
                            break
                    stack.push(one)
        elif one in allowed_numbers:
            postfix_expression += one
        else:
            raise ValueError('表达式中包含非法字符 %r，请注意使用半角字符' % one)
    while not stack.is_empty():
        postfix_expression += stack.pop()
    return postfix_expression


print(infix_to_postfix('a+b*c+(d*e+f)*g'))
print(postfix_calculate(infix_to_postfix('2+2*2+2')))
print(postfix_calculate(infix_to_postfix('(2+2)*(2+2)')))
