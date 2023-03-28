#!/usr/bin/env python
# encoding: utf-8
'''
 _______  ___   __   __  _______  ___      _______    _______  _______  ___
|       ||   | |  |_|  ||       ||   |    |       |  |   _   ||       ||   |
|  _____||   | |       ||    _  ||   |    |    ___|  |  |_|  ||    _  ||   |
| |_____ |   | |       ||   |_| ||   |    |   |___   |       ||   |_| ||   |
|_____  ||   | |       ||    ___||   |___ |    ___|  |       ||    ___||   |
 _____| ||   | | ||_|| ||   |    |       ||   |___   |   _   ||   |    |   |
|_______||___| |_|   |_||___|    |_______||_______|  |__| |__||___|    |___|

----------------------------------------------------------------------------


   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0.

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "0.1.1"
__maintainer__ = "Rick Kauffman"
__status__ = "Alpha"

A Very simple flask API to demonstrate URL mainipulation.

'''

import json
from flask import Flask

app = Flask(__name__)

" API Endpoint "
@app.route('/add/<val1>/<val2>', methods=['POST','GET'])
def add_numbers(val1, val2):
    sum = int(val1) + int(val2)
    return str(sum)

" API Endpoint "
@app.route('/subtract/<val1>/<val2>', methods=('GET', 'POST'))
def subrtact_numbers(val1, val2):
    sum = int(val1) - int(val2)
    return str(sum)

" API Endpoint "
@app.route('/multiply/<val1>/<val2>', methods=('GET', 'POST'))
def multiply_numbers(val1, val2):
    sum = int(val1) * int(val2)
    return str(sum)

" API Endpoint "
@app.route('/divide/<val1>/<val2>', methods=('GET', 'POST'))
def devide_numbers(val1, val2):
    sum = int(val1) + int(val2)
    return str(sum)

app.run(debug=True)
