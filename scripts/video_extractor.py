import os
import cv2
from pathlib import Path

def extract_frames(video_path, output_dir, num_frames=5):
    video_path = Path(video_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        print(f"无法打开视频: {video_path}")
        return None
    
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = total_frames / fps if fps > 0 else 0
    
    print(f"视频信息: {total_frames} 帧, {fps:.2f} FPS, {duration:.2f} 秒")
    
    frame_indices = [int(i * (total_frames - 1) / (num_frames - 1)) for i in range(num_frames)]
    extracted = []
    
    for idx in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            frame_filename = f"frame_{idx:04d}.jpg"
            frame_path = output_dir / frame_filename
            cv2.imwrite(str(frame_path), frame)
            extracted.append(str(frame_path))
            print(f"  已提取: {frame_filename}")
    
    cap.release()
    return {
        "video_path": str(video_path),
        "total_frames": total_frames,
        "fps": fps,
        "duration": duration,
        "extracted_frames": extracted
    }

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    video_path = script_dir / "../raw/videos/6f2303659eeafc555a1488d1d181ea61.mp4"
    output_dir = script_dir / "../raw/videos/2023-05-frames"
    
    print("=" * 50)
    print("开始处理视频...")
    print("=" * 50)
    
    result = extract_frames(video_path, output_dir)
    
    if result:
        print("\n" + "=" * 50)
        print(f"处理完成！成功提取 {len(result['extracted_frames'])} 帧")
        print(f"输出目录: {output_dir.resolve()}")
        print("=" * 50)

