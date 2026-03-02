param(
  [Parameter(Mandatory=$false)]
  [string]$Goal = "신규 반려동물 간식 브랜드 런칭",

  [Parameter(Mandatory=$false)]
  [string]$Save = "docs/sample_report.json"
)

$env:PYTHONPATH = if ($env:PYTHONPATH) { "src;$($env:PYTHONPATH)" } else { "src" }

python scripts/run_demo.py --goal $Goal --save $Save
