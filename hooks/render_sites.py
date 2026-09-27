"""MkDocs build hook: render the MeshCore Equipment page from a single data file.

All site data (equipment specs, GPS, antenna AGL, location, photo/coverage-map paths) lives in
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
_FT_PER_M = 3.28084


def _cell(value):
    if value is None or value == "":
        return "—"
    if value is True:
        return "Yes"
    if value is False:
        return "No"
    return str(value)


def _number(site_name, field, value, lo=None, hi=None):
    """Validate an optional numeric field; blank -> None, bad value -> build error."""
    if value is None or value == "":
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(
            f"sites.yml: {site_name}: {field} must be a decimal number "
            f"(e.g. 47.53012, not 47°31'48\"N), got {value!r}"
        )
    if (lo is not None and value < lo) or (hi is not None and value > hi):
        raise ValueError(f"sites.yml: {site_name}: {field}={value} out of range [{lo}, {hi}]")
    return value


def _render_site(site):
    name = str(site.get("name") or "Unknown")
    out = ["---", f"## {name}", ""]

    location = site.get("location") or ""
    if location:
        out += [f"**Location:** {location}", ""]

    gps = site.get("gps") or {}
    lat = _number(name, "gps.lat", gps.get("lat"), -90, 90)
    lon = _number(name, "gps.lon", gps.get("lon"), -180, 180)
    if (lat is None) != (lon is None):
        raise ValueError(f"sites.yml: {name}: set both gps.lat and gps.lon, or neither")
    gps_cell = f"{lat:.5f}, {lon:.5f}" if lat is not None else None

    agl_m = _number(name, "agl_m", site.get("agl_m"), 0, 600)
    agl_cell = f"{agl_m:g} m ({agl_m * _FT_PER_M:.0f} ft)" if agl_m is not None else None

    cells = [_cell(site.get(col)) for col in _COLUMNS]
    cells.insert(_COLUMNS.index("antenna") + 1, _cell(agl_cell))
    cells.append(_cell(gps_cell))
    out += [
        "Node Name | Radio | Antenna | AGL | Battery | Solar | Freq | BW | SF | CR | GPS",
        " | ".join([":---:"] * len(cells)),
        " | ".join(cells),
        "",
    ]

    photos = site.get("photo") or []
    if isinstance(photos, str):
        photos = [photos]
    if photos:
        for photo in photos:
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
