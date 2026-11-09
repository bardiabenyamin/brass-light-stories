#!/usr/bin/env bash
# POW-001 assembly (local, free). Spec: 1920x1080, 30 fps, H.264 yuv420p, AAC 48 kHz stereo.
# Shot order: SH02 insert -> SH01 wide -> SH03 -> (crossfade) SH04 -> SH05 -> SH06 -> SH07 -> black tail.
set -euo pipefail
cd "$(dirname "$0")"
T=render/tmp; mkdir -p "$T"
V="-c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 30 -an"
FIT="scale=1920:1080:flags=lanczos,setsar=1,fps=30"

# S1 clock insert: clip cut at the hand-alignment frame (1.5 s), then held 1.5 s. Crop 1280x704 -> 16:9.
ffmpeg -v error -y -i clips/POW001_SH02_CLIP_v01.mp4 -map 0:v:0 \
  -vf "trim=0:1.5,setpts=PTS-STARTPTS,crop=1252:704:14:0,$FIT,tpad=stop_mode=clone:stop_duration=1.5,fade=in:st=0:d=0.5" $V -t 3.0 "$T/s1.mp4"

# Digital push-in on a still: $1 image, $2 frames, $3 z0, $4 z1, $5 cx, $6 cy, $7 out
push() { ffmpeg -v error -y -loop 1 -i "$1" -vf "crop='min(iw,ih*16/9)':'min(ih,iw*9/16)':'(iw-min(iw,ih*16/9))/2':'(ih-min(ih,iw*9/16))/2',scale=3840:2160:flags=lanczos,zoompan=z='$3+($4-$3)*on/($2-1)':x='iw*$5-iw/zoom/2':y='ih*$6-ih/zoom/2':d=$2:s=1920x1080:fps=30,setsar=1" -frames:v "$2" $V "$7"; }

# S2 platform wide at midnight: still (hands at 12) with a slow push toward the clock (the AI clip moved the hands).
push keyframes/POW001_SH01_KF_v01.png 150 1.00 1.08 0.49 0.40 "$T/s2.mp4"
# S3 empty Early Shelf and S4 the umbrella has arrived: continuous push, joined by a 1.5 s crossfade.
push keyframes/POW001_SH03_KF_v02.png 105 1.00 1.03 0.50 0.70 "$T/s3.mp4"
push keyframes/POW001_SH04_KF_v01_retouch.png 105 1.03 1.06 0.50 0.70 "$T/s4.mp4"
ffmpeg -v error -y -i "$T/s3.mp4" -i "$T/s4.mp4" -filter_complex "[0:v][1:v]xfade=transition=fade:duration=1.5:offset=2.0,format=yuv420p" $V "$T/s34.mp4"

# S5-S7 character clips: video stream only, cropped to remove the lit lamps at the right edge.
ffmpeg -v error -y -i clips/POW001_SH05_CLIP_v01.mp4 -map 0:v:0 -vf "crop=1144:644:0:30,$FIT" -t 5.0 $V "$T/s5.mp4"
ffmpeg -v error -y -i clips/POW001_SH06_CLIP_v01.mp4 -map 0:v:0 -vf "crop=1144:644:0:30,$FIT" -t 4.5 $V "$T/s6.mp4"
ffmpeg -v error -y -i clips/POW001_SH07_CLIP_v01.mp4 -map 0:v:0 -vf "crop=1120:630:0:37,$FIT,fade=out:st=4.4:d=0.6" -t 5.0 $V "$T/s7.mp4"
# S8 black tail
ffmpeg -v error -y -f lavfi -i "color=c=black:s=1920x1080:r=30" -t 2.0 $V "$T/s8.mp4"

printf "file '%s'\n" s1.mp4 s2.mp4 s34.mp4 s5.mp4 s6.mp4 s7.mp4 s8.mp4 > "$T/list.txt"
ffmpeg -v error -y -f concat -safe 0 -i "$T/list.txt" -c copy "$T/picture.mp4"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$T/picture.mp4")

# Sound: synthesized placeholders (free) + narration.
A="-ar 48000 -ac 2"
ffmpeg -v error -y -f lavfi -i "aevalsrc='0.5*sin(2*PI*1900*t)*exp(-70*t)':s=48000:d=0.09" $A "$T/tick.wav"
ffmpeg -v error -y -f lavfi -i "aevalsrc='0.22*(sin(2*PI*523.25*t)+0.6*sin(2*PI*1046.5*t)+0.3*sin(2*PI*1568*t))*exp(-1.4*t)':s=48000:d=3.5" $A "$T/chime.wav"
ffmpeg -v error -y -f lavfi -i "aevalsrc='0.12*(sin(2*PI*220*t)+0.7*sin(2*PI*329.63*t)+0.4*sin(2*PI*440*t))*sin(PI*t/2.6)':s=48000:d=2.6" $A "$T/swell.wav"
ffmpeg -v error -y -f lavfi -i "anoisesrc=color=brown:amplitude=0.03:r=48000" -af "lowpass=f=500,volume=0.5" -t "$DUR" $A "$T/amb.wav"

VO1=audio/POW001_VO_wren_L001_annie_v01.wav
VO2=audio/POW001_VO_wren_L002_annie_v01.wav
ffmpeg -v error -y -i "$T/amb.wav" -i "$VO1" -i "$VO2" -i "$T/tick.wav" -i "$T/chime.wav" -i "$T/swell.wav" -filter_complex "\
[1:a]aresample=48000,aformat=channel_layouts=stereo,adelay=800|800,volume=1.0[vo1];\
[2:a]aresample=48000,aformat=channel_layouts=stereo,adelay=13800|13800,volume=1.0[vo2];\
[3:a]asplit=4[t0][t1][t2][t3];\
[t0]adelay=0|0,volume=0.6[k0];[t1]adelay=1000|1000,volume=0.6[k1];[t2]adelay=2000|2000,volume=0.5[k2];[t3]adelay=28800|28800,volume=0.5[k3];\
[4:a]adelay=1500|1500,volume=0.5[ch];\
[5:a]adelay=10900|10900,volume=0.9[sw];\
[0:a][vo1][vo2][k0][k1][k2][k3][ch][sw]amix=inputs=9:normalize=0:duration=first,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000" \
  -c:a pcm_s16le "$T/mix.wav"

OUT=render/POW001_RENDER_review_v01.mp4
ffmpeg -v error -y -i "$T/picture.mp4" -i "$T/mix.wav" -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart "$OUT"
echo "rendered $OUT"
