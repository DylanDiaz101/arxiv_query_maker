import xml.etree.ElementTree as ET
import urllib.request as libreq
import datetime


def fetch_entries(url):
    with libreq.urlopen(url) as response:
        xml_data = response.read()
    root = ET.fromstring(xml_data)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}

    now = datetime.datetime.now(datetime.timezone.utc)
    one_month_ago = now - datetime.timedelta(days=30)

    entries = []
    for entry in root.findall('.//atom:entry', ns):
        # extract title
        title_elem = entry.find('atom:title', ns)
        title = title_elem.text.strip() if title_elem is not None else "No Title"

        # extract published date
        published_elem = entry.find('atom:published', ns)
        if published_elem is None:
            continue
        published_date_str = published_elem.text.strip()
        try:
            published_date = datetime.datetime.fromisoformat(published_date_str.replace("Z", "+00:00"))
        except Exception:
            continue
        # only include articles from the last month
        if published_date < one_month_ago:
            continue

        # extract PDF link
        pdf_link = None
        for link in entry.findall('atom:link', ns):
            if link.attrib.get('title') == 'pdf':
                pdf_link = link.attrib.get('href')
                break
        if pdf_link:
            entries.append((title, published_date_str, pdf_link))
    return entries
