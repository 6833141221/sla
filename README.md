# Recruitment SLA analysis

โปรเจกต์นี้ผมได้สร้างชุดข้อมูลจำลองเเละทำ Dashboard เพื่อวิเคราะห์ข้อมูลในเเต่ละด้าน

## Project Workflow
1. **ER diagram:**   ***ออกเเบบ er diagram สร้างตารางที่ความสัมพันธ์กันรอรับข้อมูลที่เราจำลองมาครับ***
2. **mock data:**    ใช้ `Pandas` และ `Faker` ในการจำลองข้อมูล ใส่ข้อมูลเข้าตาราง เเละเป็นข้อมูลที่จำเป็นต้องผ่านการ cleansing ก่อน เพื่อฝึกทักษะการทำ data cleaning
3. **data cleansing:**   ทำการ cleansing และ cast ข้อมูลให้สามารถนำไปใช้ในการวิเคราะห์ได้โดยไม่มีปัญหา
4. **create SLA table:**   สร้าง ตารางข้อมูลที่เเยก column date time ของเเต่ละ process ในการ recruitment เพื่อให้ง่ายต่อการหา SLA 
5. **create dash board (tableau):**   สร้าง interactive dashboard เพื่อวิเคราะห์ประสิทธิภาพของทีม HR, ค้นหาจุดคอขวด (bottleneck) ใน process recruitment และวิเคราะห์อัตราการจ้างงานสำเร็จของเเต่ละแผนก

## Tools Used
- **Python**   ใช้สำหรับการจำลองข้อมูล (Faker, Pandas)
- **SQL**   ใช้สำหรับการทำ data cleaning and casting 
- **Tableau**   ใช้สำหรับการทำ data visualization and storytelling

---
*Dashboard Link: [https://public.tableau.com/app/profile/narawin.chotivit/viz/RecruitmentSLA/Dashboard1?publish=yes]*
