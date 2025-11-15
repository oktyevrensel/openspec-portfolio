# Portfolio Website | Portfoy Web Sitesi

[English](#english) | [Türkçe](#turkish)

---

## English

A modern, full-stack portfolio website built with Next.js and Flask, featuring a dark/light theme toggle and responsive design.

### 🚀 Tech Stack

#### Frontend
- **Next.js 16** - React framework with App Router
- **React 19** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS 4** - Styling
- **next-themes** - Dark/light mode support
- **React Hook Form** - Form handling
- **Zod** - Schema validation

#### Backend
- **Flask 3.0** - Python web framework
- **SQLAlchemy** - ORM
- **Flask-CORS** - Cross-origin resource sharing
- **Python-dotenv** - Environment variables

### 📁 Project Structure

```
openspec-portfolio/
├── portfolio-frontend/     # Next.js frontend application
│   ├── app/               # App router pages
│   ├── components/        # React components
│   │   ├── layout/       # Layout components (Header, Footer, ThemeToggle)
│   │   └── ui/           # Reusable UI components (Button, Card, Input)
│   └── lib/              # Utilities and schemas
├── backend/               # Flask backend API
│   ├── app/              # Application code
│   │   ├── models.py     # Database models
│   │   └── routes.py     # API routes
│   └── run.py            # Application entry point
└── openspec/             # Project specifications
```

### 🎨 Features

- ✨ Modern, responsive design
- 🌓 Dark/light theme toggle
- 📱 Mobile-friendly navigation
- 🎯 SEO optimized
- 📝 Blog functionality
- 💼 Project showcase
- 📄 CV/Resume page
- 📧 Contact form
- 🔄 RESTful API backend

### 🛠️ Installation

#### Prerequisites
- Node.js 20+ 
- Python 3.8+
- npm or yarn

#### Frontend Setup

```bash
cd portfolio-frontend
npm install
npm run dev
```

The frontend will run on `http://localhost:3000`

#### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python run.py
```

The backend API will run on `http://localhost:5000`

### 📝 Available Scripts

#### Frontend
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

#### Backend
- `python run.py` - Start Flask development server

### 🎨 Color Palette

- **Light Mode Background**: `#f3ede5`
- **Dark Mode Background**: `#092757`
- **Accent Green 1**: `#86e5a1`
- **Accent Green 2**: `#c5ffbc`

### 📄 License

This project is open source and available under the Aphace License.

### 👤 Author

Oktay Evrensel

### 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## Turkish

Next.js ve Flask ile oluşturulmuş, karanlık/aydınlık tema değiştirme özelliği ve duyarlı tasarıma sahip modern, full-stack bir portfoy web sitesi.

### 🚀 Teknoloji Yığını

#### Frontend
- **Next.js 16** - App Router ile React framework'ü
- **React 19** - UI kütüphanesi
- **TypeScript** - Tip güvenliği
- **Tailwind CSS 4** - Stil oluşturma
- **next-themes** - Karanlık/aydınlık mod desteği
- **React Hook Form** - Form yönetimi
- **Zod** - Şema doğrulama

#### Backend
- **Flask 3.0** - Python web framework'ü
- **SQLAlchemy** - ORM
- **Flask-CORS** - Cross-origin kaynak paylaşımı
- **Python-dotenv** - Ortam değişkenleri

### 📁 Proje Yapısı

```
openspec-portfolio/
├── portfolio-frontend/     # Next.js frontend uygulaması
│   ├── app/               # App router sayfaları
│   ├── components/        # React bileşenleri
│   │   ├── layout/       # Layout bileşenleri (Header, Footer, ThemeToggle)
│   │   └── ui/           # Yeniden kullanılabilir UI bileşenleri (Button, Card, Input)
│   └── lib/              # Yardımcı araçlar ve şemalar
├── backend/               # Flask backend API
│   ├── app/              # Uygulama kodu
│   │   ├── models.py     # Veritabanı modelleri
│   │   └── routes.py     # API rotaları
│   └── run.py            # Uygulama giriş noktası
└── openspec/             # Proje spesifikasyonları
```

### 🎨 Özellikler

- ✨ Modern, duyarlı tasarım
- 🌓 Karanlık/aydınlık tema değiştirme
- 📱 Mobil uyumlu navigasyon
- 🎯 SEO optimize edilmiş
- 📝 Blog fonksiyonalitesi
- 💼 Proje vitrin
- 📄 CV/Özgeçmiş sayfası
- 📧 İletişim formu
- 🔄 RESTful API backend

### 🛠️ Kurulum

#### Gereksinimler
- Node.js 20+ 
- Python 3.8+
- npm veya yarn

#### Frontend Kurulumu

```bash
cd portfolio-frontend
npm install
npm run dev
```

Frontend `http://localhost:3000` adresinde çalışacaktır

#### Backend Kurulumu

```bash
cd backend
pip install -r requirements.txt
python run.py
```

Backend API `http://localhost:5000` adresinde çalışacaktır

### 📝 Kullanılabilir Scriptler

#### Frontend
- `npm run dev` - Geliştirme sunucusunu başlat
- `npm run build` - Production için derle
- `npm run start` - Production sunucusunu başlat
- `npm run lint` - ESLint'i çalıştır

#### Backend
- `python run.py` - Flask geliştirme sunucusunu başlat

### 🎨 Renk Paleti

- **Aydınlık Mod Arka Plan**: `#f3ede5`
- **Karanlık Mod Arka Plan**: `#092757`
- **Vurgu Yeşili 1**: `#86e5a1`
- **Vurgu Yeşili 2**: `#c5ffbc`

### 📄 Lisans

Bu proje açık kaynaklıdır ve Apache Lisansı altında mevcuttur.

### 👤 Yazar

Oktay Evrensel

### 🤝 Katkıda Bulunma

Katkılar, sorunlar ve özellik istekleri memnuniyetle karşılanır!
