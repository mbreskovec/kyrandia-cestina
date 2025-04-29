# Překlad trilogie The Legend of Kyrandia
Dodatečné soubory pro překlady CD  verzí her The Legend of Kyrandia 1, 2 a 3.

## The Legend of Kyrandia - Book One
Složka: "**Kyra1**"

### Překlad textu v Intru
Složka: "**Intro**"

 - "**TEXT_ENG.CPS**" - Soubor s přeloženým obrázkem s textem v Intru. Stači jej nakopírovat do adresáře s CD verzí hry a přepsat původní soubor.
 - "**TEXT_ENG.xcf**" - Zdojový obrázek s českýmni úpravami pro grafický editor [GIMP](https://www.gimp.org/ "GNU IMAGE MANIPULATION PROGRAM"). Obrázek doporučuji uložit do ***.BMP** a zvolit uložení bez "palety".
 - "**TEXT_ENG.bmp**" - Soubor s přeloženým obrázkem dopisu, který jde pomocí programu **Engie File converter** konvertovat zpět do ***.CPS**. Pochopitelně umí konvertovat i ***.CPS** do ***.BMP** (je třeba zvolit export be barevné palety).

### Překlad Kallakova dopisu pro Brynn
Složka: "**NoteToBrinn**"

 - "**NOTEENG.CPS**" - Soubor s přeloženým obrázkem dopisu. Stači jej nakopírovat do adresáře s CD verzí hry a bude to fungovat. Soubor pochází z balíku "**MISC.PAK**".
 - "**NOTEENG.xcf**" - Zdojový obrázek s českýmni úpravami pro grafický editor [GIMP](https://www.gimp.org/ "GNU IMAGE MANIPULATION PROGRAM"). Obrázek doporučuji uložit do ***.BMP** a zvolit uložení bez "palety".
 - "**NOTEENG.bmp**" - Soubor s přeloženým obrázkem dopisu, který jde pomocí programu **Engie File converter** konvertovat zpět do ***.CPS**. Pochopitelně umí konvertovat i ***.CPS** do ***.BMP** (je třeba zvolit export be barevné palety).
 - "**MISC.PAK**" - Soubor s integrovaným přeloženým "**NOTEENG.CPS**". Stači jej nakopírovat do adresáře s CD verzí hry a přepsat původní soubor.

### Překlady do ScummVM
Složka: "**scummvm/devtools/create_kyradat/resources/**"

 - "**lok_dos_cd_czech.h**" - Finální soubor obahuje přeložené texty integrované do **ScummVM** souboru "**kyra.dat**". Znaky s diakritikou jsou zkonvertovány do escape sekvencí, podle tabulky "**znaky.ods**".
 - "**glok_dos_cd_czech.utf8.h**" - Pracovní soubor obahuje přeložené texty integrované do **ScummVM** souboru "**kyra.dat**". Znaky s diakritikou je potřeba konvertovat do escape sekvencí, podle tabulky "**znaky.ods**".

 
## The Legend of Kyrandia - Book Two: The Hand of Fate
Složka: "**Kyra2**"

### Lokalizace fontu v Intru
Složka: "**IntroFont**"

 - "**GOLDFONT.FNT**" - Lokalizovaný font. Lokalizace provedena pomocí **WWFontEditor**. Soubor pochází z balíku "**INTROGEN.PAK**".
 - "**INTROGEN.PAK**" - Soubor s integrovaným přeloženým intro fontem "**GOLDFONT.FNT**". Stači jej nakopírovat do adresáře s CD verzí hry a přepsat původní soubor.

### Překlady do ScummVM
Složka: "**scummvm/devtools/create_kyradat/resources/**"

 - "**hof_dos_cd_czech.h**" - Finální soubor obahuje přeložené texty integrované do **ScummVM** souboru "**kyra.dat**".
 - "**hof_dos_cd_czech.utf8.h**" - Pracovní soubor obahuje přeložené texty integrované do **ScummVM** souboru "**kyra.dat**". Znaky s diakritikou je potřeba konvertovat do escape sekvencí, podle tabulky "**znaky.ods**".

## The Legend of Kyrandia - Book Three: Malcolm's Revenge
Složka: "**Kyra3**"

### Překlady do ScummVM
Složka: "**scummvm/devtools/create_kyradat/resources/**"

 - "**mr_dos_cd_czech.h**" - Finální soubor obahuje přeložené texty integrované do **ScummVM** souboru "**kyra.dat**". Znaky s diakritikou jsou zkonvertovány do escape sekvencí, podle tabulky "**znaky.ods**".
 - "**mr_dos_cd_czech.utf8.h** - Pracovní soubor obahuje přeložené texty integrované do **ScummVM** souboru "**kyra.dat**". Znaky s diakritikou je potřeba konvertovat do escape sekvencí, podle tabulky "**znaky.ods**".

## Nástroje a aplikace
Složka: "**Tools**"

 - **Engie File Converter** - Aplikace pro export a konverzi obrázků ve Westwood formátech. Kromě mnoha jiných formátů umí zobrazovat a konvertovat i formát obrázků *.CPS a animací *.WSA. Funguje pod WINE a potřebuje .NET v3.5. Informace o apliakci lze nalézt [zde](https://ppmforums.com/topic-45680/engie-file-converter-game-formats-documentation/), přímý odkaz ke stažení [zde](http://nyerguds.arsaneus-design.com/project_stuff/2018/EngieFileConverter/release/).
 - **WestPak2** - Aplikace pro rozbalení/zabalení Westwood PAK souborů. Informace a stažení programu [zde](https://github.com/Serebriakov/westpak2).
 - **WWFontEditor** (Westwood Font Editor) - Kromě mnoha jiných formátů umí editovat i fonty v souborech *.FNT použitýh v Kyrandii.
 - **ScummVM** zdoje na GitHubu: https://github.com/scummvm/scummvm
 - **znaky.ods** - Tabulka obsahuje převod mezi ASCII znaky a escape sekvencemi použitými ve zdrojovém kódu ScummVM.
 - Soubor "```/scummvm/engines/kyra/detection_tables.h```" obsahuje názvy souborů jejich hashe a nastavení pro jednotlivé jazykové verze Kyrandie.

## Postup testování úprav ve ScummVM (Linux)

 1. Stažení ScummVM GIT repozitáře: ```git clone https://github.com/scummvm/scummvm.git```
 2. Konfigurace před kompilací: ```./configure```
 3. Kompilace ScummVM: ```make -j$(nproc)```
 4. Pokud došlo ke změně v "**scummvm/devtools/create_kyradat**":
    1. Je potřeba zkompilovat i "**devtools**": ```make devtools```
    2. Pak pomocí zkompilovaného "**devtools**" vytvořit nový "**kyra.dat**" soubor: ```scummvm/devtools/create_kyradat/create_kyradat scummvm/dists/engine-data/kyra.dat```
    3. Při další změně ve zdrojích "**devtools**" pak už stačí **zopakovat jen celý bod 4**.
