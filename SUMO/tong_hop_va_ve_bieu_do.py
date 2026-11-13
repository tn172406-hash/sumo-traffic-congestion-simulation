# -*- coding: utf-8 -*-
"""
Script tong hop so lieu mo phong va xuat bieu do cho Tieu luan ITS Hang Xanh
Ho tro 3 kich ban: Thap (KB1), Trung binh (KB2), Cao diem (KB3)
"""
import os
import csv
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Thiet lap phong chu va giao dien cho matplotlib
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Segoe UI']
plt.rcParams['axes.unicode_minus'] = False

SCENARIOS = [
    {
        'id': 'kb1',
        'name': 'Kịch bản 1 (Thấp điểm)',
        'scale': 0.5,
        'tripinfo': r'output/kb1_tripinfo.xml',
        'summary': r'output/kb1_summary.xml',
        'queue': r'output/kb1_queue.xml'
    },
    {
        'id': 'kb2',
        'name': 'Kịch bản 2 (Trung bình)',
        'scale': 1.0,
        'tripinfo': r'output/kb2_tripinfo.xml',
        'summary': r'output/kb2_summary.xml',
        'queue': r'output/kb2_queue.xml'
    },
    {
        'id': 'kb3',
        'name': 'Kịch bản 3 (Cao điểm)',
        'scale': 1.75,
        'tripinfo': r'output/kb3_tripinfo.xml',
        'summary': r'output/kb3_summary.xml',
        'queue': r'output/kb3_queue.xml'
    }
]

def analyze_tripinfo(file_path):
    if not os.path.exists(file_path):
        return None
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    total_vehicles = 0
    total_waiting = 0.0
    total_timeloss = 0.0
    total_duration = 0.0
    
    vtype_stats = {}
    
    for trip in root.findall('tripinfo'):
        total_vehicles += 1
        w = float(trip.get('waitingTime', 0))
        tl = float(trip.get('timeLoss', 0))
        d = float(trip.get('duration', 0))
        vtype = trip.get('vType', 'other')
        
        total_waiting += w
        total_timeloss += tl
        total_duration += d
        
        if vtype not in vtype_stats:
            vtype_stats[vtype] = {'count': 0, 'waiting': 0.0, 'duration': 0.0}
        vtype_stats[vtype]['count'] += 1
        vtype_stats[vtype]['waiting'] += w
        vtype_stats[vtype]['duration'] += d
        
    mean_waiting = total_waiting / total_vehicles if total_vehicles > 0 else 0
    mean_timeloss = total_timeloss / total_vehicles if total_vehicles > 0 else 0
    mean_duration = total_duration / total_vehicles if total_vehicles > 0 else 0
    
    vtype_avg = {}
    for vt, data in vtype_stats.items():
        vtype_avg[vt] = {
            'count': data['count'],
            'mean_waiting': data['waiting'] / data['count'] if data['count'] > 0 else 0,
            'mean_duration': data['duration'] / data['count'] if data['count'] > 0 else 0
        }
        
    return {
        'total_arrived': total_vehicles,
        'mean_waiting': round(mean_waiting, 2),
        'mean_timeloss': round(mean_timeloss, 2),
        'mean_duration': round(mean_duration, 2),
        'by_vtype': vtype_avg
    }

def analyze_summary(file_path):
    if not os.path.exists(file_path):
        return None
    tree = ET.parse(file_path)
    root = tree.getroot()
    steps = root.findall('step')
    if not steps:
        return None
    
    speeds = []
    haltings = []
    for s in steps:
        sp = float(s.get('meanSpeed', 0))
        h = int(s.get('halting', 0))
        speeds.append(sp)
        haltings.append(h)
        
    last_step = steps[-1]
    avg_speed_ms = sum(speeds) / len(speeds) if speeds else 0
    avg_speed_kmh = avg_speed_ms * 3.6
    max_halting = max(haltings) if haltings else 0
    
    return {
        'avg_speed_kmh': round(avg_speed_kmh, 2),
        'max_halting': max_halting,
        'inserted': int(last_step.get('inserted', 0)),
        'running': int(last_step.get('running', 0)),
        'teleports': int(last_step.get('teleports', 0)),
        'collisions': int(last_step.get('collisions', 0))
    }

