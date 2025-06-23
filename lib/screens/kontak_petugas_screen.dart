import 'package:flutter/material.dart';

class KontakPetugasScreen extends StatelessWidget {
  const KontakPetugasScreen({super.key});

  // Dummy data petugas
  final List<Map<String, String>> petugas = const [
    {
      'nama': 'ustadz willi',
      'telepon': '+628135577799',
      'email': 'kingwillikece@travelhaji.com',
      'foto': 'assets/ustadz_willi.jpg'
    },
    {
      'nama': 'Ustadzah anisa',
      'telepon': '+628987654321',
      'email': 'siti@travelhaji.com',
      'foto': 'https://via.placeholder.com/150',
    },
    {
      'nama': 'Ustadz Ghufron',
      'telepon': '+628123456789',
      'email': 'ghufron@travelhaji.com',
      'foto': 'https://via.placeholder.com/150',
    },
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Kontak Petugas',
          style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
        ),
        backgroundColor: const Color(0xFF0083B0),
        centerTitle: true,
        elevation: 0,
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
          itemCount: petugas.length,
          itemBuilder: (context, index) {
            final p = petugas[index];
            return Card(
              elevation: 4,
              margin: const EdgeInsets.only(bottom: 20),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(16),
              ),
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Row(
                  children: [
                    CircleAvatar(
                      radius: 32,
                      backgroundImage: NetworkImage(p['foto']!),
                    ),
                    const SizedBox(width: 16),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            p['nama']!,
                            style: const TextStyle(
                              fontSize: 18,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          const SizedBox(height: 4),
                          Row(
                            children: [
                              const Icon(
                                Icons.phone,
                                size: 16,
                                color: Color(0xFF0083B0),
                              ),
                              const SizedBox(width: 6),
                              Text(p['telepon']!),
                            ],
                          ),
                          const SizedBox(height: 4),
                          Row(
                            children: [
                              const Icon(
                                Icons.email,
                                size: 16,
                                color: Color(0xFF0083B0),
                              ),
                              const SizedBox(width: 6),
                              Flexible(
                                child: Text(
                                  p['email']!,
                                  overflow: TextOverflow.ellipsis,
                                ),
                              ),
                            ],
                          ),
                        ],
                      ),
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
