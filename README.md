# gtkmm Dash Docset

For https://kapeli.com/dash

## Usage

1. Download copy of site with `scrape.sh` (requires `wget`).
1. Run `gen_docset.py`.

Note that `gen_docset.py` will modify the HTML files directly to strip the "gtkmm/glibmm:" header from the `<title>` tag.
