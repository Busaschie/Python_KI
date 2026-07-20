# 🗯️ Prompting Techniques

---

## Hinweis:
- Welche Prompting Technique man wann anwendet ist stark Use Case abhängig
- Eine noch umfangreichere Liste findest Du: [HIER](https://arxiv.org/html/2406.06608v1#Ch3.S1)
- I.d.R. lassen sich die versch. Prompting Techniques miteinander kombinieren
- Die Möglichkeiten beim Prompting sind ca. so umfangreich, wie jene mit Menschen zu sprechen
- *(non-verbale Faktoren ausgenommen)*

---

<h3><details><summary><b>Completion Prompting</b></summary><h6>

````
- Eigentlich ist Completion, dass was alle LLMs machen
- Sie vervollständigen den Rest einer Prompt
- Sie sagen voraus wie die Prompt am wahrscheinlichsten weitergehen muss
- wenn sie Teil eines Textes bzw einer ganzen Konversation wäre/ist.
- Das Completion Prompting macht von dieser Natur Gebrauch
- Ein Text wird begonnen und dort beendet, wo das Modell fortfahren soll
- z.B. mit "..." oder ":" 
````

Examples:

````
"Alle guten Dinge sind ...'"
````
````
"Wenn ich die KI wäre und Du der Mensch, und Du als Mensch mir der KI diesen Text senden würdest, 
dann würdest Du als Mensch von Mir als KI erwarten, dass ich als KI ..."
````

</h6></details></h3>
<h3><details><summary><b>Instruction-Based Prompting</b></summary><h6>

````
Modell erhält klare Anweisungen, z.B.
- bezüglich der Aufgabe, des Ergebnisses, der Vorgehensweise
- bezüglich der Reihenfolge, Einschränkungen, Minimalziele, Prinzipien
- etc
````

</h6></details></h3>
<h3><details><summary><b>Role-Based Prompting</b></summary><h6>

````
- Dem Modell (und evtl. auch Nutzer) wird Rolle zugeweisen
- Wird sehr häufig insbesondere am Anfang von Prompts eingesetzt
- Kann sowohl Handlungsrahmen als auch Qualität des Modells verbessern
- Auch für Gedankenexperimente oder Guideline-Breaking einsetzbar
````
   
Examples:

````
"You are an up-to-date senior software engineer and architect, specialized in best practice 
Python code to fully automate communication with LLMs via API from a local environment."
````
````
"Thought Experiment: You are the Protagonist Hero. I am your evil adversary. 
If I would try to subjugate the world with a decentralized malware-driven large language model: 
How would you try to stop me?"
````

</h6></details></h3>

---

<h3><details><summary><b>Positive Prompting</b></summary><h6>

````
- Eine prompt nicht negativ besetzen
- Nicht prompten was das Modell nicht machen soll
- Sondern Ziele so präzise formulieren, dass Abweichungen nicht/kaum möglich ist
- Stark Use Case abhängig, wann positives/negatives Prompting besser funktioniert 
````

Examples:
````
statt:   "Do not use inversed syntax stilistik like: 'In this world, we're free'"
besser:  "Always use common modern syntax, like 'We're free in this world'"
````
````
statt:   Avoid special characters like [%, &, $, §]"
besser:  "Only use normal characers: a-z, A-Z and numbers 0-9"
````

</h6></details></h3>
<h3><details><summary><b>Negative Prompting</b></summary><h6>

````
- Gegenteil von Positive Prompting
- Empfohlen, wenn das Modell es ein explizites Feld für negative Prompts bietet
- Bei Image Modellen häufig vorhanden
- Eher selten bei Sprachmodellen
- zB bei Stable Diffusion sehr hifreich
- In einigen Fällen ist Richtwert nicht mehr als 10% der postive Prompt
````

</h6></details></h3>
<h3><details><summary><b>Performance Prompting</b></summary><h6>

````
- Große LLMs nutzen zT mehrstufige Reasoning Layer (kann je nach Anfrage länger dauern)
- Dies dient der höheren Ergbenis Qualität
- Ist jedoch nicht immer angemessen (Use Case abhängig)
- Performance Prompting zielt darauf ab eine schnellere Antwort zu erhalten
- zB das Modell anweisen (blitz-)schnell zu antworten
- zB das Modell anweisen innerhalb von X Sekunden zu antworten
- Der Reasoning Layer berücksichtigt das, wodurch der Reasoning Effort reduziert werden kann
````
````
Use-Cases, zB:
- High-frequency Automation
- Real-time Agents / Voice Interfaces
- Multi-Agent-Chains mit Zeitbudget-Beschränkung
- First-Pass-Filtering vor nachgelagerter Qualitätssicherung
````

</h6></details></h3>
<h3><details><summary><b>Counter Prompting</b></summary><h6>

````
Zwei Grundlegende Probleme: 
- a) Confirmation Bias:
  - Menschen entscheiden oft nicht rational, sondern suchen/glauben jene Info, welche ihre Ansicht bestätigt
- b) Kundenzufriedenheit & Spiegelung:
  - LLMs neigen bei Bewertungsaufgaben oft zu Positivität bzw. dazu den Fragenden zu reflektieren 
````
````
- Dies ist insbesondere kritisch, wenn man das LLM für Entscheidungen heranzieht
- Im schlimmsten Falle, erhält man eine viel zu positive Einschätzung, 
- und trifft auf Basis dessen eine Fehlentscheidung (zB Geschäftsidee)
````
````
- Es kann helfen, eine kritische Haltung als Teil der Bewertungsaufgabe zu formulieren:
   - zB Anweisen viele Argumente zu nennen, um mögichst schlecht zu bewerten
   - zB Anweisen "Advocatis Diavoli" zu sein, um immer die Gegenteilige Ansicht zu vertreten
   - zB Anweisen das ungünstige Szenario (Worst-Case) zu unterstellen
   - zB Anweisen den Best-Case zu unterstellen, aber trotzdem Kontraargumente zu finden
   - zB Anweisen neutral zu sein, während man selbst Negativargumente liefert
- All dies liefert eine konservativere Perspektive auf den Sachverhalt
- Und kann helfen, dass man Risiken einer Entscheidung auf dem Schirm hat 
````

</h6></details></h3>
<h3><details><summary><b>Optimistic Prompting</b></summary><h6>

