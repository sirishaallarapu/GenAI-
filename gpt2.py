from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
result = generator("Once there live a ghost", max_length=50, truncation=True)
print(result[0]["generated_text"])
