echo "Packing the lambda sources and libraries"
/usr/bin/python3.8 -m virtualenv tmp_venv
source tmp_venv/bin/activate
pip install -r requirements.txt
cp -R app.py /usr/lib/x86_64-linux-gnu/libpq.so.5 tmp_venv/lib/python3.8/site-packages/
cd tmp_venv/lib/python3.8/sites-packages/
zip -r app.zip *
cd -
cd tmp_venv/lib/python3.8/site-packages/app.zip
deactivate
rm -R tmp_venv