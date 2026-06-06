import instaloader
import yt_dlp
from flask import Flask, render_template, request, Response, send_from_directory
import http.cookiejar
import os
import re
import requests
import base64
import random
import string

app = Flask(__name__)

L = instaloader.Instaloader(quiet=True)
cookie_path = '/home/AtoZDownloaderBykartik/mysite/cookies.txt'

if os.path.exists(cookie_path):
    try:
        cj = http.cookiejar.MozillaCookieJar(cookie_path)
        cj.load(ignore_discard=True, ignore_expires=True)
        for cookie in cj:
            L.context._session.cookies.set_cookie(cookie)
    except Exception as e:
        print(f"Cookie Error: {e}")

@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory(os.path.dirname(__file__), 'manifest.json')

@app.route('/sw.js')
def serve_sw():
    return send_from_directory(os.path.dirname(__file__), 'sw.js')

@app.route('/logo.png')
def serve_logo():
    return send_from_directory(os.path.dirname(__file__), 'logo.png')

# 🔥 Google Search Console Verification 🔥
@app.route('/googlebdeb0be3bcb66a2e.html')
def google_verify():
    return "google-site-verification: googlebdeb0be3bcb66a2e.html"

# 🔥 FB, WHATSAPP & GOOGLE VIP PERMISSION (Robots.txt) 🔥
@app.route('/robots.txt')
def robots():
    robot_txt = '''User-agent: facebookexternalhit
Allow: /

User-agent: WhatsApp
Allow: /

User-agent: *
Allow: /
Sitemap: https://atozdownloaderbykartik.pythonanywhere.com/sitemap.xml'''
    return Response(robot_txt, mimetype='text/plain')

def get_real_url(url):
    match = re.search(r'/s/([^/?#&]+)', url)
    if match:
        b64_str = match.group(1)
        try:
            b64_str += "=" * ((4 - len(b64_str) % 4) % 4)
            decoded = base64.b64decode(b64_str).decode('utf-8')
            if decoded.startswith('highlight:'):
                hl_id = decoded.split(':')[1]
                return f"https://www.instagram.com/stories/highlights/{hl_id}/"
        except: pass
    if '/stories/' in url: return url.split('?')[0]
    return url

def get_shortcode(url):
    match = re.search(r'(?:p|reel|tv)/([^/?#&]+)', url)
    if match: return match.group(1)
    return None

# 🔥 HTML PAGE ROUTES 🔥
@app.route('/')
def home():
    return render_template('index.html',
                           page_heading="All-in-One Downloader: Insta, FB & YouTube",
                           active_tab="auto")

@app.route('/instagram-video-downloader')
def video_downloader():
    return render_template('index.html',
                           seo_title="Instagram Video Downloader - Save IG Videos in HD",
                           seo_desc="Free online tool to download Instagram Videos in High Quality (MP4).",
                           page_heading="Instagram Video Downloader",
                           active_tab="video")

@app.route('/instagram-reels-downloader')
def reels_downloader():
    return render_template('index.html',
                           seo_title="Instagram Reels Downloader - No Watermark",
                           seo_desc="Download Instagram Reels with audio in Full HD quality.",
                           page_heading="Instagram Reels Downloader",
                           active_tab="reels")

@app.route('/instagram-photo-downloader')
def photo_downloader():
    return render_template('index.html',
                           seo_title="Instagram Photo Downloader - Save IG Images",
                           seo_desc="Download Instagram photos and multiple carousel images in high resolution.",
                           page_heading="Instagram Photo Downloader",
                           active_tab="photo")

@app.route('/insta-dp-viewer')
def dp_viewer():
    return render_template('index.html',
                           seo_title="Insta DP Viewer & Downloader - Full HD",
                           seo_desc="View and download Instagram Profile Pictures (DP) in full size anonymously.",
                           page_heading="Instagram DP Viewer & Downloader",
                           active_tab="dp")

