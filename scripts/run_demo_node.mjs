#!/usr/bin/env node
import { spawnSync } from 'node:child_process';

const args = process.argv.slice(2);
const goalFlagIndex = args.indexOf('--goal');

const forwardedArgs = [...args];
if (goalFlagIndex === -1) {
  forwardedArgs.push('--goal', '신규 가습마스크 브랜드 런칭');
}

const result = spawnSync(
  'python3',
  ['scripts/run_demo.py', ...forwardedArgs],
  {
    stdio: 'inherit',
    env: {
      ...process.env,
      PYTHONPATH: process.env.PYTHONPATH
        ? `src:${process.env.PYTHONPATH}`
        : 'src',
    },
  }
);

if (result.error) {
  console.error('실행 실패:', result.error.message);
  process.exit(1);
}

process.exit(result.status ?? 0);
