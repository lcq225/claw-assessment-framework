#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ClawAF Directory Diagnostic Tool
Help users find the correct workspace directory for evaluation
"""
import sys
import io
from pathlib import Path

# Fix Windows encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def find_workspace(start_dir: Path) -> list:
    """Find all possible workspace directories"""
    workspaces = []

    # Check if current directory is a workspace
    if _is_workspace_dir(start_dir):
        workspaces.append(start_dir)

    # Check .copaw/workspaces/ subdirectories
    copaw_dir = start_dir / ".copaw" / "workspaces"
    if copaw_dir.exists():
        for item in copaw_dir.iterdir():
            if item.is_dir():
                workspaces.append(item)

    # Check parent directories
    for parent in start_dir.parents:
        if _is_workspace_dir(parent):
            workspaces.append(parent)

        copaw_parent = parent / ".copaw" / "workspaces"
        if copaw_parent.exists():
            for item in copaw_parent.iterdir():
                if item.is_dir():
                    workspaces.append(item)

    return workspaces


def _is_workspace_dir(path: Path) -> bool:
    """Check if directory is a workspace directory"""
    required_files = ["AGENTS.md", "SOUL.md", "PROFILE.md"]
    return all((path / f).exists() for f in required_files)


def diagnose_directory(path: Path):
    """Diagnose directory structure"""
    print(f"\nDiagnosing: {path}\n")

    # Check workspace indicators
    print("Workspace Indicators:")
    workspace_files = {
        "AGENTS.md": (path / "AGENTS.md").exists(),
        "SOUL.md": (path / "SOUL.md").exists(),
        "PROFILE.md": (path / "PROFILE.md").exists(),
        "skills/": (path / "skills").exists(),
        "active_skills/": (path / "active_skills").exists(),
    }

    all_present = all(workspace_files.values())
    for name, exists in workspace_files.items():
        status = "[OK]" if exists else "[  ]"
        print(f"  {status} {name}")

    if all_present:
        print(f"\n✓ This directory is a valid workspace directory!")
        print(f"  Recommended command: python assess_auto.py --dir \"{path}\"")
        return True
    else:
        print(f"\n✗ This directory is NOT a workspace directory")
        return False


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='ClawAF Directory Diagnostic Tool',
        epilog='Example: python diagnose.py --dir "D:\\CoPaw"'
    )
    parser.add_argument('--dir', type=str, default=str(Path.cwd()),
                       help='Directory to diagnose (default: current directory)')

    args = parser.parse_args()

    diag_dir = Path(args.dir)

    if not diag_dir.exists():
        print(f"Error: Directory not found: {diag_dir}")
        sys.exit(1)

    # Diagnose current directory
    is_workspace = diagnose_directory(diag_dir)

    if is_workspace:
        sys.exit(0)

    # Find workspaces
    print(f"\nSearching for workspace directories...\n")
    workspaces = find_workspace(diag_dir)

    if workspaces:
        print("Found workspace directories:\n")
        for i, ws in enumerate(workspaces, 1):
            print(f"{i}. {ws}")
            print(f"   Command: python assess_auto.py --dir \"{ws}\"")

            # Show workspace indicators
            workspace_files = {
                "AGENTS.md": (ws / "AGENTS.md").exists(),
                "SOUL.md": (ws / "SOUL.md").exists(),
                "PROFILE.md": (ws / "PROFILE.md").exists(),
            }
            print(f"   Files: {' '.join([name if exists else '' for name, exists in workspace_files.items()])}")
            print()

        print("\nRecommended: Use the first workspace directory\n")
    else:
        print("No workspace directories found.\n")
        print("Make sure you are in a Claw project directory with the following structure:\n")
        print("project-root/")
        print("├── .copaw/")
        print("│   └── workspaces/")
        print("│       └── default/")
        print("│           ├── AGENTS.md")
        print("│           ├── SOUL.md")
        print("│           ├── PROFILE.md")
        print("│           └── skills/")
        print("└── ... (project files)\n")


if __name__ == "__main__":
    import argparse
    main()