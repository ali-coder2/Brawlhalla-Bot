# 🥊 Brawlhalla-Bot

> Yapay zeka odaklı, YOLO mimarisi ve yüksek performanslı ekran yakalama (MSS) altyapısıyla çalışan otonom Brawlhalla bot projesidir.

`🐍 Python` · `👁️ OpenCV & YOLO` · `🚀 MSS & PyAutoGUI` · `🛡️ MIT License`

---

## 📋 Özellikler

* **YOLO Tabanlı Nesne Tespiti:** Sabit görseller yerine akıllı model ağırlıklarıyla karakter ve silah takibi.
* **Performans Optimizasyonu (Frame Skipping):** İşlemciyi yormamak ve milisaniyelik gecikmeleri (lag) önlemek için kare atlama mekanizması.
* **Dinamik Karar Matrisi:** Anlık koordinat analiziyle akıllı kombo, kaçış ve hamle üretimi.
* **Acil Durdurma (Failsafe):** Fareyi ekranın sol üst köşesine çekerek botu anında durdurabilme güvenliği.

---

## ⚙️ Gereksinimler

Sistemi çalıştırmadan önce aşağıdaki bileşenlerin sisteminizde kurulu olduğundan emin olun:

* Python 3.8 veya üzeri
* Brawlhalla oyununun kendisi ve özel eğitilmiş ağırlık dosyası (`brawl_model.pt`)

---

## 🛠️ Kurulum

1. Repoyu klonlayın:
   ```bash
   git clone [https://github.com/kullanici-adin/Brawlhalla-Bot.git](https://github.com/kullanici-adin/Brawlhalla-Bot.git)
   pip install -r requirements.txt
   cd Brawlhalla-Bot
