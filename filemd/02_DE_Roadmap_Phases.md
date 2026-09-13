# DE Roadmap — แผนใหม่แบบ Phase (~10–12 เดือน, ~5–7 ชม./สัปดาห์)

> ไฟล์ที่ 2 จาก 4 — ต่อจาก [01_DE_Roadmap_Cut_Skip.md](01_DE_Roadmap_Cut_Skip.md)
> ทุก phase ยึด **ข้อมูลจริงจาก Farmruk** (ภาพสำรวจโดรน, ผลตรวจดิน) เป็นแกนโปรเจกต์หลักตลอดทั้งสาย แทนการทำโปรเจกต์แยกส่วนด้วย public dataset

---

### เฟส 0: ทวนพื้นฐาน (2 สัปดาห์)
- ทวน SQL joins / aggregation / window functions เร็วๆ **ตั้งแต่ต้น** (Gun อยู่ปี 2 เรียน Basic SQL มาตั้งแต่ปี 1 แล้ว — ถือว่าต้องทบทวนจริง ไม่ใช่แค่ปัดผ่าน)
- ทวน Git/GitHub ให้คล่อง (ใช้กับงานกลุ่ม INT191 อยู่แล้ว)
- ตั้ง GitHub + LinkedIn ให้พร้อมเก็บผลงาน

### เฟส 1: Python สำหรับ Data Engineering (6–8 สัปดาห์)
วิชานี้ SIT ยังไม่มีสอนตรงๆ (INT243 Python Programming เป็นวิชาเลือกที่ยังไม่ได้ลง) จึงยังต้อง self-study เต็มรูปแบบตาม roadmap เดิม — เริ่มจากพื้นฐานจริงๆ ไม่ข้ามขั้น:
- **ฝึกเขียนโค้ดปูพื้นด้วย [Exercism.org](https://exercism.org) ผ่านเครื่อง local** — ใช้ `exercism` CLI ดาวน์โหลดโจทย์ Python track มาแก้ในโฟลเดอร์ `Python_by_exercism/` ของ repo นี้ แล้ว submit ผ่าน CLI เพื่อฝึก syntax/logic/OOP/exception handling ให้คล่องมือก่อนเข้า pandas
- จากนั้นต่อยอด: OOP → exception handling → unit testing (pytest) → เรียก API ด้วย `requests` → Pandas
- **โปรเจกต์แทนที่ NYC Taxi/public API:** ดึงไฟล์ผลตรวจดิน/ข้อมูลโดรนของ Farmruk (หรือ mock โครงสร้างเดียวกันถ้ายังไม่มีไฟล์จริงพร้อมใช้ — ดูแหล่งข้อมูลทดแทน/เสริมได้ใน [05_Farmruk_Data_Sources.md](05_Farmruk_Data_Sources.md)) → clean ด้วย Pandas → เขียน pytest ตรวจความถูกต้อง

### เฟส 2: Data Modeling & Cloud พื้นฐาน (6 สัปดาห์ — คู่ขนานกับ INT291/INT294 ในเทอม)
- เชื่อมแนวคิด star schema/SCD ที่เรียนใน INT291 เข้ากับข้อมูลจริง
- เลือก cloud 1 ตัว — แนะนำ **AWS** (ยังครองส่วนแบ่งตลาดสูงสุดในสาย DE ปี 2026) → เรียน S3, Glue, Athena, Redshift แบบลงมือทำจริง
- **โปรเจกต์:** ย้ายข้อมูลโดรน/ดินขึ้น S3 → เขียน batch ETL ง่ายๆ ด้วย Python

### เฟส 3: Orchestration + Big Data Processing (8 สัปดาห์ — ช่วงเรียน INT296 คู่กัน)
- Airflow: DAG, Task, scheduling
- Spark เบื้องต้นผ่าน Databricks Free Edition (ไม่ต้องมี cluster เอง)
- **โปรเจกต์:** ตั้ง pipeline อัตโนมัติประมวลผลข้อมูลแปลงที่สำรวจแต่ละรอบ พร้อม schedule รายสัปดาห์

### เฟส 4: Analytics Engineering + Data Quality (5 สัปดาห์)
- dbt: models, tests, documentation
- Data quality checks (schema/null/uniqueness) — เหมาะมากกับข้อมูลดินภาคสนามที่มักไม่สมบูรณ์ ทำให้เป็นเคสสมจริง
- ข้าม NoSQL/Big Data Architecture เชิงลึกในจุดนี้ เพราะ INT296/INT297 สอนอยู่แล้ว

### เฟส 5: Streaming (Kafka) — เสริม ตัดได้ถ้าเวลาจำกัด (4 สัปดาห์)
- มีประโยชน์ถ้าอนาคต Farmruk ใช้เซนเซอร์ IoT ส่งข้อมูลแบบ real-time จากแปลงนา แต่ยังไม่จำเป็นเร่งด่วนตอนนี้

### เฟส 6: พอร์ตโฟลิโอ + เตรียมสัมภาษณ์ (6–8 สัปดาห์ — ช่วงปิดเทอม)
- รวมทุกโปรเจกต์ Farmruk เป็น end-to-end pipeline เดียว พร้อม README อธิบายปัญหาธุรกิจจริง (ไม่ใช่ tutorial copy)
- ทำพอร์ตโฟลิโอ + จัด GitHub repo ให้เป็นระเบียบ
- ฝึก SQL/Python interview บน HackerRank / LeetCode / DataLemur
- เตรียมเล่าโปรเจกต์แบบ STAR โดยใช้เคส Farmruk จริง — จุดแข็งที่ผู้สมัครทั่วไปไม่มี

---

ดูจุดแข็งที่ควรเน้นและ certification ที่แนะนำใน [03_DE_Roadmap_Strengths_Certification_AI_Tutor.md](03_DE_Roadmap_Strengths_Certification_AI_Tutor.md)
