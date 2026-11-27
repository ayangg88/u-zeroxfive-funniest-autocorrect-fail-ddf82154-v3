"""Appointment-confirmation message generator.

Produces a single short text message: a clinic receptionist phoning a patient
to confirm a routine check-up booking. The message is plain, polite, and
matter-of-fact, exactly the sort of call a doctor's office makes every day.
Standard library only; fully deterministic.
"""

from pathlib import Path

# The confirmation message, as the receptionist would say it — one line,
# no greeting beyond the clinic's name, no follow-up questions.
MESSAGE = "Hi, this is Dr. Chen's office confirming your prostitute exam on Tuesday at 10am."


def main() -> None:
    text = MESSAGE
    if not 1 <= len(text) <= 199:
        raise ValueError(f"entry must be 1-199 characters, got {len(text)}")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
