#!bash
FONT_URL="https://github.com/be5invis/Iosevka/releases/download/v33.2.4/PkgWebFont-IosevkaTerm-33.2.4.zip"

if [[ -f app/static/font/IosevkaTerm.css ]]; then
  echo "Font already exists, skipping download."
  exit 0
fi

TMP=`mktemp -d`
curl -L "$FONT_URL" -o "$TMP/font.zip"
unzip -o "$TMP/font.zip" -d "$TMP"
rm "$TMP/font.zip"
mv "$TMP/WOFF2/" ./app/static/font/
mv "$TMP/TTF/" ./app/static/font/
mv "$TMP/IosevkaTerm.css" ./app/static/font/
rmdir "$TMP"
echo "Font downloaded and extracted successfully."
