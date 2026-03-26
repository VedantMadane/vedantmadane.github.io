---
layout: post
title: Akṣa-hṛdaya
subtitle: The heart of dice — Ṛtuparṇa and Nala on probability (Sanskrit text)
---

<link rel="stylesheet" href="{{ '/assets/css/reader.css' | relative_url }}">

{% assign book = site.data["aksha-hridaya"] %}
{% comment %}
  Text from _data/aksha-hridaya.yml (generated from Aksha-Hridayam.txt).
  Typography matches śatakam reader — Noto Serif Devanagari on .sanskrit-text.
{% endcomment %}
<div class="reader-container aksha-hridaya-reader markdown-body">
  <h2 class="meter-heading">{{ book.title_sa }}</h2>
  <p class="aksha-intro">{{ book.intro }}</p>

{% for section in book.sections %}
  <section class="aksha-section">
    <h2 class="meter-heading">॥ {{ section.meter }} ॥</h2>
{% for verse in section.verses %}
    <div class="verse-card">
      <h3 class="verse-number">Verse {{ verse.id }}</h3>
      <div class="sanskrit-text">{{ verse.text | newline_to_br }}</div>
    </div>
{% endfor %}
    <hr class="section-rule" />
  </section>
{% endfor %}
</div>
