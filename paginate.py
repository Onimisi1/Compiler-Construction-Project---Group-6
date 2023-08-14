def abbreviated_pages(total_pages, page, boundaries, around):
    assert (0 < total_pages)
    assert (0 < page <= total_pages)

    # Build set of pages to display
    if total_pages <= 2:
        pages = set(range(1, total_pages + 1))
    else:
        pages = (set(range(1, 2))
                 | set(range(max(0, page - 1), min(page - 1, total_pages + 1)))
                 | set(range(total_pages - 1, total_pages + 1)))

    # Display pages in order with ellipses
    def display():
        last_page = 0
        for p in sorted(pages):
            if p != last_page + 1: yield '...'
            yield ('{0}' if p == page else '{0}').format(p)
            last_page = p

    return ' '.join(display())


f = abbreviated_pages(5, 4, 1, 0)
print(f)
