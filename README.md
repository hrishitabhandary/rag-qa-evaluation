# RAG QA Evaluation

This repository contains code used for transcript extraction and QA generation for the RAG assessment.

## Project Structure

```
LIVO.AI ASSESSMENT/
│
├── QA Manual/
│   ├── main.py              # Generates transcripts with timestamps for 4 YouTube videos
│   └── 4 transcript .txt files created
│
├── QA Automated/
│   ├── main.py              # Generates transcripts & experiments with transformer-based QA generation (FLAN-T5)
│   ├── 4 transcript .txt files
│   └── qa_output/           # Generated QA outputs (filename_qa.txt)
```

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
