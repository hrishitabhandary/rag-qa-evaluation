from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import os

videos = {
    "Neural Networks": "aircAruvnKk",
    "Transformers": "wjZofJX0v4M",
    "Deep Learning Hindi 1": "fHF22Wxuyw4",
    "Deep Learning Hindi 2": "C6YtPJxNULA"
}

# Folders
os.makedirs("transcripts", exist_ok=True)
os.makedirs("qa_output", exist_ok=True)

# APIs
ytt_api = YouTubeTranscriptApi()

#  Better model than t5-small
generator = pipeline("text2text-generation", model="google/flan-t5-base")

for title, video_id in videos.items():
    print(f"\n--- {title} ---\n")

    try:
        transcript = ytt_api.fetch(video_id, languages=["en", "hi"])

        filename = title.replace(" ", "_").lower()

        #  Save transcript
        txt_path = os.path.join("transcripts", f"{filename}.txt")
        with open(txt_path, "w", encoding="utf-8") as f:
            for entry in transcript:
                f.write(f"{entry.start:.2f}s -> {entry.text}\n")

        #  BIG chunks (~200 words)
        chunks = []
        current_chunk = ""
        word_limit = 200

        for entry in transcript:
            text = entry.text.replace("\n", " ")

            # remove noise
            if len(text.strip()) < 10:
                continue

            current_chunk += " " + text

            if len(current_chunk.split()) >= word_limit:
                chunks.append(current_chunk.strip())
                current_chunk = ""

        if current_chunk:
            chunks.append(current_chunk.strip())

        print(f"✅ {len(chunks)} chunks created")

        #  Generate QA
        qa_file = os.path.join("qa_output", f"{filename}_qa.txt")

        with open(qa_file, "w", encoding="utf-8") as f:
            for i, chunk in enumerate(chunks[:8]):  # limit for quality

                prompt = f"""
You are creating evaluation questions for a RAG system.

From the context below, generate ONE meaningful, non-trivial question 
that tests understanding of a key concept. Avoid simple or obvious questions.

Then provide a clear and complete answer based ONLY on the context.

Format:
Question: ...
Answer: ...

Context:
{chunk}
"""

                result = generator(
                    prompt,
                    max_length=150,
                    do_sample=True,
                    temperature=0.7
                )

                qa_text = result[0]['generated_text']

                f.write(f"QA {i+1}:\n{qa_text}\n\n")

        print(f"✅ QA saved to {qa_file}")

        # Preview
        print("\n--- Sample QA ---")
        print(qa_text)

    except Exception as e:
        print(f"❌ Error fetching {title}: {e}")