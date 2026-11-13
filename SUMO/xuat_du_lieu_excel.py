import xml.etree.ElementTree as ET
import csv
import sys
import os

def parse_tripinfo(xml_file, csv_file):
    if not os.path.exists(xml_file):
        print(f"File {xml_file} khong ton tai!")
        return
    
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Vehicle_ID', 'Depart_Time', 'Arrival_Time', 'Duration_s', 'RouteLength_m', 'WaitingTime_s', 'TimeLoss_s', 'vType'])
        
        for trip in root.findall('tripinfo'):
            v_id = trip.get('id')
            depart = trip.get('depart')
            arrival = trip.get('arrival')
            duration = trip.get('duration')
            length = trip.get('routeLength')
            waiting_time = trip.get('waitingTime')
            time_loss = trip.get('timeLoss')
            vtype = trip.get('vType')
            writer.writerow([v_id, depart, arrival, duration, length, waiting_time, time_loss, vtype])
            
    print(f"Da xuat thanh cong du lieu ra file: {csv_file}")

if __name__ == '__main__':
    tripinfo_path = 'output_tripinfo.xml'
    csv_path = 'ket_qua_danh_gia.csv'
    parse_tripinfo(tripinfo_path, csv_path)
