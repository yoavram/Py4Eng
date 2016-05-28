import io

import requests
import click

base_url = "http://127.0.0.1:5000/api/1"

def error(msg):
    click.secho(msg, fg="red")

def upload_image(filename):
    url = "{}/image".format(base_url)
    with open(filename, 'rb') as f:
        resp = requests.post(url, files={'file': f})        
    if not resp.ok:
        raise Exception(resp.reason)
    return resp.json()['image_id']

def download_image(url, filename=None):
    resp = requests.get(url)
    if not resp.ok:
        raise Exception(resp.reason)
    if filename is not None:
        with open(filename, "wb") as f:
            f.write(resp.content)
    else:
        return io.BytesIO(resp.content)
        
def segment_image(image_id):
    url = "{}/image/{}/segment".format(base_url, image_id)
    resp = requests.get(url)
    if not resp.ok:
        raise Exception(resp.reason)
    return resp.json()['url']

@click.command()
@click.argument("src", type=click.Path(exists=True, readable=True, dir_okay=False))
@click.argument("dst", type=click.Path(writable=True, dir_okay=False))
def main(src, dst):    
    image_id = upload_image(src)
    url = segment_image(image_id)    
    download_image(url, dst)

if __name__ == '__main__':
    main()