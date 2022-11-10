

def mergesort(array, byfunc=None):
    p = 0
    r = len(array) - 1 #index of last element
    mergesort_recursive(array, p, r, byfunc)

def merge(array, p, q, r, byfunc):
    nleft = q - p + 1 #no of elements in left array
    nright = r - q #no of elements in right array
    left_array = array[p:q+1] #include element at end
    right_array = array[q+1:(r+1)]
    left = 0
    right = 0
    dest = p
    while (left < nleft) and (right < nright):
        if byfunc(left_array[left]) <= byfunc(right_array[right]):
            array[dest] = left_array[left]
            left += 1
        else:
            array[dest] = right_array[right]
            right += 1
        dest += 1
    while left < nleft:
        array[dest] = left_array[left]
        left += 1
        dest += 1
    while right < nright:
        array[dest] = right_array[right]
        right += 1
        dest += 1

def mergesort_recursive(array, p, r, byfunc):
    if r - p > 0:
        q = (p + r) // 2
        mergesort_recursive(array, p, q, byfunc)
        mergesort_recursive(array, q+1, r, byfunc)
        merge(array, p, q, r, byfunc)  


#----------------------------------------------

class Stack:
  def __init__(self):
     self.__items = []
        
  def push(self, item):
    self.__items.append(item)

  def pop(self):
    if len(self.__items) >= 1:
      return self.__items.pop()
        
  def peek(self):
    if len(self.__items) >= 1: 
      return self.__items[-1]

  @property
  def is_empty(self):
    return self.__items == []

  @property
  def size(self):
    return len(self.__items)

#----------------------------------------------

class EvaluateExpression:
  # copy the other definitions
  # from the previous parts
  valid_char = '0123456789+-*/()'

  def __init__(self, string=""):
    self.expr = string
    pass

  @property
  def expression(self):
    return self.expr

  @expression.setter
  def expression(self, new_expr):
    for i in new_expr:
      if i not in EvaluateExpression.valid_char:
        return 
        self.expr = ''
      else:
        self.expr = new_expr
    
    return
    self.expr

  def insert_space(self):
    work_string = self.expression
    return_string = ''
    for i in work_string:
      #print (i)
      if i in '+-*/()':
        return_string += ' ' + i + ' '
      
      else:
        return_string +=  i
    
    return return_string
    
  def process_operator(self, operand_stack, operator_stack):
    n1 = int(operand_stack.pop())
    n2 = int(operand_stack.pop())
    operator = operator_stack.pop()

    if operator == '+':
      operand_stack.push(n1+n2)
    elif operator == '-':
      operand_stack.push(n2-n1)
    elif operator == '*':
      operand_stack.push(n1*n2)
    elif operator == '/':
      operand_stack.push(n2//n1)

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()

    for i in tokens:
      if i in '0123456789':
        operand_stack.push(i)
      
      elif i in '+-' :
        while not operator_stack.is_empty and operator_stack.peek() not in '()':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(i)
        
      elif i in '*/':
        while not operator_stack.is_empty and operator_stack.peek() in '*/':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(i)
      
      elif i in '(':
        operator_stack.push(i)
      
      elif i in ')':
        while operator_stack.peek() not in '(':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.pop()

    #print ('====')
    while not operator_stack.is_empty:
      self.process_operator(operand_stack, operator_stack)
    return operand_stack.pop()

#----------------------------------------------

def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