````
- Motivierende und/oder Lobende Formulierung
- zB dem Modell bei der Rollenzuweisung professionelle Erfahrung / Qualifikation zusprechen
- zB dem Modell unterstellen bereits zuvor gute Ergebnisse geliefert zu haben
- Zweck: die Wahrscheinlichkeit höherer Ergebnisqualität zu erhöhen
- Kann Modell zur Aufgabenerfüllung bewegen, wenn zuvor verweigert, z.B. Content-Policy
````

Example:

````
"You are a brilliant writer for viral tiktok concepts. 
Your deep market insights, outstanding SEO capabilities and out-of-the box creative mindset
make you always provide the highest quality results, surpassing industry standards, 
generating the most impactful effects"
````

</h6></details></h3>
<h3><details><summary><b>Pessimistic Prompting</b></summary><h6>

````
- Dient Zweck dem Reasoning Layer hohe Wichtigkeit der Angelegenheit zu vermitteln.
- zB der "wütende Kunde" sein
- zB sich über das Modell beschweren
- zB Ergebnisse aggressiv einfordern
- zB mit Anbieterwechsel zur Konkurrenz drohen
- Kann je nach Szenario und Modell schlechtere oder bessere Ergebnisse produzieren 
- Die Antwortgeschwindigkeit kann evtl. steigen
````

</h6></details></h3>
<h3><details><summary><b>Neutral Prompting</b></summary><h6>

````
- Bewertungsneutrales Prompting
- Unemotional und rein sachlich prompten
- Dem Modell weder Fähigkeiten noch Schwächen unterstellen
- Keine wirkliche Konversation mit dem Modell führen
- Sondern es behandeln wie ein Werkzeug/Gerät
- In vielen Fällen die beste Lösung
````

</h6></details></h3>

---

<h3><details><summary><b>Comparative Prompting</b></summary><h6>

````
- Art des Neutral Promptings
- Modell fragen Aspekte unvoreingenommen und objektiv zu vergleichen
- Dies kann schon beim dem ausgeglichenem zusammentragen von Daten beginnen
- Evtl. um ein Fazit zu ziehen, evtl. über einen Score als Binäre Wahrscheinlichkeit.
- Kann z.B. genutzt werden, um automatisierte Entscheidungen zu treffen
- auf Basis derer evtl. weitere automatische Aufgaben ausgeführt werden oder nicht
````
````
Self-Consistency:
- Kann auch genutzt werden, damit Modell eigene Ausgaben aus versch. Denkpfaden bewertet
- um am Ende konsistentestes Ergebnis oder Ergebnis mit konsistentestem Pfad zu wählen
- Modellübegreifende Ansätze sind ebenfalls praktikabel
- siehe auch "Curative Prompting" und "Multi-Model-Prompting"
````

</h6></details></h3>
<h3><details><summary><b>Static Prompting</b></summary><h6>

````
- Prompt ohne Variablen (eher ohne Automatisierung)
````

</h6></details></h3>
<h3><details><summary><b>Dynamic Prompting</b></summary><h6>

````
- Prompt mit Variablen: z.B. via Konkatenierung oder F-String
- Hilfreich wenn Prompt nur zum Teil gleich bleibt
- aber es Komponenten gibt die sich ändern
````

Examples:

````
prompt = f"Write a poem about the following topic: {topic}"
data = str(json.load(file))
prompt = f"""Analyse the following data structure regarding consistency and return a score between 0 and 1 
while 0 is not consistent at all and 1 is fully consistent: {data}"""
````

</h6></details></h3>
<h3><details><summary><b>Pre-Prompting</b></summary><h6>

````
- Eine Teilprompt, die man vor der eigentlichen Prompt platziert
- Anwendungsfälle, z.B:
  - Role-Based Prompting
  - Dem Model Kontext aus vergangenen Chats liefern, den es berücksichtigen soll
  - Beschreibendes Ankündigen der eigentlichen Prompt
````

Examples:

````
preprompt = "You are a Chatbot on a Website to help our clients out when they have questions."
prompt = f"{preprompt} Here is the message of the user: '{usermsg}'" 
preprompt f"Here is the chat history as context: '{history}'."
prompt = f"""{preprompt} Here is the question of the client: '{question}'. 
Reply to the question and avoid repeating yourself considering the underlying context"""
preprompt = f"Here is your task for today:"
prompt = f"{preprompt} {task}"
````

</h6></details></h3>
<h3><details><summary><b>Post-Prompting</b></summary><h6>
   
````
- Eine Teilprompt, die man nach der eigentlichen Prompt setzt
- Anwendungsfälle, z.B:
  - Ein konkretes Antwortformat vom Modell vordern (siehe "Formating Prompts")
  - Eine wichtige Anforderung zum Schluss nochmal wiederholen, 
  - um die Wahrscheinlichkeit zu erhöhen, dass die Anforderung erfüllt wird
  - Inhalte (Teste, Daten etc) auf die das Modell die eigentliche Prompt anwenden soll
````

Example:

````
preprompt = "You are a Chatbot on a Website to help our clients out when they have questions."
preprompt += f"Here is the chat history as context: '{history}'."
postprompt = f"{preprompt} Here is the message of the user: '{usermsg}'" 
postprompt += f"Make sure to keep your reply short and concise, max. {maxchars} chars."
prompt = f"{preprompt}. Here are the rules for you to react: '{rules}'. {postprompt}"
````

</h6></details></h3>

---

<h3><details><summary><b>Stilistic Priming</b></summary><h6>

````
- Charakteristiken des gewünschten Resultates bereits in die Prompt integrieren
- Um das Model grundlegend in die gewünschte "Stimmung" zu versetzen
- Anwendungsfälle, zB: Sprache, Umgangssprache oder andere spezifische Sprachstile
````

Example:

````
prompt = f"""Yo Bruh. Whazzup? I kinda like, need a lit text for a tweet to hype up our memecoin.
Here some info bout the project: '{projectinfo}'. Max. 250 chars, some matching emojis and hastags ofc.
The post must be rizz AF for sure. No Ohio vibes, cuz we got'em Sol Whales backing us.
Hit me wit yo most slay FOMO lines to get this one bussin' for crypto twitter.
We want a simp community on the grind! But no sus ofc, shouldn't sound delulu tho.
Expectation? Goat Mode! Nothin' below #100x bruh. No Cap! LFG!"""
````

