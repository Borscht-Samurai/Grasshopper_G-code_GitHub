# Grasshopper G-code GitHub連携ツール  
Grasshopper G-code GitHub Integration Tool

---

## 概要 | Overview

このツールは、**Grasshopper上で生成したG-codeをGitHubへ自動で保存・管理するためのPythonスクリプト**です。  
Panelコンポーネントに入力されたG-codeを、ボタンを押すだけで `.gcode` ファイルとして保存し、Gitリポジトリに追加・コミット・GitHubにプッシュまでを自動化します。

This tool is a **Python script that allows G-code generated in Grasshopper to be automatically saved and pushed to GitHub**.  
By entering G-code into a Panel component and pressing a Button, it saves the data as a `.gcode` file and runs Git operations (`add → commit → push`) automatically.

---

## 特徴 | Features

- `.gcode` 形式での保存
- コミットメッセージのカスタム入力対応
- GitHubへの自動push
- Grasshopper内での実行ログ表示
- インデックス（"0 G90"のような形式）の自動除去

---

## 必要環境 | Requirements

- Rhino 8
- Grasshopper
- Git（インストール済み）
- GitHubアカウントとリモートリポジトリ
- Python Scriptコンポーネント

---

## セットアップ方法 | Setup Instructions

### 1. Gitリポジトリの準備 | Prepare the Git Repository

```bash
cd [your_local_repo_path]
git init
git remote add origin https://github.com/your-username/your-repo.git
git branch -M master
git push --set-upstream origin master
```
## Grasshopper構成 | Grasshopper Components

| 入力名 | Input Name   | 説明 / Description                        |
|--------|--------------|-------------------------------------------|
| `gcode_text` | G-code文字列（複数行Panel入力）<br>G-code text as multiline input from Panel |
| `file_name`  | 保存ファイル名（拡張子不要、例: `output1`）<br>Filename to save (e.g., `output1`) |
| `repo_path`  | ローカルGitリポジトリのフルパス<br>Full path to local Git repository |
| `commit_msg` | コミットメッセージ（空でも可）<br>Commit message (optional) |
| `run_trigger`| Buttonからの実行トリガー<br>Execution trigger from Button |

- 出力ポート `out` を `Panel` に接続すると実行ログを確認できます  
- Connect the `out` output to a `Panel` to view logs and debug output

---

## 使用方法 | How to Use

1. `gcode_text` にG-codeを複数行で入力する  
   Enter multiline G-code into the `gcode_text` Panel  
2. `file_name` に保存したいファイル名を入力する（例: `test1`）  
   Provide a filename to save (e.g., `test1`)  
3. `repo_path` にGitのローカルリポジトリの絶対パスを入力する  
   Input the full path of your local Git repository  
4. `commit_msg` に任意でコミットメッセージを入力（空でもOK）  
   Optionally enter a commit message (optional)  
5. `run_trigger` にButtonを接続し、ボタンを押すと `.gcode` が保存されてGitHubにプッシュされる  
   Press the Button to trigger save and push to GitHub  
6. `out` に操作ログが表示されるので内容を確認できる  
   Operation logs are shown in the `out` output  

---

## 注意点 | Notes

- 最初の `git push` には手動での `--set-upstream` が必要になる場合があります  
  Initial `git push` may require manual `--set-upstream`
- `repo_path` にスペースや全角文字（例：日本語）が含まれているとエラーになる可能性があります  
  Avoid full-width characters or spaces in `repo_path` if possible
- GitHubへの認証設定（Personal Access TokenまたはSSHキー）が必要です  
  Authentication (PAT or SSH key) must be set up beforehand
- ファイル保存やGit操作に失敗した場合、出力 `out` にエラーメッセージが表示されます  
  If the save or Git operation fails, error messages will appear in `out`

---

## ライセンス | License

このプロジェクトはMITライセンスの下で公開されています。  
This project is released under the MIT License.

詳しくは `LICENSE` ファイルをご確認ください。  
See the `LICENSE` file for more information.
