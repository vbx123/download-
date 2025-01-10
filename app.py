from flask import Flask, render_template, request
import yt_dlp

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # عرض الصفحة الرئيسية (HTML)

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    if url:
        ydl_opts = {'outtmpl': '%(title)s.%(ext)s'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "تم تحميل الفيديو بنجاح!"
    return "يرجى إدخال رابط الفيديو."

if __name__ == '__main__':
    app.run(debug=True)