def analyze_queue(file_path):
    if not os.path.exists(file_path):
        return {}
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    edge_queues = {}
    for step in root.findall('data'):
        lanes = step.findall('.//lane')
        for l in lanes:
            lane_id = l.get('id')
            q_len = float(l.get('queueing_length', 0))
            edge_id = lane_id.rsplit('_', 1)[0]
            if edge_id not in edge_queues:
                edge_queues[edge_id] = []
            edge_queues[edge_id].append(q_len)
            
    summary_q = {}
    for e, vals in edge_queues.items():
        summary_q[e] = {
            'max_queue_m': round(max(vals), 1) if vals else 0,
            'avg_queue_m': round(sum(vals)/len(vals), 1) if vals else 0
        }
    return summary_q

def export_summary_csv(results, csv_path='Bao_Cao_Tong_Hop_3_Kich_Ban.csv'):
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['CHỈ SỐ ĐÁNH GIÁ GIAO THÔNG NÚT GIAO HÀNG XANH (SUMO)', 'KỊCH BẢN 1 (THẤP ĐIỂM)', 'KỊCH BẢN 2 (TRUNG BÌNH)', 'KỊCH BẢN 3 (CAO ĐIỂM)'])
        
        writer.writerow(['Tỷ lệ lưu lượng (%)', '50%', '100%', '175%'])
        
        # Tong so phuong tien
        writer.writerow(['Tổng số xe nạp vào mạng (xe)',
                         results['kb1']['summary']['inserted'],
                         results['kb2']['summary']['inserted'],
                         results['kb3']['summary']['inserted']])
        writer.writerow(['Tổng số xe hoàn thành lộ trình (xe)',
                         results['kb1']['trip']['total_arrived'],
                         results['kb2']['trip']['total_arrived'],
                         results['kb3']['trip']['total_arrived']])
        writer.writerow(['Số xe đang kẹt tại thời điểm kết thúc (xe)',
                         results['kb1']['summary']['running'],
                         results['kb2']['summary']['running'],
                         results['kb3']['summary']['running']])
                         
        # Van toc
        writer.writerow(['Vận tốc trung bình toàn mạng (km/h)',
                         results['kb1']['summary']['avg_speed_kmh'],
                         results['kb2']['summary']['avg_speed_kmh'],
                         results['kb3']['summary']['avg_speed_kmh']])
                         
        # Thoi gian cho
        writer.writerow(['Thời gian chờ trung bình toàn mạng (giây)',
                         results['kb1']['trip']['mean_waiting'],
                         results['kb2']['trip']['mean_waiting'],
                         results['kb3']['trip']['mean_waiting']])
        writer.writerow(['Tổn thất thời gian trung bình (giây)',
                         results['kb1']['trip']['mean_timeloss'],
                         results['kb2']['trip']['mean_timeloss'],
                         results['kb3']['trip']['mean_timeloss']])
                         
        # Theo loai xe
        writer.writerow(['--- THỜI GIAN CHỜ THEO LOẠI XE (giây) ---', '', '', ''])
        for vt, label in [('motorcycle', 'Xe máy'), ('passenger', 'Ô tô con'), ('bus', 'Xe buýt')]:
            w1 = results['kb1']['trip']['by_vtype'].get(vt, {}).get('mean_waiting', 0)
            w2 = results['kb2']['trip']['by_vtype'].get(vt, {}).get('mean_waiting', 0)
            w3 = results['kb3']['trip']['by_vtype'].get(vt, {}).get('mean_waiting', 0)
            writer.writerow([f'Thời gian chờ: {label}', round(w1, 1), round(w2, 1), round(w3, 1)])
            
        writer.writerow(['Số xe dừng đỗ kẹt lớn nhất tại 1 thời điểm (xe)',
                         results['kb1']['summary']['max_halting'],
                         results['kb2']['summary']['max_halting'],
                         results['kb3']['summary']['max_halting']])
                         
    print(f"[OK] Da xuat bao cao tong hop ra: {csv_path}")

