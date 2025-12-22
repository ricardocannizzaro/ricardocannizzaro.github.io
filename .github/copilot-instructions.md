## Quick orientation for AI coding agents

This repository is a Jekyll-based GitHub Pages site (a fork of the Minimal Mistakes theme). The site is served from the `gh-pages` branch and uses Ruby/Bundler for Jekyll and Node/npm for a small JS build step.

This repository is an instantiation of the template for Ricardo Cannizzaro's academic website.
Use the CV/resume (files\ricardo_cannizzaro_cv.pdf), publications list, and publically available linkedin profile of Ricardo Cannizzaro (https://www.linkedin.com/in/ricardo-cannizzaro) to update any *new* information about his academic background, publications, and professional experience.

Update:
- _pages/about.md to reflect Ricardo Cannizzaro's current academic status, research interests, and contact information.
- _pages/projects.md to include Ricardo Cannizzaro's notable projects and contributions.

Do NOT change:
- _pages/cv.md (the CV is embedded as a PDF and should not be altered in markdown)
- _pages/terms.md (privacy policy should remain unchanged)
- _pages/publications.md (the publications list is auto-generated; do not edit manually)

High-level architecture (what to know quickly):
- Content: markdown files live in `_posts/`, `_pages/`, `_talks/`, `_publications/`, `_teaching/`, `_portfolio/` etc. New content is usually added by creating a new markdown file with YAML front matter in the appropriate folder.
- Templates: Liquid templates live under `_layouts/` and reusable fragments under `_includes/` (eg. `_layouts/default.html` calls `{% include head.html %}` and `{% include scripts.html %}`). Refer to these when changing page structure or metadata.
- Styling: SCSS lives in `_sass/` and the compiled stylesheet is `assets/css/main.css`. Keep changes to SASS scoped to `_sass/*` and the theme variables in `_sass/_variables.scss`.
- JS: `package.json` contains small build scripts (uglify + watch). The `uglify` script builds `assets/js/main.min.js`. Use `npm run build:js` or `npm run uglify` to rebuild JS.
- Config: site-wide settings live in `_config.yml` (base URL, collections, defaults). Changing `_config.yml` requires restarting the Jekyll server.
- Static files: uploaded assets go into `files/` and `images/` and are referenced with `{{ base_path }}` or absolute paths depending on `baseurl`.
- Generators: The repo contains helper scripts in `markdown_generator/` and `talkmap/` (Python/Jupyter notebooks) to auto-generate markdown for talks/publications. Inspect those before reimplementing generation logic.

Common developer workflows (commands observed in repo)
- Install Ruby deps and run Jekyll (recommended):
  - Install Ruby + Bundler, then: `bundle install`
  - Serve locally: `bundle exec jekyll liveserve` (this repo's README uses `liveserve`; if that fails try `bundle exec jekyll serve`)
  - If you change `_config.yml`, restart the server — Jekyll doesn't auto-reload that file.
- JS tasks (small):
  - Build JS: `npm run build:js` or `npm run uglify`
  - Watch JS changes: `npm run watch:js`

Project-specific conventions and patterns
- Front matter defaults: Many pages inherit defaults from `_config.yml` (for example, posts default to `layout: single`, `comments: true`, `author_profile: true`). When adding content, omit repeated fields if defaults suffice.
- Collections: `talks`, `publications`, `portfolio`, and `teaching` are configured as collections in `_config.yml`; create files under `_talks/`, `_publications/`, etc. with `output: true` in their front matter if publishing individually.
- Includes & `base_path`: The project commonly uses a `base_path` include (see `_includes/base_path`) and references `{{ base_path }}` in templates — preserve this when adding absolute/relative links.
- JS/asset exclusions: `_config.yml` explicitly excludes `assets/js/_main.js`, `assets/js/plugins`, `assets/js/vendor`, `package.json`, and `node_modules` from the Jekyll build. If changing how JS is built, update the exclude list accordingly.
- Branch: `staticman` (comment system) is configured to use branch `gh-pages` in `_config.yml`. If you change comment generation, note the branch and generated path `_data/comments/{options.slug}`.

Integration points & external dependencies
- GitHub Pages (`github-pages` gem) is used via the `Gemfile`. The site is safe to run with `bundle exec jekyll` and mirrors GitHub Pages behaviour.
- Node tools: `uglify-js`, `onchange`, `npm-run-all` are used for the JS build/watch steps.
- Optional services configured in `_config.yml`: Disqus, Discourse, Google analytics. They are disabled by default — provide credentials in `_config.yml` to enable.

Practical tips for code edits (actionable examples)
- To change header/meta tags: edit `_includes/head.html` or `_includes/seo.html` (both are included from `_layouts/default.html`).
- To modify page chrome (masthead, footer): edit `_includes/masthead.html` and `_includes/footer.html`.
- To add a new talk: create `/_talks/YYYY-MM-DD-title.md` with YAML front matter using `layout: talk` (see `_layouts/talk.html`).
- To update CSS variables: edit `_sass/_variables.scss` and re-run the site build.
- To change JS behavior: update `assets/js/_main.js` and run `npm run build:js` to produce `assets/js/main.min.js` (Jekyll excludes the unminified file by default).

What NOT to change lightly
- `Gemfile` and `Gemfile.lock` — the README warns to delete `Gemfile.lock` if you get a security alert, but otherwise changes can affect GitHub Pages. When updating dependencies, test locally with `bundle exec jekyll liveserve`.
- `base_path` include and `_config.yml` baseurl — changing base-path behaviour affects all asset and link references site-wide.

When you update this file
- Keep the file short and factual. If you add new developer scripts or automation, add a one-line entry here with exact command invocations.

If something is missing or unclear, point me to a file or task you want covered and I'll expand this guidance or add examples (front matter snippets, full command sequences, or checks).

Files to reference while coding: `_config.yml`, `_layouts/default.html`, `_includes/head.html`, `_sass/_variables.scss`, `assets/js/_main.js`, `package.json`, `Gemfile`, `markdown_generator/`.
