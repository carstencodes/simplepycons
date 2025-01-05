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


class TrillertvIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trillertv"

    @property
    def original_file_name(self) -> "str":
        return "trillertv.svg"

    @property
    def title(self) -> "str":
        return "TrillerTV"

    @property
    def primary_color(self) -> "str":
        return "#E61414"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TrillerTV</title>
     <path d="m9.496.07-1.8
 3.107-.868-.498c-1.269-.729-2.852.184-2.852
 1.64v6.28l3.9-6.734L9.933.319a.14.14 0 0 0-.053-.19l-.19-.11a.143.143
 0 0 0-.193.05Zm-.713 3.734-4.807 8.301v7.163c0 .674.338 1.23.826
 1.562l-1.65 2.85a.14.14 0 0 0 .05.192l.192.109a.142.142 0 0 0
 .193-.05l1.665-2.874L13.629 6.59Zm11.63 2.547-1.8
 3.108-4.33-2.49-8.217 14.186a1.91 1.91 0 0 0 .764-.248l8.598-4.948
 5.42-9.356a.141.141 0 0
 0-.05-.193c-.065-.035-.128-.073-.192-.11-.027-.02-.14-.041-.193.051zm-.711
 3.735-2.967 5.123 3.08-1.774c1.268-.731 1.268-2.556 0-3.285z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