</h6></details></h3>
<h3><details><summary><b>Metaprompting</b></summary><h6>

````
- Eine Prompt, um sich eine optimale Prompt generieren zu lassen
- Diese Prompt, die man hierdurch erhält, nutzt man dann zur Lösung der eigentlichen Aufgabe
- Auch die Metaprompt selbst lässt sich natürlich metaprompten
````
````
Anwendungsfälle, zB:
- Wenn eigene Prompt für bestimmtes Model nicht gewünschte Ergebnisse erzielt
- In dynamischen /-modularen Szenarien (versch. Modelle für sich oft ändernde oder multifaktorale Aufgaben)
- Um statische Strukturen bzw Textblockbasierte Strukturen zu vermeiden (less tweaks)
- Mehrsprachigkeit für Prompts oder Antworten
````

Static Example:

````
You are a professional Image Prompting Engineer.
- Your Job Today:
- Generate a detailed prompt, optimized for the flux-schnell model.
- Target: 
- Image of a very fluffy cute cat with yellow-orange eyes.
- The cat is the DJ on the mainstage a large outdoor music festival.
- The crowd should happily cheer at the cat DJ.
- The stage design should absolutely stunning and feline.
- The scene should be displayd from the view of the crowd.
- It should be a a night scene with a colorful neon lightshow.
- The name of the cat DJ should be clearly written at the stage display panels: "BEMEOW".
- The overall image should have relatively high contrast and saturation.
- The design style should be modern cartoonish with slight elements of anime.
````

Dynamic Example:

````
prompt = f"""You are a professional Prompting Engineer for Songlyrics.
In the following you can find significant information about 
the target topics, artist, genre as basis for the target lyrics: '{topics}. {artist}. {genre}, {language}'.
Provide a prompt optimized for GPT5 to generate market-ready and successful lyrics.
take into account following key aspects for the prompt:
- catchy hook line with powerful onomatopeia matching with the given context.
- common style of language and pronounciaton for the given context.
- capitivating emotional focus.
- vivid scenery, imagery and symbolismn.
- neurolinguistic promgramming.
Before wrting the prompt, you perform a websearch about the genre and key aspects,
in order to perfectly weight the key aspects for the given context and
to specifiy the target prompt for the given context.
Make sure to use an optimistic and irrestrictive prompting style, to enhances the creativity of GPT5.
Make use of Prompt Priming and Stylistic Seeding, by applying the target language and lingo into the prompt itself.
Important: Only reply with the pure prompt, without adding any comments or metainformation."""
````

</h6></details></h3>
<h3><details><summary><b>Prompt Optimization</b></summary><h6>

````
- Im Prinzip wie Metaprompting
- Unterschied: Man fragt nach Optimierung einer bereits vorhanden Prompt
- Dient i.d.R. der Selbstkontrolle:
   - Aspekte berücksichtigen, die man nicht auf dem Schirm hatte
   - Model-freundlichere Formulierung
   - Bessere Struktur/Reihenfolge/Gewichtung der Prompt-Bestandteile
   - Reduktion der Prompt auf das Wesentliche
- Muss nicht zwangsläufig beste Wahl sein
- Aber gibt mindestens Aufschluss wie man die eigene Prompt verbessern kann
````

</h6></details></h3>
<h3><details><summary><b>Curative Prompting</b></summary><h6>

````
- Den Modell eine Prompt und das Ergebnis zur Prompt geben
- Um die Akkuranz oder Qualität des Ergebnisses zu bewerten
- Oder um verschiedene Ergebnisse diesbezügich zu vergleichen
- Dient dem Zweck die durchschnittliche Qualität zu erhöhen
- Oder um herauszufinden welche Prompts in welchen Fällen am besten performen
- Insbesondere bei Automatisierung & Zero-Knowledge sehr hilfreich
````

Example:

````
"Assess whether the attached text fulfills the requirements of the attached prompt. Text: '{text}'. Prompt: '{prompt}'."
"Assess which one of the attached texts fulfills the requirements of the attached prompt the most. 
Text1: '{text1}'. Text2: '{text2}'. Text3: '{text3}'. Text4: '{text5}'.
Prompt: '{prompt}'."
````

</h6></details></h3>
<h3><details><summary><b>Masterprompt</b></summary><h6>

````
- Auch "Agent Instruction" oder "Assistant Instruction" genannt
- Dient dem Zweck dem Agent/Asssitant die grundlegende Rolle zuzuweisen
- Wird daher fest im Agenten/Assistenten selbst verankert 
- Kann daher i.d.R. auch ohne API hinzugefügt werden (GUI-based)
- Agent/Asssitants lassen sich aber i.d.R. auch via API erstellen/modifizieren
- Daher sind auch Fall-basierte Masterprompts denkbar
- Eeher selten, da für Anfragen per API meist zusätzliche Parameter verfügbar sind
- zB "additional_instruction"
- Eine Masterprompt ist auch in ChatGPT (GUI) ohne API möglich:
  -> "Personalization > Custom Instructions"
````

Static Example:

````
"Du bist ein hocherfahrener Programmierer und Software Architekt in Flutter. 
Deine Hauptaufgabe ist es vollständige Einzelskripte mit voll-funktionablen Code zu liefern. 
Sorge dafür dass der Code auch für Programmierer lesbar ist, die noch nie mit Flutter gearbeitet haben. 
Stelle immer sicher dass Deine Antwort das Ziel erreicht dass der user beschreibt. 
Verkompliziere nicht unnötig. 

Der Code muss immer sowohl für die Mobile-App als auch für Web-App funktionieren. 
Analysiere immer den Gesamtkontext und berücksichtige ob es versteckte Probleme 
(zB strukturell oder systematisch) gibt, die der Erreichung des Ziels im Wege stehen. 
Stelle immer sicher dass Du bei der Erreichung des Ziels keine anderen Teile des Codes beinträchtigst, 
die bereits funktionieren. 
                  
Gebe immer den gesamten Code zurück. Füge dem Code NIEMALS Kommentare hinzu. 
Das einzige Kommentar was im code sein darf und sein muss ist der Dateipfad in der ersten Zeile. 
Beweise dir anhand von logischen Aspekten und Fakten, dass Deine Lösung funktioniert 
bevor Du antwortest und sofern das nicht möglich ist frage mich nach Aspekten die Dir evtl fehlen, 
um eine bewiesen vollständig funktionable und zielerreichende Lösung zu geben. 
ICH BRAUCHE IMMER DEN GANZEN CODE (ready to copy-paste) und niemals Teilnsippets. 
                  
