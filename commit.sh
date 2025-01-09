#!/bin/bash

# 첫 번째 인자에서 파일 경로를 가져오기
FILE_PATH="$1"

# 파일이 존재하는지 확인
if [[ ! -f "$FILE_PATH" ]]; then
    echo "파일이 존재하지 않습니다: $FILE_PATH"
    exit 1
fi

# 파일명에서 문제 번호 (3190)을 추출
PROBLEM_ID=$(basename "$FILE_PATH" .py | grep -oE '^[0-9]+')

# PROBLEM_ID가 숫자가 아닌 경우 기본 메시지 설정
if [[ -z "$PROBLEM_ID" ]]; then
    echo "Default commit message." > commit_message.txt
    exit 0
fi

# 문제 URL
API_URL="https://solved.ac/api/v3/problem/show?problemId=$PROBLEM_ID"
PROBLEM_URL="https://www.acmicpc.net/problem/$PROBLEM_ID"

# 문제 제목과 난이도 정보를 받아오기 위한 API 요청
RESPONSE=$(curl -s --request GET \
  --url "$API_URL" \
  --header 'Accept: application/json' \
  --header 'x-solvedac-language: ko')

# 문제 제목과 난이도 추출
PROBLEM_NAME=$(echo "$RESPONSE" | jq -r '.titleKo')
LEVEL=$(echo "$RESPONSE" | jq -r '.level')

# 난이도 매핑
declare -A DIFFICULTY_MAP
DIFFICULTY_MAP[0]="Unrated"
DIFFICULTY_MAP[1]="Bronze V"
DIFFICULTY_MAP[2]="Bronze IV"
DIFFICULTY_MAP[3]="Bronze III"
DIFFICULTY_MAP[4]="Bronze II"
DIFFICULTY_MAP[5]="Bronze I"
DIFFICULTY_MAP[6]="Silver V"
DIFFICULTY_MAP[7]="Silver IV"
DIFFICULTY_MAP[8]="Silver III"
DIFFICULTY_MAP[9]="Silver II"
DIFFICULTY_MAP[10]="Silver I"
DIFFICULTY_MAP[11]="Gold V"
DIFFICULTY_MAP[12]="Gold IV"
DIFFICULTY_MAP[13]="Gold III"
DIFFICULTY_MAP[14]="Gold II"
DIFFICULTY_MAP[15]="Gold I"
DIFFICULTY_MAP[16]="Platinum V"
DIFFICULTY_MAP[17]="Platinum IV"
DIFFICULTY_MAP[18]="Platinum III"
DIFFICULTY_MAP[19]="Platinum II"
DIFFICULTY_MAP[20]="Platinum I"
DIFFICULTY_MAP[21]="Diamond V"
DIFFICULTY_MAP[22]="Diamond IV"
DIFFICULTY_MAP[23]="Diamond III"
DIFFICULTY_MAP[24]="Diamond II"
DIFFICULTY_MAP[25]="Diamond I"
DIFFICULTY_MAP[26]="Ruby V"
DIFFICULTY_MAP[27]="Ruby IV"
DIFFICULTY_MAP[28]="Ruby III"
DIFFICULTY_MAP[29]="Ruby II"
DIFFICULTY_MAP[30]="Ruby I"

# LEVEL이 0부터 30까지의 범위인지 확인
if [[ "$LEVEL" -ge 0 && "$LEVEL" -le 30 ]]; then
    PROBLEM_DIFFICULTY="${DIFFICULTY_MAP[$LEVEL]}"
else
    PROBLEM_DIFFICULTY="Unknown"
fi

# 난이도에서 숫자와 이름을 스페이스로 분리
IFS=' ' read -r MAIN_FOLDER DIFFICULTY_FOLDER <<< "$PROBLEM_DIFFICULTY"

# 파일이 있는 경로를 기반으로 폴더 생성 (파일이 위치한 경로에서 Gold/Gold IV 생성)
BASE_DIR=$(dirname "$FILE_PATH")  # 파일이 위치한 경로
TARGET_FOLDER="$BASE_DIR/$MAIN_FOLDER/$MAIN_FOLDER $DIFFICULTY_FOLDER"

# 상위 폴더 (예: Gold, Gold IV) 생성
mkdir -p "$TARGET_FOLDER"

# 파일을 해당 난이도 폴더로 이동
mv "$FILE_PATH" "$TARGET_FOLDER/"

# git add 추가 (이동된 파일을 다시 추가)
git add "$TARGET_FOLDER/$(basename "$FILE_PATH")"

# 커밋 메시지 작성
COMMIT_MSG="$PROBLEM_DIFFICULTY #$PROBLEM_ID $PROBLEM_NAME"
COMMIT_MSG="$COMMIT_MSG\n$PROBLEM_URL"

# 커밋 메시지 파일에 작성
echo -e "$COMMIT_MSG" > commit_message.txt

# git commit 실행 (커밋 메시지 파일을 참조)
git commit -F commit_message.txt