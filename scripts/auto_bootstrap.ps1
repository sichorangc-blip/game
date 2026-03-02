param(
  [Parameter(Mandatory=$false)]
  [string]$Goal = "신규 반려동물 간식 브랜드 런칭",

  [Parameter(Mandatory=$false)]
  [string]$Save = "docs/sample_report.json"
)

python .\scripts\auto_bootstrap.py --goal $Goal --save $Save
