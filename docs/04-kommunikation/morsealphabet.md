# Morsealphabet – internationaler Morsecode

!!! info "Status: Quellenbasierter Entwurf"
    Zeichen und Zeitregeln nach ITU-R M.1677-1 (2009) dokumentiert. Eine redaktionelle Prüfung steht noch aus (Stand: 25.10.2026).

## Kurzüberblick

Der **internationale Morsecode** stellt Buchstaben und Ziffern durch kurze Signale (**Punkte**) und lange Signale (**Striche**) dar. Er lässt sich durch Lichtblitze, hörbare Töne oder geeigneten Funk übertragen. Dafür sind ein gleichmäßiger Rhythmus und ein erreichbarer Empfänger notwendig.

![Morsealphabet, alle Buchstaben von A bis Z und Ziffern von 0 bis 9 mit Zeitregeln](../assets/kommunikation/morsealphabet.svg){ width=100% }

## Morsezeichen mit einem Baum entschlüsseln

Wer den Code nicht auswendig kennt, kann jedes empfangene Zeichen **Schritt für Schritt** im Morsebaum suchen. Bei jeder Verzweigung folgt man **·** (kurz, Punkt) oder **—** (lang, Strich). Nach dem letzten Signal liest du den Buchstaben am erreichten Knoten ab. Ein Knoten kann schon einen vollständigen Buchstaben enthalten, auch wenn weitere Zweige abgehen.

Die beiden Diagramme enthalten zusammen **alle 26 Buchstaben A–Z**. Für die Lesbarkeit in der Buchausgabe sind die beiden Hälften des Binärbaums getrennt. Beginne mit dem passenden ersten Signal. Die Ziffern findest du in der Tabelle weiter unten.

### Erstes Signal kurz (·)

```mermaid
%% alt: Morsebaum für Buchstaben mit kurzem ersten Signal, von E bis zu vier Signalzeichen
flowchart TB
    root((Start))
    root -->|·| E["E"]
    E -->|·| I["I"]
    E -->|—| A["A"]
    I -->|·| S["S"]
    I -->|—| U["U"]
    A -->|·| R["R"]
    A -->|—| W["W"]
    S -->|·| H["H"]
    S -->|—| V["V"]
    U -->|·| F["F"]
    R -->|·| L["L"]
    W -->|·| P["P"]
    W -->|—| J["J"]
```

### Erstes Signal lang (—)

```mermaid
%% alt: Morsebaum für Buchstaben mit langem ersten Signal, von T bis zu vier Signalzeichen
flowchart TB
    root((Start))
    root -->|—| T["T"]
    T -->|·| N["N"]
    T -->|—| M["M"]
    N -->|·| D["D"]
    N -->|—| K["K"]
    M -->|·| G["G"]
    M -->|—| O["O"]
    D -->|·| B["B"]
    D -->|—| X["X"]
    K -->|·| C["C"]
    K -->|—| Y["Y"]
    G -->|·| Z["Z"]
    G -->|—| Q["Q"]
```

**Beispiel:** · — · ergibt **R**: Im kurzen Baum von Start über E (·), A (—) zu R (·). Zunächst einzelne Buchstaben üben, danach kurze Wörter mit klaren Pausen.

## Buchstaben A–Z

| Buchstabe | Morsecode | Buchstabe | Morsecode |
| --- | --- | --- | --- |
| **A** | `.-` | **N** | `-.` |
| **B** | `-...` | **O** | `---` |
| **C** | `-.-.` | **P** | `.--.` |
| **D** | `-..` | **Q** | `--.-` |
| **E** | `.` | **R** | `.-.` |
| **F** | `..-.` | **S** | `...` |
| **G** | `--.` | **T** | `-` |
| **H** | `....` | **U** | `..-` |
| **I** | `..` | **V** | `...-` |
| **J** | `.---` | **W** | `.--` |
| **K** | `-.-` | **X** | `-..-` |
| **L** | `.-..` | **Y** | `-.--` |
| **M** | `--` | **Z** | `--..` |

## Ziffern 0–9

| Ziffer | Morsecode | Ziffer | Morsecode |
| --- | --- | --- | --- |
| **0** | `-----` | **5** | `.....` |
| **1** | `.----` | **6** | `-....` |
| **2** | `..---` | **7** | `--...` |
| **3** | `...--` | **8** | `---..` |
| **4** | `....-` | **9** | `----.` |

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

## Grenzen und Vorsicht

- Lichtzeichen und Töne benötigen freie Sicht- beziehungsweise Hörreichweite; Funk benötigt geeignete Geräte und verfügbare Frequenzen.
- Signale sind meist öffentlich wahrnehmbar und können den eigenen Standort verraten.
- Für Funkübertragungen die geltenden Vorschriften beachten; in akuten Notfällen verfügbare etablierte Rettungs- und Warnkanäle bevorzugen.

## Quellen

- Internationale Fernmeldeunion (ITU), [ITU-R M.1677-1 – International Morse code](https://www.itu.int/rec/R-REC-M.1677-1-200910-I/), 10/2009 (Zugriff: 25.10.2026).
- American Radio Relay League, [A Standard for Morse Timing Using the Farnsworth Technique](https://www.arrl.org/files/file/Technology/x9004008.pdf) (Zugriff: 25.10.2026).

**Redaktioneller Status:** Quellenbasierter Entwurf; fachlicher Review ausstehend.
