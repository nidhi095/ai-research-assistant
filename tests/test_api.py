import io
from app import app

def test_upload_no_file():
    client = app.test_client()
    r = client.post('/upload')
    assert r.status_code == 400

def test_upload_sample_file():
    client = app.test_client()
    data = {'file': (io.BytesIO(b"hello world"), 'sample.txt')}
    r = client.post('/upload', data=data, content_type='multipart/form-data')
    assert r.status_code == 200
    assert r.get_json()['word_count'] == 2
 
