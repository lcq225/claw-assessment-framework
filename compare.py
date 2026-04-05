#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ClawAF Comparison Script
Compare two evaluation results
"""
import json
import sys
from pathlib import Path
from typing import Dict, List


def load_result(file_path: str) -> Dict:
    """Load evaluation result from JSON file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file: {file_path}")
        sys.exit(1)


def compare_results(result1: Dict, result2: Dict) -> None:
    """Compare two evaluation results"""
    print("\n" + "="*70)
    print("ClawAF - Evaluation Comparison")
    print("="*70 + "\n")

    # Basic info
    print("Basic Information:")
    print(f"  Result 1: {result1.get('claw_directory', 'Unknown')}")
    print(f"            {result1.get('date', 'Unknown')}")
    print(f"  Result 2: {result2.get('claw_directory', 'Unknown')}")
    print(f"            {result2.get('date', 'Unknown')}\n")

    # Total score
    score1 = result1.get('total_score', 0)
    score2 = result2.get('total_score', 0)
    diff = score2 - score1

    print("Total Score:")
    print(f"  Result 1: {score1}/800 ({result1.get('level', 'Unknown')})")
    print(f"  Result 2: {score2}/800 ({result2.get('level', 'Unknown')})")

    if diff > 0:
        print(f"  Change:   +{diff} points")
    elif diff < 0:
        print(f"  Change:   {diff} points")
    else:
        print(f"  Change:   No change")

    # Dimensions
    print("\n" + "-"*70)
    print("Dimension Comparison:")
    print("-"*70)

    dimensions1 = result1.get('dimensions', {})
    dimensions2 = result2.get('dimensions', {})

    for dim in dimensions1.keys():
        score1_dim = dimensions1.get(dim, 0)
        score2_dim = dimensions2.get(dim, 0)
        diff_dim = score2_dim - score1_dim

        # Format dimension name
        dim_name = dim.replace('_', ' ').title()

        # Determine indicator
        if diff_dim > 0:
            indicator = f"+{diff_dim}"
            arrow = "↑"
        elif diff_dim < 0:
            indicator = str(diff_dim)
            arrow = "↓"
        else:
            indicator = "-"
            arrow = "→"

        print(f"\n{dim_name}:")
        print(f"  Result 1: {score1_dim}/100")
        print(f"  Result 2: {score2_dim}/100")
        print(f"  Change:   {indicator} {arrow}")

        # Show details if changed
        if diff_dim != 0:
            details1 = result1.get('details', {}).get(dim, {})
            details2 = result2.get('details', {}).get(dim, {})

            if details1 != details2:
                print(f"\n  Details Changed:")
                for key in set(list(details1.keys()) + list(details2.keys())):
                    val1 = str(details1.get(key, 'N/A'))
                    val2 = str(details2.get(key, 'N/A'))
                    if val1 != val2:
                        print(f"    {key}: {val1} → {val2}")

    print("\n" + "="*70 + "\n")


def main():
    """Main function"""
    if len(sys.argv) != 3:
        print("Usage: python compare.py <result1.json> <result2.json>")
        print("\nExample:")
        print("  python compare.py clawaf_result_before.json clawaf_result_after.json")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    result1 = load_result(file1)
    result2 = load_result(file2)

    compare_results(result1, result2)


if __name__ == "__main__":
    main()