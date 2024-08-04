#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class GocdIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gocd"

    @property
    def original_file_name(self) -> "str":
        return "gocd.svg"

    @property
    def title(self) -> "str":
        return "GoCD"

    @property
    def primary_color(self) -> "str":
        return "#94399E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GoCD</title>
     <path d="M18.043 13.237l-8.907 5.935a1.47 1.47 0 01-.823.25 1.449
 1.449 0 01-.696-.173 1.48 1.48 0 01-.784-1.308V12a1.482 1.482 0
 112.957 0v3.163L14.537 12 7.478 7.304A1.49 1.49 0 119.13 4.823l8.913
 5.94a1.492 1.492 0 010 2.474M12 0a12 12 0 1012 12A12.012 12.012 0
 0012 0" />
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