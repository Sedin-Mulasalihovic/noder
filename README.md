# 📝 Noder

**Noder** ist eine einfache, terminalbasierte Notiz-App, geschrieben in **Python**.  
Sie läuft direkt im Terminal (z. B. Kali Linux) und bietet grundlegende Funktionen zum Erstellen, Anzeigen, Durchsuchen und Löschen von Notizen – inklusive Passwortschutz.

---

## 🚀 Features

- 🔐 Passwortgeschützter Zugriff
- 🕒 Zeitstempel für jede Notiz
- 📝 Notizen erstellen
- 🗑️ Notizen löschen
- 🔍 Notizen durchsuchen (Suchfunktion)
- 📜 Verlauf anzeigen
- 🧹 Automatisches Leeren des Terminals
- ⏳ Ladeanimationen
- 📊 Statusleiste (Anzahl Notizen & Uhrzeit)
- 🎨 ASCII-Logo & simples Terminal-Design

---

## 📦 Voraussetzungen

- Python **3.8 oder höher**
- Linux / macOS / WSL  
  (getestet unter **Kali Linux**)

Benötigte Module (Standardbibliothek):
- `datetime`
- `os`
- `time`
- `getpass`
- `hashlib`

➡️ **Keine externen Libraries nötig**

---

## ⚙️ Installation

```bash
git clone https://github.com/dein-name/noder.git
cd noder
python3 notizen.py
