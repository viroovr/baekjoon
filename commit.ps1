param(
    [string]$FilePath
)

# 파일 존재 여부 확인
if (-not (Test-Path $FilePath)) {
    Write-Host "파일이 존재하지 않습니다: $FilePath"
    exit 1
}

# 문제 번호 추출 (파일명 앞 숫자)
$FileName = [System.IO.Path]::GetFileNameWithoutExtension($FilePath)
if ($FileName -match '^\d+') {
    $ProblemId = $matches[0]
} else {
    "Default commit message." | Out-File -FilePath commit_message.txt -Encoding utf8
    exit 0
}

# API URL
$ApiUrl = "https://solved.ac/api/v3/problem/show?problemId=$ProblemId"
$ProblemUrl = "https://www.acmicpc.net/problem/$ProblemId"

# API 요청
try {
    $Response = Invoke-RestMethod -Uri $ApiUrl -Headers @{ "Accept"="application/json"; "x-solvedac-language"="ko" }
} catch {
    Write-Host "API 요청 실패"
    exit 1
}

$ProblemName = $Response.titleKo
$Level = $Response.level

# 난이도 매핑
$DifficultyMap = @(
    "Unrated","Bronze V","Bronze IV","Bronze III","Bronze II","Bronze I",
    "Silver V","Silver IV","Silver III","Silver II","Silver I",
    "Gold V","Gold IV","Gold III","Gold II","Gold I",
    "Platinum V","Platinum IV","Platinum III","Platinum II","Platinum I",
    "Diamond V","Diamond IV","Diamond III","Diamond II","Diamond I",
    "Ruby V","Ruby IV","Ruby III","Ruby II","Ruby I"
)

if ($Level -ge 0 -and $Level -lt $DifficultyMap.Count) {
    $ProblemDifficulty = $DifficultyMap[$Level]
} else {
    $ProblemDifficulty = "Unknown"
}

# 난이도에서 폴더명 생성 (공백 -> _)
$DifficultyParts = $ProblemDifficulty -split ' '
$MainFolder = $DifficultyParts[0]
$DifficultyFolder = if ($DifficultyParts.Count -gt 1) { $DifficultyParts[1] } else { "" }
$DifficultyFolder = $DifficultyFolder -replace ' ', '_'

# 이동 대상 폴더
$BaseDir = Split-Path $FilePath
if ([string]::IsNullOrEmpty($DifficultyFolder)) {
    $TargetFolder = Join-Path -Path $BaseDir -ChildPath $MainFolder
} else {
    $TargetFolder = Join-Path -Path $BaseDir -ChildPath "$MainFolder\$MainFolder $DifficultyFolder"
}

# 폴더 생성
New-Item -Path $TargetFolder -ItemType Directory -Force | Out-Null

# 파일 이동
$FileNameWithExt = [System.IO.Path]::GetFileName($FilePath)
Move-Item -Path $FilePath -Destination (Join-Path $TargetFolder $FileNameWithExt) -Force

# git add
git add "`"$TargetFolder\$FileNameWithExt`""

# 커밋 메시지 작성
$CommitMsg = "$ProblemDifficulty #$ProblemId $ProblemName`n$ProblemUrl"
$CommitMsg | Out-File -FilePath commit_message.txt -Encoding utf8

# git commit
git commit -F commit_message.txt
