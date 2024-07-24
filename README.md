# AI Quran
### *AI pake I bukan pake l, i kapital.

Manusia punya masalah, tuhan punya solusi. Punya masalah? Al-Quran adalah pedoman solusi dari tuhan.
Al-Quran pedoman manusia yang bisa ngesolve berbagai problem hidupnya.
So, kenapa nggak langsung cari solusi masalah dari Al-Quran aja? Gatau ayat mana yang relate?
Jrengg sekarang kita punya AI Quran yey. AI Quran bisa ngasi respon ayat quran mana yang relate sama problem yang dikasih dengan harapan ayat tersebut bisa membantu menelusuri jalan keluar dari problem yang dihadapi.

Meski keliatan interesting and exciting, AI ini masi butuh banyak banget belajar dan masih banyak gataunya, masi bayi. masih sangat rawan ngasi output yang ga relevan sebab dataset yang difeed cuman beberapa, sedangkan ayat Al-Quran total ada 6000 lebih. Artinya kita harus mapping 6000 ayat itu ke masalah yang relate sesuai relevansi problem dan ayatnya. We need more data. In fact, buat saat ini cuman bisa ngasi ayat sama translate nya doang tanpa ngegenerate teks buat explain, ngasi kesimpulan/saran yang bisa diambil dari ayat tsb buat ngesolve problem soale kita ngebuild dari nol tanpa pake API kek OpenAI API dkk. But in further development, it's not impossible at all.


## Required packages

1. pandas
2. numpy
3. nltk
4. scikit-learn
5. flask

## Daftar Isi/Rincian File

1. app.py = isinya flask, buat ngerender html file, routing dan ngepost respon dengan ngasi tau user input ke module chat.py biar jalanin function chatbot(). cukup ngerun app.py = udah ngerun AI Quran nya tinggal pake di localhost

2. chat.py = jalanin function chatbot() buat manggil method get_response() di class QASystem di module model.py untuk dikasi ke app.py biar dipost ke web sama buat mastiin berhasil ngerespon apa engga

3. model.py = ini basically model AI kita di sini. Dari mulai initializing required packages nya, ngeread dataset, preprocessing, vectorizing, dan ngapply cosine similarity ke text input dan kolom "isu" yang ada di dataset buat ngambil ayat yang sesuai di kolom "dalil" melalui method get_response()

4. dataset.csv = isinya data tentang isu-isu yang mungkin akan diinput user dan ayat Al-Quran serta terjemah dan navigasinya

5. clean_dataset.csv = dataset yang udah dibersihin biar bisa diread tanpa error

6. chat.html = tampilan front-end web, include internal css styling sama js script

## Running the program

1. Clone repository ke lokal
2. Open/navigate ke project directory nya
3. Run file app.py
4. Go to local host

## Future improvements

Versi ini masi need much more improvements. Yang mungkin bisa diimprove:

1. Bikin algoritma biar bisa ngerespon lebih dari satu ayat yang sesuai
2. Generate teks di bawah dalil buat ngasi penjelasan, kesimpulan dan saran dari dalil yang ditunjukin
3. Mungkin bisa ditambahin hadis meski ntar ada yang salah dengan namanya
4. Ngesave user input dan responnya ke dataset biar bisa dievaluasi dan biar bisa self learning.
   