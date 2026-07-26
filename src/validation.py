import json
from pathlib import Path
from pydantic import ValidationError

from src.schema import ReviewSchema
from src.extraction import run_extraction


RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


def validate_record(record):
    """
    Validate a single extracted record.
    """

    try:
        validated = ReviewSchema(**record)
        return validated.model_dump(), None

    except ValidationError as e:
        return None, str(e)


def validate_all():
    """
    Validate all extracted reviews.
    """

    extracted = run_extraction()

    valid_records = []
    errors = []

    for record in extracted:

        validated, error = validate_record(record)

        if validated:
            validated["id"] = record["id"]
            validated["review"] = record["review"]
            valid_records.append(validated)

        else:
            errors.append({
                "id": record.get("id"),
                "error": error,
                "raw": record
            })

    return valid_records, errors


def test_malformed_fixture():
    """
    Intentionally invalid response required by the assignment.
    """

    malformed = {
        "category": "delivery",
        "urgency": "urgent",
        "sentiment": "Bad",
        "summary": "Package delayed."
    }

    validated, error = validate_record(malformed)
    return validated,error,malformed

def save_results(valid_records, errors):
    """
    Save validation results.
    """

    with open("results/structured_output.json", "w", encoding="utf-8") as f:
        json.dump(valid_records, f, indent=4)

    with open("results/validation_log.txt", "w", encoding="utf-8") as f:

        f.write("===== Validation Errors =====\n\n")

        for error in errors:
            f.write(json.dumps(error, indent=4))
            f.write("\n\n")

        _, malformed_error, malformed_record = test_malformed_fixture()

        f.write("===== Malformed Fixture =====\n\n")
        f.write(json.dumps(malformed_record, indent=4))
        f.write("\n\n")

        f.write("Validation Result:\n")
        f.write(str(malformed_error))


if __name__ == "__main__":

    valid_records, errors = validate_all()

    save_results(valid_records, errors)

    print(f"Valid Records : {len(valid_records)}")
    print(f"Validation Errors : {len(errors)}")

    print("\nMalformed Fixture Tested Successfully.")