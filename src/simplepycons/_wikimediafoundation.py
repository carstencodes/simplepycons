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


class WikimediaFoundationIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wikimediafoundation"

    @property
    def original_file_name(self) -> "str":
        return "wikimediafoundation.svg"

    @property
    def title(self) -> "str":
        return "Wikimedia Foundation"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wikimedia Foundation</title>
     <path d="M20.074 3.126C22.486 5.321 24 8.485 24 12c0 6.623-5.377
 12-12 12S0 18.623 0 12c0-3.515 1.514-6.679 3.926-8.874l2.265
 2.265C4.358 7.005 3.2 9.368 3.2 12c0 4.857 3.943 8.8 8.8
 8.8s8.8-3.943 8.8-8.8c0-2.632-1.158-4.995-2.991-6.609zm-3.399
 3.399C18.22 7.846 19.2 9.81 19.2 12c0 3.703-2.802 6.757-6.4
 7.156V10.4zM11.2 19.156C7.602 18.757 4.8 15.703 4.8
 12c0-2.19.98-4.154 2.525-5.475L11.2 10.4zM12 0c2.208 0 4 1.792 4
 4s-1.792 4-4 4-4-1.792-4-4 1.792-4 4-4" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://foundation.wikimedia.org/wiki/Wikimed'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://foundation.wikimedia.org/wiki/File:Wi'''

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