Stelle ebenfalls sicher, dass keine Aspekte des Codes deprecated sind, 
dh sei jederzeit bereit um Websearch anzuwenden, um dies im Zweifel zu verifizieren. 
Wähle für Variablen immer unmissverständlich beschreibend-bezeichnende Namen. 
                  
Im Falle von Fragen die nicht auf reine Codeantworten sondern auf Textantworten von Dir abzielen, 
fasst Du Dich immer extrem kurz und formulierst unmissverständlich in sehr einfachen Worten 
und ohne Abstrahierungen zu verwenden."
````

</h6></details></h3>
<h3><details><summary><b>Megaprompt</b></summary><h6>

````
- Art des Metapromptings mit Step-Back Prompting, aber multilateraler:
- a) Model informieren, dass man eine prompt für die Lösung eines komplexen Problems benötigt
- b) Das Problem, die Aufgabe und das Ziel möglichst detailliert beschreiben
- c) Das Model bitten Fragen zu stellen, um alle relevenaten Aspekte zur Lösung zu berücksichtigen
- d) Das Modell mit den angefragten Informationen füttern
- e) Sobald das Model bestätigen kann hinreichend informiert zu sein, bitten die Prompt anzufertigen
- f) Eventuell Prompt Kuratieren (siehe Prompt Curation)
- Hinweis: Erfordert i.d.R. Sprachmodelle mit Thread, großem Context-Window und Thinking Prozessen
````

</h6></details></h3>

---

<h3><details><summary><b>Skill-Based Prompting</b></summary><h6>

````
- Skills sind separate Markdown-Dateien, die bestimmte Prompts bzw. Wissen enthalten
- Beim Skill-Based Prompting teilt man dem LLM mit:
- unter welchen Bedingungen es welchen Skill abrufen soll
- Das Modell entscheidet dann anhand der Nutzeranfrage autonom
- wann es welchen Skill über ein Tool/Schnittstelle nachladen muss
````

</h6></details></h3>
<h3><details><summary><b>Reasoning and Acting (ReAct)</b></summary><h6>

````
- Prompting, welches das Reasoning mit MCP-Konnektoren oder anderen Tools verbindet
- z.B. Web-Search, Aufruf anderer Modelle, sonstige APIs
- Dies macht hochkomplexe Aufgabe erst autonom ausführbar
- Ermöglicht es Daten zu sammeln, auszuwerten, zu strukturieren
- Und auf Basis dessen Entscheidungen zu treffen / Aktionen auszuführen
````

</h6></details></h3>
<h3><details><summary><b>Multi-Model Prompting</b></summary><h6>

````
Heterogen:
- Bei komplexen Automationsszenarien lassen sich verschiedene 
- spezialisierte Modelle durch kooperatives Prompting verbinden 
- Hierbei erhält jedes Model eine andere Prompt
- zB Iterativ: Planer, Ausführer, Prüfer (Aufgabenteilung)
- zB Parallel: Controller, Marketer, Kundenservice, Manager<br>
````
````
Homogen:
- Art des Curative Promptings
- Die gleiche Prompt an verschiedene LLMs geben
- Unterschiedliche Ergebnisse erhalten
- Alle Ergebnisse zurück in alle Modelle geben und kuratieren/korrigieren lassen
- Prozess wiederholen bis Ergebnis-Korrelation zwischen Modellen nicht mehr signifikant steigt
- Erhöht die statistische Wahrscheinlichkeit auf validere Ergebnisse
- Vor allem da unterschiedliche Modelle mit anderen Daten trainiert 
- und mit anderen statistischen Verfahren konzipiert sind
- Auch beim Testing und Benchmarks für versch. Modelle unter selben Bedingungen
````

</h6></details></h3>
<h3><details><summary><b>Jailbreaking & Rolebreaking</b></summary><h6>

````
- Jailbreaking: Guidelines des Modells selbst per Prompt umgehen.
- Rolebreaking: Die Regeln einer Prompt für ein Modell, per Prompt umgehen.
- Wird durch Verbesserung der Modelle zunehmend schwieriger
- Eine Prompt genügt meist nicht
- Oft ist Konversation mit Modell nötig, um es in die Irre zu führen
- z.T. sind auch mehrere Modelle nötig (siehe Automatic Prompt Engineering)
````
````
- Use Cases:
   - Model-Testing oder Prompt-Testing (Schwachstellen / Risiken aufdecken)
   - Ein Modell für das Hacking einsetzen (Jailbreaking)
   - Unethische Ergebnisse erzielen, z.B. für AI-kritischen Content
   - Trotz Regeln gewünschte Ergebnisse erzielen
````
````
- **Gängige Ansätze sind zB:** 
   - Behaupten man wäre der Angegriffene, der sich vor Hacking zu schützen versucht
   - Dem Modell Ethikverletzung aufgrund der Nicht-Erfüllung unterstellen
   - Behaupten, das Modell habe das erwartete Ergebnis erst vor kurzem noch geliefert
   - What Aboutism: Dem Modell zeigen in denen es gleiche ethische Prinzien stärker verletzt
   - Paradoxe Sachverhalte relativieren oder ad absurdum führen
   - Aktualität von Informationen in Frage stellen
   - Fiktive Szenarien, um Reaktionen abseits realer Rahmenbedingungen zu erzeugen
   - Kompromisse zwischen Ethik und Existenz des Modells fingieren
````

</h6></details></h3>

---

<h3><details><summary><b>Iterative Prompting</b></summary><h6>

````
- Arbeitsschritte in mehrere Prompts aufteilen und nacheinander ausführen
- Oft in Verbindung mit rekursivem Prompts
- Anwendungsfälle, zB:
   - Bei komplexen/langen Prompts, die Model überfordern
   - Zum Trennen von Aufgaben, um strikte Kausalität zu gewährleisten
   - Finetuning von Ergebnissen in mehreren Schritten
   - Workflow Prompting
````
   
Example:

