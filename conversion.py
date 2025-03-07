import xml.etree.ElementTree as ET
from pathlib import Path

def xml_to_ini(xml_path, ini_path):
    """
    Convertit un fichier bookmarks.xml en fichier Streams.ini
    
    Args:
        xml_path (str): Chemin vers le fichier bookmarks.xml
        ini_path (str): Chemin où sauvegarder le fichier Streams.ini
    """
    # Lecture du fichier XML
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Création de la liste des entrées
    entries = []
    
    # Traitement des bookmarks racines
    for bookmark in root[0]:
        if bookmark.tag == 'bookmark':
            entries.append(f"{bookmark.attrib['name']} = {bookmark.attrib['url']}")
    
    # Traitement des groupes (sauf "Flac International")
    for group in root[0]:
        if group.tag == 'group':
            if group.attrib['name'] != 'Flac International':  # Nouvelle condition pour exclure le groupe
                entries.append(f"\n[{group.attrib['name']}]")
                for bookmark in group:
                    entries.append(f"{bookmark.attrib['name']} = {bookmark.attrib['url']}")

    # Écriture dans le fichier INI
    with open(ini_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(entries))

def main():
    xml_input = Path('bookmarks.xml')
    ini_output = Path('Streams.ini')
    
    if xml_input.exists():
        xml_to_ini(str(xml_input), str(ini_output))
        print(f"Fichier converti avec succès : {ini_output}")
    else:
        print("Erreur : Le fichier bookmarks.xml n'a pas été trouvé")

if __name__ == "__main__":
    main()
