import re

file_path = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens\home_screen.dart'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add Weather and Currency Info
weather_kurs_widget = '''
            // WEATHER & CURRENCY WIDGET
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20),
              child: Row(
                children: [
                  Expanded(
                    child: Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: theme.cardTheme.color,
                        borderRadius: BorderRadius.circular(20),
                        border: Border.all(color: theme.cardBorder),
                        boxShadow: [
                          BoxShadow(color: theme.cardShadow, blurRadius: 10, offset: const Offset(0, 4)),
                        ],
                      ),
                      child: Row(
                        children: [
                          Container(
                            padding: const EdgeInsets.all(10),
                            decoration: BoxDecoration(
                              color: const Color(0xFFFDE68A).withValues(alpha: 0.3),
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: const Icon(Icons.wb_sunny_rounded, color: Color(0xFFD97706), size: 24),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text('Makkah', style: GoogleFonts.plusJakartaSans(fontSize: 12, color: theme.textSecondary, fontWeight: FontWeight.w600)),
                                Text('38°C Cerah', style: GoogleFonts.plusJakartaSans(fontSize: 14, color: theme.textPrimary, fontWeight: FontWeight.bold)),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(width: 14),
                  Expanded(
                    child: Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: theme.cardTheme.color,
                        borderRadius: BorderRadius.circular(20),
                        border: Border.all(color: theme.cardBorder),
                        boxShadow: [
                          BoxShadow(color: theme.cardShadow, blurRadius: 10, offset: const Offset(0, 4)),
                        ],
                      ),
                      child: Row(
                        children: [
                          Container(
                            padding: const EdgeInsets.all(10),
                            decoration: BoxDecoration(
                              color: const Color(0xFF10B981).withValues(alpha: 0.15),
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: const Icon(Icons.currency_exchange_rounded, color: Color(0xFF059669), size: 24),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text('1 SAR', style: GoogleFonts.plusJakartaSans(fontSize: 12, color: theme.textSecondary, fontWeight: FontWeight.w600)),
                                Text('Rp 4.250', style: GoogleFonts.plusJakartaSans(fontSize: 14, color: theme.textPrimary, fontWeight: FontWeight.bold)),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),
'''

target = "const SizedBox(height: 14),\n                    _buildDepartureCountdownCard(context),\n                  ],\n                ),\n              ),\n            ),\n"
content = content.replace(target, target + weather_kurs_widget)

old_services = '''      {
        'title': 'Tasbih Digital',
        'subtitle': 'Dzikir Harian',
        'icon': Icons.fingerprint_rounded,
        'color': const Color(0xFFEA580C),
        'onTap': () => Navigator.push(
              context,
              MaterialPageRoute(builder: (_) => const DigitalTasbihScreen()),
            ),
      },
    ];'''
    
new_services = '''      {
        'title': 'Tasbih Digital',
        'subtitle': 'Dzikir Harian',
        'icon': Icons.fingerprint_rounded,
        'color': const Color(0xFFEA580C),
        'onTap': () => Navigator.push(
              context,
              MaterialPageRoute(builder: (_) => const DigitalTasbihScreen()),
            ),
      },
      {
        'title': 'Kalkulator',
        'subtitle': 'Kurs Riyal',
        'icon': Icons.calculate_rounded,
        'color': const Color(0xFF6366F1),
        'onTap': () => Navigator.push(
              context,
              MaterialPageRoute(builder: (_) => const KalkulatorKursScreen()),
            ),
      },
    ];'''
    
content = content.replace(old_services, new_services)
content = content.replace("import 'digital_tasbih_screen.dart';", "import 'digital_tasbih_screen.dart';\nimport 'kalkulator_kurs_screen.dart';")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