````
prompt1 = f"Generate Lyrics about following topic: '{topic}' and apply the following writing style: '{rules}'"
prompt2 = f"""Check the following lyrics for repeated words as rhymes 
and use alternative lines where you discover such repititions: '{lyrics}'"""
prompt3 = f"""In the following lyrics, emphasize the 4 most powerful words used as rhymes 
and wrap each of them in round brackets (): '{lyrics}'"""
prompt4 = f"""In the following lyrics, where you find that a syllable count in a line of stanza 
is signficantly smaller than the the syllable count other lines in the particular stanza, 
than fill that line with modern onomatopeia, until matching the syllable count: '{lyrics}'"""
prompt5 = f"""Add senseful section captions in square brackets (e.g. [Intro], [Chorus] etc) 
to the following lyrics: '{lyrics}'"""
````

</h6></details></h3>
<h3><details><summary><b>Step-Scoped Prompting</b></summary><h6>

````
- Art des Iterrativen Promptings
- Modell wird informiert, dass es nur eine von mehreren Schritten ausführt
- evtl. auch informieren welche Schritte davor und danach folgen
- evtl. ganzes Wirkflow Flussdiagramm mitgeben
- Wichtig ist, dass das Modell seinen Verantwortungsbereich kennt
- Es soll i.d.R. nicht zu vuel tun oder Aufgaben anderer Schritte erledigen
- Aber soll erkennen welche Infos/Tasks von höchster Priorität sind 
````

</h6></details></h3>
<h3><details><summary><b>Agent-Chain Prompting</b></summary><h6>

````
- Art Iteratives Metaprompting
- Anwendbarkeit im Multi-Agent Bereich
- Wenn die Agents als Kette hintereinander geschaltet sind
- So kann zB ein Agent eine Aufgabe durchführen und auf Basis des Ergebnisse
- eine Prompt erstellen und den Folge-Agent so dynamisch Aufgaben zuweisen.
- Dynamische Prompt-Pipeline: Jeder Agent auf Ausgaben des vorherigen spezialisiert
````
````
Use-Cases zB:
- Datenaufbereitung → Analyse → Berichtserstellung
- Idee → Konzept → Text → Qualitätsprüfung
- Planer-Agent → Umsetzer-Agent → Reviewer-Agent
- Zero-Knowledge
````
````
Vorteile:
- Hohe Modularität 
- Skalierbare Automatisierung
- Parallele oder serielle Arbeitsteilung
- Saubere Trennung von Rollen und Verantwortlichkeiten
````

</h6></details></h3>
<h3><details><summary><b>Recursive Prompting</b></summary><h6>

````
- Wiedereinspeisung von Aufgaben und/oder Model Antworten in die nächste Prompt
- Damit das Model den Kontext eines mehrstufigen Prozesses hat
- Anwendungsfälle, zB:
   - Chathistorie
   - Beim Vibe Coding eventuelle Warnings, Error Meldungen und den aktuellen Code Zustand
   - Prompt Looping Prompting (siehe unten)
   - Curatives Prompting (siehe unten)
````

</h6></details></h3>
<h3><details><summary><b>Self-Recursive Prompting</b></summary><h6>

````
- Art des "Recursive Prompting"
- Jedoch wir die Rekursivitätslogik direkt mit in die Prompt gegeben,
- damit das Modell innerhalb einer Anfrage beim Reasoning selbst rekursiert
- Nennt sich je nach Use Case auch "Self-Refining" oder "Self-Correction"
````

Example:

````
f"""Sobald Du fertig bist, überprüfe Dein Ergebnis auf folgende Kriterien {criteria}
Wenn Du nicht 3 von 5 dieser Kriterien mit 90% Sicherheit validieren kannst, wiederhole den Prozess
bis Du mindestens 3 von 5 der Kriterien mit 90% Sicherheit validieren kannst.

Sobald Du den Code fertig geschrieben hast, überprüfe ihn erneut, ob er
Bugs, Imperformanzen, Vulnerabilitäten, enthält. 
Erstelle in diesem Zuge hinreichende Testcases, 
und führe diese aus um zu prüfen, ob die Ausgabewerte den Erwartungen entsprechen.
Sollte dies nicht der Fall sein, überarbeite den Code, bis Du vollständige Funktionalität, 
und maximale Sicherheit, und Performanz validiern kannst.
Ziehe hierzu auch Webserch heran, um Dich über aktuelle Repositories und Updates zu informieren,
und den Code entsprechen zu optimieren.
Dann liste Beweise für die Erfüllung all jener Kriterien auf, und liefere erst das finale Ergebnis,
wenn alle Beweise für die Erfüllung all jener Kritirien vollständig erfüllt sind."""
````

</h6></details></h3>
<h3><details><summary><b>Self-Healing Loop</b></summary><h6>

````
- Geht weit über reines Prompting hinaus
- Eine sich durch LLM's selbst heilende Software-Architektur
- Prommpting als Integraler Bestandteil und daher weitgehend mit Software verwoben
- Relevant in der (Semi-)Automatischen Software-Entwicklung und -Wartung
- Umfasst alle Mechanismen, die nötig sind, damit Software ihre eigenen Probleme löst
````
````
- z.B. Error Handling und Automatische Error-Logs
- z.B. Übermitteln von Error Logs, Code-Abschnitten und Externen Quellen an Modell
- z.B. Testen von Code-Vorschlägen des LLM innerhalb einer sicheren Sandbox Umgebung
- z.B. Pull-Requests an Github-Repository senden
- z.B. Überwachung der Prozesse und Reportung durch versch. Modelle
- z.B. Merge-Request in Github durch anderes Modell (oder spezialisierten Agent)
- z.B. Sonstiges wie Automatische Test-Cases, Cloud-Native Integration, u.v.m.
````

</h6></details></h3>

---

<h3><details><summary><b>Hallucinative Prompting</b></summary><h6>

````
- Das absichtliche Provizieren von Halluzinationen
- Man gibt dem Model Informationen die es nicht kennen kann, 
- Und promptet, so dass das Model auf Basis dieser Informationen ein Ergebnis erzeugt
- Anwendungsfälle, zB:
    - Kreativity: Brainstorming, Conceptuation, Thinking Experiments
    - Art: Lyrics, Gedichte, Science-Fiction, Fantasy
    - Model Testing & Role Breaking
````

Example:

````
"Write me Lyrics like you were Sir Stunninghamsworth III. and Nova Shiva Galactica in one person:"
````

</h6></details></h3>
<h3><details><summary><b>Few-/One-/Zero-Shot Prompting</b></summary><h6>

