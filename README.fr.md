
Cela installera les outils nécessaires au fonctionnement du script.

---

### 3. ✅ Installer l’extension Scrap.io

Rendez-vous sur la page Chrome Web Store de Scrap.io :

🔗 https://chrome.google.com/webstore/detail/scrapio-google-maps-scrap/lhdoppojpmngadmnindnejefpokejbdd

Une fois installée, vous devrez retrouver le chemin local de l’extension pour permettre au script de la charger.

---

## 🔍 Trouver le chemin local de l’extension

1. Ouvrez Chrome et allez sur `chrome://extensions`  
2. Activez le **Mode développeur** (en haut à droite)  
3. Trouvez **Scrap.io** et cliquez sur **Détails**  
4. Copiez l’**ID de l’extension** — une longue chaîne comme :  
   `mjllncbijgeccmolnikpkbkpbjggcgij`

5. Sur votre ordinateur, allez dans le dossier **User Data** de Chrome :

   - **Windows :**  
     `C:\Users\<VotreNom>\AppData\Local\Google\Chrome\User Data\`

   - **macOS :**  
     `~/Library/Application Support/Google/Chrome/`

   - **Linux :**  
     `~/.config/google-chrome/`

6. Dans ce dossier, vous trouverez plusieurs profils :  
   `Default`, `Profile 1`, `Profile 2`, etc.

7. Allez dans le dossier `Extensions` du bon profil :  
   Par exemple :  
   `C:\Users\<VotreNom>\AppData\Local\Google\Chrome\User Data\Profile 1\Extensions`

8. Trouvez le dossier correspondant à l’ID Scrap.io  
9. Ouvrez le dossier de la version la plus récente (ex. `1.6.4_0`)  
10. Copiez le **chemin complet** de ce dossier (clic droit > "Copier en tant que chemin")

Ce chemin sera utilisé avec `--extension-path` lors du lancement du script.

---

## 🏃 Exécuter le script

### 📦 Télécharger le script

1. Téléchargez le dépôt GitHub :  
   - Cliquez sur le bouton **Code** (vert)  
   - Cliquez sur **Download ZIP**  
   - Extrayez le ZIP dans un dossier

   ou bien clonez-le via Git :  
   `git clone https://github.com/votreutilisateur/votre-repo.git`

2. Ouvrez un terminal ou une invite de commande  
   Placez-vous dans le dossier du script avec `cd` :  
   `cd "C:\Users\VotreNom\Desktop\scrapio-scraper"`

3. Lancez le script :  
   `python scrape_maps.py --extension-path "CHEMIN_VERS_L’EXTENSION" --output "mes_données.xlsx"`

   Exemple :  
   `python scrape_maps.py --extension-path "C:\Users\Clara\AppData\Local\Google\Chrome\User Data\Profile 1\Extensions\mjllncbijgeccmolnikpkbkpbjggcgij\1.6.4_0" --output "paris_restaurants.xlsx"`

---

## 🔍 Instructions de scraping

1. Une fenêtre Chrome s’ouvre avec Google Maps  
2. Zoomez sur la zone souhaitée  
3. Cherchez un type d’entreprise, ex. **“Fleuriste”**  
4. Faites défiler les résultats à gauche jusqu’à la fin  
5. Attendez l’apparition des icônes Scrap.io  
6. Revenez dans le terminal et appuyez sur **Entrée**  
7. Attendez que le script affiche combien d’entreprises ont été extraites  
8. Revenez sur Maps, effectuez une nouvelle recherche  
9. Répétez si nécessaire  
10. Tapez `STOP` et appuyez sur **Entrée** pour terminer

Les données seront nettoyées et enregistrées dans votre fichier Excel.

---

## 📂 Exemple de sortie

| maps_link | email             | phone       | website           | contact_page       | facebook             | instagram             |
|-----------|------------------|-------------|-------------------|--------------------|----------------------|-----------------------|
| https://... | info@domaine.com | +33612345678 | www.exemple.com   | /contact           | fb.com/votrepage     | instagram.com/votrebiz |

---

## ❓ En cas de problème

- **Rien n’est extrait ?**  
  → Vérifiez que les icônes Scrap.io sont bien chargées avant d’appuyer sur Entrée

- **L’extension ne fonctionne pas ?**  
  → Vérifiez le chemin complet (avec le dossier de version)

- **Erreurs Playwright ?**  
  → Exécutez `playwright install` à nouveau

- **"Permission denied" ?**  
  → Lancez le terminal en mode administrateur

---

## 💡 Conseils

- Utilisez des recherches plus précises  
  ex. `"photographes à Lyon"` au lieu de `"photographes"`

- Ajustez le zoom si les résultats ne s’affichent pas  
- Attendez quelques secondes après avoir fait défiler avant d’extraire

---

## 🧼 Ce que fait le script

- Ouvre Chrome avec l’extension Scrap.io  
- Vous permet de naviguer manuellement sur Google Maps  
- Récupère les informations de contact visibles  
- Nettoie les doublons et garde l’essentiel  
- Sauvegarde le tout dans un fichier Excel

---

## 📞 Besoin d'aide?

Contactez clawara sur Discord.

---
