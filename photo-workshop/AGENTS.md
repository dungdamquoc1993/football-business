# Photo workshop operating instructions

Read this file, then the relevant current job brief and the matching entries in 04-WORKSPACE/source-index.json before image work. Keep workshop documentation, filenames, prompts and records in English. User conversation may remain Vietnamese.

## Ownership and source handling

This workshop owns source files, editing history and approved image sets. Marketing owns posts, campaigns, publication IDs and performance; link to its records rather than duplicating them. Catalog/admin owns current product/color IDs and stock. Never infer current stock from photos or the legacy catalog manifest.

Preserve originals unchanged. Intake new files from 01-INBOX into 04-WORKSPACE/sources by source type and batch; register original path/name, current relative path, SHA-256, size, stable asset ID and provenance before clearing intake. Do not delete intake files until the registered copy is verified. Detect duplicates by hash, but do not merge distinct source claims silently. Allocate new SRC IDs after the current maximum; never renumber existing IDs.

Existing source-index entries have not been visually identified. Null product_color means unknown, not missing stock. Inspect images before assigning model, color, view or factual confidence. Historic labels may differ from current catalog labels; verify mapping. Prior AI edits are not authoritative evidence of hidden construction. For this refresh, user correction after pilot review establishes existing legacy AI images as the primary edit bases: preserve their form, color, lighting, background and composition. Use own photos only for concrete local corrections or unseen details; do not reconstruct the entire product from own photos. Supplier references support intended healthy silhouette. Missing legacy prompts stay unknown.

## Jobs and generation

Use 04-WORKSPACE/jobs/YYYY-MM-DD-short-name with BRIEF.md, runs.jsonl and decisions.jsonl. Separate user decisions from assistant proposals. Read the image generation skill when generation/editing begins.

Prepare each input deliberately: own photos for observed construction; supplier photos for the exact color and missing views; legacy AI images for presentation; external references for pose/lighting/composition. Reference style must not override actual product geometry, logos, seams, sole or color layout. Record unsupported views rather than inventing certainty.

Each run records run_id, time, product/color ID or unresolved label, input asset IDs with roles, exact submitted prompt, tool/model if available, output paths and hashes, parent run/image when editing, and observed limitations. Preserve actual prompts, not reconstructed substitutes. Register generated images with stable IMG IDs in the job records.

Start with one well-documented color to establish the visual approach before scaling. Core/extra view lists in the brief are proposals until approved. Image evidence status and stock availability are separate.

## Review and release

Put numbered review images in 02-REVIEW/product/color/revision. Never overwrite a revision submitted for review. Record approval scope and source of approval; do not treat generation or silence as approval.

Release approved sets to 03-READY/By-product/product/color. Keep prompt files and logs out. Use descriptive ordered image filenames with revision markers. READ-ME-FIRST.txt is optional, maximum four short lines: core views; extras and their purpose; quick posting selection; material limitation if needed. Do not place empty examples in ready folders.

When preparing a campaign, copy the chosen approved files into 03-READY/By-campaign/date-name/product and record their image IDs, hashes and source release in the job release record. Campaign selections are frozen; changing them creates a new selection revision. Product releases are reusable; no independent editing of their campaign copies. Promotion of a newer product release moves the prior release into the job's retained releases and records the change. Keep a release record containing release ID, product/color, image IDs, approval reference and ready paths.

Log publication usage by linking exact release/image IDs to the owning marketing record and post/ad IDs when actually known. Delivery does not imply publication. Reported historical effectiveness is user observation until linked to measured performance.

## Cleanup triggers

After review: record selected/rejected images and reasons; remove superseded candidates from the current review surface, retaining material revisions with the job.
After release/publication: update release and usage links; verify ready files match approved hashes.
At job close: remove reproducible temporary files only, consolidate meaningful attempts, and keep originals, prompts, approvals and every published version. Never automatically delete originals or published assets. README instructions are execution triggers, not a background scheduler.
At the next job: check duplicates, unresolved mappings, broken links, current release and prior corrections before generating.

The former san-pham folder and its compatibility aliases were removed after reference checks. source-index.json original_path values are historical provenance, not live links; use path to open an asset. Physical image originals and preserved posting derivatives live here. Supplier quotes are in `supplier-quotes/` at the repo root. Marketing keeps posting selections, hashes and publication evidence in `marketing/fanpage-posts/`; do not retain another image library there. Do not rewrite historical narratives to imply new images existed earlier.

For the 2026-11-08 refresh, selected-review-v01.json owns the selected 96-image review package. Older review revisions moved into the job review-history; review-relocations.json resolves original submitted paths. runs.jsonl preserves historical output_path and adds current_path where relocated. The user approved all 12 sets on 2026-11-08; see release-v01.json for the exact released images and hashes.
