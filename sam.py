from google.cloud import generativelanguage_v1beta

client = generativelanguage_v1beta.GenerativeServiceClient()
models = client.list_models(parent="projects/YOUR_PROJECT_ID")
for model in models:
    print(model.name)
