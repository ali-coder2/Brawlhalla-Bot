import random
import time
import cv2
from ultralytics import YOLO
import mss
import numpy as np
import pyautogui

# --- GÜVENLİK VE GENEL AYARLAR ---
pyautogui.FAILSAFE = (
    True  # Fareyi ekranın sol üst köşesine çekerek botu acil durdurabilirsin
)
pyautogui.PAUSE = 0.01  # Komutlar arası milisaniyelik bekleme

# Ekran Çözünürlüğü
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
MONITOR = {"top": 0, "left": 0, "width": SCREEN_WIDTH, "height": SCREEN_HEIGHT}


class BrawlhallaAIBot:

  def __init__(self, model_path="brawl_model.pt"):
    print("[BILGI] Yapay zeka modeli yükleniyor...")
    try:
      # Özel eğittiğin model yüklenir (Eğer yoksa varsayılan nano model dener)
      self.model = YOLO(model_path)
    except Exception as e:
      print(
          f"[UYARI] Özel model bulunamadı ({e}), 'yolov8n.pt' yedek olarak"
          " yükleniyor."
      )
      self.model = YOLO("yolov8n.pt")

    self.sct = mss.mss()
    self.is_running = True
    print("[BILGI] Bot başarıyla başlatıldı ve aktif!")

  def ekran_goruntusu_al(self):
    """MSS kütüphanesi ile ekranı anlık ve hızlı yakalar."""
    img = np.array(self.sct.grab(MONITOR))
    return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

  def menu_ve_baslangic(self):
    """Oyun başlangıç ve menü geçişlerini klavye simülasyonu ile yönetir."""
    print("[BILGI] Menü yönlendirmeleri yapılıyor...")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(1.5)
    pyautogui.press("enter")
    time.sleep(3)

  def karakter_sec(self):
    """Karakter seçim ekranındaki otomatik yön tuşu kombinasyonları."""
    print("[BILGI] Karakter seçiliyor...")
    time.sleep(2)
    for _ in range(3):
      pyautogui.press("d")
      time.sleep(0.1)
    pyautogui.press("space")
    time.sleep(1.5)

  def otonom_mac_dongusu(self):
    """Yapay zeka odaklı, kare atlama optimizasyonlu ana maç döngüsü."""
    print(
        "[BILGI] Maç başladı, yapay zeka ve dinamik karar döngüsü devrede!"
    )
    start_time = time.time()
    max_match_time = 300  # 5 dakika güvenlik sınırı

    frame_counter = 0
    son_hedef_x = None
    son_silah_x = None

    while self.is_running:
      # Maç süre aşımı kontrolü
      if time.time() - start_time > max_match_time:
        print("[BILGI] Maç süresi doldu, çıkış yapılıyor.")
        pyautogui.press("esc")
        time.sleep(2)
        pyautogui.press("enter")
        break

      # Anlık ekran karesi al
      frame = self.ekran_goruntusu_al()

      # --- PERFORMANS OPTİMİZASYONU: KARE ATLAMA (FRAME SKIPPING) ---
      # İşlemciyi yormamak için model her 3 karede bir çalıştırılır.
      frame_counter += 1
      if frame_counter % 3 == 0:
        results = self.model(frame, conf=0.50, verbose=False)

        son_hedef_x = None
        son_silah_x = None

        for r in results:
          for box in r.boxes:
            cls_id = int(box.cls[0])
            # Sabit ID'ler yerine modelin kendi etiket sözlüğünden ismi çekiyoruz
            class_name = self.model.names.get(cls_id, "unknown")

            xyxy = box.xyxy[0].cpu().numpy()
            center_x = int((xyxy[0] + xyxy[2]) / 2)

            # Özel modelindeki etiket isimlerine göre eşleştirme (Örn: 'opponent', 'weapon')
            if class_name in ["opponent", "rakip", "player"]:
              son_hedef_x = center_x
            elif class_name in ["weapon", "silah", "item"]:
              son_silah_x = center_x

      # --- DINAMİK KARAR VE AKSİYON MATRİSİ ---
      if son_hedef_x is not None:
        # Rakibin konumuna göre hareket et ve saldır
        if son_hedef_x < SCREEN_WIDTH / 2:
          pyautogui.press("a")
        else:
          pyautogui.press("d")

        # Akıllı kombo üretimi
        aksiyon = random.choice(["light", "heavy", "kombo"])
        if aksiyon == "light":
          pyautogui.press("j")
        elif aksiyon == "heavy":
          pyautogui.press("k")
        elif aksiyon == "kombo":
          pyautogui.press("j")
          time.sleep(0.03)
          pyautogui.press("w")
          pyautogui.press("j")

      elif son_silah_x is not None:
        # Silaha doğru yönel ve topla
        if son_silah_x < SCREEN_WIDTH / 2:
          pyautogui.press("a")
        else:
          pyautogui.press("d")
        pyautogui.press("j")

      else:
        # Hedef yoksa haritada aktif kalmak için rastgele taktiksel hareket
        taktik = random.choice(["zipla", "bekle", "sag_sol"])
        if taktik == "zipla":
          pyautogui.press("space")
        elif taktik == "sag_sol":
          pyautogui.press("a" if random.random() > 0.5 else "d")

      # Döngü hızı dengesi
      time.sleep(0.02)


if __name__ == "__main__":
  try:
    # Model dosyası adını buraya yazabilirsin (Örn: 'brawl_model.pt')
    bot = BrawlhallaAIBot(model_path="brawl_model.pt")
    bot.menu_ve_baslangic()
    bot.karakter_sec()
    bot.otonom_mac_dongusu()
  except KeyboardInterrupt:
    print(
        "\n[BILGI] Bot kullanıcı tarafından güvenli bir şekilde durduruldu."
    )
