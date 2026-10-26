#!/usr/bin/env python3
"""Generate the project contribution QR code as a printable SVG."""
from io import BytesIO
from pathlib import Path

import qrcode
from qrcode.image.svg import SvgPathImage

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "docs" / "assets" / "mitmachen-qr.svg"
PROJECT_URL = "https://github.com/cvieth/survivor-guide"


def main() -> None:
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(PROJECT_URL)
    qr.make(fit=True)

    buffer = BytesIO()
    qr.make_image(image_factory=SvgPathImage).save(buffer)
    svg = buffer.getvalue().decode("utf-8")
    # Solid white background ensures contrast in the dark web theme.
    svg = svg.replace(
        "<path ",
        '<rect width="100%" height="100%" fill="#ffffff"/><path ',
        1,
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(svg, encoding="utf-8")
    print(f"Generated: {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
