# ILSpy yordamida .exe faylni decompile qilish
# Decompiling a .exe File Using ILSpy

## ILSpy nima? / What is ILSpy?

**ILSpy** — bu .NET assembly larini (`.exe` va `.dll` fayllarni) manba kodiga aylantiruvchi ochiq manbali dekompilator dastur.  
**ILSpy** is a free, open-source .NET assembly browser and decompiler that converts compiled `.exe` and `.dll` files back into readable source code (C#, VB.NET, IL).

- **Rasmiy sayt / Official site:** https://github.com/icsharpcode/ILSpy
- **Litsenziya / License:** MIT

---

## 1-qadam: ILSpy-ni yuklab olish va o'rnatish / Step 1: Download and Install ILSpy

**O'zbek:**
1. [https://github.com/icsharpcode/ILSpy/releases](https://github.com/icsharpcode/ILSpy/releases) sahifasiga o'ting.
2. Eng so'nggi relizdan `ILSpy_binaries_*.zip` faylini yuklab oling (masalan, `ILSpy_binaries_9.x.zip`).
3. ZIP arxivini qulay papkaga chiqarib oling.
4. `ILSpy.exe` faylini ishga tushiring (o'rnatish talab qilinmaydi).

**English:**
1. Go to [https://github.com/icsharpcode/ILSpy/releases](https://github.com/icsharpcode/ILSpy/releases).
2. Download `ILSpy_binaries_*.zip` from the latest release (e.g., `ILSpy_binaries_9.x.zip`).
3. Extract the ZIP archive to a convenient folder.
4. Run `ILSpy.exe` (no installation required).

> **Talab / Requirement:** .NET Desktop Runtime 8.0 yoki undan yuqori versiyasi kerak.  
> .NET Desktop Runtime 8.0 or later is required. Download from https://dotnet.microsoft.com/download.

---

## 2-qadam: .exe faylni ILSpy'da ochish / Step 2: Open the .exe File in ILSpy

**O'zbek:**
1. ILSpy dasturini ishga tushiring.
2. Menyu satridan **File → Open** ni bosing (yoki `Ctrl+O`).
3. Fayl tanlash oynasida o'zingizning `.exe` faylingizni toping va tanlang, so'ng **Open** ni bosing.
4. Fayl chap paneldagi assembly daraxti ko'rinishida paydo bo'ladi.

**English:**
1. Launch ILSpy.
2. From the menu bar, click **File → Open** (or press `Ctrl+O`).
3. In the file dialog, navigate to your `.exe` file, select it, and click **Open**.
4. The file appears in the assembly tree in the left panel.

> **Maslahat / Tip:** Faylni to'g'ridan-to'g'ri ILSpy oynasiga sudrab tashlashingiz ham mumkin (drag & drop).  
> You can also drag and drop the `.exe` file directly onto the ILSpy window.

---

## 3-qadam: Assembly tuzilmasini ko'rish / Step 3: Browse the Assembly Structure

**O'zbek:**
1. Chap paneldagi assembly nomini kengaytiring (uchburchak belgisini bosing).
2. Namespace, sinf (class) va metodlar ro'yxatini ko'rasiz.
3. Kerakli sinf yoki metodga bosing — o'ng panelda dekompile qilingan C# kodi ko'rinadi.

**English:**
1. Expand the assembly name in the left panel (click the triangle/arrow).
2. You will see namespaces, classes, and methods listed.
3. Click on any class or method — the decompiled C# source code appears in the right panel.

---

## 4-qadam: Kodni saqlash (export) / Step 4: Save (Export) the Decompiled Code

### Butun assembly-ni eksport qilish / Export the entire assembly

**O'zbek:**
1. Chap panelda assembly nomiga **o'ng tugma** bilan bosing.
2. **Save Code** ni tanlang.
3. Saqlash uchun papkani tanlang — ILSpy barcha sinf fayllarni `.cs` formatida yaratadi.

**English:**
1. Right-click on the assembly name in the left panel.
2. Select **Save Code**.
3. Choose a destination folder — ILSpy will generate all class files as `.cs` files.

### Alohida fayl sifatida saqlash / Save a single file

**O'zbek:**
1. Kerakli sinfga **o'ng tugma** bilan bosing.
2. **Save Code** ni tanlang va fayl nomini bering.

**English:**
1. Right-click on the desired class.
2. Select **Save Code** and provide a file name.

---

## 5-qadam: Qidiruv / Step 5: Search

**O'zbek:**
- **Ctrl+F** — joriy ko'rinishdagi matnni qidirish.
- **Ctrl+Shift+F** yoki **Edit → Search** — butun assembly bo'ylab qidirish.
- Qidiruv satriga sinf nomi, metod nomi yoki satr qiymatini kiriting.

**English:**
- **Ctrl+F** — search within the current view.
- **Ctrl+Shift+F** or **Edit → Search** — search across the entire assembly.
- Enter a class name, method name, or string literal in the search box.

---

## Muhim eslatmalar / Important Notes

> **O'zbek:**  
> Dekompilatsiya faqat o'z dasturingizni tahlil qilish, dasturiy ta'minotni qayta tiklash (backup yo'qolganda) yoki o'quv maqsadlari uchun qonuniy hisoblanadi. Uchinchi tomon dasturlarini ruxsatsiz dekompilatsiya qilish muallif huquqlari va litsenziya shartlarini buzishi mumkin.

> **English:**  
> Decompilation is legal when you analyse your own software, recover your own source code (e.g., lost backup), or use it for educational purposes. Decompiling third-party software without permission may violate copyright law and licence agreements.

---

## Foydali havolalar / Useful Links

| Resurs / Resource | Havola / Link |
|---|---|
| ILSpy GitHub | https://github.com/icsharpcode/ILSpy |
| ILSpy Releases | https://github.com/icsharpcode/ILSpy/releases |
| .NET Runtime | https://dotnet.microsoft.com/download |
| ILSpy Wiki | https://github.com/icsharpcode/ILSpy/wiki |

---

## Yordam / Help

Savollar yoki muammolar bo'lsa, ushbu repozitoriyning [Issues](../../issues) bo'limida murojaat qiling.

If you have questions or encounter any issues, please open a ticket in the [Issues](../../issues) section of this repository.
