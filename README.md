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
