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

<h1>=========================================<//h1>

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

<h1>=========================================</h1>

<h1>DNS Yönləndirmə Aləti</h1>

<p>Bu Python skripti, aşağıdakı funksiyonları yerinə yetirir:</p>

<ul>
  <li>Hədəf qurğu və ya hədəf Domain yaxud İP ünvanı daxil edilir.</li>
  <li>Hədəfin daxil olmaq istədiyi ünvan lokal serverdə saxta olaraq hazırlanmış ünvana yönləndirilir.</li>
</ul>

<h2>İstifadə Qaydaları</h2>

<p>Skriptin düzgün işləyə bilməsi üçün:</p>

<pre><code>sudo iptables -I FORWARD -j NFQUEUE --queue-num 0</code></pre>

<h2>Prosesi Dayandırmaq</h2>

<p>Skripti işlədərkən, terminalda "CTRL + C" düyməsinə basaraq prosesi dayandırmaq mümkündür.</p>

<h2>İstifadə</h2>

<p>Skripti işlədərkən, yönləndiriləcək domain və ya İP ünvanı daxil edilir.</p>

<pre><code>python dns_yon.py</code></pre>

<h1>=========================================</h1>

<!-- Şəbəkə interfeysinin Fiziki Ünvanını dəyişmək üçün Azərbaycan dilində intefeysi olan alət -->

<h1>Şəbəkə Interfeysi Fiziki Ünvanını Dəyişmək Üçün Alət</h1>

<p>Bu Python skripti, aşağıdakı funksiyonları yerinə yetirir:</p>

<ul>
  <li>Şəbəkə interfeysinin fiziki ünvanını dəyişmək.</li>
</ul>

<h2>İstifadə Qaydaları</h2>

<p>Skripti işlədərək, şəbəkə interfeysinin fiziki ünvanını dəyişmək mümkündür. İstifadəçiyə interfeys seçmək və təsadüfi və ya öz istənilən bir MAC ünvanı təyin etmək imkanı verir.</p>

<h2>Əsas Tələblər</h2>

<p>Skriptin düzgün işləyə bilməsi üçün aşağıdakı tələblərə ehtiyac var:</p>

<pre><code>sudo apt install python3</code></pre>

<h2>İstifadə</h2>

<p>Skripti işlədərkən, mövcud şəbəkə interfeyslərinin siyahısını görmək üçün:</p>

<pre><code>python mac_deyisen.py</code></pre>

<p>İstifadəçiyə bir interfeys seçməsi təklif edilir və sonra təsadüfi və ya öz istənilən bir MAC ünvanı təyin etmək imkanı verilir.</p>

<h1>=========================================</h1>

<!-- O.G.A "Ortada Gizlənmiş Adam" ARP Saxtakarlığı Aləti -->

<h1>O.G.A "Ortada Gizlənmiş Adam" ARP Saxtakarlığı Aləti</h1>

<p>Bu Python skripti, aşağıdakı funksiyonları yerinə yetirir:</p>

<ul>
  <li>Şəbəkədə hədəf və marşrutlaşdırıcı arasına girərək, ARP cədvəlini saxtalaşdırır.</li>
  <li>Hədəf qurğunun ötürdüyü məlumatları əldə etmək imkanı yaradır.</li>
</ul>

<h2>İstifadə Qaydaları</h2>

<p>Skripti işlədərək, şəbəkədəki hədəf və marşrutlaşdırıcı arasına girərək ARP saxtakarlığı təmin edilir. İnternet əlaqəsi təmin etmək üçün tələb olunan əmri daxil edin.</p>

<pre><code>sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'</code></pre>

<h2>Əsas Tələblər</h2>

<p>Skriptin düzgün işləyə bilməsi üçün aşağıdakı tələblərə ehtiyac var:</p>

<pre><code>sudo apt install python3 scapy</code></pre>

<h2>İstifadə</h2>

<p>Skripti işlədərkən, hədəf IP ünvanını daxil edin və internet əlaqəsini təyin edin:</p>

<pre><code>python oga.py</code></pre>

<p>CTRL + C düyməsinə basmaqla prosesi dayandırmaq mümkündür.</p>

<h1>=========================================</h1>

<!-- Şəbəkə İzləmə Aləti -->

<h1>Şəbəkə İzləmə Aləti</h1>

<p>Bu Python skripti, aşağıdakı funksiyonları yerinə yetirir:</p>

<ul>
  <li>Şəbəkəyə qoşulduğu interfeys üzərindən keçən informasiyanı oxuyur və log saxlayır.</li>
  <li>O.G.A aləti ilə birlikdə işlədikdə, hədəf qurğunun ötürdüyü məlumatları əldə etmək imkanı yaradır.</li>
</ul>

<h2>İstifadə Qaydaları</h2>

<p>Skripti işlədərkən, şəbəkəyə qoşulduğu interfeysi seçin və informasiyanın izlənməsinə başlayın:</p>

<pre><code>python paket_iz.py</code></pre>

<p>Nəticələri incələmək və saxlamaq üçün, CTRL + C düyməsinə basın.</p>

