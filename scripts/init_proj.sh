echo "Installing requirements"
pip install -r requirements.txt

echo "Installing pre-commit"
pre-commit install

echo "Rendering README.md"
python scripts/render_readme.py
git add .
git commit -m "rendered readme"