@app.route('/instagram-story-downloader')
def story_downloader():
    return render_template('index.html',
                           seo_title="Instagram Story Downloader & Saver",
                           seo_desc="Download Instagram Stories anonymously. Best IG Story Saver tool.",
                           page_heading="Instagram Story Downloader",
                           active_tab="story")

@app.route('/instagram-highlight-downloader')
def highlight_downloader():
    return render_template('index.html',
                           seo_title="Instagram Highlight Downloader - HD Quality",
                           seo_desc="Download Instagram Highlights online for free directly to your device.",
                           page_heading="Instagram Highlight Downloader",
                           active_tab="highlight")

@app.route('/facebook-reels-downloader')
def fb_reels():
    return render_template('index.html',
                           seo_title="Facebook Reels Downloader - HD Quality",
                           seo_desc="Download FB Reels and Videos online for free. Save Facebook videos to your device in 1-click.",
                           page_heading="Facebook HD Reels Downloader",
                           active_tab="fb")

@app.route('/youtube-downloader')
def youtube_downloader():
    return render_template('index.html',
                           page_heading="YouTube Video & Shorts Downloader",
                           active_tab="yt")
# 🔥 5 NAYE PREMIUM ROUTES 🔥
@app.route('/tiktok-downloader')
def tiktok_downloader():
    return render_template('index.html', page_heading="TikTok Downloader (No Watermark)", active_tab="tiktok")

@app.route('/twitter-downloader')
def twitter_downloader():
    return render_template('index.html', page_heading="Twitter (X) Video & GIF Downloader", active_tab="twitter")

@app.route('/youtube-mp3')
def youtube_mp3():
    return render_template('index.html', page_heading="YouTube to MP3 Audio Converter", active_tab="ytmp3")

@app.route('/pinterest-downloader')
def pinterest_downloader():
    return render_template('index.html', page_heading="Pinterest Video & Image Downloader", active_tab="pinterest")

@app.route('/threads-downloader')
def threads_downloader():
    return render_template('index.html', page_heading="Threads Video Downloader", active_tab="threads")

# 🔥 LEGAL PAGES ROUTES 🔥
@app.route('/about-us')
def about():
    return render_template('pages.html', title="About Us", page="about")

@app.route('/privacy-policy')
def privacy():
    return render_template('pages.html', title="Privacy Policy", page="privacy")

@app.route('/contact-us')
def contact():
    return render_template('pages.html', title="Contact Us", page="contact")

