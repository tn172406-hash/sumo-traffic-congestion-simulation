@echo off
title CHAY TU DONG 3 KICH BAN MO PHONG VA XUAT SO LIEU
echo =======================================================================
echo          HE THONG CHAY TU DONG 3 KICH BAN ITS HANG XANH (SUMO)
echo =======================================================================
echo.
echo [1/4] Dang mo phong Kich ban 1 (Luu luong thap - 50%%)...
"C:\Program Files (x86)\SUMO\bin\sumo.exe" -c hangxanh_kb1_thap.sumocfg --no-warnings true
echo     -> Xong Kich ban 1!
echo.
echo [2/4] Dang mo phong Kich ban 2 (Luu luong trung binh - 100%%)...
"C:\Program Files (x86)\SUMO\bin\sumo.exe" -c hangxanh_kb2_trungbinh.sumocfg --no-warnings true
echo     -> Xong Kich ban 2!
echo.
echo [3/4] Dang mo phong Kich ban 3 (Luu luong cao diem - 175%%)...
"C:\Program Files (x86)\SUMO\bin\sumo.exe" -c hangxanh_kb3_caodiem.sumocfg --no-warnings true
echo     -> Xong Kich ban 3!
echo.
echo [4/4] Dang xuat so lieu ra Excel va ve bieu do phuc vu Chuong 4...
python tong_hop_va_ve_bieu_do.py
echo.
echo =======================================================================
echo DA HOAN TAT TOAN BO!
echo Ket qua da duoc luu tai:
echo  - File Excel/CSV: Bao_Cao_Tong_Hop_3_Kich_Ban.csv
echo  - Bieu do 1: bieu_do_1_thoi_gian_cho.png
echo  - Bieu do 2: bieu_do_2_van_toc_va_un_tac.png
echo =======================================================================
pause
