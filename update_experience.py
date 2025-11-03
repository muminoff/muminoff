#!/usr/bin/env python3
"""
Update years of experience in README.md based on career start date.
Career started: August 2012
"""

import re
from datetime import datetime
from pathlib import Path


def calculate_years_of_experience(start_year: int, start_month: int) -> int:
    """Calculate years of experience from start date to now."""
    start_date = datetime(start_year, start_month, 1)
    current_date = datetime.now()

    years = current_date.year - start_date.year

    # Adjust if we haven't reached the start month yet this year
    if current_date.month < start_month:
        years -= 1

    return years


def update_readme(readme_path: Path, years: int) -> bool:
    """
    Update README.md with current years of experience.
    Returns True if file was modified, False otherwise.
    """
    content = readme_path.read_text(encoding='utf-8')

    # Pattern to match "N+ Years" or "N+ years" in the subtitle
    pattern = r'(\d+)\+ Years'

    # Check if update is needed
    match = re.search(pattern, content)
    if match:
        current_years = int(match.group(1))
        if current_years == years:
            print(f"✓ Experience is already up to date: {years}+ Years")
            return False

    # Update the content
    new_content = re.sub(pattern, f'{years}+ Years', content)

    if new_content != content:
        readme_path.write_text(new_content, encoding='utf-8')
        print(f"✓ Updated experience from {match.group(1) if match else '?'}+ to {years}+ Years")
        return True

    print("✗ No changes made")
    return False


def main():
    """Main function to update README."""
    # Career start date
    START_YEAR = 2012
    START_MONTH = 8  # August

    # Calculate current years of experience
    years = calculate_years_of_experience(START_YEAR, START_MONTH)
    print(f"Calculated years of experience: {years}")

    # Update README
    readme_path = Path(__file__).parent / 'README.md'

    if not readme_path.exists():
        print(f"✗ Error: README.md not found at {readme_path}")
        return 1

    was_updated = update_readme(readme_path, years)

    # Return 0 (success) whether updated or already current
    return 0


if __name__ == '__main__':
    exit(main())
