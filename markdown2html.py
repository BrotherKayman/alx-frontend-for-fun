#!/usr/bin/python3
"""
markdown2html.py

A script to convert a Markdown file to an HTML file.

Usage:
    ./markdown2html.py input_file.md output_file.html

Arguments:
    input_file.md     The Markdown file to be converted.
    output_file.html  The output HTML file name.

Features:
- Converts Markdown headings, bold and italic text.
- Converts unordered and ordered lists.
- Handles special syntax for md5 hash conversion and character removal.
"""

import sys
import os
import re
import hashlib

def convert_markdown_to_html(markdown_content):
    """Converts markdown text to HTML."""
    html_content = []
    unordered_start, ordered_start, paragraph = False, False, False

    for line in markdown_content:
        # Handle bold and italic text
        line = line.replace('**', '<b>', 1).replace('**', '</b>', 1)
        line = line.replace('__', '<em>', 1).replace('__', '</em>', 1)

        # Handle md5 hash conversion
        md5_matches = re.findall(r'\[\[.+?\]\]', line)
        if md5_matches:
            for md5_match in md5_matches:
                md5_text = re.findall(r'\[\[(.+?)\]\]', md5_match)[0]
                line = line.replace(md5_match, hashlib.md5(md5_text.encode()).hexdigest())

        # Handle character removal for '(())' pattern
        remove_c_matches = re.findall(r'\(\(.+?\)\)', line)
        if remove_c_matches:
            for remove_c_match in remove_c_matches:
                text_without_c = ''.join(c for c in re.findall(r'\(\((.+?)\)\)', remove_c_match)[0] if c not in 'Cc')
                line = line.replace(remove_c_match, text_without_c)

        # Handle headings
        heading_level = len(line) - len(line.lstrip('#'))
        if 1 <= heading_level <= 6:
            line = '<h{}>{}</h{}>\n'.format(heading_level, line.strip('#').strip(), heading_level)

        # Handle unordered lists
        if line.startswith('-'):
            if not unordered_start:
                html_content.append('<ul>\n')
                unordered_start = True
            line = '<li>{}</li>\n'.format(line.strip('-').strip())
        if unordered_start and not line.startswith('-'):
            html_content.append('</ul>\n')
            unordered_start = False

        # Handle ordered lists
        if line.startswith('*'):
            if not ordered_start:
                html_content.append('<ol>\n')
                ordered_start = True
            line = '<li>{}</li>\n'.format(line.strip('*').strip())
        if ordered_start and not line.startswith('*'):
            html_content.append('</ol>\n')
            ordered_start = False

        # Handle paragraphs
        if not (heading_level or unordered_start or ordered_start):
            if not paragraph and line.strip():
                html_content.append('<p>\n')
                paragraph = True
            elif line.strip():
                html_content.append('<br/>\n')
            elif paragraph:
                html_content.append('</p>\n')
                paragraph = False

        if line.strip():
            html_content.append(line)

    # Close any remaining open tags
    if unordered_start:
        html_content.append('</ul>\n')
    if ordered_start:
        html_content.append('</ol>\n')
    if paragraph:
        html_content.append('</p>\n')

    return ''.join(html_content)

def main():
    """Main function to execute the markdown to HTML conversion."""
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py input_file.md output_file.html', file=sys.stderr)
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]

    if not os.path.isfile(input_file):
        print(f'Missing {input_file}', file=sys.stderr)
        sys.exit(1)

    try:
        with open(input_file, 'r') as md_file:
            markdown_content = md_file.readlines()

        html_content = convert_markdown_to_html(markdown_content)

        with open(output_file, 'w') as html_file:
            html_file.write(html_content)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
