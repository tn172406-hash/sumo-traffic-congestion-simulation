@echo off
title CHAY TU DONG 3 KICH BAN BAN DO THAT HANG XANH
echo =======================================================================
echo     HE THONG CHAY MO PHONG BAN DO THAT OPENSTREETMAP HANG XANH
echo =======================================================================
echo.
echo [1/4] Dang chay Kich ban 1 Ban do that (50%%)...
"C:\Program Files (x86)\SUMO\bin\sumo.exe" -c hangxanh_real_kb1_thap.sumocfg --no-warnings true
echo     -> Xong Kich ban 1!
echo.
echo [2/4] Dang chay Kich ban 2 Ban do that (100%%)...
"C:\Program Files (x86)\SUMO\bin\sumo.exe" -c hangxanh_real_kb2_trungbinh.sumocfg --no-warnings true
echo     -> Xong Kich ban 2!
echo.
echo [3/4] Dang chay Kich ban 3 Ban do that (175%%)...
"C:\Program Files (x86)\SUMO\bin\sumo.exe" -c hangxanh_real_kb3_caodiem.sumocfg --no-warnings true
echo     -> Xong Kich ban 3!
echo.
echo [4/4] Dang xuat so lieu va ve bieu do phuc vu Chuong 4...
python tong_hop_va_ve_bieu_do.py
echo.
echo =======================================================================
echo DA HOAN TAT TOAN BO!
echo Ket qua da duoc luu tai:
echo  - File Excel: Bao_Cao_Tong_Hop_3_Kich_Ban.csv
echo  - Bieu do 1: bieu_do_1_thoi_gian_cho.png
echo  - Bieu do 2: bieu_do_2_van_toc_va_un_tac.png
echo =======================================================================
pause
