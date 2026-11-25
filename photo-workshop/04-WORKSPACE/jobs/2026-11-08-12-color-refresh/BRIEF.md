# Twelve-color refresh — current state

Delivered 2026-11-08: **12 sets × 8 images = 96 selected images**, approved by the user and released to `03-READY/By-product`. No images published or catalog media changed. See `release-v01.json` for approval and verified image hashes.

Current approved images: `photo-workshop/03-READY/By-product/`. Quick overviews: `photo-workshop/03-READY/Preview/`. The review queue is empty; historical paths resolve through review-relocations.json.

## Confirmed scope

- Tiempo 8: red/black, royal blue/silver, white/gold, sky blue/lime.
- Messi: silver, sky blue, black/yellow, red/white, navy/silver with orange stripes and white outsole. User explicitly clarified the last color; source folder is xanh-than-cam.
- Bata: white/turquoise, white/red, white/silver.

User reports seven stocked colors and five quickly replenishable colors. Not a live inventory check; size SKUs are separate from image sets.

## Working direction and corrections

Preserve prior successful legacy AI style, attractive healthy silhouette, color, composition and lighting. Own photos supply evidence of hidden details and concrete mismatches; their temporary shipping compression must not define final form. Supplier photos support intended form and color. Do not reconstruct the whole product or add unsupported anatomy.

First silver pilot was rejected for overall appearance. Subsequent Tiempo examples established local correction and low rear viewpoints that occlude unsupported tongues. Actual Tiempo tongues have no pull loops. User accepted low rear and angular-tip side images as ordered in their screenshot, superseding assistant's earlier internal rejection of angular-tip side. Exact approval mapping is in decisions.jsonl.

Sixteen legacy images retained unchanged; two accepted pilots reused; seventy-eight edited or additional images selected. Assistant QA corrected duplicate-shoe compositions, false tongue loops/logos, wrong lace/lining colors, missing silver/blue sole zigzag paint, and invented Bata silver toe perforations. Preserve the user's accepted tolerance; do not keep polishing a set without a concrete reason.

## Evidence and limitations

291 imported source files: 192 legacy AI, 73 own-photo, 26 supplier files. All hashes reverified. Own photos cover seven colors with selected full-resolution inspection; other sources were also assessed through overviews. Not every source is full-resolution audited. Missing historical prompts stay unknown.

- White/gold Tiempo lacks dedicated own-photo outsole evidence: slot 06 uses lacing detail instead.
- Supplier-only Messi colors use supported exterior/material/sole views rather than unverified rear/inner views.
- Supplier-only Bata sole color is supported by supplier group images; shared mold guided by photographed turquoise sample.
- Rear labels depict photographed samples: Tiempo red/blue/lime 44, white/gold 42; Messi silver 41, sky blue 42; Bata turquoise 42. Do not present these as all-size availability.
- Fine geometry, small marks, lettering and surface texture remain AI interpretations. QA is visual, not exact pixel fidelity certification.

## Records and next action

- `scope.json`: confirmed products/colors.
- `selected-review-v01.json`: exact selected image IDs, hashes, source paths, reuse/edit classification and approval state.
- `review-checks.json`: completed checks and limits.
- `runs.jsonl`: exact submitted prompts, inputs, outputs and versions; accompanying *plan.json / *results.json files retain batches and targeted retries.
- `decisions.jsonl`: user decisions, rejections, corrections and delivery history.
- `review-history/`, `rejected/`: prior attempts retained outside the user review surface. `review-relocations.json` maps their historical review paths to current paths. Do not assume an old output_path is still live; use current_path or relocation map.

The user approved all twelve sets. Released copies are recorded in `release-v01.json`; approval does not imply campaign publication.

Post-approval cleanup completed; see cleanup-v01.json. Removed redundant approved review copies and reproducible internal QA sheets. Original sources and meaningful editing history are preserved.
