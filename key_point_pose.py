from ultralytics import YOLO

# Modeli yükle
model = YOLO('C:/Staj-projects/key_point_pose/yolov8n-pose.pt')

# Kaydedilecek video ismi
output_path = 'C:/Staj-projects/key_point_pose/processed_video.mp4'

# Modeli kullanarak video işleme
results = model(source='C:/Staj-projects/key_point_pose/dancing.mp4', 
                show=True, 
                conf=0.3, 
                save=True, 
                save_txt=False,  # Eğer sadece videoyu kaydetmek istiyorsanız, TXT dosyalarını kaydetme
                project='C:/Staj-projects/key_point_pose',  # Çıktı dosyalarının kaydedileceği klasör
                name='processed_video')  # Çıktı dosyasının adı

# Çıktı videosunu `output_path` ile yeniden adlandırma
import shutil

# Çıktı klasöründen dosyanın adı
output_file = 'C:/Staj-projects/key_point_pose/runs/detect/processed_video.mp4'
shutil.move(output_file, output_path)
