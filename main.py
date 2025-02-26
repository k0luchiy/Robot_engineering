import os
import cv2
from skimage.metrics import structural_similarity as ssim

def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    video = cv2.VideoCapture (video_path)
    success, prev_image = video.read() 
    count = 0
    while success:
    #Подготовка к сохранению кадра
        
        ## Считывание следующего кадра
        success, curr_image = video.read()
        # Проверяем, если удалось считать следующий кадр
        if not success:
            break
        # Преобразуем изображения в градации серого для сравнения
        prev_gray = cv2.cvtColor(prev_image, cv2.COLOR_BGR2GRAY)
        curr_gray = cv2.cvtColor(curr_image, cv2.COLOR_BGR2GRAY)

        #Вычисляем сходство
        similarity = ssim(prev_gray, curr_gray)
        print(similarity)
        ## Если кадры не похожи, сохраняем текущий кадр
        if similarity < 0.95:
            prev_image = curr_image
            count += 1
            frame_filename = os.path.join(output_folder, f"frame_{count:04d}.jpg")
            cv2.imwrite(frame_filename, prev_image)

    video.release()
    print(f"Extracted and saved {count} unique frames to '{output_folder}'.")
    # Пример использования
video_file = '/home/koluchiy/Documents/Urfu_study/Engeniring/videos/robotCam_tst.avi'
# Укажите путь к вашему видеофайлу
output_dir = 'unique_frames_copy' # Название папки для уникальных кадров extract_frames(video_file, output_dir)

extract_frames(video_file, output_dir)
