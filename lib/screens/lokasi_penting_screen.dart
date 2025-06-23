import 'package:flutter/material.dart';

class LokasiPentingScreen extends StatelessWidget {
  const LokasiPentingScreen({super.key});

  final List<Map<String, String>> lokasiList = const [
    {'nama': 'Masjidil Haram', 'alamat': 'Makkah, Arab Saudi'},
    {'nama': 'Masjid Nabawi', 'alamat': 'Madinah, Arab Saudi'},
    {'nama': 'Jabal Rahmah', 'alamat': 'Arafah, Makkah'},
    {'nama': 'Hotel Zamzam', 'alamat': 'Makkah, Arab Saudi'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Lokasi Penting',
          style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
        ),
        backgroundColor: const Color(0xFF0083B0),
        centerTitle: true,
      ),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Color(0xFFE8F5E9), Color(0xFFB2DFDB)],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: ListView.builder(
          padding: const EdgeInsets.all(20),
          itemCount: lokasiList.length,
          itemBuilder: (context, index) {
            final lokasi = lokasiList[index];
            return Card(
              elevation: 4,
              margin: const EdgeInsets.only(bottom: 20),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(16),
              ),
              child: ListTile(
                contentPadding: const EdgeInsets.all(16),
                leading: const Icon(
                  Icons.location_on_rounded,
                  color: Color(0xFF0083B0),
                  size: 36,
                ),
                title: Text(
                  lokasi['nama']!,
                  style: const TextStyle(fontWeight: FontWeight.bold),
                ),
                subtitle: Text(lokasi['alamat']!),
              ),
            );
          },
        ),
      ),
    );
  }
}
