---
layout: post
title: मानवमति भ्रमः
tags: [sanskrit, psychology, cognitive-bias]
audio_sync: false
# audio_file: /assets/audio/FILENAME.mp3
---

<link rel="stylesheet" href="{{ '/assets/css/reader.css' | relative_url }}">

{% assign book = site.data['manavamati-bhramah'] %}
{% capture verse_nl %}
{% endcapture %}
{% comment %}
  _data/manavamati-bhramah.yml – rebuild: `python scripts/build_manavamati_yml.py`
  Source: C:\Projects\shatakam\mānavamati_bhramaḥ.txt
{% endcomment %}

<div class="reader-container audio-sync-root markdown-body">

{% if page.audio_sync %}
<div class="audio-panel">
  <audio controls preload="metadata" data-audio-sync-player>
    <source src="{{ page.audio_file | relative_url }}" type="audio/mpeg">
    Your browser does not support the audio element.
  </audio>
</div>
{% endif %}

<h2 class="work-title-iast">{{ book.title_sa }}</h2>
{% if book.title_en %}<p class="section-head-en">{{ book.title_en }}{% if book.subtitle_en and book.subtitle_en != '' %} – {{ book.subtitle_en }}{% endif %}</p>{% endif %}
{% if book.intro_visible and book.intro_visible != '' %}
<div class="prose-text" markdown="1">{{ book.intro_visible | markdownify }}</div>
{% endif %}

{% for stanza in book.stanzas %}
<div class="verse-block-manasa">
  <p class="verse-topic">{{ stanza.title }}</p>
  <div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v-stanza-{{ stanza.id }}">
    {% assign _raw = stanza.text_sa | strip %}
    {% assign _lines = _raw | split: verse_nl %}
    {% assign _line_num = 0 %}
    {%- for _piece in _lines -%}
      {% assign _ln = _piece | strip %}
      {% if _ln != '' %}
        {% assign _line_num = _line_num | plus: 1 %}
        <span data-line="{{ _line_num }}" data-start="" data-end="">{{ _ln }}</span><br />
      {% endif %}
    {% endfor %}
  </div>
  {% if stanza.translation and stanza.translation != '' %}
  <div class="prose-text translation-block-manasa">
    <p class="translation-label"><strong>Translation:</strong></p>
    <p>{{ stanza.translation | escape }}</p>
  </div>
  {% endif %}

  <details>
  <summary>पदच्छेद, अन्वय, धात्वर्थ</summary>
  <div class="prose-text" markdown="1">
    {% assign _p = stanza.padaccheda | strip %}
    {% if _p != '' %}
    <p><strong>पदच्छेदः</strong></p>
    <p>{{ _p | newline_to_br }}</p>
    {% endif %}
    {% assign _a = stanza.anvaya | strip %}
    {% if _a != '' %}
    <p><strong>अन्वयः</strong></p>
    <p>{{ _a | newline_to_br }}</p>
    {% endif %}
    {% assign _d = stanza.dhatvartha | strip %}
    {% if _d != '' %}
    <p><strong>धात्वर्थः</strong></p>
    <p>{{ _d | newline_to_br }}</p>
    {% endif %}
  </div>
  </details>
</div>
{% endfor %}

</div>

<script src="{{ '/assets/js/audio-sync.js' | relative_url }}"></script>
