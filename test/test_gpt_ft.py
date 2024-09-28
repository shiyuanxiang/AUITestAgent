from openai import OpenAI

api_key = "sk-9FZknAIsf7vqPAZKM5L1GGBnyE1oCrKGe9qBV0U8vK7RfRdG"
client = OpenAI(api_key=api_key, base_url="https://api.deepbricks.ai/v1/")

file_id = "file-ZqBgthFuQSy4BAam2aQTgTa4"  # selector-fine-tune.json

client.fine_tuning.jobs.create(
  training_file=file_id,
  model="gpt-4o-mini-2024-07-18"
)

