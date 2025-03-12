# A/B Test Analizörü

Bu uygulama, A/B test sonuçlarınızın istatistiksel analizini yapmanıza yardımcı olan bir web uygulamasıdır. Türkçe ve İngilizce dil desteği ile birlikte gelir.

## Özellikler

- İki dil desteği (Türkçe/İngilizce)
- Dönüşüm oranlarının karşılaştırılması
- İstatistiksel anlamlılık testi
- Güven aralığı hesaplaması
- Görsel sonuç gösterimi

## Kurulum

1. Repoyu klonlayın:
```bash
git clone https://github.com/KULLANICI_ADINIZ/ABTestAnalyzer.git
cd ABTestAnalyzer
```

2. Python 3.11 veya üstü gereklidir. Sanal ortam oluşturun:
```bash
python -m venv venv
```

3. Sanal ortamı aktifleştirin:
```bash
# Windows için:
.\venv\Scripts\activate

# Linux/Mac için:
source venv/bin/activate
```

4. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

5. Uygulamayı çalıştırın:
```bash
streamlit run main.py
```

## Kullanım

1. Sol menüden dil seçiminizi yapın
2. Kontrol (A) ve Test (B) grupları için verilerinizi girin
3. "Sonuçları Hesapla" butonuna tıklayın
4. Sonuçları görsel ve sayısal olarak inceleyin

## Render.com Deployment

1. Render.com hesabınıza giriş yapın
2. "New +" butonuna tıklayın ve "Web Service" seçin
3. GitHub reponuzu bağlayın
4. Aşağıdaki ayarları yapın:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run main.py`
   - Python Version: 3.11
   - Environment Variables: 
     - `PYTHON_VERSION=3.11`

## Lisans

MIT

## İletişim

GitHub: [@KULLANICI_ADINIZ](https://github.com/KULLANICI_ADINIZ) 