def plot_charts(results):
    categories = ['KB1: Thấp điểm\n(50%)', 'KB2: Trung bình\n(100%)', 'KB3: Cao điểm\n(175%)']
    
    # 1. Bieu do thoi gian cho trung binh
    plt.figure(figsize=(9, 5))
    wait_moto = [results[k]['trip']['by_vtype'].get('motorcycle', {}).get('mean_waiting', 0) for k in ['kb1', 'kb2', 'kb3']]
    wait_car = [results[k]['trip']['by_vtype'].get('passenger', {}).get('mean_waiting', 0) for k in ['kb1', 'kb2', 'kb3']]
    wait_bus = [results[k]['trip']['by_vtype'].get('bus', {}).get('mean_waiting', 0) for k in ['kb1', 'kb2', 'kb3']]
    
    import numpy as np
    x = np.arange(len(categories))
    width = 0.25
    
    plt.bar(x - width, wait_moto, width, label='Xe máy', color='#f39c12')
    plt.bar(x, wait_car, width, label='Ô tô con', color='#2980b9')
    plt.bar(x + width, wait_bus, width, label='Xe buýt', color='#c0392b')
    
    plt.xlabel('Kịch bản mô phỏng', fontsize=12, fontweight='bold')
    plt.ylabel('Thời gian chờ trung bình (giây)', fontsize=12, fontweight='bold')
    plt.title('SO SÁNH THỜI GIAN CHỜ TRUNG BÌNH THEO LOẠI XE QUA 3 KỊCH BẢN', fontsize=13, fontweight='bold', pad=15)
    plt.xticks(x, categories)
    plt.legend(frameon=True)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('bieu_do_1_thoi_gian_cho.png', dpi=300)
    plt.close()
    print("[OK] Da tao: bieu_do_1_thoi_gian_cho.png")

    # 2. Bieu do van toc trung binh va so xe bi ket
    fig, ax1 = plt.subplots(figsize=(9, 5))
    speeds = [results[k]['summary']['avg_speed_kmh'] for k in ['kb1', 'kb2', 'kb3']]
    haltings = [results[k]['summary']['max_halting'] for k in ['kb1', 'kb2', 'kb3']]
    
    color = '#27ae60'
    ax1.set_xlabel('Kịch bản mô phỏng', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Vận tốc trung bình (km/h)', color=color, fontsize=12, fontweight='bold')
    bars = ax1.bar(x - 0.15, speeds, 0.3, color=color, alpha=0.85, label='Vận tốc (km/h)')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories)
    
    # hien thi gia tri tren cot
    for bar in bars:
        h = bar.get_height()
        ax1.annotate(f'{h} km/h', xy=(bar.get_x() + bar.get_width()/2, h), xytext=(0, 3),
                    textcoords="offset points", ha='center', va='bottom', fontweight='bold')
    
    ax2 = ax1.twinx()
    color = '#e74c3c'
    ax2.set_ylabel('Số xe kẹt lớn nhất (xe)', color=color, fontsize=12, fontweight='bold')
    line = ax2.plot(x + 0.15, haltings, color=color, marker='o', linewidth=2.5, markersize=8, label='Số xe kẹt cực đại')
    ax2.tick_params(axis='y', labelcolor=color)
    
    for i, txt in enumerate(haltings):
        ax2.annotate(f'{txt} xe', xy=(x[i] + 0.15, txt), xytext=(0, 7),
                     textcoords="offset points", ha='center', color=color, fontweight='bold')

    plt.title('TƯƠNG QUAN GIẢM VẬN TỐC VÀ GIA TĂNG ÙN Ứ GIAO THÔNG TẠI NÚT GIAO', fontsize=13, fontweight='bold', pad=15)
    plt.grid(axis='both', linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.savefig('bieu_do_2_van_toc_va_un_tac.png', dpi=300)
    plt.close()
    print("[OK] Da tao: bieu_do_2_van_toc_va_un_tac.png")

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    results = {}
    for sc in SCENARIOS:
        print(f"Dang doc ket qua {sc['name']}...")
        t_data = analyze_tripinfo(sc['tripinfo'])
        s_data = analyze_summary(sc['summary'])
        q_data = analyze_queue(sc['queue'])
        
        if not t_data or not s_data:
            print(f"Chua co du du lieu cho {sc['id']}. Vui long chay mo phong truoc!")
            return
            
        results[sc['id']] = {
            'trip': t_data,
            'summary': s_data,
            'queue': q_data
        }
        
    export_summary_csv(results)
    plot_charts(results)
    print("\n=== HOAN TAT XU LY SO LIEU VA VE BIEU DO CHO TIEU LUAN ===")

if __name__ == '__main__':
    main()
