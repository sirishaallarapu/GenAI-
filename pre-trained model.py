from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
text = """Artificial intelligence is transforming industries across the world. 
Companies are investing in AI technologies to improve efficiency, 
automate tasks, and gain insights from large datasets. AI is expected to play a crucial role in healthcare, 
finance, and various other sectors in the coming years."""
summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
print("Summary:", summary[0]['summary_text'])


