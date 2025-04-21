# ファイル名: save_gcode_and_git_push.py

import os
import subprocess
import datetime

if 'prev_state' not in globals():
    prev_state = False

a = ""

# --- デバッグ出力 ---
a += "=== デバッグ出力 ===\n"
a += f"type(gcode_text): {type(gcode_text)}\n"
a += f"gcode_text is None: {gcode_text is None}\n"

# .NET List の場合を含めて変換処理
try:
    lines = list(gcode_text)  # どんな型でもリストに変換試みる
    a += f"gcode_text length: {len(lines)}\n"
    a += f"gcode_text content (first 5 lines):\n"
    for i, line in enumerate(lines[:5]):
        a += f"  {i}: {line}\n"
except Exception as e:
    lines = []
    a += f"[変換エラー] gcode_text を list に変換できませんでした: {str(e)}\n"

a += "====================\n\n"

# --- インデックス除去 ---
cleaned_lines = []
for line in lines:
    line = str(line).strip()
    parts = line.split(None, 1)
    if len(parts) == 2 and parts[0].rstrip('.').isdigit():
        cleaned_lines.append(parts[1])
    else:
        cleaned_lines.append(line)

gcode_text = "\n".join(cleaned_lines)

# --- Git保存処理 ---
if run_trigger and not prev_state:
    a += "=== Git Push Triggered ===\n"

    try:
        if not file_name.lower().endswith('.gcode'):
            file_name += '.gcode'

        file_path = os.path.join(repo_path, file_name)
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(gcode_text)
        a += f"[保存完了] {file_path}\n"

        result_add = subprocess.run(['git', '-C', repo_path, 'add', file_name], capture_output=True, text=True)
        a += "[git add] stderr:\n" + result_add.stderr + "\n"

        # 入力からコミットメッセージを受け取る（空ならデフォルトメッセージ）
        if commit_msg and commit_msg.strip() != "":
            commit_message = commit_msg.strip()
        else:
            commit_message = f"Add G-code file: {file_name} at {datetime.datetime.now().isoformat()}"

        result_commit = subprocess.run(['git', '-C', repo_path, 'commit', '-m', commit_message], capture_output=True, text=True)
        a += "[git commit] stderr:\n" + result_commit.stderr + "\n"

        result_push = subprocess.run(['git', '-C', repo_path, 'push'], capture_output=True, text=True)
        a += "[git push] stdout:\n" + result_push.stdout + "\n"
        a += "[git push] stderr:\n" + result_push.stderr + "\n"

    except Exception as e:
        a += f"[例外発生] {str(e)}\n"

prev_state = run_trigger

# --- 最終出力 ---
out = a
