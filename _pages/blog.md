---
layout: personal
title: Writing
description: Essays and notes on AI speech, agency, philosophy, and everyday life.
permalink: /blog/
section: writing
---
<header class="index-header">
  <h1>Writing</h1>
  <p>Essays and notes on agency, responsibility, and the ways we understand our lives.</p>
</header>
<section class="writing-feature" aria-labelledby="recent-writing-title">
  <h2 class="index-section-title" id="recent-writing-title">Recent writing</h2>
  {% include personal/featured-essay.liquid %}
</section>
<section class="writing-archive" aria-labelledby="earlier-writing-title">
  <h2 class="index-section-title" id="earlier-writing-title">Earlier essays and notes</h2>
  <div class="writing-list">
    {% assign posts = site.posts | sort: 'writing_order' %}
    {% for post in posts %}
    <article class="writing-row">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%Y' }}</time>
      <div><h3><a href="{{ post.url | relative_url }}"{% if post.lang %} lang="{{ post.lang }}"{% endif %}>{{ post.home_title | default: post.title }}</a></h3><p{% if post.lang %} lang="{{ post.lang }}"{% endif %}>{{ post.description }}</p><span class="writing-meta">{{ post.topic }}</span></div>
    </article>
    {% endfor %}
  </div>
</section>
