# Định nghĩa các toán tử và dấu ngoặc
OPERATORS = ['+', '-', '*', '/']
PARENTHESES = ['(', ')']

def is_valid_expression(expr):

  stack = []  # Stack để theo dõi dấu ngoặc đơn
  prev_char = None  # Biến theo dõi ký tự trước đó

  for char in expr:
    if char.isdigit():  # Bỏ qua các số
      pass

    elif char in OPERATORS:
      # Kiểm tra toán tử có nằm ở các vị trí không hợp lệ
      if prev_char is None or prev_char in OPERATORS or prev_char in PARENTHESES:
        return False  # Biểu thức không hợp lệ

    elif char == '(':
      stack.append(char)  # Thêm dấu ngoặc mở vào stack

    elif char == ')':
      # Kiểm tra dấu ngoặc đóng không cân bằng
      if not stack or stack.pop() != '(':
        return False  # Biểu thức không hợp lệ

    else:
      return False  # Báo hiệu ký tự không hợp lệ

    prev_char = char  # Cập nhật ký tự trước đó

  return len(stack) == 0  # Kiểm tra tất cả dấu ngoặc đơn đóng

expression1 = "3+4*2/(1-5)"
print(f"Biểu thức '{expression1}' Kết Quả: {is_valid_expression(expression1)}")  # True

expression2 = "3+4*2)"
print(f"Biểu thức '{expression2}' Kết Quả: {is_valid_expression(expression2)}")  # False

expression3 = "+42+3"
print(f"Biểu thức '{expression3}' Kết Quả: {is_valid_expression(expression3)}")  # False

expression4 = "3+4*+2"
print(f"Biểu thức '{expression4}' Kết Quả: {is_valid_expression(expression2)}")  # False
