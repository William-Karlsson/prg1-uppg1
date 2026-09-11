
# Tärningsspelet

Välkommen till Tärningsspelet! :D

Denna enkla Python app har två primära lägen:
- Single player
- Online

Online tillåter ett i teorin oändligt antal spelare att spela tillsammans, medans singleplayer fungerar fint att spela ensam!

Appen var skapad för Python 3.13.15. För att starta appen, kör main.py. 

Här är en (ej komplett) lista på ett par implementerade funktioner:
- Online multiplayer baserat på REST endpoints. Dock inget skydd mot fusk alls.
- Möjlighet att både starta en egen server och ansluta till en befintlig server
- Användarnamn som fungerar för Online-funktionen
- En "slogan" funktion som låter vinnaren av en Online-match hälsa någonting till de andra. 
- Ett pengarsystem(MONEY™) som begränsar hur mycket en spelare kan satsa i en Online-match. 
- Pengar sparas lokalt och påverkas av resultatet i singleplayer och Online
- En lokal spelarprofil där Användarnamn, slogan, mängd MONEY™, vunna spel, förlorade spel, och totalt antal spel kan visas.
- Singleplayer-läge där spelaren spelar mot ett mål på 21 genom att kasta en D6
    - Vinst vid exakt 21 och förlust baserat på avstånd från 21
    - Möjlighet för flera singleplayer matcher direkt efter varandra.
- Ett huvudmenysystem för att navigera mellan spelets olika funktioner 
- En seperat meny for Online-läget och dess funktioner.
- Spelardata sparas i användarens AppData-mapp så att informationen finns kvar mellan programstarter
- Möjlighet att radera sperad spelar-data och skapa om spelarprofilen
- Hantering av ogiltiga menyalternativ 
- Färgkodad text i konsolen via ANSI escape codes
- Automatisk anslutningskontroll när en spelare försöker ansluta till en Online-server
    - Flera anslutningsförsök om den råkar misslyckas de första par gångerna
- Hantering av grundläggande fel i flera delar av programmet så att programmet återgår till menyer istället för att gå sönder om någonting går fel. Dock inte perfekt, finns förmodligen många edge-cases som jag inte haft tid att hantera (det är lite invecklat att skriva en hel online-server för en så låten skoluppgift)
- Online-servern håller koll på flera saker, bland annat alla användare som är uppkopplade till den.
- I online-läget deltar flera spelare samtidigt och den som tar sig närmast 21 vinner hela potten. Resultatet slumpas om två användare råkar få samma resultat. 

# Buggar

Det finns förmodligen buggar och edge-cases i serverkoden. Det kändes lite onödigt att spendera absurt många fler timmar på den här uppgiften, så jag blev lite lat med min errorhantering. För normal användning bör det till störst del fungera som jag vill att den ska, men du bör inte anta att jag skrivit en perfekt server för denna uppgift.