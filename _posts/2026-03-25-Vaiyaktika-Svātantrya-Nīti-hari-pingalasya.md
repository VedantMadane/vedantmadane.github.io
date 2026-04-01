---
layout: post
title: Vaiyaktika-Svātantrya-Nīti
subtitle: Based on the book 'How I Found Freedom In An Unfree World by Harry Browne (Hari Piṅgalā)
# Set to true after adding MP3 under assets/audio/ (default file: shatakam-recitation.mp3).
# Optional: shatakam_audio_url: /assets/audio/your-file.mp3
# shatakam_audio: true
---

<link rel="stylesheet" href="{{ '/assets/css/reader.css' | relative_url }}">

{% comment %}
  Data: _data/hari-pingala.yml → site.data["hari-pingala"]
  Markup mirrors _layouts/shatakam-reader.html (.verse-card, .sanskrit-text, .verse-topic, .translation-block)
  so Noto Serif Devanagari and sizing match the Mūlya-Nīti reader.
{% endcomment %}
<div class="reader-container hari-pingala-reader markdown-body">
{% for chapter in site.data["hari-pingala"] %}
<section class="hari-pingala-chapter">
<h2>{{ chapter.chapter_id }}. {{ chapter.title_sa }} ({{ chapter.title_en }})</h2>

{% if chapter.verses %}
  {% for verse in chapter.verses %}
<div class="verse-card">
  <h3 class="verse-number">Verse {{ verse.verse_id }}{% if verse.meter %} <small class="text-muted">(Meter: {{ verse.meter }})</small>{% endif %}</h3>
  {% if verse.title_sa %}
  <h4 class="verse-topic">{{ verse.title_sa }} - {{ verse.title_en }}</h4>
  {% endif %}
  <div class="sanskrit-text">{{ verse.sanskrit | newline_to_br }}</div>
  <div class="translation-block">
    <div class="prose-text" markdown="1"><strong>Meaning:</strong> {{ verse.meaning }}</div>
  </div>
</div>
  {% endfor %}
{% endif %}

{% if chapter.traps %}
  {% for trap in chapter.traps %}
<div class="verse-card trap-card">
  <h3 class="verse-topic">Trap {{ trap.trap_id }}: {{ trap.name_sa }} ({{ trap.name_en }})</h3>
  <p><strong>The Diagnosis</strong> <small class="text-muted">(Meter: {{ trap.diagnosis_verse.meter }})</small></p>
  <div class="sanskrit-text">{{ trap.diagnosis_verse.sanskrit | newline_to_br }}</div>
  <div class="translation-block">
    <div class="prose-text" markdown="1"><strong>Meaning:</strong> {{ trap.diagnosis_verse.meaning }}</div>
  </div>
  <p><strong>The Escape</strong> <small class="text-muted">(Meter: {{ trap.escape_verse.meter }})</small></p>
  <div class="sanskrit-text">{{ trap.escape_verse.sanskrit | newline_to_br }}</div>
  <div class="translation-block">
    <div class="prose-text" markdown="1"><strong>Meaning:</strong> {{ trap.escape_verse.meaning }}</div>
  </div>
</div>
  {% endfor %}
{% endif %}

<hr class="chapter-rule" />

</section>
{% endfor %}
</div>
