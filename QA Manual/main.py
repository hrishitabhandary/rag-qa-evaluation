from youtube_transcript_api import YouTubeTranscriptApi

videos = {
    "Neural Networks": "aircAruvnKk",
    "Transformers": "wjZofJX0v4M",
    "Deep Learning Hindi 1": "fHF22Wxuyw4",
    "Deep Learning Hindi 2": "C6YtPJxNULA"
}

ytt_api = YouTubeTranscriptApi()

for title, video_id in videos.items():
    print(f"\n--- {title} ---\n")

    try:
        transcript = ytt_api.fetch(video_id, languages=["en", "hi"])

        # Create dynamic filename
        filename = title.replace(" ", "_") + ".txt"

        #  Save transcript WITH timestamps
        with open(filename, "w", encoding="utf-8") as f:
            for entry in transcript:
                f.write(f"{entry.start:.2f}s -> {entry.text}\n")

        print(f"Transcript saved to {filename} ✅")

        # Preview (still useful)
        preview_text = " ".join([entry.text for entry in transcript])
        print("\n--- Preview ---")
        print(preview_text[:300])

        # Print timestamps in terminal (first 10)
        print("\n--- Timestamps ---")
        for entry in transcript[:10]:
            print(f"{entry.start:.2f}s -> {entry.text}")

    except Exception as e:
        print(f"Error fetching {title}: {e}")