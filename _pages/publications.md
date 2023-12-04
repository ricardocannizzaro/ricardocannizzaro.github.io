---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

**Note: This site is currently under construction. Some sections may be incomplete.**

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
