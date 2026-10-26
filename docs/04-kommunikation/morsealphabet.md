# Morsealphabet – internationaler Morsecode

!!! info "Status: Quellenbasierter Entwurf"
    Zeichen und Zeitregeln nach ITU-R M.1677-1 (2009) dokumentiert. Eine redaktionelle Prüfung steht noch aus (Stand: 25.10.2026).

## Kurzüberblick

Der **internationale Morsecode** stellt Buchstaben und Ziffern durch kurze Signale (**Punkte**) und lange Signale (**Striche**) dar. Er lässt sich durch Lichtblitze, hörbare Töne oder geeigneten Funk übertragen. Dafür sind ein gleichmäßiger Rhythmus und ein erreichbarer Empfänger notwendig.

**Zeichenschlüssel:** Kurzes Signal = Kreis (Punkt), langes Signal = Balken (Strich). Die Tabelle verwendet dafür Vektorgrafiken statt Satzzeichen.

## Buchstaben A–Z

Ein **Kreis** bedeutet kurz, ein **Balken** bedeutet lang. Jedes Signal ist als echte SVG-Form gezeichnet und wird von links nach rechts gelesen.

| Buchstabe | Morsezeichen |
| :---: | :--- |
| **A** | ![A: kurz, lang](../assets/kommunikation/morsezeichen/a.svg){ height="16px" } |
| **B** | ![B: lang, kurz, kurz, kurz](../assets/kommunikation/morsezeichen/b.svg){ height="16px" } |
| **C** | ![C: lang, kurz, lang, kurz](../assets/kommunikation/morsezeichen/c.svg){ height="16px" } |
| **D** | ![D: lang, kurz, kurz](../assets/kommunikation/morsezeichen/d.svg){ height="16px" } |
| **E** | ![E: kurz](../assets/kommunikation/morsezeichen/e.svg){ height="16px" } |
| **F** | ![F: kurz, kurz, lang, kurz](../assets/kommunikation/morsezeichen/f.svg){ height="16px" } |
| **G** | ![G: lang, lang, kurz](../assets/kommunikation/morsezeichen/g.svg){ height="16px" } |
| **H** | ![H: kurz, kurz, kurz, kurz](../assets/kommunikation/morsezeichen/h.svg){ height="16px" } |
| **I** | ![I: kurz, kurz](../assets/kommunikation/morsezeichen/i.svg){ height="16px" } |
| **J** | ![J: kurz, lang, lang, lang](../assets/kommunikation/morsezeichen/j.svg){ height="16px" } |
| **K** | ![K: lang, kurz, lang](../assets/kommunikation/morsezeichen/k.svg){ height="16px" } |
| **L** | ![L: kurz, lang, kurz, kurz](../assets/kommunikation/morsezeichen/l.svg){ height="16px" } |
| **M** | ![M: lang, lang](../assets/kommunikation/morsezeichen/m.svg){ height="16px" } |
| **N** | ![N: lang, kurz](../assets/kommunikation/morsezeichen/n.svg){ height="16px" } |
| **O** | ![O: lang, lang, lang](../assets/kommunikation/morsezeichen/o.svg){ height="16px" } |
| **P** | ![P: kurz, lang, lang, kurz](../assets/kommunikation/morsezeichen/p.svg){ height="16px" } |
| **Q** | ![Q: lang, lang, kurz, lang](../assets/kommunikation/morsezeichen/q.svg){ height="16px" } |
| **R** | ![R: kurz, lang, kurz](../assets/kommunikation/morsezeichen/r.svg){ height="16px" } |
| **S** | ![S: kurz, kurz, kurz](../assets/kommunikation/morsezeichen/s.svg){ height="16px" } |
| **T** | ![T: lang](../assets/kommunikation/morsezeichen/t.svg){ height="16px" } |
| **U** | ![U: kurz, kurz, lang](../assets/kommunikation/morsezeichen/u.svg){ height="16px" } |
| **V** | ![V: kurz, kurz, kurz, lang](../assets/kommunikation/morsezeichen/v.svg){ height="16px" } |
| **W** | ![W: kurz, lang, lang](../assets/kommunikation/morsezeichen/w.svg){ height="16px" } |
| **X** | ![X: lang, kurz, kurz, lang](../assets/kommunikation/morsezeichen/x.svg){ height="16px" } |
| **Y** | ![Y: lang, kurz, lang, lang](../assets/kommunikation/morsezeichen/y.svg){ height="16px" } |
| **Z** | ![Z: lang, lang, kurz, kurz](../assets/kommunikation/morsezeichen/z.svg){ height="16px" } |

## Ziffern 0–9

| Ziffer | Morsezeichen |
| :---: | :--- |
| **0** | ![0: lang, lang, lang, lang, lang](../assets/kommunikation/morsezeichen/0.svg){ height="16px" } |
| **1** | ![1: kurz, lang, lang, lang, lang](../assets/kommunikation/morsezeichen/1.svg){ height="16px" } |
| **2** | ![2: kurz, kurz, lang, lang, lang](../assets/kommunikation/morsezeichen/2.svg){ height="16px" } |
| **3** | ![3: kurz, kurz, kurz, lang, lang](../assets/kommunikation/morsezeichen/3.svg){ height="16px" } |
| **4** | ![4: kurz, kurz, kurz, kurz, lang](../assets/kommunikation/morsezeichen/4.svg){ height="16px" } |
| **5** | ![5: kurz, kurz, kurz, kurz, kurz](../assets/kommunikation/morsezeichen/5.svg){ height="16px" } |
| **6** | ![6: lang, kurz, kurz, kurz, kurz](../assets/kommunikation/morsezeichen/6.svg){ height="16px" } |
| **7** | ![7: lang, lang, kurz, kurz, kurz](../assets/kommunikation/morsezeichen/7.svg){ height="16px" } |
| **8** | ![8: lang, lang, lang, kurz, kurz](../assets/kommunikation/morsezeichen/8.svg){ height="16px" } |
| **9** | ![9: lang, lang, lang, lang, kurz](../assets/kommunikation/morsezeichen/9.svg){ height="16px" } |

