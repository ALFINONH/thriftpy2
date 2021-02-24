
#### Installation

```
git clone https://github.com/alfinonh/thriftpy2
cd line
pip install -r requirements.txt
python setup.py install
```

#### Example

```
from line.cilent import LineClient

client = LineClient()
client.qr_login()
```
