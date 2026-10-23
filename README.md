# Lucas Han — personal website

A small Jekyll site for projects and writing, hosted by GitHub Pages at https://haojunhan.com. The source lives in `LucasH1225/LucasH1225.github.io`.

## Local development

Use Ruby **3.3.5**, Bundler **2.6.5** and Python 3.10 or newer. `.ruby-version`, `Gemfile` and the tracked lockfile pin the Ruby build. Dependencies stay under ignored `vendor/`.

```sh
scripts/site setup
scripts/site build
scripts/site preview
```

Open http://127.0.0.1:8768/. The preview serves the complete generated `_site`, includes the site's real 404 page, and sends `noindex` headers locally. Re-run the build after source changes. To use another port: `scripts/site preview 8770`.

This checkout also has an ignored, locally compiled Ruby in `vendor/runtime/ruby-3.3.5/`; the helper uses it when present. Other machines should install the pinned Ruby with their preferred version manager. No global Ruby installation is modified by the helper.

## Editing content

- `index.html`: homepage biography and selected sections.
- `_data/personal.yml`: navigation, contact information, asset version and competition-essay summary/status.
- `_projects/`: four project case studies. Front matter supplies summaries to the homepage and projects index. `featured: true` and `featured_order` control homepage selection.
- `_posts/`: four published essays and two original notes marked `published: false`. Explicit permalinks preserve the published articles’ addresses. `selected` and `selected_order` control homepage writing links.
- `_pages/`: projects/writing indexes, CV landing page, 404, and compatibility pages for two retired original placeholders.
- `_layouts/`, `_includes/personal/`: shared presentation.
- `assets/personal/`: CSS, screenshot interaction, local font, project media and CV PDF.

The author authorised publication of “Should AI speech be limited?” on 23 October 2026. Its full article is published at `/blog/2026/should-ai-speech-be-limited/`, using the final-essay tab of the original document. Keep its competition status as result pending until a result is confirmed; do not infer an award from the date. Project status and contribution claims should track the actual implementation.

Use `asset_version` in `_data/personal.yml` when changing CSS/JS. Keep page descriptions, image alt text/dimensions and collaborator/asset credits current. Mathematical notation in the existing determinism essay uses native MathML, without a client-side library.

## Verification

`scripts/site build` performs a clean production Jekyll build and runs the standard-library site checker. The build rejects duplicate output destinations. The checker covers the intended page inventory, local references/fragments, image metadata, canonicals, feed, sitemap and unintended public files. Run `node --check assets/personal/project.js` after interaction changes.

Review representative pages at 320, 390, 768, 1024 and 1280px, and check keyboard access, screenshot tabs, zoom and no-JavaScript links. Static checks complement browser review.

## Deployment

The workflow builds/checks pull requests, retains the checked artifact for 30 days, and deploys that same artifact only from `main`/`master` to the existing `gh-pages` branch. Changes on the working feature branch do not publish. No path filters can accidentally omit CSS, plugins or CNAME changes. Action revisions and Ruby dependencies are pinned.

GitHub Pages was inspected on 23 October 2026: its source is `gh-pages` at `/`, with custom domain `haojunhan.com`. The existing account setting did not enforce HTTPS; no hosting settings were changed during the local redesign. Confirm that setting and the live certificate/redirect behaviour at release.

Before release, record the current deployment SHA/artifact. Roll back by redeploying the prior artifact or reverting the release change and rebuilding. Preserve `CNAME`. Never force-push source history for rollback.

## Reference and archived material

Local `_preview/` and `_archive/` folders hold review artifacts and source backups when present. Both are ignored by Git and excluded from Jekyll output. Earlier tracked source remains recoverable in Git history. Keep local planning notes and screenshots out of the public source repository.

The original al-folio MIT notice remains in `LICENSE`. The self-hosted Manrope font licence is at `assets/personal/fonts/OFL.txt`.
