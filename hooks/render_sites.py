"""MkDocs build hook: render the MeshCore Equipment page from a single data file.

All site data (equipment specs, GPS, location, photo/coverage-map paths) lives in
docs/data/sites.yml. This hook replaces the `<!-- sites:render -->` marker on
docs/meshcore/equipment.md with one generated section per site, preserving the
original per-site format: an equipment table, the node/site photo, and a
clickable coverage map. To add or edit a site, edit sites.yml only.
"""
from pathlib import Path
import yaml

_TARGET = "meshcore/equipment.md"
_MARKER = "<!-- sites:render -->"
_COLUMNS = ["node_name", "radio", "antenna", "battery", "solar", "freq", "bw", "sf", "cr"]


def _cell(value):
    if value is None or value == "":
        return "—"
    if value is True:
        return "Yes"
    if value is False:
        return "No"
    return str(value)


def _render_site(site):
    name = str(site.get("name") or "Unknown")
    out = ["---", f"## {name}", ""]

    location = site.get("location") or ""
    gps = site.get("gps") or {}
    lat, lon = gps.get("lat"), gps.get("lon")
    if location or (lat is not None and lon is not None):
        line = "**Location:** " + (location or "TBD")
        if lat is not None and lon is not None:
            line += f" ({lat}, {lon})"
        out += [line, ""]

    out += [
        "Node Name | Radio | Antenna | Battery | Solar | Freq | BW | SF | CR",
        ":---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:",
        " | ".join(_cell(site.get(col)) for col in _COLUMNS),
        "",
    ]

    photo = site.get("photo") or ""
    if photo:
        out += [f"![{name} node]({photo})", ""]
    else:
        out += ["*Node/site photo coming soon.*", ""]

    cover = site.get("coverage_map") or ""
    link = site.get("coverage_link") or ""
    if cover:
        out.append("Click to enlarge and see the larger coverage map.")
        img = f"![{name} coverage map]({cover})"
        out.append(f"[{img}]({link})" if link else img)
        out.append("")
    else:
        out += ["*Coverage map coming soon.*", ""]

    return "\n".join(out)


def on_page_markdown(markdown, page, config, files, **kwargs):
    if page.file.src_uri != _TARGET or _MARKER not in markdown:
        return markdown
    data_file = Path(config["docs_dir"]) / "data" / "sites.yml"
    data = yaml.safe_load(data_file.read_text(encoding="utf-8")) or {}
    sites = data.get("sites") or []
    return markdown.replace(_MARKER, "\n".join(_render_site(s) for s in sites))