# 🔥 ADVANCED SEO SITEMAP ROUTE 🔥
@app.route('/sitemap.xml')
def sitemap():
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url><loc>https://atozdownloaderbykartik.pythonanywhere.com/</loc><priority>1.0</priority></url>
      <url><loc>https://atozdownloaderbykartik.pythonanywhere.com/instagram-video-downloader</loc><priority>0.9</priority></url>
      <url><loc>https://atozdownloaderbykartik.pythonanywhere.com/instagram-reels-downloader</loc><priority>0.9</priority></url>
      <url><loc>https://atozdownloaderbykartik.pythonanywhere.com/instagram-photo-downloader</loc><priority>0.8</priority></url>
      <url><loc>https://atozdownloaderbykartik.pythonanywhere.com/insta-dp-viewer</loc><priority>0.8</priority></url>
      <url><loc>https://atozdownloaderbykartik.pythonanywhere.com/instagram-story-downloader</loc><priority>0.8</priority></url>
      <url><loc>https://atozdownloaderbykartik.pythonanywhere.com/instagram-highlight-downloader</loc><priority>0.8</priority></url>
      <url><loc>https://atozdownloaderbykartik.pythonanywhere.com/facebook-reels-downloader</loc><priority>0.9</priority></url>
      <url><loc>https://atozdownloaderbykartik.pythonanywhere.com/about-us</loc><priority>0.5</priority></url>
      <url><loc>https://atozdownloaderbykartik.pythonanywhere.com/privacy-policy</loc><priority>0.5</priority></url>
      <url><loc>https://atozdownloaderbykartik.pythonanywhere.com/contact-us</loc><priority>0.5</priority></url>
    </urlset>"""
    return Response(xml_content, mimetype='text/xml')

# 🔥 MAIN DOWNLOAD LOGIC 🔥
# 🔥 MAIN DOWNLOAD LOGIC WITH CAPTION FETCHING 🔥
# 🔥 MAIN DOWNLOAD LOGIC WITH CAPTION FETCHING & YOUTUBE SHORTS JUGAAD 🔥
@app.route('/download', methods=['POST'])
def download():
    raw_url = request.form.get('url', '').strip()
    current_tab = request.form.get('active_tab', 'auto')
    media_list = []
    full_caption = ""  # 📝 Caption aur Title save karne ke liye dabba

    # 1. 📸 INSTA DP FILTER
    if current_tab == 'dp':
        if '/' in raw_url or '.' in raw_url:
            return render_template('index.html', error="Bhai, yahan link nahi, sirf Instagram Username daalein!", active_tab=current_tab)
        try:
            profile = instaloader.Profile.from_username(L.context, raw_url)
            dp_url = profile.get_profile_pic_url()
            media_list = [{'type': 'Photo', 'url': dp_url, 'thumb': dp_url, 'title': f"{raw_url}_DP"}]
            return render_template('index.html', media_list=media_list, active_tab=current_tab, caption="")
        except:
            return render_template('index.html', error="Invalid Username! Sahi username check karein.", active_tab=current_tab)

    # 2. 📱 INSTAGRAM REELS FILTER
    elif current_tab == 'reels':
        if 'instagram.com/reels/' not in raw_url and 'instagram.com/reel/' not in raw_url:
            return render_template('index.html', error="Bhai, ye Reels link nahi hai! Kripya valid Insta Reel link dalein.", active_tab=current_tab)

    # 3. ▶️ INSTAGRAM VIDEO FILTER
    elif current_tab == 'video':
        if 'instagram.com/p/' not in raw_url and 'instagram.com/tv/' not in raw_url and 'video' not in raw_url:
            return render_template('index.html', error="Bhai, ye Instagram Video link nahi hai! Sahi link check karein.", active_tab=current_tab)

    # 4. 🖼️ INSTAGRAM PHOTO FILTER
    elif current_tab == 'photo':
        if 'instagram.com/p/' not in raw_url:
            return render_template('index.html', error="Bhai, ye Instagram Photo link nahi hai!", active_tab=current_tab)

    # 5. 🤳 INSTAGRAM STORY FILTER
    elif current_tab == 'story':
        if 'instagram.com/stories/' not in raw_url:
            return render_template('index.html', error="Bhai, valid Instagram Story link dalein!", active_tab=current_tab)

    # 6. 🌟 INSTAGRAM HIGHLIGHT FILTER
    elif current_tab == 'highlight':
        if 'instagram.com/s/' not in raw_url and 'highlight' not in raw_url:
            return render_template('index.html', error="Bhai, valid Instagram Highlight link dalein!", active_tab=current_tab)

    # 7. 🎞️ FACEBOOK REELS FILTER
    elif current_tab == 'fb':
        if 'facebook.com' not in raw_url and 'fb.watch' not in raw_url and 'fb.gg' not in raw_url:
            return render_template('index.html', error="Bhai, ye Facebook link nahi hai! FB Reels link dalein.", active_tab=current_tab)

        # 8. 🎞️youtube FILTER
    elif current_tab == 'yt':
        if 'youtube.com' not in raw_url and 'youtu.be' not in raw_url:
            return render_template('index.html', error="Bhai, ye YouTube ka link nahi hai! Sahi Shorts ya Video ka link dalein.", active_tab=current_tab)
    elif current_tab == 'tiktok':
        if 'tiktok.com' not in raw_url:
            return render_template('index.html', error="Bhai, ye TikTok ka link nahi hai!", active_tab=current_tab)

    elif current_tab == 'twitter':
        if 'twitter.com' not in raw_url and 'x.com' not in raw_url:
            return render_template('index.html', error="Bhai, ye Twitter (X) ka link nahi hai!", active_tab=current_tab)

    elif current_tab == 'ytmp3':
        if 'youtube.com' not in raw_url and 'youtu.be' not in raw_url:
            return render_template('index.html', error="Bhai, ye YouTube ka link nahi hai!", active_tab=current_tab)

    elif current_tab == 'pinterest':
        if 'pinterest.com' not in raw_url and 'pin.it' not in raw_url:
            return render_template('index.html', error="Bhai, ye Pinterest ka link nahi hai!", active_tab=current_tab)

    elif current_tab == 'threads':
        if 'threads.net' not in raw_url and 'threads.com' not in raw_url:
            return render_template('index.html', error="Bhai, ye Threads ka link nahi hai!", active_tab=current_tab)
    url = get_real_url(raw_url)

    try:
        # 🔥 ENGINE 1: YOUTUBE SHORTS & LONG VIDEO JUGAD 🔥
   # 🔥 ENGINE 1: YOUTUBE SHORTS, VIDEO & MP3 🔥
        if 'youtube.com' in url or 'youtu.be' in url:
            video_id = ""
            if 'youtu.be/' in url:
                video_id = url.split('youtu.be/')[1].split('?')[0]
            elif '/shorts/' in url:
                video_id = url.split('/shorts/')[1].split('?')[0]
            elif 'v=' in url:
                video_id = url.split('v=')[1].split('&')[0]

            if not video_id:
                return render_template('index.html', error="Bhai, ye YouTube link thik nahi lag raha.", active_tab=current_tab)

            api_url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"
            querystring = {"videoId": video_id, "urlAccess": "normal", "videos": "auto", "audios": "auto"}
            headers = {
                "X-RapidAPI-Key": "34ed1f8149msh8968a77b1783e63p17b3aejsn78ff14f8b053",
                "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
            }

            try:
                response = requests.get(api_url, headers=headers, params=querystring, timeout=15)
                data = response.json()

                if data:
                    dl_link = None
                    video_title = data.get('title') or "YouTube_Media"
                    thumb = ""
                    if data.get('thumbnails') and isinstance(data['thumbnails'], list) and len(data['thumbnails']) > 0:
                        thumb = data['thumbnails'][-1].get('url')

                    media_type = 'Video'

                    # 🎵 MP3 AUDIO NIKALNE KA JUGAAD 🎵
                    if current_tab == 'ytmp3':
                        media_type = 'Audio'
                        audios_data = data.get('audios')
                        if isinstance(audios_data, list) and len(audios_data) > 0:
                            dl_link = audios_data[0].get('url')
                        elif isinstance(audios_data, dict) and 'items' in audios_data:
                            dl_link = audios_data['items'][0].get('url')

                    # 🎥 VIDEO NIKALNE KA JUGAAD 🎥
                    else:
                        videos_data = data.get('videos')
                        if isinstance(videos_data, list) and len(videos_data) > 0:
                            dl_link = videos_data[0].get('url')
                        elif isinstance(videos_data, dict):
                            if 'items' in videos_data and isinstance(videos_data['items'], list) and len(videos_data['items']) > 0:
                                dl_link = videos_data['items'][0].get('url')
                            else:
                                dl_link = videos_data.get('url')

                        if not dl_link:
                            dl_link = data.get('url') or data.get('downloadUrl')

                    if dl_link:
                        media_list.append({
                            'type': media_type,
                            'url': dl_link,
                            'thumb': thumb if thumb else dl_link,
                            'title': video_title[:30]
                        })
                        return render_template('index.html', media_list=media_list, caption=f"🎵 {video_title}" if media_type=='Audio' else video_title, active_tab=current_tab)
                    else:
                        safe_data = {k: v for k, v in data.items() if k != 'description'}
                        return render_template('index.html', error=f"Link chhupa hai! Debug Info: {str(safe_data)[:300]}", active_tab=current_tab)
                else:
                    return render_template('index.html', error="API ne khali data bheja hai.", active_tab=current_tab)

            except Exception as yt_err:
                return render_template('index.html', error=f"RapidAPI Timeout/Failed: {yt_err}", active_tab=current_tab)


        # 🔥 ENGINE 4: TIKTOK (NO WATERMARK) 🔥
        if 'tiktok.com' in url:
            api_url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/rich_response/index"
            querystring = {"url": url}
            headers = {
                "X-RapidAPI-Key": "34ed1f8149msh8968a77b1783e63p17b3aejsn78ff14f8b053",
                "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
            }

            try:
                response = requests.get(api_url, headers=headers, params=querystring, timeout=15)
                data = response.json()

                dl_link = None
                video_title = "TikTok Viral Video"
                thumb = ""

                # Smart Extraction for TikTok
                if data and isinstance(data, dict):
                    # Trying common TikTok API JSON formats
                    if 'data' in data and isinstance(data['data'], dict):
                        dl_link = data['data'].get('play') or data['data'].get('wmplay') or data['data'].get('hdplay')
                        video_title = data['data'].get('title') or "TikTok Video"
                        thumb = data['data'].get('cover') or ""

                    if not dl_link:
                        dl_link = data.get('play') or data.get('nwm_video_url') or data.get('video_url')
                        video_title = data.get('desc') or data.get('title') or "TikTok Video"
                        thumb = data.get('cover') or data.get('thumbnail') or ""

                if dl_link:
                    media_list.append({
                        'type': 'Video',
                        'url': dl_link,
                        'thumb': thumb if thumb else dl_link,
                        'title': video_title[:30]
                    })
                    return render_template('index.html', media_list=media_list, caption=video_title, active_tab=current_tab)
                else:
                    # Agar API format alag nikla, toh ye error hume bata dega
                    return render_template('index.html', error=f"TikTok URL Blocked/Changed! Debug: {str(data)[:300]}", active_tab=current_tab)

            except Exception as tk_err:
                return render_template('index.html', error=f"TikTok API Failed: {tk_err}", active_tab=current_tab)

                # 🔥 ENGINE 5: PINTEREST 🔥
        if 'pinterest.com' in url or 'pin.it' in url:
            api_url = "https://pinterest-video-and-image-downloader.p.rapidapi.com/pinterest"
            querystring = {"url": url}
            headers = {
                "X-RapidAPI-Key": "34ed1f8149msh8968a77b1783e63p17b3aejsn78ff14f8b053",
                "X-RapidAPI-Host": "pinterest-video-and-image-downloader.p.rapidapi.com"
            }

            try:
                response = requests.get(api_url, headers=headers, params=querystring, timeout=15)
                data = response.json()

                dl_link = None
                video_title = "Pinterest Media"
                thumb = ""
                media_type = "Photo" # Default photo manenge

               # 🌟 Smart Extraction for Pinterest
                if data and isinstance(data, dict):
                    # API ne data ke andar ek aur data dabba bheja hai
                    inner_data = data.get('data')

                    if isinstance(inner_data, dict) and inner_data.get('url'):
                        dl_link = inner_data.get('url')
                        thumb = inner_data.get('thumbnail') or ""

                        # API khud bata rahi hai ki type video hai
                        if data.get('type') == 'video' or '.mp4' in dl_link:
                            media_type = 'Video'
                        else:
                            media_type = 'Photo'

                    # Backup check (Agar kabhi API format badle)
                    if not dl_link:
                        dl_link = data.get('video') or data.get('image') or data.get('url')
                        if dl_link and '.mp4' in dl_link:
                            media_type = 'Video'

                    video_title = data.get('title') or "Pinterest Media"
                    if not thumb:
                        thumb = dl_link

                if dl_link:
                    media_list.append({
                        'type': media_type,
                        'url': dl_link,
                        'thumb': thumb if thumb else dl_link,
                        'title': video_title[:30]
                    })
                    return render_template('index.html', media_list=media_list, caption=video_title, active_tab=current_tab)
                else:
                    # Agar API ka format alag nikla, toh ye dabba exact data print kar dega
                    safe_data = {k: v for k, v in data.items() if k != 'description'}
                    return render_template('index.html', error=f"Link chhupa hai! Debug Info: {str(safe_data)[:300]}", active_tab=current_tab)

            except Exception as pin_err:
                return render_template('index.html', error=f"Pinterest API Failed: {pin_err}", active_tab=current_tab)

   # 🔥 ENGINE 6: TWITTER (X) VIA NEW RAPIDAPI 🔥
        if 'twitter.com' in url or 'x.com' in url:
            api_url = "https://twitter-x-video-downloader4.p.rapidapi.com/api/v1/twitter"
            querystring = {"url": url}

            headers = {
                "X-RapidAPI-Key": "34ed1f8149msh8968a77b1783e63p17b3aejsn78ff14f8b053",
                "X-RapidAPI-Host": "twitter-x-video-downloader4.p.rapidapi.com"
            }

            try:
                response = requests.get(api_url, headers=headers, params=querystring, timeout=15)
                data = response.json()

                # 🌟 API "Success" hone par logic
                if data and isinstance(data, dict) and data.get('status') == 'success':
                    tweet_data = data.get('data', {})

                    if tweet_data.get('mediaCount', 0) == 0:
                        return render_template('index.html', error="Bhai, is Tweet mein koi Video ya Photo nahi hai! Sahi link daalein.", active_tab=current_tab)

                    dl_link = None
                    media_type = 'Video'

                    # 🕵️‍♂️ SMART EXTRACTION LEVEL 99
                    # 1. Normal Check
                    if 'media' in tweet_data and isinstance(tweet_data['media'], list) and len(tweet_data['media']) > 0:
                        media_item = tweet_data['media'][0]

                        # Agar video multiple qualities (HD/SD) me chhupi ho
                        if 'video_info' in media_item and 'variants' in media_item['video_info']:
                            variants = media_item['video_info']['variants']
                            mp4_links = [v for v in variants if v.get('content_type') == 'video/mp4']
                            if mp4_links:
                                best_video = sorted(mp4_links, key=lambda x: x.get('bitrate', 0), reverse=True)[0]
                                dl_link = best_video.get('url')

                        # 🔥 YAHAN 'image' ADD KIYA HAI PHOTO KE LIYE 🔥
                        if not dl_link:
                            dl_link = media_item.get('url') or media_item.get('video_url') or media_item.get('image')

                        if media_item.get('type') == 'photo' or (dl_link and ('.jpg' in dl_link.lower() or '.png' in dl_link.lower())):
                            media_type = 'Photo'

                    # 2. Direct Check
                    if not dl_link:
                        dl_link = tweet_data.get('video_url') or tweet_data.get('media_url')

                    # 3. 🔥 THE BRAHMASTRA: REGEX HACK (For Hidden Videos) 🔥
                    if not dl_link:
                        import re
                        mp4_matches = re.findall(r'https?://[^\s\'"]+\.mp4[^\s\'"]*', str(data))
                        if mp4_matches:
                            dl_link = mp4_matches[0]

                    # Final Download Render
                    if dl_link:
                        video_title = tweet_data.get('description') or "Twitter / X Media"
                        thumb = tweet_data.get('thumbnail') or ""

                        media_list.append({
                            'type': media_type,
                            'url': dl_link,
                            'thumb': thumb if thumb else dl_link,
                            'title': video_title[:30]
                        })
                        return render_template('index.html', media_list=media_list, caption=video_title, active_tab=current_tab)
                    else:
                        debug_media = str(tweet_data.get('media', 'Media hi nahi aaya'))[:600]
                        return render_template('index.html', error=f"Media format alag hai. Debug: {debug_media}", active_tab=current_tab)

                else:
                    return render_template('index.html', error="API ne Error return kiya hai. Dobara try karein.", active_tab=current_tab)

            except Exception as tw_err:
                return render_template('index.html', error=f"Twitter API Failed: {tw_err}", active_tab=current_tab)

      # 🔥 ENGINE 7: THREADS (NEW UNLIMITED API) 🔥
# 🔥 ENGINE 7: THREADS (PREMIUM BOT-NET APIs) 🔥
        if 'threads.net' in url or 'threads.com' in url:
            try:
                import requests
                
                # URL ka kachra saaf karna
                clean_url = url.replace('threads.com', 'threads.net').split('?')[0]
                
                # 3 Premium Bot APIs (WhatsApp aur Telegram bots inhi par chalte hain)
                api_endpoints = [
                    f"https://bk9.fun/download/threads?url={clean_url}",
                    f"https://api.vreden.web.id/api/threads?url={clean_url}",
                    f"https://api.ryzendesu.vip/api/downloader/threads?url={clean_url}"
                ]
                
                dl_link = None
                media_type = "Video"
                thumb = ""
                
                # Ek-ek karke APIs ko check karna
                for api in api_endpoints:
                    try:
                        res = requests.get(api, timeout=12)
                        if res.status_code == 200:
                            data = res.json()
                            
                            # API ka response parse karna
                            if isinstance(data, dict):
                                # Alag-alag APIs alag-alag naam se data bhejti hain
                                result = data.get('BK9') or data.get('result') or data.get('data') or data
                                
                                # Agar list ke andar link hai
                                if isinstance(result, list) and len(result) > 0:
                                    if isinstance(result[0], dict):
                                        dl_link = result[0].get('url') or result[0].get('video') or result[0].get('media')
                                    elif isinstance(result[0], str):
                                        dl_link = result[0]
                                # Agar direct dict ke andar link hai
                                elif isinstance(result, dict):
                                    dl_link = result.get('video_url') or result.get('url') or result.get('media')
                                    
                            # Agar real media link mil gaya, toh dhoondhna band karo
                            if dl_link and ('mp4' in dl_link or 'jpg' in dl_link or 'instagram' in dl_link):
                                break 
                    except:
                        continue # Agar ek API down hai toh agle par jao
                        
                if dl_link:
                    # Media type check karna
                    if '.jpg' in dl_link.lower() or '.png' in dl_link.lower() or '.webp' in dl_link.lower():
                        media_type = "Photo"
                        
                    media_list.append({
                        'type': media_type,
                        'url': dl_link,
                        'thumb': dl_link,
                        'title': "Threads Media"
                    })
                    return render_template('index.html', media_list=media_list, caption="Threads Media", active_tab=current_tab)
                else:
                    return render_template('index.html', error="Bhai, is video ko Threads ne kaafi zyada secure kar rakha hai, ya link private hai.", active_tab=current_tab)

            except Exception as th_err:
                return render_template('index.html', error=f"Threads Bot-Net Engine Failed: {str(th_err)}", active_tab=current_tab)
        # 🔥 ENGINE 2: INSTAGRAM

        # 🔥 ENGINE 2: INSTAGRAM
        elif 'instagram.com' in url:
            if '/stories/' in url:
                ydl_opts = {'quiet': True, 'format': 'best', 'cookiefile': cookie_path if os.path.exists(cookie_path) else None}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    full_caption = info.get('description') or info.get('title') or ""
                    if 'entries' in info:
                        for entry in info['entries']:
                            dl_url = entry.get('url')
                            if dl_url: media_list.append({'type': 'Video' if entry.get('ext') in ['mp4', 'webm'] else 'Photo', 'url': dl_url, 'thumb': entry.get('thumbnail') or dl_url, 'title': entry.get('title') or "Insta_Highlight"})
                    else:
                        dl_url = info.get('url')
                        if dl_url: media_list.append({'type': 'Video' if info.get('ext') in ['mp4', 'webm'] else 'Photo', 'url': dl_url, 'thumb': info.get('thumbnail') or dl_url, 'title': "Insta_Story"})
            else:
                shortcode = get_shortcode(url)
                if not shortcode: return render_template('index.html', error="Sahi Insta Link daalein.", active_tab=current_tab)
                post = instaloader.Post.from_shortcode(L.context, shortcode)

                full_caption = post.caption if post.caption else ""
                caption_title = post.caption[:30] if post.caption else "Insta_Post"

                if post.typename == 'GraphSidecar':
                    for node in post.get_sidecar_nodes():
                        media_list.append({'type': 'Video' if node.is_video else 'Photo', 'url': node.video_url if node.is_video else node.display_url, 'thumb': node.display_url, 'title': caption_title})
                else:
                    media_list.append({'type': 'Video' if post.is_video else 'Photo', 'url': post.video_url if post.is_video else post.url, 'thumb': post.url, 'title': caption_title})

        # 🔥 ENGINE 3: UNIVERSAL FALLBACK (FACEBOOK REELS, ETC.)
        else:
            ydl_opts = {
                'quiet': True,
                'format': 'best',
                'extractor_args': {'youtube': {'player_client': ['android']}},
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'referer': 'https://www.google.com/',
                'nocheckcertificate': True,
                'ignoreerrors': True,
                'no_warnings': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

                if not info:
                    return render_template('index.html', error="Ye platform hamare free server par blocked hai. Instagram ya Facebook use karein!", active_tab=current_tab)

                full_caption = info.get('description') or info.get('title') or ""

                if 'entries' in info:
                    for entry in info['entries']:
                        dl_url = entry.get('url')
                        if dl_url: media_list.append({'type': 'Video' if entry.get('ext') in ['mp4', 'webm'] else 'Photo', 'url': dl_url, 'thumb': entry.get('thumbnail') or dl_url, 'title': entry.get('title') or "AToZ_Media"})
                else:
                    dl_url = info.get('url')
                    if dl_url: media_list.append({'type': 'Video' if info.get('ext') in ['mp4', 'webm'] else 'Photo', 'url': dl_url, 'thumb': info.get('thumbnail') or dl_url, 'title': info.get('title') or "AToZ_Media"})

        if media_list:
            return render_template('index.html', media_list=media_list, caption=full_caption, active_tab=current_tab)
        else:
            return render_template('index.html', error="Media nahi mila. Link check karein.", active_tab=current_tab)

    except Exception as e:
        print(f"Error: {e}")
        return render_template('index.html', error="Media fetch karne me dikkat aayi. Link check karein ya thodi der baad try karein.", active_tab=current_tab)

@app.route('/proxy_image')
def proxy_image():
    img_url = request.args.get('url')
    try:
        resp = requests.get(img_url, stream=True)
        return Response(resp.iter_content(chunk_size=1024), content_type=resp.headers.get('Content-Type'))
    except: return "Error", 500

@app.route('/force_download')
def force_download():
    media_url = request.args.get('url')
    media_type = request.args.get('type', 'Video')
    raw_title = request.args.get('title', 'AToZ_Media')

    try:
        # Smart Extension Selector
        ext = 'mp3' if media_type == 'Audio' else ('mp4' if media_type == 'Video' else 'jpg')
        clean_title = re.sub(r'[^A-Za-z0-9 ]+', '', raw_title).replace(" ", "_")[:30]
        if not clean_title: clean_title = "AToZ_Media"
        filename = f"{clean_title}_{random.randint(100,999)}.{ext}"

        # 🔥 HEAVY BYPASS HEADERS 🔥
        req_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Connection': 'keep-alive'
            # Referer hata diya kyunki kuch RapidAPI links direct hit maangte hain
        }

        resp = requests.get(media_url, stream=True, headers=req_headers)

        # Agar Server ne File de di
        if resp.status_code == 200:
            headers = {
                'Content-Disposition': f'attachment; filename="{filename}"',
                'Content-Type': resp.headers.get('Content-Type') or 'video/mp4'
            }
            if 'Content-Length' in resp.headers:
                headers['Content-Length'] = resp.headers['Content-Length']

            return Response(resp.iter_content(chunk_size=1048576), headers=headers)
        else:
            # 💥 AB REDIRECT NAHI HOGA, SCREEN PAR ERROR AAYEGA 💥
            return f"Bhai, YouTube ne Server ko Block kar diya! Status Code: {resp.status_code}. Original Link IP-Locked hai."

    except Exception as e:
        return f"Force Download Crash Error: {e}"
