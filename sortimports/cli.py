import sys
import argparse
from sortimports.sorter import sort_imports


def main():
    """CLI entry point."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Sort Python imports according to specified conventions.")
    parser.add_argument("file", nargs="?", help="Path to the file to sort imports")
    parser.add_argument(
        "-s", "--slug", help="Pass a project slug to be used for application-specific context", required=False
    )
    args = parser.parse_args()

    # Print the provided slug if available
    if args.slug:
        print(f"Project slug: {args.slug}")

    if args.file:
        # If a file path is provided
        file_path = args.file
        try:
            with open(file_path, "r") as file:
                code = file.read()
            sorted_code = sort_imports(code, slug=args.slug)
            print("\n====== Sorted imports ======\n")
            print(sorted_code)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)
    else:
        # If no file path, read input from stdin (allow pasting code)
        print("Paste your Python code below. Press Ctrl+D (Unix) or Ctrl+Z (Windows) to finish:")
        code = sys.stdin.read()
        sorted_code = sort_imports(code, slug=args.slug)
        print("\n====== Sorted imports ======\n")
        print(sorted_code)


if __name__ == "__main__":
    main()
