# Farmruk — แหล่งข้อมูลดิน/โดรน/โรคพืช (นำมาจาก repo DataSci_Farmrak)

> ไฟล์ที่ 5 — ต่อจาก [04_Farmruk_Project_Context.md](04_Farmruk_Project_Context.md)
> คัดลอก/ย่อจาก `DataSci_Farmrak/filemd/01_Farmrak_DataSci_Opportunity.md` เฉพาะส่วนแหล่งข้อมูล เพื่อใช้เป็น input ของ pipeline ในเฟส 1-4 ของ DE roadmap
> ข้อมูลจริงของ Farmruk เอง (ผลตรวจดิน, ภาพโดรน) ยังไม่ได้ upload เข้า repo นี้ — ไฟล์นี้บอกว่า "ถ้ายังไม่มีไฟล์จริงพร้อมใช้ จะไปดึง/mock จากไหนได้บ้าง"

---

## แหล่งข้อมูลดิน (pH, NPK, ความชื้น) ของประเทศไทย

### ภาครัฐไทย — กรมพัฒนาที่ดิน (LDD)
- **ดินออนไลน์** — https://dinonline.ldd.go.th — แผนที่กลุ่มชุดดินและการใช้ที่ดิน
- **ระบบวิเคราะห์ดิน น้ำ ปุ๋ย (OSD101)** — https://osd101.ldd.go.th — ค้นหาผลวิเคราะห์ดินย้อนหลังตามพิกัดพื้นที่ได้ มีประโยชน์เวลาไม่มีข้อมูลของตัวเองในพื้นที่นั้น
- **บัญชีรายการข้อมูล LDD** — http://sql.ldd.go.th/ldddata — แคตตาล็อกข้อมูลกลุ่มชุดดิน/ความเหมาะสมของดินต่อพืชในรูป GIS

### Open Data ภาครัฐ (มี API — ใช้ทำ pipeline ingestion ได้จริง)
- **data.go.th** — CKAN Data API ดึงข้อมูลผ่าน HTTP ได้โดยตรง (รองรับ CSV/XLS/XLSX)
  - Dataset **soilseries**: https://data.go.th/dataset/soilseries
  - Dataset **soilseries25000**: https://data.go.th/dataset/soilseries25000
  - คู่มือ API: https://api.data.go.th/en/pages/data-go-th-api

### แหล่งข้อมูลระดับโลก (fallback เวลาข้อมูลไทยไม่ครบพื้นที่)
- **SoilGrids (ISRIC)** — ความละเอียด 250m ทั่วโลกรวมไทย เข้าถึงผ่าน REST API/WCS ฟรี
- **NASA POWER API** — ข้อมูลภูมิอากาศ (ฝน, รังสีดวงอาทิตย์, ความชื้นสัมพัทธ์) ใช้ประกอบข้อมูลดิน

---

## ข้อมูลภาพสำรวจโดรน (Multispectral)

ข้อมูลหลักของ Farmruk เองที่ยังไม่ได้อยู่ใน repo นี้ — เป็นภาพจากโดรนติดกล้อง Multispectral ที่บินสำรวจ pilot area (ด่านช้าง สุพรรณบุรี / บ่อพลอย กาญจนบุรี) ใช้คำนวณดัชนี NDVI/SRPI/NPCI/NGBDI สำหรับ Plant Health Report — **เมื่อได้ไฟล์จริงจากทีม Farmruk ควรนำมาวางในโครงสร้างที่ pipeline เฟส 1-2 ของ DE roadmap ดึงไปใช้ได้ (เช่น โฟลเดอร์ raw data หรือ S3 bucket ตามที่ออกแบบในเฟส 2)**

## แหล่งข้อมูลโรค/แมลงศัตรูพืช (บริบทเสริม — ใช้อ้างอิงเวลาโยง pipeline ไปเชื่อมโมดูล Plant Health)

- **กรมวิชาการเกษตร — สำนักวิจัยพัฒนาการอารักขาพืช**: https://www.doa.go.th/plprotect
- **กรมส่งเสริมการเกษตร — ห้องสมุดภาพโรค/แมลงศัตรูพืช**: https://esc.doae.go.th (⚠️ มีลิขสิทธิ์ ต้องขออนุญาตก่อนใช้เชิงพาณิชย์)
- Dataset สำหรับ Computer Vision (ใช้ฝั่ง DS มากกว่า DE โดยตรง — ใส่ไว้เผื่อ pipeline ต้อง ingest ภาพเข้าโมเดลในอนาคต): PlantVillage (Kaggle/HuggingFace), PlantDoc, PlantSeg (2026)

---

## ข้อจำกัด/สิ่งที่ต้องวางแผนล่วงหน้า (สำคัญสำหรับ DE pipeline)

1. ข้อมูลภาครัฐไทยจำนวนมากอยู่ในรูปแผนที่ GIS/shapefile ไม่ใช่ API พร้อมใช้ทั้งหมด — ต้องมีขั้นตอนแปลง shapefile/GIS เป็นตารางก่อนเข้า pipeline ปกติ
2. ข้อมูลภาคสนามจริงของ Farmruk (ผลตรวจดิน/ภาพโดรน) มักไม่สมบูรณ์ (ค่าขาด, ไฟล์เพี้ยน, พิกัดผิด) — ใช้เป็นเคส data quality checks ในเฟส 4 ได้ตรงจุด
3. ภาพจากกรมส่งเสริมการเกษตรมีลิขสิทธิ์ — ใช้เพื่อเรียนรู้/อ้างอิงได้ แต่ก่อนใช้จริงเชิงพาณิชย์ต้องตรวจสอบเงื่อนไขก่อน

## อ้างอิง
- ดินออนไลน์ (LDD): https://dinonline.ldd.go.th
- e-Service วิเคราะห์ดิน (OSD101): https://osd101.ldd.go.th
- บัญชีข้อมูล LDD: http://sql.ldd.go.th/ldddata
- data.go.th soilseries: https://data.go.th/dataset/soilseries
- data.go.th soilseries25000: https://data.go.th/dataset/soilseries25000
- data.go.th API guide: https://api.data.go.th/en/pages/data-go-th-api
- กรมวิชาการเกษตร (Plant Protection): https://www.doa.go.th/plprotect
- ห้องสมุดภาพศัตรูพืช (DOAE): https://esc.doae.go.th
