# Copilot instructions for resume-jd-matcher

Quick context
- Purpose: small pipeline to match resumes to job descriptions (JD) using text preprocessing, feature extraction, and similarity scoring.
- Data: `data/raw/` contains plain text sample JDs (`data/raw/sample_jds/jd_1.txt`) and resumes (`data/raw/sample_resumes/resume_1.txt`). Processed artifacts belong in `data/processed/`.

Where to look first
- `src/` is the source package. Key logical areas:
  - `src/preprocessing/` — text cleaning, tokenization, normalization
  - `src/features/` — feature engineering (bag-of-words, tf-idf, engineered skill features)
  - `src/similarity/` — scoring functions (cosine, soft matching, ensemble)
  - `src/skills/` — curated skill lists, heuristics for skill extraction
- `src/main.py` is the expected entrypoint for orchestration (read raw data → preprocess → extract features → compute similarity → output results).

Concrete coding patterns and conventions
- Small modules per responsibility. Add new algorithms under the appropriate package (e.g., a new scoring algorithm goes in `src/similarity/`).
- Tests go in `tests/` with filenames `test_*.py` and import from `src` (e.g., `from src.similarity import my_score`). Use `pytest` as test runner.
- Data files are plain text; code should handle simple newline-separated plaintext. See `data/raw/sample_resumes/resume_1.txt` for the expected minimal format.

Common developer workflows
- Setup: create a venv, then `pip install -r requirements.txt` (this project relies on `nltk`, `scikit-learn`, `pandas`, etc.).
- Run (expected): `python -m src.main` (or `python app.py` if `app.py` is implemented to call `src.main`).
- Tests: `pytest` (run from repo root).
- When adding dependencies: update `requirements.txt` and run install in CI / locally.

Examples (copy-paste ready)
- Read a raw resume: `open('data/raw/sample_resumes/resume_1.txt').read()`
- Typical pipeline call (pseudocode):

  from src.preprocessing import clean_text
  from src.features import extract_features
  from src.similarity import score_pair

  text = clean_text(open('data/raw/sample_resumes/resume_1.txt').read())
  feats = extract_features([text])
  score = score_pair(feats[0], jd_feats)

Project-specific tips
- Keep raw data in `data/raw/` and write artifacts to `data/processed/` to avoid reprocessing during development.
- Favor algorithm code in `src/` and small, well-scoped functions that are easy to unit test.
- Use small sample files under `data/raw/sample_*` to write and run quick unit tests.

What not to guess
- There is no current CI or test policy in this repo—ask before adding CI workflows or presets.
- There is no canonical CLI yet; prefer modifying `src/main.py` or `app.py` for top-level behavior and document the new entrypoint in the README.

If anything above is unclear or you want me to include conventions for commit messages, CI, or coding style, tell me which area to expand and I will iterate. ✅