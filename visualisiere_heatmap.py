import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.colors import ListedColormap, BoundaryNorm

def lade_heatmap(dateipfad):
    """Lädt eine Heatmap aus einer .npy-Datei."""
    if not os.path.exists(dateipfad):
        print(f"Die Datei {dateipfad} existiert nicht.")
        return None
    return np.load(dateipfad)

def zeige_heatmap(heatmap, titel="Heatmap der Besuchshäufigkeit"):
    """Zeigt die Heatmap an, mit Schwarz für 0 und einem warmen Verlauf von Weiß bis Rot für Besuche."""
    plt.figure(figsize=(10, 10))

    # Farbschema mit Weiß für "0 Besuche" und einem warmen Verlauf von Weiß, Gelb, Orange, bis Rot
    farben = [
        "white",    # Nie besucht (0)
        "#ffffe0",  # Sehr wenige Besuche (1–Schwelle 1, sehr helles Gelb)
        "#ffff00",  # Wenige Besuche (Schwelle 1–Schwelle 2, Gelb)
        "#ffcc00",  # Wenig besucht (Schwelle 2–Schwelle 3, Gelb-Orange)
        "#ff9900",  # Moderat besucht (Schwelle 3–Schwelle 4, Orange)
        "#ff6600",  # Häufig besucht (Schwelle 4–Schwelle 5, Orange-Rot)
        "#ff3300",  # Sehr häufig besucht (Schwelle 5–Schwelle 6, Rot)
        "#cc0000",  # Sehr intensiv besucht (Schwelle 6–Schwelle 7, Dunkelrot)
        "#990000",  # Extrem besucht (Schwelle 7–Schwelle 8, Dunkelrot)
        "#660000",  # Nahezu maximal besucht (Schwelle 8–Schwelle 9, Sehr Dunkelrot)
        "#330000",  # Maximal besucht (>Schwelle 9, Fast Schwarz-Rot)
    ]
    cmap = ListedColormap(farben)

    # Dynamische Schwellenwerte
    max_wert = np.max(heatmap)
    
    if max_wert == 0:  # Kein Besuch überhaupt
        grenzen = [0, 1]  # Nur Weiß sichtbar
        labels = ["Nie"]
    else:
        # Schwellenwerte manuell berechnen
        # Da wir 10 Bereiche wollen, müssen wir die Grenzwerte explizit festlegen.
        # Die Werte sind manuell berechnet, damit keine Formel verwendet wird.
        
        # Manuelle Berechnungen der Grenzen
        grenzen = [0]  # Startet bei 0 (Nie besucht)
        grenzen.append(1)  # Für 1 (sehr wenige Besuche)
        grenzen.append(max_wert // 10)  # Bereich für 2-3 Besuche
        grenzen.append(max_wert // 5)   # Bereich für 4-5 Besuche
        grenzen.append(max_wert // 4)   # Bereich für 6-7 Besuche
        grenzen.append(max_wert // 3)   # Bereich für 8-9 Besuche
        grenzen.append(max_wert // 2)   # Bereich für 10-12 Besuche
        grenzen.append(2 * max_wert // 3)  # Bereich für 13-15 Besuche
        grenzen.append(max_wert - 1)  # Bereich für 16-20 Besuche
        grenzen.append(max_wert)    # Bereich für Maximalbesuche
        grenzen.append(max_wert + 1)  # Für Werte größer als der Maximalwert

        # Labels für die jeweiligen Bereiche manuell anpassen
        labels = ["Nie"]  # Nie besuchte Felder
        labels.append(f"1–{grenzen[2] - 1}")  # Bereich 1–Schwelle 1
        labels.append(f"{grenzen[2]}–{grenzen[3] - 1}")  # Bereich Schwelle 1–Schwelle 2
        labels.append(f"{grenzen[3]}–{grenzen[4] - 1}")  # Bereich Schwelle 2–Schwelle 3
        labels.append(f"{grenzen[4]}–{grenzen[5] - 1}")  # Bereich Schwelle 3–Schwelle 4
        labels.append(f"{grenzen[5]}–{grenzen[6] - 1}")  # Bereich Schwelle 4–Schwelle 5
        labels.append(f"{grenzen[6]}–{grenzen[7] - 1}")  # Bereich Schwelle 5–Schwelle 6
        labels.append(f"{grenzen[7]}–{grenzen[8] - 1}")  # Bereich Schwelle 6–Schwelle 7
        labels.append(f"{grenzen[8]}–{grenzen[9] - 1}")  # Bereich Schwelle 7–Schwelle 8
        labels.append(f">{grenzen[9]}")  # Für Maximalbesuche

    norm = BoundaryNorm(grenzen, cmap.N)

    # Heatmap darstellen
    im = plt.imshow(heatmap, cmap=cmap, norm=norm, interpolation="nearest")
    cbar = plt.colorbar(im, ticks=grenzen[:-1], boundaries=grenzen)
    cbar.set_label("Besuchshäufigkeit")
    cbar.ax.set_yticklabels(labels)  # Korrektur: Anzahl der Labels stimmt jetzt mit Ticks überein

    plt.title(titel)
    plt.xlabel("X-Achse (Spalten)")
    plt.ylabel("Y-Achse (Zeilen)")
    plt.show()

def Heatmap():
    print("Heatmap-Visualisierung")
    dateipfad = input("Geben Sie den Pfad zur Heatmap-Datei (.npy) ein: ")

    # Heatmap laden
    heatmap = lade_heatmap(dateipfad)
    if heatmap is None:
        return

    # Titel generieren (optional)
    dateiname = os.path.basename(dateipfad)
    titel = f"Heatmap aus Datei: {dateiname}"

    # Heatmap anzeigen
    zeige_heatmap(heatmap, titel=titel)

Heatmap()