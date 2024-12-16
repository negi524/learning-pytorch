# プログラムを実行する
main: log/ src/.env
	poetry run python src/main.py

# テストを実行する
test:
	poetry run pytest tests/

# ファイルのフォーマットを行う
format:
	poetry run black src/ tests/

# プログラムの型チェックを行う
type-check:
	poetry run mypy -p src

# requirements.txtを出力する
export:
	poetry export -f requirements.txt --output requirements.txt
