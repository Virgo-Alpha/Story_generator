# TODO: Get a free LLM API
# TODO: Test the API using a simple prompt

import openllm

client = openllm.client.HTTPClient('http://localhost:3000')
response = client.query('What is the capital of France?')

print(response)