## Morsebaum: Buchstaben entschlüsseln

**Finger oben auf START legen.** Für ein kurzes Signal geht es nach **links**, für ein langes Signal nach **rechts**. Nach dem letzten Signal den Buchstaben am erreichten Knoten ablesen. Auch Knoten mit weiteren Ästen sind bereits gültige Buchstaben.

```mermaid
%% alt: Ein einziger zusammenhängender Morsebaum für A bis Z. Vom Startpunkt führt kurz jeweils nach links und lang jeweils nach rechts. Kurz, lang, kurz ergibt R.
flowchart TB
    ROOT(("START"))
    ROOT -->|kurz| N0["E"]
    ROOT -->|lang| N1["T"]
    N0 -->|kurz| N00["I"]
    N0 -->|lang| N01["A"]
    N1 -->|kurz| N10["N"]
    N1 -->|lang| N11["M"]
    N00 -->|kurz| N000["S"]
    N00 -->|lang| N001["U"]
    N01 -->|kurz| N010["R"]
    N01 -->|lang| N011["W"]
    N10 -->|kurz| N100["D"]
    N10 -->|lang| N101["K"]
    N11 -->|kurz| N110["G"]
    N11 -->|lang| N111["O"]
    N000 -->|kurz| N0000["H"]
    N000 -->|lang| N0001["V"]
    N001 -->|kurz| N0010["F"]
    N010 -->|kurz| N0100["L"]
    N011 -->|kurz| N0110["P"]
    N011 -->|lang| N0111["J"]
    N100 -->|kurz| N1000["B"]
    N100 -->|lang| N1001["X"]
    N101 -->|kurz| N1010["C"]
    N101 -->|lang| N1011["Y"]
    N110 -->|kurz| N1100["Z"]
    N110 -->|lang| N1101["Q"]
```

**Beispiel:** kurz (links zu E), lang (rechts zu A), kurz (links zu R) ergibt **R**.

## Signalzeiten und Pausen

| Element | Länge |
| --- | ---: |
| Punkt | 1 Zeiteinheit |
| Strich | 3 Zeiteinheiten |
| Pause zwischen Bestandteilen eines Buchstabens | 1 Zeiteinheit |
| Pause zwischen Buchstaben | 3 Zeiteinheiten |
| Pause zwischen Wörtern | 7 Zeiteinheiten |

**SOS:** `... --- ...` – drei Punkte, drei Striche, drei Punkte. Im Funkverkehr wird das SOS-Notsignal zusammenhängend ohne reguläre Buchstabenpausen übertragen; die Dreiteilung ist eine Merkhilfe.

## So wird übermittelt

1. Signalmedium auswählen (etwa Taschenlampe, Pfeife oder geeignetes Morsefunkgerät) und Reichweite beziehungsweise Sicht- oder Hörkontakt sicherstellen.
2. Eine möglichst gleichmäßige Zeiteinheit wählen und zwischen Punkt, Strich und den unterschiedlichen Pausen klar unterscheiden.
3. Buchstaben der Nachricht nacheinander übermitteln. Wichtige Angaben und Notmeldungen bei vorhandenem Rückkanal bestätigen lassen.
4. Mit einfachen kurzen Nachrichten üben; für Adressen, Zahlen und Koordinaten auf Eindeutigkeit achten.

## Alternative: Winkeralphabet mit zwei Flaggen

Mit dem [Flaggensemaphore (Winkeralphabet)](flaggenalphabet.md) können Buchstaben durch **gleichzeitig sichtbare Armstellungen** übermittelt werden. Dafür sind zwei Flaggen und freie Sicht erforderlich. Im Gegensatz zu diesem Morseverfahren braucht der Empfänger keine Folge von kurzen und langen Signalen zu unterscheiden.

## Grenzen und Vorsicht

- Lichtzeichen und Töne benötigen freie Sicht- beziehungsweise Hörreichweite; Funk benötigt geeignete Geräte und verfügbare Frequenzen.
- Signale sind meist öffentlich wahrnehmbar und können den eigenen Standort verraten.
- Für Funkübertragungen die geltenden Vorschriften beachten; in akuten Notfällen verfügbare etablierte Rettungs- und Warnkanäle bevorzugen.

## Quellen

- Internationale Fernmeldeunion (ITU), [ITU-R M.1677-1 – International Morse code](https://www.itu.int/rec/R-REC-M.1677-1-200910-I/), 10/2009 (Zugriff: 25.10.2026).
- American Radio Relay League, [A Standard for Morse Timing Using the Farnsworth Technique](https://www.arrl.org/files/file/Technology/x9004008.pdf) (Zugriff: 25.10.2026).

**Redaktioneller Status:** Quellenbasierter Entwurf; fachlicher Review ausstehend.
