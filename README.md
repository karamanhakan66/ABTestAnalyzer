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
git clone https://github.com/karamanhakan66/ABTestAnalyzer.git
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


## Lisans

MIT

## İletişim

GitHub: [@karamanhakan66](https://github.com/karamanhakan66) 