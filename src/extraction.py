import os
import json
import time
from openai import OpenAI
from dotenv import load_dotenv

# =====================================================
# Load Environment Variables
# =====================================================
load_dotenv()

# =====================================================
# Configure Mistral Client
# =====================================================
client = OpenAI(
    api_key=os.getenv("MISTRAL_API_KEY"),
    base_url="https://api.mistral.ai/v1"
)

MODEL_NAME = "mistral-small-latest"

# =====================================================
# Load Reviews
# =====================================================
def load_reviews(file_path="data/reviews.json"):
    """
    Load customer reviews from JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


# =====================================================
# Build Prompt
# =====================================================
def build_prompt(review):
    """
    Create a prompt for structured information extraction.
    """

    return f"""
You are an AI Customer Support Analyst.

Analyze the following customer review.

Return ONLY valid JSON.

Do NOT include markdown.
Do NOT include explanations.
Do NOT wrap the JSON inside ```.

Allowed Categories:
- Delivery
- Product
- Refund
- Payment
- Customer Support
- App

Allowed Urgency:
- Low
- Medium
- High

Allowed Sentiment:
- Positive
- Neutral
- Negative

Output Format:

{{
    "category": "",
    "urgency": "",
    "sentiment": "",
    "summary": ""
}}

Customer Review:
"{review}"
"""


# =====================================================
# Extract Information
# =====================================================
def extract_review(review_text):
    """
    Send one review to Mistral and return structured JSON.
    """

    prompt = build_prompt(review_text)

    retries = 3

    for attempt in range(retries):

        try:

            response = client.chat.completions.create(
                model=MODEL_NAME,
                temperature=0,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert customer support analyst. Always respond with valid JSON only."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            text = response.choices[0].message.content.strip()

            text = (
                text.replace("```json", "")
                .replace("```", "")
                .strip()
            )

            return json.loads(text)

        except json.JSONDecodeError:

            return {
                "error": "Invalid JSON returned",
                "raw_response": text
            }

        except Exception as e:

            if "429" in str(e):

                print(f"Rate limit reached. Retry {attempt+1}/{retries}")
                time.sleep(5)

            else:

                print(e)
                return {
                    "error": str(e)
                }

    return {
        "error": "Maximum retries exceeded."
    }


# =====================================================
# Process Reviews
# =====================================================
def run_extraction():

    reviews = load_reviews()

    extracted_results = []

    for item in reviews:

        print(f"Processing Review {item['id']}...")

        result = extract_review(item["review"])

        result["id"] = item["id"]
        result["review"] = item["review"]

        extracted_results.append(result)

        time.sleep(1)

    return extracted_results


# =====================================================
# Main
# =====================================================
if __name__ == "__main__":

    results = run_extraction()

    os.makedirs("output", exist_ok=True)

    output_file = "output/extracted_reviews.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)

    print("\nExtraction Completed Successfully!")
    print(f"Results saved to: {output_file}")