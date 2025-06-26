###Program Name: html_to_epub.py
###Programmer: Aaliyah Raderberg
###Description: Create a Python Application to convert a Word Doc--> HTML ==>ePUB *ebook

import os
from bs4 import BeautifulSoup
from ebooklib import epub
import chardet


def load_html_with_encoding_detection(html_path):
    with open(html_path, "rb") as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result["encoding"] or "utf-8"

    return raw_data.decode(encoding, errors="replace")


def clean_html_content(html_content):
    replacements = {
        '“': '"',  # “
        '”': '"',  # ”
        '‘': "'",  # ‘
        '’': "'",  # ’
        '\xa0': ' ',  # Non-breaking space
    }
    for bad, good in replacements.items():
        html_content = html_content.replace(bad, good)

    soup = BeautifulSoup(html_content, "html.parser")

    # Remove tags with namespaced prefixes
    for tag in soup.find_all():
        if ":" in tag.name:
            tag.decompose()

    # Remove namespaced attributes
    for tag in soup.find_all(True):
        for attr in list(tag.attrs):
            if ":" in attr:
                del tag.attrs[attr]

    # Remove problematic <xml>, <style>, <script> blocks
    for bad_tag in soup.find_all(["xml", "style", "script"]):
        if any(ns in bad_tag.get_text().lower() for ns in ["v:", "o:", "mso-", "shape", "word"]):
            bad_tag.decompose()

    return soup


def split_html_into_chapters(soup, max_chapters=7):
    custom_titles = [
        "Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4",
        "Chapter 5", "Chapter 6", "Chapter 7"
    ]
    chapters = []
    body = soup.body or soup
    heading_tags = ["h1", "h2"]

    headings = body.find_all(heading_tags)
    if not headings:
        chapters.append({
            "title": custom_titles[0],
            "file_name": "chap_1.xhtml",
            "content": f'<html><head><title>{custom_titles[0]}</title></head><body>{str(body)}</body></html>'
        })
        return chapters

    # Add pre-heading content as first chapter
    first_heading = headings[0]
    pre_heading_content = []
    for el in first_heading.previous_siblings:
        pre_heading_content.insert(0, el)
    if any(str(el).strip() for el in pre_heading_content):
        chapter_html = f'<html><head><title>Introduction</title></head><body>' + ''.join(str(e) for e in pre_heading_content) + '</body></html>'
        chapters.append({
            "title": "Introduction",
            "file_name": "chap_0.xhtml",
            "content": chapter_html
        })

    for i, heading in enumerate(headings):
        start = heading
        end = headings[i + 1] if i + 1 < len(headings) else None
        content_elements = []

        for elem in start.next_siblings:
            if elem == end:
                break
            content_elements.append(elem)

        section_title = custom_titles[i] if i < len(custom_titles) else f"Chapter {i+1}"
        section_body = str(heading) + ''.join(str(el) for el in content_elements)
        chapter_html = f'<html><head><title>{section_title}</title></head><body>{section_body}</body></html>'

        chapters.append({
            "title": section_title,
            "file_name": f"chap_{i+1}.xhtml",
            "content": chapter_html
        })

    return chapters[:max_chapters+1]  # +1 to include the intro if present


def create_epub_from_html(html_path, title="Converted Book", author="Unknown"):
    html_content = load_html_with_encoding_detection(html_path)
    soup = clean_html_content(html_content)

    book = epub.EpubBook()
    book.set_identifier("id-html-epub")
    book.set_title(title)
    book.set_language("en")
    book.add_author(author)
    book.add_metadata("DC", "description", "Love, Loss, Betrayal, and Spiritual Breakthrough")
    book.add_metadata("DC", "subject", "Spiritual awakening, Romance, lesbian love story")
    book.add_metadata("DC", "date", "2025-07-01")
    book.add_metadata("DC", "rights", "All rights reserved-Aaliyah Raderberg")
    book.add_metadata("DC", "format", "EPUB")
    book.add_metadata("DC", "relation", "https://aaliyahraderberg.com/shelovedmewrong/")

    chapters_data = split_html_into_chapters(soup)
    chapters = []
    image_items = {}
    used_images = set()

    for chapter_data in chapters_data:
        chapter_soup = BeautifulSoup(chapter_data["content"], "html.parser")

        for img_tag in chapter_soup.find_all("img"):
            src = img_tag.get("src", "").strip()
            if not src or src.startswith("http") or not os.path.exists(src):
                print(f"[SKIP] Missing or remote image: {src}")
                img_tag.decompose()
                continue

            filename = os.path.basename(src)
            if filename not in image_items:
                with open(src, "rb") as f:
                    img_item = epub.EpubImage()
                    img_item.file_name = filename
                    img_item.content = f.read()
                    img_item.media_type = f"image/{os.path.splitext(filename)[1][1:]}"
                    book.add_item(img_item)
                    image_items[filename] = img_item

            if filename not in used_images:
                img_tag["src"] = filename
                used_images.add(filename)
            else:
                img_tag.decompose()

        epub_chapter = epub.EpubHtml(
            title=chapter_data["title"],
            file_name=chapter_data["file_name"],
            lang="en"
        )
        epub_chapter.set_content(str(chapter_soup))
        book.add_item(epub_chapter)
        chapters.append(epub_chapter)

    book.toc = chapters
    book.spine = ["nav"] + chapters
    book.add_item(epub.EpubNav())
    book.add_item(epub.EpubNcx())

    output_name = title.replace(" ", "_") + ".epub"
    epub.write_epub(output_name, book)
    print(f"[DONE] EPUB created: {output_name}")


if __name__ == "__main__":
    html_file = "epub.html"
    create_epub_from_html(html_file, title="She Loved Me Wrong", author="Anayansi")
