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
