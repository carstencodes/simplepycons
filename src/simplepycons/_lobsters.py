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


class LobstersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lobsters"

    @property
    def original_file_name(self) -> "str":
        return "lobsters.svg"

    @property
    def title(self) -> "str":
        return "Lobsters"

    @property
    def primary_color(self) -> "str":
        return "#AC130D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lobsters</title>
     <path d="M0 0v24h24V0zm5.414 4.02h7.86c.105 0
 .15.014.15.134-.015.285 0 .556 0 .841v.12c-.21.015-.42
 0-.615.03-.3.045-.6.089-.885.164-.525.165-.793.527-.853 1.022a5.09
 5.09 0 0 0-.047.674v9.586c0 .405.046.808.091
 1.198.045.435.33.72.736.87.345.135.718.167 1.078.182.945.03 1.877.014
 2.792-.226 1.32-.33 2.204-1.156
 2.64-2.46.134-.42.193-.855.298-1.29.015-.03.046-.09.076-.09h.99c-.03
 1.8.03 3.599 0 5.399H5.25v-.944c0-.165
 0-.149.15-.164.344-.03.689-.045 1.034-.105.69-.12 1.005-.467
 1.11-1.172.03-.21.047-.434.047-.644V7.035c0-.27-.032-.54-.062-.795-.045-.465-.344-.749-.779-.914-.405-.15-.825-.166-1.245-.196h-.226v-.976c0-.105.03-.134.135-.134z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/lobsters/lobsters/blob/dcd'''

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
