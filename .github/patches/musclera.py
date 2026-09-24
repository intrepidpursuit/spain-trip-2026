# One-off patch: add La Musclera as the Sep 24 backup. Idempotent.
CO = '<span class="tag co" tabindex="0" data-tip="Clothing optional" aria-label="Clothing optional">CO</span>'

d = open('day.html', encoding='utf-8').read()
if 'Backup: La Musclera beach' not in d:
    old = "<li><time>13:30</time><span>Castell de Santa Florentina — but check it is actually open. September is Saturdays only, 10:00–12:00, per the castle's own site.</span></li>"
    assert d.count(old) == 1, 'day sched anchor'
    d = d.replace(old, old[:-len('</span></li>')] + " Backup: La Musclera beach, five minutes down the coast.</span></li>")
    anchor = '<div class="opt-grid"><div class="optc"><img data-wiki="Canet de Mar" alt="Skip the castle">'
    assert d.count(anchor) == 1, 'day card anchor'
    card = ('<div class="opt-grid"><div class="optc"><img data-wiki="Arenys de Mar" alt="La Musclera"><div class="ob">\n'
            '              <h4>La Musclera ' + CO + '</h4>\n'
            '              <div class="ok">Backup · Beach</div>\n'
            "              <p>Five minutes down the coast from Canet, between Arenys de Mar and Caldes d'Estrac. Drops straight into the 13:30 castle slot and still gets you to Girona by 15:45. Coarse sand — water shoes help.</p>"
            '<div class="ol"><a href="https://www.google.com/maps/search/?api=1&amp;query=Platja+de+la+Musclera+Arenys+de+Mar" target="_blank" rel="noopener">Maps ↗</a>'
            '<a class="nav" href="https://www.google.com/maps/dir/?api=1&amp;destination=Platja+de+la+Musclera+Arenys+de+Mar&amp;dir_action=navigate" target="_blank" rel="noopener">Navigate ▸</a></div>\n'
            '            </div></div><div class="optc"><img data-wiki="Canet de Mar" alt="Skip the castle">')
    d = d.replace(anchor, card)
    open('day.html', 'w', encoding='utf-8').write(d)

i = open('index.html', encoding='utf-8').read()
old = '<li><time>13:30</time><span>Castell de Santa Florentina &mdash; the castle at Canet</span></li>'
if old in i:
    i = i.replace(old, '<li><time>13:30</time><span>Castell de Santa Florentina &mdash; the castle at Canet &middot; backup: La Musclera ' + CO + '</span></li>')
    open('index.html', 'w', encoding='utf-8').write(i)
print('patched')
