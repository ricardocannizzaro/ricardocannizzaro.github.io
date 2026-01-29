---
permalink: /
title: "Ricardo Cannizzaro"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

## About
<!-- Intro -->
I am a causal AI and robotics researcher and final-stage DPhil (PhD) candidate with the [Cognitive Robotics Group](https://ori.ox.ac.uk/labs/cognitive-robotics-group) and the Goal-Oriented Long-Lived Systems group at the [Oxford Robotics Institute](https://ori.ox.ac.uk), [University of Oxford Department of Engineering Science](https://eng.ox.ac.uk), supervised by [Prof Lars Kunze](https://scholar.google.com/citations?user=TLC0azYAAAAJ&hl=en) and [Prof Nick Hawes](https://scholar.google.co.uk/citations?user=bRsi4zoAAAAJ&hl=en). I have submitted my PhD thesis and am currently awaiting defence.

My doctoral research was funded by the Australian Defence Science and Technology Group, where I previously worked as a Defence Research Scientist on trusted autonomous systems.

During my PhD, I completed two PhD Research Internships at [Microsoft Research (MSR)](https://www.microsoft.com/en-us/research/) with the AI Interaction and Learning and People-Centric AI teams in Redmond. My work focused on improving consistency and reasoning in foundation and generative AI models operating in interactive, causally complex environments, including counterfactual consistency for image fine-tuning and parallel-world consistency for generative modelling in video game environments.

I have over 10 years’ experience designing and implementing AI/ML-enabled software and hardware systems for learning, inference, and decision-making under uncertainty, spanning real-world robotics deployments and large-scale simulated environments.

## Research Focus
<!-- PhD Research -->
My research explores probabilistic generative causal models for encoding structured knowledge and uncertainty, combining domain expertise with data-driven learning. Methodologically, this includes causal representation learning, Bayesian inference, probabilistic programming, and deep generative models such as diffusion models and transformers.

A central focus of my work is learning human-aligned causal representations and developing faithful, counterfactual-based explanations that support understanding and trust by non-technical users. I am particularly interested in human-facing AI systems that must behave consistently, robustly, and transparently in real-world settings.

<!-- Research Interests -->
Research Interests: *probabilistic generative causal modelling, Bayesian causal inference, causal representation learning, counterfactual reasoning and explanations, probabilistic programming, foundation and generative models, uncertainty-aware decision-making, and human-centred AI systems.*

## Currently Seeking
<!-- Mission Statement -->
I am currently seeking full-time industry research roles, particularly within applied research environments such as Microsoft Research.

## News
<!-- Recent News -->
{% assign news_items = site.data.news | sort: "date" | reverse %}
<ul>
{% for item in news_items limit: 15 %}
	<li><strong>{{ item.date | date: "%d/%m/%Y" }}</strong> — {{ item.text }}</li>
{% endfor %}
</ul>

[All news](/news/)

## Contact
<!-- Call to Action -->
To have a chat about my research or to discuss collaborations, please reach out to me at [ricardo@robots.ox.ac.uk](mailto:ricardo@robots.ox.ac.uk) or via [LinkedIn](https://www.linkedin.com/in/ricardo-cannizzaro).

## Work Experience &amp; Education
<!-- Work Experience -->
<details>
  <summary style="font-weight: bold; cursor: pointer;">Work Experience</summary>
  <div id="work-experience" markdown="1">
  Before my DPhil I was working as a Defence Research Scientist in the Aerial Autonomy group of the [Australian Defence Science and Technology Group](https://www.dst.defence.gov.au) (2017-2021), where my research focused on decentralised teams of autonomous aerial and ground robots for missions in challenging uncertain and complex environments, such as the urban terrain. My research was at the exciting intersection of AI/ML, software and hardware engineering to develop autonomous behaviours, integrate them into hardware, and experimentally validate the complete autonomous systems through flight trials in real urban environments across Australia, Singapore, Montreal, and New York City.  

  My AI/ML and robotics research at DSTG has spanned a wide range of robotics and AI/ML topics, including:
  * [Decentralised task planning in unknown environments with heterogeneous multi-robot systems](https://ieeexplore.ieee.org/abstract/document/9560822)
  * [Robotic swarming methods for scalable and adaptive drone data-ferrying](https://ieeexplore.ieee.org/document/8463151)
  * Adaptive GNSS-SLAM localisation methods for autonomous robot navigation in mixed GNSS-available environments (internal technical report)
  * Path- and motion-planning for safe, smooth, and efficient aerial robot navigation (internal technical report)
  * Command, Control, Communication, and Computers (C4) architectures for autonomous drone system integration with federated common operating picture software (internal technical report)
  * [A novel Random-Finite-Set-based SLAM algorithm for aerial robots with scanning and solid-state LIDARS](https://ssl.linklings.net/conferences/acra/acra2019_proceedings/views/includes/files/pap105s1-file1.pdf)
  * [An evaluation of LIDAR and X-band radar sensors in a particle-dense environment for resilient drone sensing](https://www.researchgate.net/publication/348620221_Evaluation_of_LIDAR_and_X-Band_Radar_Sensors_in_a_Particle-Dense_Environment)
  * [Passive source localisation with a novel particle-filter-based bearings-only tracking algorithm](https://www.araa.asn.au/acra/acra2015/papers/pap170.pdf)
  </div>
</details>

<!-- Education -->
<details>
  <summary style="font-weight: bold; cursor: pointer;">Education</summary>
  <div id="education" markdown="1">
  
  <h3> DPhil (PhD) Engineering Science </h3>
  Oxford Robotics Institute, University of Oxford  
  *Thesis submitted; defence expected 2026*

  **Supervisors:** Prof Lars Kunze and Prof Nick Hawes  
  (Cognitive Robotics Group; Goal-Oriented Long-Lived Systems Group)  
  Funded by the Australian Defence Science and Technology Group

  **Thesis:** *Causal Artificial Intelligence for Robust Robot Reasoning under Uncertainty*

  My doctoral research focuses on uncertainty-aware and probabilistic causal modelling for learning, inference, decision-making, and explanation in complex, partially observable environments. A central theme of my work is learning human-aligned causal representations and developing faithful, counterfactual-based explanations to support understanding and trust by non-technical users.

  Methodologically, this work combines causal representation learning, Bayesian inference, probabilistic programming, and deep generative models, applied across both interactive virtual environments and real-world, hardware-integrated robotic systems. This research included, and subsequently extended, work completed through two Microsoft Research PhD internships, each forming a core thesis chapter.

  **Selected Coursework:** Oxford Scientific Entrepreneurship Course; Oxford Language Centre Italian Fast-Track Course (Parts 1–2)
  <br>

  <h3> Bachelor of Engineering (Honours) (Robotics & Mechatronics) (First Class Honours) </h3>
  I completed my Bachelor of Engineering (Honours) (Robotics & Mechatronics) (First Class Honours) in 2016 at the Swinburne University of Technology in Melbourne, Australia, [School of Engineering](https://www.swinburne.edu.au/science-engineering-technology/schools-departments/engineering/index.php) (4 years + industry-based learning year at DSTG). For my honours thesis project I created an autonomous ground robot system for remote chemical detection and localisation, under the supervision of [Professor Zhenwei Cao](https://scholar.google.com/citations?user=Xgac2EoAAAAJ&hl=en) and [Dr Jennifer Palmer](https://scholar.google.com/citations?hl=en&user=R22EoSYAAAAJ). I implemented a passive chemical-emitter localisation algorithm and integrated a novel bespoke DSTG chemical detection sensor into an autonomous Clearpath Robotics [TurtleBot 2](https://clearpathrobotics.com/turtlebot-2-open-source-robot/) robot system.
  <br>

  <h3> Bachelor of Science (Mechanical Systems) </h3>
  I completed my Bachelor of Science (Mechanical Systems) in 2012 at the University of Melbourne in Melbourne, Australia, [Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/) / [Faculty of Science](https://science.unimelb.edu.au/). I spent 6 months at KTH Stockholm in 2012 as a visiting student at the [Division of Robotics, Perception and Learning](https://www.kth.se/is/rpl) and [Department of Engineering Mechanics (Aerospace Engineering)](https://www.kth.se/en/tekmek).
  </div>
</details>


