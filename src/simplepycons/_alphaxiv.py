#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class AlphaxivIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "alphaxiv"

    @property
    def original_file_name(self) -> "str":
        return "alphaxiv.svg"

    @property
    def title(self) -> "str":
        return "alphaXiv"

    @property
    def primary_color(self) -> "str":
        return "#9A2036"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>alphaXiv</title>
     <path d="M19.749 12.21 24 16.46l-1.827
 1.821-4.248-4.23zm-10.6-8.626a4.03 4.03 0 0 1 3.09 1.12L15.4
 7.867l-1.841 1.822-3.232-3.226A1.38 1.38 0 0 0 8.55 6.5l-6.725
 6.722L0 11.399l6.84-6.837a4.06 4.06 0 0 1 2.309-.979m13.026.033L24
 5.44 10.032 19.403c-3.823 3.204-8.805-1.788-5.58-5.598l5.361-5.356
 1.825 1.824-5.274 5.271c-1.108 1.347.633 3.054 1.96 1.921z" />
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