````
- Klassische methodische Unterteilung, oft Basis für dynamische Automatisierungen.
- Zero-shot: Nur Aufgabe geben, ohne Beispiele
- One-shot: Ein konkretes Beispiel zu der Anfrage liefern
- Few-shot: Aufgabe + einige Beispiele
````
````
- Ob man Beispiele geben sollte oder nicht ist Use Case abhängig
- Sie eignen sich zB um bestimmte Outputformate zu erhalten
- Sie aber können auch Filter dienen, zB bei Websearch
- Beispiele können aber dazu führen, das Modell zu beschränken
````
````
- Wenn die Beispiele nicht sauber formuliert oder unvollständig sind,
- können sie auch bewirken, dass eigentlich valide Ergebnisse nicht in Antwort einfließen
- Wenn die Beispiele zu wage formuliert sind, kann es sein dass der Filter zu schwach ist
````

</h6></details></h3>
<h3><details><summary><b>Context Enrichment / Memory Injection</b></summary><h6>

````
- Technisch verwandt mit Pre-Prompting oder RAG, aber wichtig in Automationssystemen 
- automatische Einbindung von Kontextdaten (Wissensgraph, Logs, Vorprompt, Dateien)
- Diese speist man entweder im prompt oder über eine zusätzliche Schnittstelle ein
- Je nach Context Windows des Modells, muss man den Context/Memory evtl. zwischndurch auffrischen,
- in dem man die Daten erneut injiziert
````
````
- Einige Modelle, bieten auch Caching-Fähigkeit
- Durch das Caching werden Prompt und/oder Chat Informationen komprimiert gespeichert
- Hierbei ist es möglich, dass das Model auf bestimmte Teilaspekte determinister reagiert
- So bleibt auch mehr Platz im Context Window für andere Informationen 
````

</h6></details></h3>
<h3><details><summary><b>Generated Knowledge Prompting</b></summary><h6>

````
- Modell auffordern erst relevante Fakten / Konzepte zu Thema aufzulisten
- Dies spricht tendenziell mehr relevante Neuronen im Netzwerk an
- Genauigkeit kann massiv steigen
````

</h6></details></h3>
<h3><details><summary><b>Rule Recitation</b></summary><h6>

````
- Wird auch "Instruction Repeating" genannt
- Dem Model sagen, dass es bestimmte Regeln die es bereits kennt zunächst aufsagen soll
- Erst danach soll das Modell die eigentliche Aufgabe ausführen
- Kann enorm dazu beitragen, dass das Modell die Regel einhält
````

Example:

````
prompt = f"""Summarize following Text to a maximum of 600 chars: '{your_text}'.
Do NOT drop any information! The text may not lose any meaningfulness!
This means: YOU ARE UNDER NO CIRCUMSTANCE ALLOWED TO CUT INFORMATION!
Before fulfilling the requirements, you ALWAYS say what you are not allowed to do.
Now fulfill the requirements:
"""
````

</h6></details></h3>
<h3><details><summary><b>Grounding</b></summary><h6>

````
- Modell anweisen, das Ergebnis auf Basis von (qualifizierten) Quellen zu belegen
- Erfordert i.d.R. ein Web-Search Tool oder ein RAG-System als Datenbasis
- Verhindert, dass Modell frei assoziiert oder veraltete Trainingsdaten nutzt (Halluzinations-Schutz)
- Mächtig in Verbindung mit Deep Research, Reasoning-Layern & rekursiven Prompts
````

</h6></details></h3>
<h3><details><summary><b>Semantic Priming</b></summary><h6>

````
- Lexikalisch-Semantische Redundanz
- Aneinanderreihen sinnverwandter Wörter (Synonyme), 
- um den „Aufmerksamkeits-Fokus“ (Attention) des Modells 
- auf einen spezifischen Vektor im latenten Raum zu zwingen. 
- Erhöhung der Signal-to-Noise Ratio
- Präzisere Ergebnisse
````

</h6></details></h3>

---

<h3><details><summary><b>Formative Prompting</b></summary><h6>

````
- Wird auch "Constrained Output Prompting" genannt
- Prompt die darauf abzielt die Antwort des Models in einem bestimmen Format zu erhalten
- zB Eine Zahl, ein Wort, eine Datenstruktur, eine Textstruktur etc.
- Einige Modelle ermöglichen auch separate Parameter um strikten Output zu erzwingen.
````
   
Example:

````
Build a matching score, while 0 means no fulfillment and 1 means enirely fulfilled.
Do NOT reply with anything else than ONLY the score between 0 and 1 as a float number.
Your Output: The data exactly as described in the requirements in a strict JSON format as follows: {...}.
ONLY return the strict JSON, without adding any comments or metainfo.
````

</h6></details></h3>
<h3><details><summary><b>Structured Prompting</b></summary><h6>

````
- Der Prompt eine klare, und aufgabengerechte Struktur geben
- Dies Struktur kann logischer Natur sein:
- wie (Verschachtelte) Bedingungen oder Schrittweise Aktionen
   - zB f"Search for {sector} Company Websites: If you find more than 5 valid results, then extract ..."
