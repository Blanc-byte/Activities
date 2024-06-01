import 'package:flutter/material.dart';
import 'package:todolistapp/todo_list_screen.dart'; // Assuming TodoListScreen is in a separate file

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'To-Do List App',
      home: TodoListScreen(),
    );
  }
}
