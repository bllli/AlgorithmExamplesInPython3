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


# 后序表达式计算
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
            raise ValueError('表达式中包含非法字符 %s，请注意使用半角字符', one)
    return int(stack.pop())


# 测试
print('测试后缀表达式计算, 6523+8*+3+*, 结果应为288')
print(postfix_calculate('6523 + 8 * + 3 + *'))


# 中序 -> 后序
def infix_to_postfix(infix_expression: str) -> str:
    """
    使用栈将中序表达式处理为后续表达式
    每个输入四种情况::

      操作数 -> 入栈
      (     -> 入栈
      操作符 -> 将栈顶输出, 直到栈空或栈顶操作符优先级小于本操作符, 最后把本操作符入栈
      )     -> 出栈并输出, 直到将(出栈

    最后输出栈内剩余操作符
    :param infix_expression: 中序表达式
    :return: 后序表达式
    """
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
                try:  # 出栈, 直到遇到'('.没遇到的情况可认为括号不匹配
                    last_pop = stack.pop()
                    while last_pop is not '(':
                        postfix_expression += last_pop
                        last_pop = stack.pop()
                except IndexError:
                    raise ValueError('表达式中括号不匹配')
            elif one is '(':
                stack.push(one)
            else:  # 一直出栈, 直到栈空或顶部操作数小于当前操作数.
                while not stack.is_empty() and get_priority(stack.top()) >= get_priority(one):
                    last_pop = stack.pop()
                    postfix_expression += last_pop
                stack.push(one)
        elif one in allowed_numbers:
            postfix_expression += one
        else:
            raise ValueError('表达式中包含非法字符 %r，请注意使用半角字符' % one)
    while not stack.is_empty():  # 输出栈内剩下的操作符
        postfix_expression += stack.pop()
    return postfix_expression


print(infix_to_postfix('a+b*c+(d*e+f)*g'))
print(postfix_calculate(infix_to_postfix('2+2*2+2')))
print(postfix_calculate(infix_to_postfix('(2+2)*(2+2)')))