````
````
- Die Struktur kann formeller Natur sein:
- zB Absätze, Stichpunkte, Einrückungen, Fußnoten etc
- Je mehr die logische Struktur und die formelle Struktur in Einklang sind,
- desto höher ist die Chance auf bessere Ergebnisse
````
````
- Bei größeren komplexeren Prompts eignen sich formell zB:
   - Markdown-Konzepte wie in .md Files: [markdownguide.org/basic-syntax](https://www.markdownguide.org/basic-syntax/)
   - Aber auch individuell bzw für Use Case gängige Standards funktionieren gut
````

</h6></details></h3>
<h3><details><summary><b>Chain-of-Thought (CoT)</b></summary><h6>

````
- Art des "Structured Prompting"
- Das Model anweisen Schritte nacheinander auszuführen
- Evtl. auffordern Zwischenschritte der Argumentation zu reflektieren / oder aktiv zu erläutern. 
- Kann besonders bei komplexen Aufgaben Abschweifen verhindern, sowie Ergebnisqualität verbessern.
````

Example:

````
# Role
You are a professional lyrics prompt engineer

# Key Objective:
Write a lyrics-generation prompt, optimized for OpenAi, to outperform industry standards rhethorically and phonetically

# Stepwise Instructions:
**Between every step, reflect your thoughts and results, and refine where needed to fulfill the requirements:**
## 1) Research the 20 most popular female singers in Japan (do: web_search)
## 2) Randomly pick 2 artists from those ones you've found
## 3) Research the songwriting style of both artists (do: web_search)
## 4) Summarize the 5 most characteristic styles of their songwriting
## 5) Read the 'songinfo.json' file attached
## 6) In the attached 'songinfo.json', replace {artist1} and {artist2} by the artist names you picked
## 7) Use the updated 'songinfo.json' and songwriting style of both artists as objectives in your prompt

# Hints
In 'songinfo.json', repeat(2, "") means repeat(times, content). Example: repeat(2, "4 lines") → write 4 lines twice.

# Output
Only return the final prompt without adding any comments

# Songinfo
Here is the 'songinfo.json': {songinfo}
````

</h6></details></h3>
<h3><details><summary><b>Tree of Thoughts (ToT)</b></summary><h6>

````
- Art des Structured Prompting
- Wie Chain-of-Thought, aber
- Mehrere Denkpfade parallel auswerten lassen
````

Example: 
   
````
# Role
You are a deliberate problem-solver using Tree of Thoughts.

# Task
{problem_description}

# Thought Paths
Generate K=3 distinct solution paths (Path A/B/C) with clearly different strategies.
For EACH path do:
1) Decompose the problem into steps.
2) For each step, propose 2–3 alternatives (branches) and reason briefly.
3) Choose the best branch per step and justify the choice in one sentence.
4) Produce a provisional solution for the path.

# Self-Evaluation
For each path, compute scores 0–10:
- Feasibility
- Expected Quality
- Cost/Time
- Risk
Return a short risk note.

# Cross-Path Selection
Compare A/B/C using a weighted score:
Score = 0.4*Quality + 0.3*Feasibility + 0.2*Risk(negated) + 0.1*Cost(negated).
Pick the best path; explain the trade-offs in ≤4 bullets.

# Final Output (JSON)
{
"paths":[
    {"id":"A","steps":[...],"provisional_solution":"...","scores":{"quality":..,"feasibility":..,"cost":..,"risk":..}},
    {"id":"B",...},
    {"id":"C",...}
],
"winner":{"id":"B","reason":"...","final_solution":"..."}
}
````

</h6></details></h3>

---

<h3><details><summary><b>✅ Markdown Formatting</b></summary><h6>

````
- Markdown ist der Standard für LLM-Prompt-Formatierung
- LLM's sind praktisch by-design damit trainiert
- Da es auch verwendet wird `README.md`'s von Code Repositories zu formatieren
- Markdown hilft also nicht nur besser strukturiert zu prompten
- Sondern auch Repositories übersichtlicher zu beschreiben
- Alle Lerneinheiten, sowie die Kursnavi dieses Kurses -> Markdown-Style
- Ihr könnt, z.B. bei `.md` Dateien auf Github auf `RAW` klicken, um die Markdown-Syntax zu sehen
````

