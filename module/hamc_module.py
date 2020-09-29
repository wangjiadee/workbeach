#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hmac
import os
h = hmac.new(b'fucking',os.urandom(32))
ret = h.digest()
print(ret)
