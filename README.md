# git Gedicht

## Arbeiten mit diesem Repository

Erstellen Sie einen Fork aus diesem Repository.
Damit erhalten Sie ihre eigene Kopie unter
`git@github.com:USERNAME/git-gedicht.git` in der Sie arbeiten können.

Clonen Sie ihren Fork via SSH, um lokal ein Gedicht zu schreiben.

```bash
git clone git@github.com:USERNAME/git-gedicht.git
```

Um Änderungen in dieses Repository hochzuladen ersellen Sie ein pull request
von Ihrem Fork aus.

## Schreiben Sie ein Gedicht

Organisieren Sie sich in Gruppen (3-5 Personen) und einigen Sie sich auf einen
Titel für das Gedicht. Erstellen Sie eine Text- (`.txt`) oder eine Markdown
`.md` Datei mit dem Namen des Gedichts.

Arbeiten Sie auf einem neuen Branch.

```bash
git checkout -b hello-world
```

Jedes Gruppenmitglied erstellt Beiträge mit separaten Commits.
Führen Sie all Ihre Änderungen auf einem Fork zusammen.
Sie können direkt alle auf einem Fork arbeiten oder mit `merge` einen Branch aus
einem anderen Fork in ihren Branch mischen.

```bash
# Erstellen eines Remotes.
git remote add GRUPPENMITGLIED git@github.com:GRUPPENMITGLIED/git-gedicht.git
# Aktuelle Änderungen runterladen, es wird aber noch nichts geändert
git fetch GRUPPENMITGLIED
# Änderungen vom branch hello-world aus remote GRUPPENMITGLIED in aktuellen
# branch mergen
git merge GRUPPENMITGLIED/hello-world
```



Erstellen Sie einen Absatz in Ihrem Gedicht oder ändern Sie bereits vorhandene
Zeilen in Ihrem ❤️-Texteditor.


`hello-world.md`
```markdown
# Hello World

Erst ein, dann zwei
dann drei, dann vier,
irgendwas mit 🦈
dann merge hier.
```

Pushen Sie Ihre Änderungen auf den Fork Ihres Gruppenmitglieds.
```bash
git add hello-world.md
git commit
git push GRUPPENMITGLIED/hello-world
```

Eventuell müssen konflikte erst behoben werden:

```bash
git fetch GRUPPENMITGLIED
git merge GRUPPENMITGLIED/hello-world
git commit
```

## Zurückführen in das Original

Wenn Sie mit Ihrem Gedicht zufrieden sind erstellen Sie ein
pull request in dem original Repository:
- https://github.com/AnHeuermann/git-gedicht/pulls




