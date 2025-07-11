# 🤖 Virgil – Discord Bot per GDR Cyberpunk

Virgil è un bot Discord progettato per campagne di gioco di ruolo ambientate in mondi **cyberpunk** e in particolare per il sistema **Carbon 2185**, una reinterpretazione futuristica del regolamento D&D 5E.

Il bot funge da **assistente virtuale** per sessioni fluide e immersive, fornendo strumenti automatizzati per master e giocatori.

---

## ✨ Funzionalità principali

- 🎲 **Tiri di dado personalizzati** (compatibili con D&D 5E)
- 🧾 **Gestione schede personaggio** (semplificata)
- 📋 **Tracciamento missioni e obiettivi**
- ⚔️ **Sistema iniziativa e combattimento**
- 💉 **Supporto cyberware, modificatori e classi Carbon 2185**
- 💬 **Comandi slash intuitivi** con interfaccia moderna

---

## 🚧 Stato di sviluppo

| Stato       | Funzionalità                            | Descrizione                                                  |
|-------------|-----------------------------------------|--------------------------------------------------------------|
| ✅           | Comandi base                            | /aiuto, /tira, /ping                                          |
| ✅           | Tiri di dado 5E                         | Supporto a /tira 1d20+X                                      |
| 🟡           | Iniziativa                              | Inserimento e ordinamento turni                              |
| 🟡           | Gestione schede PG                      | Salvataggio e recupero dati                                 |
| 🟡           | Mission tracker                         | Tracciamento obiettivi e quest                              |
| 🔲           | Moduli cyberware e classi Carbon 2185   | Modificatori automatici                                      |
| 🔲           | Integrazione AI (facoltativa)           | Prompt narrativi, nomi, ambientazioni                       |

---

## 🚀 Deploy

Puoi ospitare il bot su una delle seguenti piattaforme:

### Render.com _(consigliato)_
- ✅ Deploy continuo da GitHub
- ✅ Piano gratuito con 550 ore/mese
- 🌐 [https://render.com](https://render.com)

### Railway.app
- ✅ Interfaccia moderna, hosting e DB integrati
- 🌐 [https://railway.app](https://railway.app)

### Replit + UptimeRobot _(trucco gratuito)_
- ✅ Hosting sempre attivo con workaround
- 🌐 [https://replit.com](https://replit.com)

### VPS (Hetzner, Contabo, etc.)
- ✅ Pieno controllo e autonomia
- ❌ Richiede gestione manuale

---

## 🛠️ Setup locale

```bash
# Clona il repository
git clone https://github.com/tuo-utente/VirgilBot.git
cd VirgilBot

# Installa le dipendenze (Node.js)
npm install

# Crea un file .env con il tuo token Discord
cp .env.example .env

# Avvia il bot
node src/index.js
