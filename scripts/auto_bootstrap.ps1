param(
  [Parameter(Mandatory=$false)]
  [string]$Goal = "신규 가습마스크 브랜드 런칭",

  [Parameter(Mandatory=$false)]
  [string]$Save = "docs/sample_report.json"
)

python .\scripts\auto_bootstrap.py --goal $Goal --save $Save
