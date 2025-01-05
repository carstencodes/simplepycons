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


class TensorflowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tensorflow"

    @property
    def original_file_name(self) -> "str":
        return "tensorflow.svg"

    @property
    def title(self) -> "str":
        return "TensorFlow"

    @property
    def primary_color(self) -> "str":
        return "#FF6F00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TensorFlow</title>
     <path d="M1.292 5.856L11.54 0v24l-4.095-2.378V7.603l-6.168
 3.564.015-5.31zm21.43 5.311l-.014-5.31L12.46
 0v24l4.095-2.378V14.87l3.092 1.788-.018-4.618-3.074-1.756V7.603l6.168
 3.564z" />
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
