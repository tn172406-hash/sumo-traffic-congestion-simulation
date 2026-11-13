@echo off
title CHAY TU DONG 3 KICH BAN BAN DO THAT
echo =======================================================================
echo     HE THONG CHAY MO PHONG BAN DO THAT OPENSTREETMAP HANG XANH
echo =======================================================================
echo.
echo [1/3] Dang chay Kich ban 1 Ban do that (50%%)...
"C:\Program Files (x86)\SUMO\bin\sumo.exe" -c hangxanh_real_kb1_thap.sumocfg --no-warnings true
echo     -> Xong Kich ban 1!
echo.
echo [2/3] Dang chay Kich ban 2 Ban do that (100%%)...
"C:\Program Files (x86)\SUMO\bin\sumo.exe" -c hangxanh_real_kb2_trungbinh.sumocfg --no-warnings true
echo     -> Xong Kich ban 2!
echo.
echo [3/3] Dang chay Kich ban 3 Ban do that (175%%)...
"C:\Program Files (x86)\SUMO\bin\sumo.exe" -c hangxanh_real_kb3_caodiem.sumocfg --no-warnings true
echo     -> Xong Kich ban 3!
echo.
echo =======================================================================
echo DA HOAN TAT CHAY 3 KICH BAN BAN DO THAT!
echo Ket qua duoc luu tai thu muc: SUMO/output_real/
echo =======================================================================
pause
