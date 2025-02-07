import os
import sys
import subprocess

def profile_script(script_path):
    if not os.path.exists(script_path):
        print(f"❌ Error: 파일 '{script_path}'이(가) 존재하지 않습니다.")
        sys.exit(1)

    prof_file = "output.prof"

    # Step 1: cProfile 실행 및 .prof 파일 저장
    print(f"🚀 Profiling '{script_path}' ...")
    command = f"python -m cProfile -o {prof_file} {script_path}"
    subprocess.run(command, shell=True)

    # Step 2: SnakeViz로 분석 및 브라우저 열기
    print(f"📊 Opening SnakeViz for '{prof_file}' ...")
    url_command = f"snakeviz {prof_file}"
    process = subprocess.Popen(url_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ 사용법: python profile_and_visualize.py <파일명.py>")
        sys.exit(1)

    script_path = sys.argv[1]
    profile_script(script_path)
