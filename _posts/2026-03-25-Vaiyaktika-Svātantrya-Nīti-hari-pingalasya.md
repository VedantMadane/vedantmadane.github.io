---
layout: shatakam-reader
title: Vaiyaktika-Svātantrya-Nīti
subtitle: Based on the book 'How I Found Freedom In An Unfree World by Harry Browne (Hari Piṅgalā)
# Set to true after adding MP3 under assets/audio/ (default file: shatakam-recitation.mp3).
# Optional: shatakam_audio_url: /assets/audio/your-file.mp3
# shatakam_audio: true
---
{% for chapter in site.data.shatakam %}

## {{ chapter.chapter_id }}. {{ chapter.title_sa }} ({{ chapter.title_en }})

{% if chapter.verses %}
  {% for verse in chapter.verses %}
**Verse {{ verse.verse_id }} (Meter: {{ verse.meter }})**
{% if verse.title_sa %}*{{ verse.title_sa }} - {{ verse.title_en }}*{% endif %}
> {{ verse.sanskrit | newline_to_br }}
>
> *Meaning:* {{ verse.meaning }}

  {% endfor %}
{% endif %}

{% if chapter.traps %}
  {% for trap in chapter.traps %}
### Trap {{ trap.trap_id }}: {{ trap.name_sa }} ({{ trap.name_en }})

**The Diagnosis (Meter: {{ trap.diagnosis_verse.meter }})**
> {{ trap.diagnosis_verse.sanskrit | newline_to_br }}
>
> *Meaning:* {{ trap.diagnosis_verse.meaning }}

**The Escape (Meter: {{ trap.escape_verse.meter }})**
> {{ trap.escape_verse.sanskrit | newline_to_br }}
>
> *Meaning:* {{ trap.escape_verse.meaning }}

  {% endfor %}
{% endif %}

---
{% endfor %}
