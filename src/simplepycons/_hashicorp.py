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


class HashicorpIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hashicorp"

    @property
    def original_file_name(self) -> "str":
        return "hashicorp.svg"

    @property
    def title(self) -> "str":
        return "HashiCorp"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HashiCorp</title>
     <path d="M10.114 4.094 4.215 7.5v13.09L.666 18.542V5.45L10.114
 0v4.094zm3.772 13.37 3.549-2.049V2.05L13.885
 0v10.426h-3.77v-3.89L6.562 8.585v13.357l3.551
 2.054V13.599h3.772v3.865zM19.783 3.41V16.5l-5.897
 3.405V24l9.448-5.45V5.458l-3.551-2.05z" />
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
