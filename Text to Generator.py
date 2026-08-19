import os
from huggingface_hub import InferenceClient
from datetime import datetime
HF_API_KEY ="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"
MODELS = [
"black-forest-labs/FLUX.1-schnell",
"stabilityai/stable-diffusion-xl-base-1.0",
"stabilityai/sdxl-turbo",
]

client = InferenceClient(api_key=HF_API_KEY,provider='auto')

while True:
    prompt = input("Enter your prompt (or type 'exit' to quit): ")
    if prompt.lower() == 'exit':
        print("Goodbye!")
        break
    image = None

    for model in MODELS:
        image = client.text_to_image(prompt,model=model)
        break

    if image:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_image_{timestamp}.png"
        image.save(filename)
        image.show()