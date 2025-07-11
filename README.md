# Virgil - Discord Bot per GDR Cyberpunk Carbon 2185

## Descrizione
Virgil è un bot Discord scritto in Python con discord.py, progettato per supportare il server di gioco di ruolo ambientato in Carbon 2185.

## Funzionalità base
- Comando slash `/ping` per testare la risposta del bot

## Setup e Deploy

1. Clona questo repository.
2. Crea un file `.env` con le variabili:
   ```
   DISCORD_TOKEN=tuo-token-bot
   GUILD_ID=id-del-server
   ```
3. Installa dipendenze:
   ```
   pip install -r requirements.txt
   ```
4. Avvia il bot localmente:
   ```
   python src/bot.py
   ```
5. Per il deploy su Render:
   - Crea un Web Service su Render collegando questo repo
   - Imposta Runtime: Python 3
   - Build command: `pip install -r requirements.txt`
   - Start command: `python src/bot.py`
   - Aggiungi variabili d'ambiente `DISCORD_TOKEN` e `GUILD_ID`

## Licenza
MIT
