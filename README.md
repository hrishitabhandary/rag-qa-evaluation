# rag-qa-evaluation
# RAG QA Evaluation

This repository contains code used for transcript extraction and QA generation for the RAG assessment.

## Project Structure

- `QA Automated/` – Scripts and experiments for automated QA generation:
  - `main.py` – Generate transcripts with timestamps from YouTube videos, Experimented with transformer-based QA generation (FLAN-T5)
  - qa-output/
     - `transformers_qa.txt` – sample output of automated QA generation
  -transcripts
    Transformers.txt
-  `QA Manual/` -
  -transcripts
    - Transformers.txt
  - `main.py` – Generate transcripts with timestamps from YouTube videos

## Notes

- Final QA pairs were manually created and are included in the submitted report.
- Automated QA generation was explored but outputs were not consistently high-quality.
- This repository demonstrates both manual preparation (via Word report) and experimental automation.

##  How to Run

```bash
# Install dependencies
pip install youtube-transcript-api torch transformers sentencepiece

# Run transcript generation
python transcript_script.py

# Run automated QA generation (experiment)
python qa_generation.py
