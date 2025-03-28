from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")
sentence = "Hello, Are you attempting the test today?"
tokens = tokenizer(sentence, return_tensors="pt")
print(tokens)
