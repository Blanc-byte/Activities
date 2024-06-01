import 'dart:convert';
import 'package:http/http.dart' as http;

void main() async {
  final response = await http.get(Uri.parse('https://api.thecatapi.com/v1/breeds'));

  if (response.statusCode == 200) {
    final jsonData = jsonDecode(response.body);
    for (var breed in jsonData) {
      print('Breed: ${breed['name']}');
    }
  } else {
    print('Failed to load breeds');
  }
}