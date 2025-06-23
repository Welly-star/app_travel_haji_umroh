import 'package:flutter/material.dart';
import 'formulir_pendaftaran_screen.dart';
import 'panduan_ibadah_screen.dart';
import 'jadwal_penerbangan_screen.dart';
import 'kontak_petugas_screen.dart'; 
import 'lokasi_penting_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Beranda',
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
        child: ListView(
          padding: const EdgeInsets.all(20),
          children: [
            _buildCard(
              title: 'Pendaftaran Jamaah',
              icon: Icons.assignment_rounded,
              subtitle: 'Daftarkan diri Anda untuk Haji & Umrah',
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => const FormulirPendaftaranScreen(),
                  ),
                );
              },
            ),
            _buildCard(
              title: 'Jadwal Keberangkatan',
              icon: Icons.calendar_today,
              subtitle: 'Lihat informasi jadwal Haji & Umrah terdekat',
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => const JadwalPenerbanganScreen(),
                  ),
                );
              },
            ),
            _buildCard(
              title: 'Panduan Ibadah',
              icon: Icons.menu_book_rounded,
              subtitle: 'Panduan lengkap Haji & Umrah sesuai sunnah',
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => const PanduanIbadahScreen(),
                  ),
                );
              },
            ),
            _buildCard(
              title: 'Lokasi Penting',
              icon: Icons.location_on_rounded,
              subtitle: 'Masjid, hotel, tempat ziarah & lainnya',
              onTap: () {
                // Nanti ganti ke LokasiPentingScreen()
                Navigator.push(
                   context,
                   MaterialPageRoute(
                     builder: (_) => const LokasiPentingScreen(),
                   ),
                 );
              },
            ),
            _buildCard(
              title: 'Kontak Petugas',
              icon: Icons.support_agent,
              subtitle: 'Hubungi pembimbing atau travel agent',
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => const KontakPetugasScreen(),
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildCard({
    required String title,
    required String subtitle,
    required IconData icon,
    required VoidCallback onTap,
  }) {
    return Card(
      elevation: 4,
      margin: const EdgeInsets.only(bottom: 20),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: ListTile(
        contentPadding: const EdgeInsets.all(16),
        leading: Icon(icon, color: const Color(0xFF0083B0), size: 36),
        title: Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
        subtitle: Text(subtitle),
        trailing: const Icon(Icons.arrow_forward_ios_rounded, size: 16),
        onTap: onTap,
      ),
    );
  }
}
