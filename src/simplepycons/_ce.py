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


class CeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ce"

    @property
    def original_file_name(self) -> "str":
        return "ce.svg"

    @property
    def title(self) -> "str":
        return "CE"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CE</title>
     <path d="M24 20.53v-2.59a6 6 0 0 1-.857.06 6 6 0 0
 1-5.862-4.714h5.005v-2.571H17.28A6 6 0 0 1 24 6.06V3.47a9 9 0 0
 0-.857-.042 8.571 8.571 0 1 0 .857 17.1M0 12a8.57 8.57 0 0 0 9.486
 8.524V17.93q-.448.07-.915.07a6 6 0 1 1 .915-11.93V3.477a9 9 0 0
 0-.915-.048A8.57 8.57 0 0 0 0 12" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://single-market-economy.ec.europa.eu/si'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://single-market-economy.ec.europa.eu/si'''

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
