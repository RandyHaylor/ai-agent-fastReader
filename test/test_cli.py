import unittest
from src.fastReader.cli import parse_args


class TestCLIParsing(unittest.TestCase):
    """Test CLI argument parsing for FastReader."""

    def test_load_subcommand(self):
        """Test parsing 'load myfile.txt' correctly."""
        args = parse_args(['load', 'myfile.txt'])
        self.assertEqual(args.command, 'load')
        self.assertEqual(args.filepath, 'myfile.txt')

    def test_toc_chapters(self):
        """Test parsing 'toc --chapters' correctly."""
        args = parse_args(['toc', '--chapters'])
        self.assertEqual(args.command, 'toc')
        self.assertTrue(args.chapters)

    def test_toc_sections_with_preview(self):
        """Test parsing 'toc --sections --preview 60' correctly."""
        args = parse_args(['toc', '--sections', '--preview', '60'])
        self.assertEqual(args.command, 'toc')
        self.assertTrue(args.sections)
        self.assertEqual(args.preview, 60)

    def test_get_chapter(self):
        """Test parsing 'get --chapter 3' correctly."""
        args = parse_args(['get', '--chapter', '3'])
        self.assertEqual(args.command, 'get')
        self.assertEqual(args.chapter, 3)

    def test_get_block_range(self):
        """Test parsing 'get --block 7-9' correctly."""
        args = parse_args(['get', '--block', '7-9'])
        self.assertEqual(args.command, 'get')
        self.assertEqual(args.block, '7-9')

    def test_get_listing_single_index(self):
        """Test parsing 'get-listing 1' correctly."""
        args = parse_args(['get-listing', '1'])
        self.assertEqual(args.command, 'get-listing')
        self.assertEqual(args.listing_ref, '1')

    def test_get_listing_range(self):
        """Test parsing 'get-listing 3-5' correctly."""
        args = parse_args(['get-listing', '3-5'])
        self.assertEqual(args.command, 'get-listing')
        self.assertEqual(args.listing_ref, '3-5')


if __name__ == '__main__':
    unittest.main()
