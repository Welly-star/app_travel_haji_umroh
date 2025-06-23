import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class FormulirPendaftaranScreen extends StatefulWidget {
  const FormulirPendaftaranScreen({super.key});

  @override
  State<FormulirPendaftaranScreen> createState() =>
      _FormulirPendaftaranScreenState();
}

class _FormulirPendaftaranScreenState extends State<FormulirPendaftaranScreen> {
  final _nameController = TextEditingController();
  final _phoneController = TextEditingController();
  final _nikController = TextEditingController();
  final _kkController = TextEditingController();
  final _passportController = TextEditingController();
  String? _selectedPackage;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      backgroundColor: Colors.transparent,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        centerTitle: true,
        title: Text(
          'Formulir Pendaftaran',
          style: GoogleFonts.poppins(
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Color(0xFF6DD5FA), Color(0xFF2980B9)],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: SafeArea(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(24),
            child: Column(
              children: [
                const SizedBox(height: 16),
                // Logo elegan (ikon Ka'bah / Masjid)
                Container(
                  width: 80,
                  height: 80,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: Colors.white.withOpacity(0.2),
                    border: Border.all(color: Colors.white, width: 2),
                  ),
                  child: const Center(
                    child: Icon(
                      Icons.mosque, // Ganti ke Icons.account_balance jika perlu
                      color: Colors.white,
                      size: 40,
                    ),
                  ),
                ),
                const SizedBox(height: 16),
                Container(
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.15),
                    borderRadius: BorderRadius.circular(30),
                    border: Border.all(color: Colors.white.withOpacity(0.3)),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black26,
                        blurRadius: 12,
                        offset: Offset(0, 8),
                      ),
                    ],
                  ),
                  padding: const EdgeInsets.all(24),
                  child: Column(
                    children: [
                      _formTitle("Data Pribadi"),
                      const SizedBox(height: 16),
                      _buildInput(
                        _nameController,
                        'Nama Lengkap',
                        Icons.person,
                      ),
                      const SizedBox(height: 16),
                      _buildInput(
                        _phoneController,
                        'Nomor Telepon',
                        Icons.phone,
                        keyboardType: TextInputType.phone,
                      ),
                      const SizedBox(height: 16),
                      _buildInput(
                        _nikController,
                        'NIK (No. KTP)',
                        Icons.badge,
                        keyboardType: TextInputType.number,
                      ),
                      const SizedBox(height: 16),
                      _buildInput(
                        _kkController,
                        'No. Kartu Keluarga',
                        Icons.group,
                        keyboardType: TextInputType.number,
                      ),
                      const SizedBox(height: 16),
                      _buildInput(
                        _passportController,
                        'No. Paspor',
                        Icons.book,
                        keyboardType: TextInputType.text,
                      ),
                      const SizedBox(height: 16),
                      _formTitle("Paket Perjalanan"),
                      const SizedBox(height: 10),
                      DropdownButtonFormField<String>(
                        decoration: _dropdownStyle("Pilih Paket"),
                        value: _selectedPackage,
                        onChanged: (value) =>
                            setState(() => _selectedPackage = value),
                        items: const [
                          DropdownMenuItem(
                            value: 'Haji Reguler',
                            child: Text('Haji Reguler'),
                          ),
                          DropdownMenuItem(
                            value: 'Haji Plus',
                            child: Text('Haji Plus'),
                          ),
                          DropdownMenuItem(
                            value: 'Umrah',
                            child: Text('Umrah'),
                          ),
                        ],
                        dropdownColor: Colors.white,
                      ),
                      const SizedBox(height: 20),
                      _formTitle("Upload Dokumen"),
                      const SizedBox(height: 10),
                      _buildUploadField("Upload Foto KTP"),
                      const SizedBox(height: 10),
                      _buildUploadField("Upload Foto Paspor"),
                      const SizedBox(height: 30),
                      ElevatedButton(
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.white,
                          foregroundColor: const Color(0xFF2980B9),
                          padding: const EdgeInsets.symmetric(vertical: 16),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(16),
                          ),
                        ),
                        onPressed: () {
                          ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(
                              content: Text('Formulir berhasil dikirim'),
                            ),
                          );
                        },
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            const Icon(Icons.check_circle_outline),
                            const SizedBox(width: 10),
                            Text(
                              'Kirim Pendaftaran',
                              style: GoogleFonts.poppins(
                                fontSize: 16,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildInput(
    TextEditingController controller,
    String label,
    IconData icon, {
    TextInputType keyboardType = TextInputType.text,
  }) {
    return TextField(
      controller: controller,
      keyboardType: keyboardType,
      style: const TextStyle(color: Colors.white),
      decoration: InputDecoration(
        labelText: label,
        labelStyle: GoogleFonts.poppins(color: Colors.white),
        prefixIcon: Icon(icon, color: Colors.white),
        filled: true,
        fillColor: Colors.white.withOpacity(0.1),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
          borderSide: const BorderSide(color: Colors.white),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
          borderSide: const BorderSide(color: Colors.white, width: 2),
        ),
      ),
    );
  }

  InputDecoration _dropdownStyle(String label) {
    return InputDecoration(
      labelText: label,
      labelStyle: GoogleFonts.poppins(color: Colors.white),
      prefixIcon: const Icon(Icons.card_travel, color: Colors.white),
      filled: true,
      fillColor: Colors.white.withOpacity(0.1),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(14),
        borderSide: const BorderSide(color: Colors.white),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(14),
        borderSide: const BorderSide(color: Colors.white, width: 2),
      ),
    );
  }

  Widget _formTitle(String title) {
    return Text(
      title,
      style: GoogleFonts.poppins(
        color: Colors.white,
        fontWeight: FontWeight.bold,
        fontSize: 18,
      ),
    );
  }

  Widget _buildUploadField(String label) {
    return InkWell(
      onTap: () {
        ScaffoldMessenger.of(
          context,
        ).showSnackBar(SnackBar(content: Text('$label dipilih')));
      },
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 14, horizontal: 16),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(14),
          border: Border.all(color: Colors.white),
          color: Colors.white.withOpacity(0.1),
        ),
        child: Row(
          children: [
            const Icon(Icons.upload_file, color: Colors.white),
            const SizedBox(width: 12),
            Text(label, style: GoogleFonts.poppins(color: Colors.white)),
            const Spacer(),
            const Icon(Icons.arrow_forward_ios, size: 14, color: Colors.white),
          ],
        ),
      ),
    );
  }
}
