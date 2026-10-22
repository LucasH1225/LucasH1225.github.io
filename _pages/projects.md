---
layout: personal
title: Projects
description: Personal AI tools, robot coverage research, physics-driven games, and reusable website-building workflows.
permalink: /projects/
section: projects
---
<header class="index-header">
  <h1>Projects</h1>
  <p>Tools for everyday life, experiments in robot planning, and games built around physical interaction.</p>
</header>
<section aria-labelledby="selected-projects-title">
  <h2 class="index-section-title" id="selected-projects-title">Selected projects</h2>
  <div class="project-list">
    {% assign projects = site.projects | where: 'featured', true | sort: 'featured_order' %}
    {% for project in projects %}{% include personal/project-row.liquid project=project %}{% endfor %}
  </div>
</section>
<section class="secondary-projects" aria-labelledby="workflow-title">
  <h2 class="index-section-title" id="workflow-title">Tools and workflows</h2>
  {% assign workflows = site.projects | where: 'featured', false | sort: 'order' %}
  {% for project in workflows %}
  <article class="secondary-project">
    <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
    <p>{{ project.summary }}</p>
    <div class="project-bottom"><span class="technology">{{ project.stack }}</span><span class="status">{{ project.status }}</span></div>
  </article>
  {% endfor %}
</section>
