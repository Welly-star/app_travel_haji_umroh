import 'package:flutter/material.dart';
import 'screens/landing_page.dart';


void main() {
  runApp(const TravelerApp());
}

class TravelerApp extends StatelessWidget {
  const TravelerApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Traveler Haji & Umrah',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primaryColor: const Color(0xFF00B894),
        scaffoldBackgroundColor: const Color(0xFFE8F5E9),
        colorScheme: ColorScheme.fromSwatch(
          primarySwatch: Colors.green,
          accentColor: const Color(0xFF006A60),
        ),
        textTheme: const TextTheme(
          bodyMedium: TextStyle(color: Color(0xFF1B1B1B), fontSize: 16),
          titleLarge: TextStyle(
            color: Color(0xFF1B1B1B),
            fontWeight: FontWeight.bold,
            fontSize: 28,
          ),
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            backgroundColor: const Color(0xFF00B894),
            foregroundColor: Colors.white,
            padding: const EdgeInsets.symmetric(horizontal: 40, vertical: 16),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(30),
            ),
          ),
        ),
      ),
      home: const LandingPage(),
    );
  }
}
