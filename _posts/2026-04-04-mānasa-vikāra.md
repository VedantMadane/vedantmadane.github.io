---
layout: post
title: मानस-विकाराः
subtitle: Mahābhārata and Rāmāyaṇa through cognitive psychology and behavioral economics
tags: [sanskrit, mahābhārata, rāmāyaṇa, psychology]
audio_sync: false
# audio_file: /assets/audio/FILENAME.mp3
---

<link rel="stylesheet" href="{{ '/assets/css/reader.css' | relative_url }}">

{% assign book = site.data['manasa-vikara'] %}
{% capture verse_nl %}
{% endcapture %}
{% comment %}
  _data/manasa-vikara.yml — source: C:\Projects\shatakam\mānasa-vikāra.txt
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
<p class="section-head-en">{{ book.title_en }}{% if book.subtitle_en %} — {{ book.subtitle_en }}{% endif %}</p>
<div class="prose-text">{{ book.intro_visible | markdownify }}</div>

{% for sec in book.sections %}
<section class="khandam" id="{{ sec.slug }}">
  <h3 class="section-head-iast">{{ sec.title_sa }}</h3>
  {% if sec.title_en %}<p class="section-head-en">{{ sec.title_en }}</p>{% endif %}

  {% if sec.plan_after_verses != true %}
    {% if sec.slug == 'yojana' %}
    <div class="prose-text">{{ book.plan_commentary | markdownify }}</div>
    {% endif %}
  {% endif %}

{% for verse in sec.verses %}
  <div class="verse-block-manasa">
    <p class="verse-topic">{% if verse.topic_en %}{{ verse.topic_en }}{% endif %} <small class="text-muted">({{ verse.meter_en }})</small>{% if verse.id %} — śloka {{ verse.id }}{% endif %}</p>
    <div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v-{{ sec.slug }}-{{ verse.id }}">
      {% assign _raw = verse.text_sa | strip %}
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
    {% if verse.meaning and verse.meaning != '' %}
    <div class="prose-text translation-block-manasa">
      <p class="translation-label"><strong>Gloss:</strong></p>
      {{ verse.meaning | markdownify }}
    </div>
    {% endif %}
  </div>
{% endfor %}

  {% if sec.plan_after_verses == true %}
  <div class="prose-text">{{ book.plan_commentary | markdownify }}</div>
  {% endif %}

  {% unless forloop.last %}<hr class="section-rule" />{% endunless %}
</section>
{% endfor %}

<details>
<summary>पदच्छेदः, अन्वयः, शब्दार्थः च (word analysis)</summary>
<div class="prose-text">{{ book.appendix_word_analysis | markdownify }}</div>
</details>

<details>
<summary>नूतन-शब्द-व्युत्पत्तिः (glossary of coined terms)</summary>
<div class="prose-text">{{ book.appendix_glossary | markdownify }}</div>
</details>

</div>

<script src="{{ '/assets/js/audio-sync.js' | relative_url }}"></script>
