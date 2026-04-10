import argparse
from typing import List, Optional


def parse_args(argv: List[str]) -> argparse.Namespace:
    """Parse command-line arguments for FastReader CLI.

    Args:
        argv: List of command-line arguments (excluding program name).

    Returns:
        Parsed arguments namespace.
    """
    parser = argparse.ArgumentParser(
        prog='llm-fast-reader',
        description='FastReader — Document Structure Layer for AI Agents'
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # 'load' subcommand
    load_parser = subparsers.add_parser('load', help='Scan a document and create manifest')
    load_parser.add_argument('filepath', help='Path to the document file')

    # 'toc' subcommand
    toc_parser = subparsers.add_parser('toc', help='Display table of contents at a zoom level')
    toc_parser.add_argument('--chapters', action='store_true', help='Show chapters')
    toc_parser.add_argument('--sections', action='store_true', help='Show sections')
    toc_parser.add_argument('--subsections', action='store_true', help='Show subsections')
    toc_parser.add_argument('--pages', action='store_true', help='Show pages')
    toc_parser.add_argument('--blocks', action='store_true', help='Show blocks')
    toc_parser.add_argument('--preview', type=int, default=30, help='Preview length (default: 30)')

    # 'get' subcommand
    get_parser = subparsers.add_parser('get', help='Retrieve content by reference')
    get_parser.add_argument('--chapter', type=int, help='Chapter number')
    get_parser.add_argument('--section', type=int, help='Section number')
    get_parser.add_argument('--page', type=int, help='Page number')
    get_parser.add_argument('--block', type=str, help='Block number or range (e.g., 7-9)')

    # 'get-listing' subcommand
    get_listing_parser = subparsers.add_parser('get-listing', help='Retrieve by index from recent listing')
    get_listing_parser.add_argument('listing_ref', help='Index or range (e.g., 1 or 3-5)')

    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> argparse.Namespace:
    """Main entry point for FastReader CLI.

    Args:
        argv: Optional list of arguments. If None, uses sys.argv[1:].

    Returns:
        Parsed arguments namespace.
    """
    return parse_args(argv)
