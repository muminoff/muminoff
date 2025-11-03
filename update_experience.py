#!/usr/bin/env python3
"""
Update years of experience in README.md based on career start date.
Career started: August 2012
"""

import re
from datetime import datetime
from pathlib import Path


def calculate_years_of_experience(start_year: int, start_month: int) -> tuple[int, int]:
    """
    Calculate years and months of experience from start date to now.
    Returns: (years, months)
    """
    start_date = datetime(start_year, start_month, 1)
    current_date = datetime.now()

    total_months = (current_date.year - start_date.year) * 12 + (current_date.month - start_date.month)

    years = total_months // 12
    months = total_months % 12

    return years, months


def update_readme(readme_path: Path, years: int, months: int) -> bool:
    """
    Update README.md with current years and months of experience.
    Returns True if file was modified, False otherwise.
    """
    content = readme_path.read_text(encoding='utf-8')

    # Pattern to match "N Years, M Months" or "N+ Years" (for migration)
    pattern = r'(\d+)(?:\+)? Years(?:, (\d+) Months)?'

    # Build new experience string
    new_experience = f'{years} Years, {months} Months'

    # Check if update is needed
    match = re.search(pattern, content)
    if match:
        current_years = int(match.group(1))
        current_months = int(match.group(2)) if match.group(2) else None

        if current_years == years and current_months == months:
            print(f"✓ Experience is already up to date: {new_experience}")
            return False

    # Update the content
    new_content = re.sub(pattern, new_experience, content)

    if new_content != content:
        readme_path.write_text(new_content, encoding='utf-8')
        old_exp = match.group(0) if match else "unknown"
        print(f"✓ Updated experience from '{old_exp}' to '{new_experience}'")
        return True

    print("✗ No changes made")
    return False


def main():
    """Main function to update README."""
    # Career start date
    START_YEAR = 2012
    START_MONTH = 8  # August

    # Calculate current years and months of experience
    years, months = calculate_years_of_experience(START_YEAR, START_MONTH)
    print(f"Calculated experience: {years} years, {months} months")

    # Update README
    readme_path = Path(__file__).parent / 'README.md'

    if not readme_path.exists():
        print(f"✗ Error: README.md not found at {readme_path}")
        return 1

    was_updated = update_readme(readme_path, years, months)

    # Return 0 (success) whether updated or already current
    return 0


if __name__ == '__main__':
    exit(main())
