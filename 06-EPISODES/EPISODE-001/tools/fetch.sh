#!/usr/bin/env bash
# fetch.sh KIND ID URL  -> downloads a finished generation to its canonical EPISODE-001 path (never overwrites).
set -euo pipefail
cd "$(dirname "$0")/.."
kind=$1; id=$2; url=$3; v=${4:-v01}
case $kind in
  kf)   out="images/keyframes/E001_${id}_KF_${v}.png" ;;
  ref)  out="references/characters/E001_CHR_${id}_front_${v}.png" ;;
  clip) out="clips/E001_${id}_CLIP_${v}.mp4" ;;
  vo)   out="audio/dialogue/E001_VO_${id}_${v}.wav" ;;
  mus)  out="audio/music/E001_MUS_${id}_${v}.wav" ;;
  sfx)  out="audio/sfx/E001_SFX_${id}_${v}.wav" ;;
  *) echo "unknown kind"; exit 1 ;;
esac
mkdir -p "$(dirname "$out")"
[ -e "$out" ] && { echo "EXISTS, not overwritten: $out"; exit 1; }
curl -sS -m 120 -o "$out" "$url"
echo "$out $(stat -c %s "$out") bytes"
