# Python Projects Collection

Eine Sammlung verschiedener Python-Projekte für Lernen, Experimentieren und praktische Anwendungen.

## 📁 Projektübersicht

### 🌐 Netzwerk & Kommunikation

#### **APIComm**
- **Beschreibung**: API-Kommunikationstools
- **Dateien**: `send.py`
- **Zweck**: Implementierung von API-Aufrufen und Datenübertragung

#### **PingVerarbeitung**
- **Beschreibung**: Web-basierte Ping-Monitoring-Anwendung
- **Technologie**: Flask Web-Framework
- **Features**: 
  - Dashboard für Netzwerk-Monitoring
  - Ping-Tests und Traceroute-Funktionalität
  - Benutzerregistrierung und -anmeldung
  - Log-Verwaltung und -Visualisierung
- **Hauptdateien**: `app.py`, `scripte/ping.py`, `scripte/tracert.py`

#### **portscanner**
- **Beschreibung**: Port-Scanner-Tool
- **Dateien**: `scanner.py`
- **Zweck**: Netzwerk-Port-Scanning und -Analyse

#### **opcua**
- **Beschreibung**: OPC UA Client/Server-Implementierung
- **Struktur**: Getrennte Client- und Server-Module
- **Technologie**: OPC UA-Protokoll für industrielle Kommunikation
- **Dateien**: `Client/main.py`, `Server/main.py`

### 🎮 Spiele & Algorithmen

#### **Chess**
- **Beschreibung**: Schach-Tutorial-Projekt
- **Struktur**: Tutorial-basiertes Lernen
- **Features**: Schachlogik und -visualisierung
- **Technologie**: Python mit Pygame (vermutlich)

#### **conwayFinder**
- **Beschreibung**: Conway's Game of Life Implementierung
- **Dateien**: `main.py`
- **Zweck**: Zelluläre Automaten-Simulation

### 🛠️ Utilities & Tools

#### **mmover**
- **Beschreibung**: Datei-/Maus-Movement-Tool
- **Dateien**: `main.py`
- **Zweck**: Automatisierung von Maus- oder Dateibewegungen

#### **NumberChecker**
- **Beschreibung**: Zahlenvalidierung und -überprüfung
- **Dateien**: `main.py`
- **Zweck**: Verschiedene Zahlenoperationen und -validierungen

#### **argparse**
- **Beschreibung**: Command-Line-Argument-Parsing
- **Dateien**: `read_input.py`, `test.py`
- **Zweck**: Beispiele für Kommandozeilen-Interface-Entwicklung

### 🎓 Grundlagen & Lernprojekte

#### **Baasics**
- **Beschreibung**: Python-Grundlagen und erste Projekte
- **Dateien**: 
  - `Ceasar.py` - Caesar-Verschlüsselung
  - `HelloWorld.py` - Erstes Python-Programm
  - `PrintSameLine.py` - Ausgabe-Formatierung
- **Zweck**: Lernprojekte für Python-Anfänger

## 🚀 Installation & Verwendung

### Voraussetzungen
- Python 3.7+
- pip (Python Package Manager)

### Projekt-spezifische Abhängigkeiten
Jedes Projekt mit einem `requirements.txt` kann wie folgt installiert werden:

```bash
cd [Projektname]
pip install -r requirements.txt
```

### Virtual Environments
Mehrere Projekte nutzen eigene Virtual Environments:
- `Chess/Tutorial/chess/`
- `conwayFinder/venvConwayFinder/`
- `mmover/mmover/`
- `opcua/opcua/` und `opcua/opcuaVENV/`
- `PingVerarbeitung/env/`

### Beispiel-Nutzung

#### PingVerarbeitung starten:
```bash
cd PingVerarbeitung
python app.py
```

#### OPC UA Server starten:
```bash
cd opcua/Server
python main.py
```

#### Port-Scanner ausführen:
```bash
cd portscanner
python scanner.py [Ziel-IP] [Port-Bereich]
```

## 📚 Lernressourcen

### Anfänger
- Starten Sie mit den Projekten im `Baasics/` Ordner
- `HelloWorld.py` für erste Schritte
- `argparse/` für Command-Line-Tools

### Fortgeschrittene
- `PingVerarbeitung/` für Web-Entwicklung mit Flask
- `opcua/` für industrielle Kommunikation
- `Chess/` für Spieleentwicklung

### Netzwerk-Programmierung
- `APIComm/` für API-Integration
- `portscanner/` für Netzwerk-Analyse
- `PingVerarbeitung/` für Monitoring-Tools

## 🔒 Sicherheitshinweise

- Alle sensiblen Daten (SQLite-Datenbanken, Logs, Konfigurationsdateien) sind über `.gitignore` ausgeschlossen
- Virtual Environments werden nicht versioniert
- Private Konfigurationsdateien und API-Keys sind geschützt

## 🤝 Beitragen

1. Fork das Repository
2. Erstelle einen Feature-Branch (`git checkout -b feature/AmazingFeature`)
3. Committe deine Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Push zum Branch (`git push origin feature/AmazingFeature`)
5. Öffne eine Pull Request

## 📝 Lizenz

Diese Sammlung dient Lern- und Demonstrationszwecken. Einzelne Projekte können unterschiedliche Lizenzen haben.

## 📧 Kontakt

Bei Fragen oder Anregungen, erstelle gerne ein Issue in diesem Repository.

---

**Letzte Aktualisierung**: Juni 2025
