$root = (Get-Location).Path
$rawDir = Join-Path $root 'glossary-work\raw'
$outDir = Join-Path $root 'glossary-work\merged'
$auditDir = Join-Path $root 'glossary-work\audit'
New-Item -ItemType Directory -Force $outDir,$auditDir | Out-Null
$records = @()
foreach ($file in Get-ChildItem $rawDir -File -Filter '*.md') {
  $lines = Get-Content $file.FullName
  $topic = ($lines | Where-Object { $_ -match '^- Topic:\s*(.+)' } | Select-Object -First 1)
  if (-not $topic) { $topic = ($lines | Where-Object { $_ -match '^- Topic Title:\s*(.+)' } | Select-Object -First 1) }
  if ($topic -match '^- Topic:\s*(.+)') { $topicName=$Matches[1].Trim() } elseif ($topic -match '^- Topic Title:\s*(.+)') { $topicName=$Matches[1].Trim() } else { $topicName=$file.BaseName }
  $module = if($file.BaseName -match '^(\d{2})-'){ $Matches[1] } else { '' }
  foreach($line in $lines){
    if($line -notmatch '^\|'){continue}
    $cells=$line.Trim('|').Split('|') | ForEach-Object {$_.Trim()}
    if($cells.Count -ne 4 -or $cells[0] -eq 'English Term' -or $cells[0] -match '^---') {continue}
    if([string]::IsNullOrWhiteSpace($cells[0])){continue}
    $records += [pscustomobject]@{Module=$module;Topic=$topicName;EnglishTerm=$cells[0];Chinese=$cells[1];SimpleEnglish=$cells[2];ChineseExplanation=$cells[3];SourceFile=($file.BaseName+'.html');RawFile=$file.Name;CandidateType='Main Candidate'}
  }
}
$records | Export-Csv (Join-Path $outDir 'all-raw-terms.csv') -NoTypeInformation -Encoding UTF8
function Key($s){ return (($s -replace '[`*_]','' -replace '\s+',' ' -replace '[：:]$','').Trim().ToLowerInvariant()) }
$groups=$records | Group-Object @{Expression={Key $_.EnglishTerm}}
$final=@();$merge=@()
foreach($g in $groups){
  $keep=$g.Group | Select-Object -First 1
  $final += $keep
  foreach($dup in ($g.Group | Select-Object -Skip 1)){$merge += [pscustomobject]@{OriginalTerm=$dup.EnglishTerm;MergedInto=$keep.EnglishTerm;Reason='Normalized exact-term duplicate; retained first canonical entry';SourceTopic=$dup.Topic}}
}
$final | Sort-Object {[int]$_.Module},Topic,EnglishTerm | Export-Csv (Join-Path $outDir 'final-glossary.csv') -NoTypeInformation -Encoding UTF8
$md=@('# Final AI Glossary','',('| English Term | 中文 | Simple English | 中文小白理解 |'),('|---|---|---|---|'))
foreach($r in ($final | Sort-Object {[int]$_.Module},Topic,EnglishTerm)){$md += "| $($r.EnglishTerm) | $($r.Chinese) | $($r.SimpleEnglish) | $($r.ChineseExplanation) |"}
$md | Set-Content (Join-Path $outDir 'final-glossary.md') -Encoding UTF8
@('# Duplicate Decisions','',('| Original Term | Merged Into | Reason | Source Topic |'),('|---|---|---|---|')) + @($merge | ForEach-Object {"| $($_.OriginalTerm) | $($_.MergedInto) | $($_.Reason) | $($_.SourceTopic) |"}) | Set-Content (Join-Path $auditDir 'duplicates-report.md') -Encoding UTF8
$rawRows=$records.Count;$unique=$groups.Count;$dups=$rawRows-$unique
@('# Raw Statistics','',"- Raw files: $((Get-ChildItem $rawDir -File).Count)","- Raw Candidate Rows: $rawRows","- Unique Raw Terms (normalized): $unique","- Exact/normalized duplicates: $dups","- Final Unique Glossary Terms: $($final.Count)",'','Note: candidate rows are parsed from each raw file Glossary Candidates table; raw files are preserved unchanged.') | Set-Content (Join-Path $auditDir 'raw-statistics.md') -Encoding UTF8
@('# Do Not Confuse','','| Concept A | Concept B | 中文小白理解 |','|---|---|---|','| Training | Inference | Training 是学习；Inference 是训练后运行模型。 |','| Prompt | Context | Prompt 是指令；Context 是模型当前可见的全部信息。 |','| Embedding | Vector Database | Embedding 是向量表示；Vector Database 是保存和搜索向量的系统。 |','| Search | Retrieval | Search 找候选结果；Retrieval 把相关内容取回。 |','| RAG | Fine-tuning | RAG 提供外部资料；Fine-tuning 修改模型参数。 |','| Model | Agent | Model 负责理解生成；Agent 可结合工具和流程行动。 |','| Latency | Throughput | Latency 是单次等待时间；Throughput 是单位时间处理量。 |') | Set-Content (Join-Path $outDir 'do-not-confuse.md') -Encoding UTF8
Write-Output "RawRows=$rawRows Unique=$unique Duplicates=$dups Final=$($final.Count)"
