# -*- coding: utf-8 -*-

try:
    from django.http.multipartparser import parse_header
except ImportError:
    from django.utils.http import parse_header_parameters

    def parse_header(line):
        if isinstance(line, bytes):
            line = line.decode("latin1")
        return parse_header_parameters(line)
