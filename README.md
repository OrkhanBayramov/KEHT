<!-- Şəbəkə Analiz Aləti ARI -->

<h1>Şəbəkə Analiz Aləti  - "ARI" </h1>

<p>Bu Python skripti, aşağıdakı əsas funksiyonları yerinə yetirir:</p>

<ul>
  <li>Şəbəkədə routerin IP ünvanını tapmaq.</li>
  <li>Routerin IP ünvanını istifadə edərək şəbəkədə olan qurğuların IP və MAC ünvanlarını tapmaq.</li>
  <li>MAC ünvanları üçün istehsalçı adını tapmaq (macvendors.com veb saytından əldə edilir).</li>
</ul>

<h2>İstifadə Qaydaları</h2>

<p>Skripti işlədərək, şəbəkədə olan cihazların IP və MAC ünvanları əldə edilir və istehsalçı adları ilə birgə göstərilir. Skript, <code>netifaces</code>, <code>scapy</code>, və <code>requests</code> kimi üçüncü tərəfli Python kitabxanalarını istifadə edir. Eğer bu kitabxanalar yüklü deyilsə, skript özü avtomatik olaraq bu kitabxanaları yükləyir.</p>

<h2>Prosesi Dayandırmaq</h2>

<p>Skripti işlədərkən, terminalda "CTRL + C" düyməsinə basaraq prosesi dayandırmaq mümkündür.</p>

<h2>Quraşdırılma</h2>

<p>Skriptin düzgün işləyə bilməsi üçün aşağıdakı əlavə kitabxanaların quraşdırılması tövsiyə olunur:</p>

<pre><code>pip install netifaces scapy requests</code></pre>

<h2>Nümunə</h2>

<pre><code>python ari.py</code></pre>

<h1> ======================================== </h1>

<!-- HTTPS BYPASS -->

<h1> HTTPS BYPASS aləti </h1>

<p>Bu Python skripti, aşağıdakı funksiyonları yerinə yetirir:</p>

<ul>
  <li>Hədəf qurğunun HTTPS ötürmələrini HTTP protokolu ilə əvəzləyir.</li>
  <li>Hədəf qurğunun ötürdüyü məlumatları əldə etmək imkanı yaradır.</li>
</ul>

<h2>İstifadə Qaydaları</h2>

<p>Skripti işlədərək, hədəf qurğunun HTTPS bağlantılarında SSL-TLS şifrlənməsinin ləğvi mümkündür.</p>

<h2>Tələblərin Yoxlanılması və Quraşdırılması</h2>

<p>Skriptin düzgün işləyə bilməsi üçün əsas tələblərin yoxlanılması və quraşdırılması:</p>

<pre><code>sudo apt install python3-pip -y
sudo pip3 install netifaces</code></pre>

<p>Skript, Bettercap alətini istifadə edir. Əgər sistemdə yoxdursa, onu avtomatik quraşdırmaq üçün:</p>

<pre><code>sudo apt install bettercap -y</code></pre>

<h2>İstifadə</h2>

<p>Skripti işlədərkən, şəbəkə interfeysi seçilir və Bettercap vasitəsilə HTTPS bypass prosesi başladılır.</p>

<pre><code>sudo python3 bypass_https.py</code></pre>

