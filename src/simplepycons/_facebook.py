#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class FacebookIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "facebook"

    @property
    def original_file_name(self) -> "str":
        return "facebook.svg"

    @property
    def title(self) -> "str":
        return "Facebook"

    @property
    def primary_color(self) -> "str":
        return "#0866FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Facebook</title>
     <path d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085
 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1
 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0
 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0
 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287
 1.564h-3.246v8.245C19.396 23.238 24 18.179 24
 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35
 9.101 11.647Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://about.meta.com/brand/resources/facebo'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://about.meta.com/brand/resources/facebo'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
