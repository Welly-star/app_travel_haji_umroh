import 'package:flutter/material.dart';

class JadwalPenerbanganScreen extends StatelessWidget {
  const JadwalPenerbanganScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final List<Map<String, String>> jadwal = [
      {
        'tanggal': '20 Juni 2025',
        'maskapai': 'Garuda Indonesia',
        'jam': '08:00 WIB',
        'rute': 'Jakarta (CGK) → Madinah (MED)',
      },
      {
        'tanggal': '22 Juni 2025',
        'maskapai': 'Saudia Airlines',
        'jam': '13:45 WIB',
        'rute': 'Surabaya (SUB) → Jeddah (JED)',
      },
      {
        'tanggal': '25 Juni 2025',
        'maskapai': 'Lion Air Charter',
        'jam': '05:30 WIB',
        'rute': 'Bandung (BDO) → Madinah (MED)',
      },
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Jadwal Keberangkatan',
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
          itemCount: jadwal.length,
          itemBuilder: (context, index) {
            final item = jadwal[index];
            return Card(
              elevation: 4,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(16),
              ),
              margin: const EdgeInsets.only(bottom: 20),
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      item['tanggal']!,
                      style: const TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                        color: Color(0xFF0083B0),
                      ),
                    ),
                    const SizedBox(height: 8),
                    Row(
                      children: [
                        const Icon(Icons.flight, color: Color(0xFF0083B0)),
                        const SizedBox(width: 8),
                        Text(
                          item['maskapai']!,
                          style: const TextStyle(fontSize: 16),
                        ),
                      ],
                    ),
                    const SizedBox(height: 8),
                    Row(
                      children: [
                        const Icon(Icons.schedule, color: Colors.grey),
                        const SizedBox(width: 8),
                        Text(
                          item['jam']!,
                          style: const TextStyle(fontSize: 16),
                        ),
                      ],
                    ),
                    const SizedBox(height: 8),
                    Row(
                      children: [
                        const Icon(Icons.place, color: Colors.redAccent),
                        const SizedBox(width: 8),
                        Text(
                          item['rute']!,
                          style: const TextStyle(fontSize: 16),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            );
          },
        ),
      ),
    );
  }
}
