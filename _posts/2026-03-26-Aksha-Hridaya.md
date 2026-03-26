---
layout: post
title: Akṣa-hṛdaya
subtitle: The heart of dice — Ṛtuparṇa and Nala on probability (Sanskrit with English gloss)
---

<link rel="stylesheet" href="{{ '/assets/css/reader.css' | relative_url }}">

{% assign book = site.data["aksha-hridaya"] %}
{% comment %}
  Text from _data/aksha-hridaya.yml (build: python scripts/build_aksha_hridaya_yml.py).
  English glosses live in scripts/aksha_hridaya_meanings_en.py.
{% endcomment %}
<div class="reader-container aksha-hridaya-reader markdown-body">
  <h2 class="meter-heading">{{ book.title_sa }}</h2>
  <p class="aksha-intro">{{ book.intro }}</p>
  <div class="translation-block aksha-intro-en">
    <div class="prose-text">{{ book.intro_en | markdownify }}</div>
  </div>

{% for section in book.sections %}
  <section class="aksha-section">
    <h2 class="meter-heading">॥ {{ section.meter }} ॥</h2>
{% for verse in section.verses %}
    <div class="verse-card">
      <h3 class="verse-number">Verse {{ verse.id }}</h3>
      <div class="sanskrit-text">{{ verse.text | newline_to_br }}</div>
      <div class="translation-block">
        <div class="prose-text">
          <p class="translation-label"><strong>Translation:</strong></p>
          {{ verse.meaning | markdownify }}
        </div>
      </div>
    </div>
{% endfor %}
    <hr class="section-rule" />
  </section>
{% endfor %}
</div>
