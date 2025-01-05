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


class PycharmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pycharm"

    @property
    def original_file_name(self) -> "str":
        return "pycharm.svg"

    @property
    def title(self) -> "str":
        return "PyCharm"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PyCharm</title>
     <path d="M7.833
 6.666v-.055c0-1-.667-1.5-1.778-1.5H4.389v3.055h1.723c1.111 0
 1.721-.666 1.721-1.5zM0 0v24h24V0H0zm2.223 3.167h4c2.389 0 3.833
 1.389 3.833 3.445v.055c0 2.278-1.778 3.5-4.001
 3.5H4.389v2.945H2.223V3.167zM11.277
 21h-9v-1.5h9V21zm4.779-7.777c-2.944.055-5.111-2.223-5.111-5.057C10.944
 5.333 13.056 3 16.111 3c1.889 0 3 .611 3.944 1.556l-1.389
 1.61c-.778-.722-1.556-1.111-2.556-1.111-1.658 0-2.873 1.375-2.887
 3.084.014 1.709 1.174 3.083 2.887 3.083 1.111 0 1.833-.445
 2.61-1.167l1.39 1.389c-.999 1.112-2.166 1.779-4.054 1.779z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.jetbrains.com/company/brand/logos'''

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
