class Stack {
  List<dynamic> _stack = [];

  void push(dynamic element) {
    _stack.add(element);
  }

  dynamic pop() {
    if (!isEmpty()) {
      return _stack.removeLast();
    } else {
      return null;
    }
  }

  bool isEmpty() {
    return _stack.isEmpty;
  }
}

void main() {
  Stack stack = Stack();

  // Pushing elements onto the stack
  stack.push(1);
  stack.push(2);
  stack.push(3);

  // Popping elements from the stack
  print(stack.pop()); // Output: 3
  print(stack.pop()); // Output: 2
  print(stack.pop()); // Output: 1

  // Checking if the stack is empty
  print(stack.isEmpty()); // Output: true
}