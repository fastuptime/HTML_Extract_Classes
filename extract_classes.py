#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import os

def extract_classes_from_html(file_path):
    if not os.path.exists(file_path):
        print(f"Hata: {file_path} dosyası bulunamadı!")
        return []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except Exception as e:
        print(f"Dosya okuma hatası: {e}")
        return []
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    class_set = set()
    
    for element in soup.find_all(attrs={"class": True}):
        classes = element.get('class')
        if classes:
            if isinstance(classes, str):
                classes = classes.split()
            
            for cls in classes:
                if cls.strip():  
                    class_set.add(cls.strip())
    
    return sorted(list(class_set))

def save_classes_to_file(classes, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("HTML Dosyasındaki Tüm CSS Class Adları\n")
            file.write("=" * 50 + "\n\n")
            
            for i, cls in enumerate(classes, 1):
                file.write(f"{i:3d}. {cls}\n")
            
            file.write(f"\nToplam: {len(classes)} farklı class bulundu.\n")
        
        print(f"Class listesi '{output_file}' dosyasına kaydedildi.")
    except Exception as e:
        print(f"Dosya yazma hatası: {e}")

def main():
    html_file = "index.html"
    output_file = "css_classes.txt"
    
    print("HTML dosyasından CSS class adları çıkarılıyor...")
    print(f"Dosya: {html_file}")
    print("-" * 50)
    
    classes = extract_classes_from_html(html_file)
    
    if classes:
        print(f"\nBulunan CSS Class Adları ({len(classes)} adet):")
        print("-" * 50)
        
        for i, cls in enumerate(classes, 1):
            print(f"{i:3d}. {cls}")
        
        save_classes_to_file(classes, output_file)
        
        print(f"\n📊 İstatistikler:")
        print(f"   • Toplam farklı class: {len(classes)}")
        print(f"   • En uzun class adı: {max(classes, key=len) if classes else 'N/A'}")
        print(f"   • En kısa class adı: {min(classes, key=len) if classes else 'N/A'}")
        
        prefixes = {}
        for cls in classes:
            parts = cls.split('_')
            if len(parts) > 1:
                prefix = parts[0]
                prefixes[prefix] = prefixes.get(prefix, 0) + 1
        
        if prefixes:
            print(f"\n🏷️  En yaygın class prefiksleri:")
            sorted_prefixes = sorted(prefixes.items(), key=lambda x: x[1], reverse=True)
            for prefix, count in sorted_prefixes[:5]:
                print(f"   • {prefix}_*: {count} adet")
    
    else:
        print("❌ Hiç CSS class bulunamadı!")

if __name__ == "__main__":
    main()