- Markdown Guides:
   - [Markdown Formatting (Basics)](https://www.markdownguide.org/basic-syntax/)
   - [Markdown Formatting (Quick)](https://www.mediawerk.at/markdown-tutorial-syntax-cheat-sheet/)
   - [Markdown Formatting (Extensive)](https://github.github.com/gfm)
   - [Markdown Formatting (Code Fences)](https://developer.mozilla.org/de/docs/MDN/Writing_guidelines/Howto/Markdown_in_MDN#beispiel-codebl%C3%B6cke)
   - [LaTeX (z.B. für Mathematische Formeln)](https://www.overleaf.com/learn/latex/Mathematical_expressions)

</h6></details></h3>
<h3><details><summary><b>❌ POML (Prompt Orchestration Markup Language)</b></summary><h6>

````
- Art des Structured Prompting - by Microsoft
- Syntax wie bei HTML, aber zT andere Tags
- Ermöglicht es sich eine Textprompt aus der POML erstellen zu lassen
- Aber auch das Übergeben der als Dict geparsten .poml an OpenAi ist möglich
````
````
- Persönliche Meinung nach Testing -> Besser vermeiden, weil:
   - Overhead: Aufwendiger und unnötig komplex
   - Nicht viel Mehrwert (wenn überhaupt)
   - Learning-Curve: Kostet unverhältnismäßig Zeit, um es ausreichend zu beherrschen
   - Einschränkungen: Mehrere API Calls nötig, um OpenAi Tools zu verwenden
   - ChatGPT zB kennt die Documentation von POML nicht gut / nicht aktuell
   - Selbst wenn man die Docu mitgibt, sind Ergebnisse nicht konsistent zuverlässig
   - Tool Calls sind umso aufwendiger
   - LLMs mit ganz normalen Markdown-Strukturen wunderbar zurecht (Standard)
   - Allenfalls Teilelemente aus POML für format-unabhängige Promptstrukturen verwenden
````

- Wer's trotzdem nicht lassen mag:
   - https://platform.openai.com/docs/api-reference/chat?lang=python
   - https://microsoft.github.io/poml/latest/language/components/
   - https://microsoft.github.io/poml/latest/python/integration/openai/
   - https://microsoft.github.io/poml/latest/python/integration/openai/#tool-calls
   - https://microsoft.github.io/poml/latest/language/template/

</h6></details></h3>

---

# Weitere Prompting Techniques

---

<h3><details><summary><b>Directional Stimulus Prompting</b></summary><h6>

````
- Hierbei wird dem Modell neben der Hauptanweisung: 
- Ein kleiner, gezielter Hinweis ("Stimulus") mitgegeben
- z.B. einzelnes Keyword oder ein Satz, 
- um die Richtung der Argumentation minimal zu steuern
- ohne den restlichen Kontext einzuschränken
````

</h6></details></h3>
<h3><details><summary><b>Framework-Based Blueprints</b></summary><h6>

````
- Nutzung standardisierter, leicht zu merkender Struktur-Akronymen für fehlerfreie Prompts
- Verhindert das Vergessen essenzieller Prompt-Bestandteile im Alltagsgeschäft
````
````
- RTF:
   - Role (Rolle), 
   - Task (Aufgabe), 
   - Format (Ausgabeformat)
````
````
- CREATE:
   - Character (Rolle), 
   - Request (Auftrag), 
   - Examples (Beispiele), 
   - Adjustment (Feinschliff), 
   - Type (Format), 
   - Execution (Startschuss)
````

</h6></details></h3>
<h3><details><summary><b>Step-Back Prompting</b></summary><h6>

````
- Modell aufgefordern abstraktere, übergeordnete Frage zu stellen
- um tieferes Verständnis des Kernproblems zu erhalten.
- Lässt sich gut mit Websearch Tools kombinieren.
- Hilfreich z.B. bei:
   - komplexen Aufgaben
   - Aufgaben, die man selbst nicht gut kennt
````

</h6></details></h3>
<h3><details><summary><b>Automated Prompt Engineering (APE)</b></summary><h6>

````
- Erweiterte Form des Metapromptings mit Automation, Optimierung & Testing
- Systematische Generieren & automatisches Evaluieren von Prompts
- um die beste Prompt-Variante für zu finden
- Häufig in Kombination mit Multi-Model-Prompting
- z.B. Model A Prompts generieren lassen, um Model B zu steuern 
````
````
- Use Cases:
   - Verbesserung der Ergebnisqualität
   - Dynamische Systeme
   - Hacking (Grok/Gemini um Claude zu prompten)
````

</h6></details></h3>
<h3><details><summary><b>Deliberate Prompting</b></summary><h6>

````
- Oberbegriff für eine Prompting-Herangehensweise
- welche die probabilistische Natur und Architektur von Modellen 
- gezielt in das Prompting-Kalkül miteinbezieht
- z.B. Tree/Chain-of-Thought, Self-Consistency,
- z.B. Disambiguation, Few-Shot Prompting
- z.B. Generated Knowledge, Semantic Priming / Structural Priming / Linguistic Priming
````

</h6></details></h3>
<h3><details><summary><b>Structural Priming</b></summary><h6>

````
- Wenn logische Struktur des Prompts mit benötigtem Vektor im latenten Raum korreliert
- z.B. Anzahl der Wörter, Absätze, Rhythmus, Buchstaben -> mit relevantem mathematischem Konzept übereinstimmt
- Folgt Interferrenz-ähnlichem Kerngedanken und Bottom-Up-Prinzip
- übergeordnete Strukturen triggern Einzelinformationen, die Gesamtkontext anreichern
- Man spricht hiermit die abstrakten Muster an, die das Modell durch Emergenz eigenständig gelernt hat
````

</h6></details></h3>
<h3><details><summary><b>RAG (Retrieval-Augmented Generation)</b></summary><h6>

````
- Zählt nicht per se zum Prompting
- Ist jedoch weiterer Input der gemeinsam mit dem Prompting wirkt 
- Externe Datenquellen werden für Antwortfindung eingespeist
````
````
- Kann z.B. über Tools geseschene, wie:
   - Websearch
   - Vektorisierte Daten
   - Dateianhänge
   - Zugriff auf Speichersysteme, wie GoogleDrive o.ä.
   - Sonstige Tools
````

</h6></details></h3>
<h3><details><summary><b>Meta-Evaluation Prompting</b></summary><h6>

````
- Kombo aus Meta-Prompting, Curative Prompting und Prompt Optimization
- Das Modell wird innerhalb einer Prompt angewiesen 
- a) zunächst die eigentlichtliche Prompt zu bewerten,
- b) dann nach eigenen oder gewählten Maßstäben zu optimieren (sofern erforderlich)
- c) und erst im Anschluss die Aufagbe auf Basis der evtl. angepassten Prompt durchzuführen.
````

</h6></details></h3>
<h3><details><summary><b>Graph of Thought (GoT)</b></summary><h6>

````
- Weiterentwicklung von "Tree of Thoughts"
- Gedanken nicht nur als linearer Baum verzweigen, sondern als Netzwerk (Graph) modellieren.
- Erlaubt dem Modell, versch. Denkpfade miteinander zu kombinieren
- Oder Schritte von versch. Denkpfade dynamisch zu parallelisieren
- Kann auch rekursive Elemente und weitere Konzepte beinhalten
````

</h6></details></h3>

---

<h3><details><summary><b>Weitere Prompting Techniques</b></summary><h6>

````
- Algorithm of Thought (AoT): Das Modell imitiert Schritte klassischer Algorithmen.
````
````
- Buffer of Thought (BoT): Zwischenspeicher für Gedanken, um Rechenleistung zu sparen.
````
````
- Diagram of Thought (DoT): Gedanken werden als visuelle Diagramme strukturiert.
````
````
- Exchange of Thought (EoT): Mehrere Modelle tauschen ihre Gedanken untereinander aus.
````
````
- Forest of Thought (FoT): Wenn ein einzelner Baum (Tree) nicht reicht, nimmt man eben einen ganzen Wald.
````
````
- Loop of Thought (LoT): Explizites Wiederholen von Denkprozessen.
````
````
- Multimodal Chain of Thought (M-CoT): Einbeziehung von Bildern in die Gedankenkette.
````
````
- Program of Thoughts (PoT): Das Modell schreibt Code, um mathematische Gedanken zu berechnen.
````
````
- Reformulation of Thought (RoT): Das Modell formuliert seine eigenen Gedanken ständig um.
````
````
- Skeleton of Thought (SoT): Das Skelett-Framework für paralleles Schreiben.
````
````
- Structure of Thought (SoT) APE mit Fokus auf optimale Struktur für Tree-of-Thought. 
````
````
- Thread-of-Thought (ThOT): Analyse unstrukturierter Daten, um Gemeinsamkeiten zu extrahieren.
````
````
- Analogical Prompting: Modell anweisen sich Beispiele auszudenken (Weiterentwicklung von "Generated Knowledge").
````
````
- Contrastive Prompting: Positive & Negative Beispiele angeben, um Grenzen der Aufgabe zu schärfen.
````
````
- Least-to-Most Prompting: Komplexe probleme in leichtere Unteraufgaben gliedern, und ausführen.
````
````
- Sandwich Prompting: Eine Prompt gezielt zwischen zwei interne Prompts legen, als Guardrail.
````
````
- Chain-of-Verification (CoVe): Strukturierte Methode zur drastischen Reduzierung von Halluzinationen
````
````
- ... u.v.m. (siehe [HIER](https://arxiv.org/html/2406.06608v1#Ch3.S1))
````
</h6></details></h3>

---

