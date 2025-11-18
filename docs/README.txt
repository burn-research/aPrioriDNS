Main commands to build the docs:

1. Activate virtual env
source .venv_sphinx/bin/activate

2. Remove the build folder content
rm -rf docs/build/html

3. Remove the previously generated autodoc (optional)
rm -rf docs/source/autoapi

4. Build html
python -m sphinx -b html docs/source docs/build/html