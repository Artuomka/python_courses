import codecs


def delete_html_tags(html_file, result_file="cleaned.txt"):
    with codecs.open(html_file, "r", "utf-8") as file:
        html = file.read()

    in_tag = False
    output_chars = []
    for ch in html:
        if ch == "<":
            in_tag = True
        elif ch == ">":
            in_tag = False
        else:
            if not in_tag:
                output_chars.append(ch)

    text_without_html = "".join(output_chars)

    text_lines = [ln.strip() for ln in text_without_html.splitlines() if ln.strip()]
    cleaned_lines = "\n".join(text_lines)

    with codecs.open(result_file, "w", "utf-8") as out_file:
        out_file.write(cleaned_lines)


delete_html_tags("draft.html", "cleaned.txt")
